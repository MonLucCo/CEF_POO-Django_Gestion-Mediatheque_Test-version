from pathlib import Path
from django.conf import settings
from django.core.management import call_command
from django.urls import reverse
from bibliothecaire.tests import LoginRequiredTestCase


class BaseLogsTestCase(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        call_command('loaddata', 'membres_test.json', verbosity=0)
        call_command('loaddata', 'medias_test.json', verbosity=0)
        call_command('loaddata', 'emprunts_test.json', verbosity=0)
        call_command('loaddata', 'jeux_test.json', verbosity=0)

        cls.url_login = reverse("accounts:login")
        cls.url_logout = reverse("accounts:logout")
        cls.url_accueil_bib = reverse("bibliothecaire:accueil")
        cls.log_file = Path(settings.BASE_DIR) / "mediatheque_test.log"

        # On remet le fichier à zéro pour éviter le bruit des tests précédents
        cls.log_file.write_text("", encoding="utf-8")

    def read_log(self) -> str:
        """Retourne le contenu du fichier de log en UTF-8 (chaîne vide si absent)."""
        try:
            return self.log_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return ""

    def read_last_log_line(self) -> str:
        """Retourne uniquement la dernière ligne du fichier de log (ou chaîne vide si absent)."""
        try:
            with self.log_file.open(encoding="utf-8") as f:
                lines = f.readlines()
                return lines[-1].strip() if lines else ""
        except FileNotFoundError:
            return ""


# 🧪 Fonctionnel – UC-LOGS
class TestLogs(BaseLogsTestCase):

    def test_log_01_fichier_log_cree_et_alimente(self):
        """T-LOG-01 : Vérifie la création et l’alimentation du fichier mediatheque.log."""
        self.logout(url=True)
        self.assertTrue(self.log_file.exists(), "Le fichier mediatheque.log n'existe pas.")
        content = self.read_log()
        self.assertTrue(len(content) > 0, "Le fichier mediatheque.log est vide.")

    def test_log_02_connexion_genere_un_log_LOGIN(self):
        """T-LOG-02 : Vérifie qu’une connexion génère un message [LOGIN]."""
        self.logout()
        self.login_as(self.RoleTest.STAFF, url=True)
        content = self.read_log()
        self.assertIn("[LOGIN]", content, "Aucun [LOGIN] dans le fichier de logs.")

    def test_log_03_deconnexion_genere_un_log_LOGOUT(self):
        """T-LOG-03 : Vérifie qu’une déconnexion génère [LOGOUT] ou [LOGOUT_INVALID]."""
        self.logout()
        self.login_as(self.RoleTest.SUPERADMIN, url=True)
        self.client.post(self.url_logout)
        last_line = self.read_last_log_line()
        self.assertTrue(
            "[LOGOUT]" in last_line or "[LOGOUT_INVALID]" in last_line,
            "La dernière ligne ne contient pas [LOGOUT] ou [LOGOUT_INVALID]."
        )

    def test_log_04_acces_refuse_genere_un_log_ACCESS_DENIED(self):
        """T-LOG-04 : Vérifie qu’un accès refusé génère [ACCESS_DENIED]."""
        self.logout()
        self.client.get(self.url_accueil_bib)
        content = self.read_log()
        self.assertIn("[ACCESS_DENIED]", content, "Aucun [ACCESS_DENIED] dans le fichier de logs.")

    def test_log_05_acces_accepte_genere_un_log_ACCESS_GRANTED(self):
        """T-LOG-05 : Vérifie qu’un accès accordé génère [ACCESS_GRANTED]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        content = self.read_log()
        self.assertIn("[ACCESS_GRANTED]", content, "Aucun [ACCESS_GRANTED] dans le fichier de logs.")

    def test_log_10_reset_retard_session(self):
        """T-LOG-10 : Vérifie que le changement de date de marquage génère [ResetRetardSession]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:rejeu_reset_retard_session"), {"nb_jours": 1})
        content = self.read_log()
        self.assertIn("[ResetRetardSession]", content)

    def test_log_11_media_create(self):
        """T-LOG-11 : Vérifie que la création d’un média génère [MediaCreate]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:media_create"), {"name": "TestMedia", "theme": "TestTheme"})
        content = self.read_log()
        self.assertIn("[MediaCreate]", content)

    def test_log_16_media_update(self):
        """T-LOG-16 : Vérifie que la modification d’un média génère [MediaUpdate]."""
        from bibliothecaire.models import Media

        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)

        # On récupère un média existant depuis les fixtures
        media = Media.objects.first()
        payload = {
            "name": media.name,  # garder les valeurs existantes
            "theme": "ThemeModif",  # modifier uniquement ce champ
            "annee_edition": media.annee_edition,
            "consultable": media.consultable,
            "disponible": media.disponible,
            "media_type": media.media_type,
        }

        self.client.post(reverse("bibliothecaire:media_update", args=[media.pk]), payload)
        content = self.read_log()
        self.assertIn("[MediaUpdate]", content)

    def test_log_18_livre_create(self):
        """T-LOG-18 : Vérifie que la création d’un Livre génère [LivreCreate]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:media_create_livre"),
                         {"name": "TestLivre", "theme": "TestTheme", "auteur": "TestAuteur", "resume": "TestResume"})
        content = self.read_log()
        self.assertIn("[LivreCreate]", content)

    def test_log_20_media_typage_livre(self):
        """T-LOG-20 : Vérifie que le typage d’un média en Livre génère [MediaTypageLivre]."""
        from bibliothecaire.models import Media

        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)

        # Étape 1 : créer un média générique NON_DEFINI
        self.client.post(
            reverse("bibliothecaire:media_create"),
            {"name": "MediaNonType", "theme": "Divers"}
        )
        media = Media.objects.filter(media_type="NON_DEFINI").order_by("-pk").first()

        # Étape 2 : typer ce média en Livre
        self.client.post(
            reverse("bibliothecaire:media_typage_livre", args=[media.pk]),
            {
                "name": media.name,
                "theme": media.theme,
                "media_type": "LIVRE",
                "auteur": "AuteurTest",
                "resume": "Résumé test"
            }
        )

        # Vérification du log
        content = self.read_log()
        self.assertIn("[MediaTypageLivre]", content)

    def test_log_21_livre_update(self):
        """T-LOG-21 : Vérifie que la modification d’un Livre génère [LivreUpdate]."""
        from bibliothecaire.models import Livre

        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)

        # On récupère un Livre existant depuis les fixtures
        livre = Livre.objects.first()

        payload = {
            "name": livre.name,
            "annee_edition": livre.annee_edition,
            "consultable": livre.consultable,
            "disponible": livre.disponible,
            "theme": livre.theme,
            "media_type": livre.media_type,  # doit être LIVRE
            "auteur": livre.auteur,
            "nb_page": livre.nb_page,
            "resume": "Résumé modifié",  # champ modifié pour déclencher le log
        }

        self.client.post(reverse("bibliothecaire:media_update_livre", args=[livre.pk]), payload)
        content = self.read_log()
        self.assertIn("[LivreUpdate]", content)

    def test_log_23_dvd_create(self):
        """T-LOG-23 : Vérifie que la création d’un DVD génère [DvdCreate]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:media_create_dvd"),
                         {"name": "TestDVD", "theme": "TestTheme", "realisateur": "TestRealisateur", "histoire": "TestHistoire"})
        content = self.read_log()
        self.assertIn("[DvdCreate]", content)

    def test_log_27_cd_create(self):
        """T-LOG-27 : Vérifie que la création d’un CD génère [CdCreate]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:media_create_cd"),
                         {"name": "TestCD", "theme": "TestTheme", "artiste": "TestArtiste", "nb_piste": 1})
        content = self.read_log()
        self.assertIn("[CdCreate]", content)

    def test_log_31_membre_create(self):
        """T-LOG-31 : Vérifie que la création d’un Membre génère [MembreCreate]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:membre_create"), {"name": "Jean Dupont"})
        content = self.read_log()
        self.assertIn("[MembreCreate]", content)

    def test_log_32_membre_create_emprunteur(self):
        """T-LOG-32 : Vérifie que la création d’un Membre emprunteur génère [MembreCreateEmprunteur]."""
        self.logout()
        self.client.get(self.url_accueil_bib)
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.post(reverse("bibliothecaire:membre_create_emprunteur"), {"name": "Marie Durand"})
        content = self.read_log()
        self.assertIn("[MembreCreateEmprunteur]", content)

    def test_log_37_membre_update(self):
        """T-LOG-37 : Vérifie que la modification d’un Membre génère [MembreUpdate]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:membre_update", args=[1]), {"name": "Jean Modif"})
        content = self.read_log()
        self.assertIn("[MembreUpdate]", content)

    def test_log_38_membre_activate_emprunteur(self):
        """T-LOG-38 : Vérifie que l’activation d’un emprunteur génère [MembreActivateEmprunteur]."""
        from bibliothecaire.models import Membre, StatutMembre

        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)

        # Étape 1 : créer un membre standard (statut MEMBRE)
        membre = Membre.objects.create(
            name="TestMembre",
            compte=Membre.generer_compte("TestMembre"),
            statut=StatutMembre.MEMBRE
        )

        # Étape 2 : activer ce membre en emprunteur
        self.client.post(reverse("bibliothecaire:membre_activate_emprunteur", args=[membre.pk]), {"confirmer": True})

        # Vérification du log
        content = self.read_log()
        self.assertIn("[MembreActivateEmprunteur]", content)

    def test_log_41_emprunt_create(self):
        """T-LOG-41 : Vérifie que la création d’un Emprunt génère [EmpruntCreate]."""
        self.logout()
        self.login_as(self.RoleTest.GESTION, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:emprunt_create"), {"emprunteur": 1, "media": 1})
        content = self.read_log()
        self.assertIn("[EmpruntCreate]", content)

    def test_log_42_emprunt_retour_confirm(self):
        """T-LOG-42 : Vérifie que la confirmation du retour génère [EmpruntRetourConfirm]."""
        self.logout()
        self.login_as(self.RoleTest.GESTION, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:emprunt_retour_confirm", args=[2]), {"confirmer": True})
        content = self.read_log()
        self.assertIn("[EmpruntRetourConfirm]", content)

    def test_log_43_media_emprunter(self):
        """T-LOG-43 : Vérifie que l’emprunt depuis un média génère [EmpruntCreateFromMedia] ou [EmpruntCreate]."""
        from bibliothecaire.models import Membre, StatutMembre, Media

        self.logout()
        self.login_as(self.RoleTest.GESTION, url=True)
        self.client.get(self.url_accueil_bib)

        # Étape 1 : créer un membre emprunteur
        membre = Membre.objects.create(
            name="EmprunteurTest",
            compte=Membre.generer_compte("EmprunteurTest"),
            statut=StatutMembre.EMPRUNTEUR
        )

        # Étape 2 : récupérer un média typé et disponible (ex: pk=1 issu des fixtures)
        media = Media.objects.filter(media_type="LIVRE", disponible=True).first()

        # Étape 3 : créer l’emprunt depuis le média
        self.client.post(reverse("bibliothecaire:media_emprunter", args=[media.pk]), {"emprunteur": membre.pk})

        # Étape 4 : vérifier le log
        content = self.read_log()
        # Selon l’implémentation actuelle, c’est [EmpruntCreate]
        self.assertTrue(
            "[EmpruntCreateFromMedia]" in content or "[EmpruntCreate]" in content,
            "Aucun log d’emprunt depuis média trouvé."
        )

    def test_log_44_media_rendre(self):
        """T-LOG-44 : Vérifie que le rendu depuis un média génère [EmpruntRetourConfirm]."""
        self.logout()
        self.login_as(self.RoleTest.GESTION, url=True)
        self.client.get(self.url_accueil_bib)

        # Étape 1 : accéder à la vue de rendu depuis le média pk=7
        self.client.get(reverse("bibliothecaire:media_rendre", args=[7]))

        # Étape 2 : confirmer le retour de l’emprunt pk=4
        self.client.post(reverse("bibliothecaire:emprunt_retour_confirm", args=[4]), {"confirmer": True})

        # Étape 3 : vérifier le log
        content = self.read_log()
        self.assertIn("[EmpruntRetourConfirm]", content)

    def test_log_45_membre_emprunter(self):
        """T-LOG-45 : Vérifie que la création d’un emprunt depuis un membre génère [EmpruntCreate]."""
        from bibliothecaire.models import Membre, Media

        self.logout()
        self.login_as(self.RoleTest.GESTION, url=True)
        self.client.get(self.url_accueil_bib)

        # Étape 1 : récupérer un membre emprunteur depuis les fixtures
        membre = Membre.objects.filter(pk=1).first()

        # Étape 2 : récupérer un média disponible et typé
        media = Media.objects.filter(pk=1).first()

        # Étape 3 : créer l’emprunt depuis le membre
        self.client.post(reverse("bibliothecaire:membre_emprunter", args=[membre.pk]), {"media": media.pk})

        # Étape 4 : vérifier le log
        content = self.read_log()
        # Implémentation actuelle écrit [EmpruntCreate]
        self.assertIn("[EmpruntCreate]", content)

    def test_log_46_membre_rendre(self):
        """T-LOG-46 : Vérifie que le rendu d’un emprunt depuis un membre génère [EmpruntRetourConfirm]."""
        from bibliothecaire.models import Emprunt, Membre

        self.logout()
        self.login_as(self.RoleTest.GESTION, url=True)
        self.client.get(self.url_accueil_bib)

        # Étape 1 : récupérer un membre emprunteur depuis les fixtures
        membre = Membre.objects.get(pk=4)

        # Étape 2 : récupérer un emprunt en cours lié à ce membre
        emprunt = Emprunt.objects.filter(emprunteur=membre, statut__in=[0, 1]).first()  # RETARD ou EN_COURS

        # Étape 3 : accéder à la vue membre_rendre
        self.client.get(reverse("bibliothecaire:membre_rendre", args=[membre.pk]))

        # Étape 4 : confirmer le retour de l’emprunt
        self.client.post(reverse("bibliothecaire:emprunt_retour_confirm", args=[emprunt.pk]), {"confirmer": True})

        # Étape 5 : vérifier le log
        content = self.read_log()
        self.assertIn("[EmpruntRetourConfirm]", content)

    def test_log_48_jeu_create(self):
        """T-LOG-48 : Vérifie que la création d’un Jeu génère [JeuCreate]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        self.client.post(reverse("bibliothecaire:jeu_create"),
                         {"name": "TestJeu", "createur": "TestCreateur", "categorie": "non classé",
                          "duree_partie": 30, "nb_joueur_min": 1, "nb_joueur_max": 3, "age_min": 1})
        content = self.read_log()
        self.assertIn("[JeuCreate]", content)
