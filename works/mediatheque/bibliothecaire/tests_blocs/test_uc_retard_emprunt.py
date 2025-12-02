from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from datetime import date, timedelta
from bibliothecaire.models import Membre, Media, Emprunt, StatutEmprunt, StatutMembre
from bibliothecaire.tests import LoginRequiredTestCase


class BaseEmpruntRetardTestCase(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        # Chargement du jeu de données (fixtures)
        call_command('loaddata', 'test_uc_emprunt_retard.json', verbosity=0)

        # Définir les objets pour les tests hérités
        cls.membre = Membre.objects.get(pk=1)
        cls.media = Media.objects.get(pk=1)
        cls.emprunt = Emprunt.objects.get(pk=1)

        # Vérification des assertions Métier en assertion standard Python, car dans une méthode de classe
        # Assertion 1 : est_en_retard
        assert cls.emprunt.est_en_retard, "L'emprunt devrait être en retard"
        # Assertion 2 : date_retour_prevu ≠ aujourd’hui
        assert cls.emprunt.date_retour_prevu != date.today(), "La date de retour prévue ne doit pas être aujourd’hui"
        # Assertion 3 : date_retour_prevu < aujourd’hui
        assert cls.emprunt.date_retour_prevu < date.today(), "La date de retour prévue doit être antérieure à aujourd’hui"

        # Nettoyage du contexte session simulé (si emploi nécessaire dans les tests)
        cls.retard_session_keys = [
            "retard_last_check_date",
            "retard_message",
            "emprunts_marques_ids",
            "affiche_table"
        ]


# 🧭 Navigation
class TestNavigationEmpruntUcRetard(BaseEmpruntRetardTestCase):
    def test_nav_19_acces_vue_retard_manuel(self):
        response = self.client.get(reverse("bibliothecaire:emprunt_retard"))
        self.assertEqual(response.status_code, 200)

    def test_nav_20_acces_vue_liste_emprunts(self):
        response = self.client.get(reverse("bibliothecaire:emprunt_list"))
        self.assertEqual(response.status_code, 200)


# 🧪 Entités
class TestEntitesEmpruntUcRetard(BaseEmpruntRetardTestCase):
    def test_ent_19_transition_statut_retard(self):
        # Vérification initiale
        self.assertEqual(self.emprunt.statut, StatutEmprunt.EN_COURS)

        # Appel de la méthode métier
        resultat = Emprunt.marquer_retard()

        # Vérification du statut modifié
        self.emprunt.refresh_from_db()

        # Vérification que l’emprunt est bien dans la liste retournée
        self.assertIn(self.emprunt, resultat["emprunts_marques"])
        self.assertEqual(self.emprunt.statut, StatutEmprunt.RETARD)


# 🧪 Vues
class TestVuesEmpruntUcRetard(BaseEmpruntRetardTestCase):
    def test_vue_21_message_retard_affiche_accueil(self):
        session = self.client.session
        session["retard_message"] = "1 emprunt marqué comme en retard."
        session.save()
        response = self.client.get(reverse("bibliothecaire:accueil"))
        self.assertContains(response, "1 emprunt marqué comme en retard.")

    def test_vue_22_tableau_retard_affiche_si_toggle_true(self):
        session = self.client.session
        session["affiche_table"] = True
        session["emprunts_marques_ids"] = [self.emprunt.id]
        session.save()
        response = self.client.get(reverse("bibliothecaire:accueil"))
        self.assertContains(response, '<table id="retards_marques">')

    def test_vue_23_tableau_retard_affiche_vue_manuel(self):
        response = self.client.get(reverse("bibliothecaire:emprunt_retard"))
        self.assertContains(response, '<table id="retards_marques">')

    def test_vue_24_tableau_retard_colonnes_correctes(self):
        response = self.client.get(reverse("bibliothecaire:emprunt_retard"))
        self.assertContains(response, "Membre")
        self.assertContains(response, "Média")
        self.assertContains(response, "Date emprunt")
        self.assertContains(response, "Date retour prévu")


# 🧪 Fonctionnel
class TestFonctionnelEmpruntUcRetard(BaseEmpruntRetardTestCase):
    def test_fun_21_marquage_manuel(self):
        response = self.client.get(reverse("bibliothecaire:emprunt_retard"))
        self.assertContains(response, "1 emprunt marqué comme en retard")

    def test_fun_22_marquage_automatique(self):
        session = self.client.session
        session["retard_last_check_date"] = str(date.today() - timedelta(days=1))
        session.save()
        response = self.client.get(reverse("bibliothecaire:accueil"))
        self.assertContains(response, "1 emprunt marqué comme en retard")

    def test_fun_23_toggle_affichage_tableau(self):
        session = self.client.session
        session["affiche_table"] = False
        session["emprunts_marques_ids"] = [self.emprunt.id]
        session.save()

        # POST pour changer l’état
        self.client.post(reverse("bibliothecaire:accueil"), data={"toggle_table": "true"})
        # GET pour vérifier le rendu
        response = self.client.get(reverse("bibliothecaire:accueil"))
        self.assertContains(response, '<table id="retards_marques">')
        # Situation de la session
        session = self.client.session
        self.assertTrue(session.get("affiche_table", False))

    def test_fun_24_toggle_affichage_masque_tableau(self):
        session = self.client.session
        session["affiche_table"] = True
        session["emprunts_marques_ids"] = [self.emprunt.id]
        session.save()

        # POST pour changer l’état
        self.client.post(reverse("bibliothecaire:accueil"), data={"toggle_table": "false"})
        # GET pour vérifier le rendu
        response = self.client.get(reverse("bibliothecaire:accueil"))
        self.assertNotContains(response, '<table id="retards_marques">')
        # Situation de la session
        session = self.client.session
        self.assertFalse(session.get("affiche_table", True))

