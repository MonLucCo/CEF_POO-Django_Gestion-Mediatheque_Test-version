from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Membre, Media, Emprunt, StatutEmprunt


class BaseEmpruntCreateTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'membres_test.json', verbosity=0)
        call_command('loaddata', 'medias_test.json', verbosity=0)

        cls.membre_valide = Membre.objects.get(pk=1)  # Dupont
        cls.media_valide = Media.objects.get(pk=11)   # Thriller (CD, disponible, consultable)

        cls.url_create = reverse("bibliothecaire:emprunt_create")
        cls.url_list = reverse("bibliothecaire:emprunt_list")
        cls.template_create = "bibliothecaire/emprunts/emprunt_form.html"
        cls.template_list = "bibliothecaire/emprunts/emprunt_list.html"

        cls.url_create_from_membre = reverse("bibliothecaire:membre_emprunter", args=[cls.membre_valide.id])

    def post_emprunt(self, membre_id, media_id, follow=False):
        return self.client.post(self.url_create, data={
            "emprunteur": membre_id,
            "media": media_id
        }, follow=follow)
        # follow=True : pour disposer après redirection du rendu de la page cible (avec des messages non persistants).


# 🧭 Navigation
class TestNavigationEmpruntUcCreate(BaseEmpruntCreateTestCase):
    def test_nav_21_acces_vue_creation_emprunt(self):
        response = self.client.get(self.url_create)
        self.assertEqual(response.status_code, 200)


class TestNavigationEmpruntUcCreateFromMembre(BaseEmpruntCreateTestCase):
    def test_nav_22_acces_vue_creation_emprunt_depuis_membre(self):
        response = self.client.get(self.url_create_from_membre)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_create)


# 🧪 Entités
class TestEntitesEmpruntUcCreate(BaseEmpruntCreateTestCase):
    def test_ent_20_creation_emprunt_valide(self):
        response = self.post_emprunt(self.membre_valide.id, self.media_valide.id)
        self.assertEqual(response.status_code, 302)
        emprunt = Emprunt.objects.get(emprunteur=self.membre_valide, media=self.media_valide)
        self.assertEqual(emprunt.statut, StatutEmprunt.EN_COURS)
        self.assertIsNone(emprunt.date_retour)


# 🧪 Vues
class TestVuesEmpruntUcCreate(BaseEmpruntCreateTestCase):
    def test_vue_25_persistance_selection_si_erreur(self):
        media_non_consultable = Media.objects.get(pk=5)  # Les Misérables
        response = self.post_emprunt(self.membre_valide.id, media_non_consultable.id)
        self.assertContains(response, f'value="{self.membre_valide.id}"', html=False)
        self.assertContains(response, f'value="{media_non_consultable.id}"', html=False)

    def test_vue_26_accumulation_messages_erreur(self):
        media_non_consultable = Media.objects.get(pk=5)
        response = self.post_emprunt(self.membre_valide.id, media_non_consultable.id)
        self.assertContains(response, "<ul class=\"messages\">")
        self.assertContains(response, "Ce média ne peut pas être emprunté")

    def test_vue_27_redirection_apres_creation(self):
        response = self.post_emprunt(self.membre_valide.id, self.media_valide.id, follow=True)
        self.assertRedirects(response, self.url_list)
        self.assertContains(response, "Emprunt enregistré")
        self.assertTemplateUsed(response, self.template_list)


class TestVuesEmpruntUcCreateFromMembre(BaseEmpruntCreateTestCase):
    def test_vue_28_champ_emprunteur_fige(self):
        response = self.client.get(self.url_create_from_membre)
        self.assertContains(response, f'value="{self.membre_valide.id}"')
        self.assertContains(response, 'disabled')

    def test_vue_29_bloc_info_present(self):
        response = self.client.get(self.url_create_from_membre)
        self.assertContains(response, 'id="emprunt_membre_info"')
        self.assertContains(response, "Veuillez sélectionner un média")


# 🧪 Fonctionnel
class TestFonctionnelEmpruntUcCreate(BaseEmpruntCreateTestCase):
    def test_fun_26_creation_emprunt_valide(self):
        response = self.post_emprunt(self.membre_valide.id, self.media_valide.id)
        self.assertEqual(response.status_code, 302)
        Emprunt.objects.get(emprunteur=self.membre_valide, media=self.media_valide)
        self.media_valide.refresh_from_db()
        self.assertFalse(self.media_valide.disponible)

    def test_fun_27_refus_membre_non_abonne(self):
        membre_non_abonne = Membre.objects.create(name="Test", compte="2025_Test_1", statut=0)
        response = self.post_emprunt(membre_non_abonne.id, self.media_valide.id)
        self.assertContains(response, "abonnement non validé")

    def test_fun_28_refus_membre_retard(self):
        membre_retard = Membre.objects.get(pk=2)  # Martin
        # Simuler un emprunt en retard
        Emprunt.objects.create(emprunteur=membre_retard, media=self.media_valide, statut=StatutEmprunt.RETARD)
        response = self.post_emprunt(membre_retard.id, self.media_valide.id)
        self.assertContains(response, "retard en cours")

    def test_fun_29_refus_membre_au_quota(self):
        membre_quota = Membre.objects.get(pk=3)  # Bernard
        media_ids = [9, 6, 4]  # 3 emprunts pour atteindre le quota

        for media_id in media_ids:
            media = Media.objects.get(pk=media_id)
            Emprunt.objects.create(emprunteur=membre_quota, media=media)

        # Tentative d’emprunt supplémentaire
        media_extra = Media.objects.get(pk=13)
        response = self.post_emprunt(membre_quota.id, media_extra.id)
        self.assertTemplateUsed(response, self.template_create)
        self.assertContains(response, "<ul class=\"messages\">")
        self.assertContains(response, "quota des emprunts atteint")

    def test_fun_30_refus_media_non_typé(self):
        media_non_type = Media.objects.create(name="Objet", theme="Divers", media_type="NON_DEFINI", consultable=True, disponible=True)
        response = self.post_emprunt(self.membre_valide.id, media_non_type.id)
        self.assertContains(response, "hors gestion car non typé")

    def test_fun_31_refus_media_non_consultable(self):
        media_non_consultable = Media.objects.get(pk=5)
        response = self.post_emprunt(self.membre_valide.id, media_non_consultable.id)
        self.assertContains(response, "hors gestion")

    def test_fun_32_refus_media_indisponible(self):
        media_indispo = Media.objects.get(pk=2)
        response = self.post_emprunt(self.membre_valide.id, media_indispo.id)
        self.assertContains(response, "pas disponible")


class TestFonctionnelEmpruntUcCreateFromMembre(BaseEmpruntCreateTestCase):
    def test_fun_38_creation_emprunt_depuis_membre_valide(self):
        response = self.client.post(self.url_create_from_membre, data={
            "media": self.media_valide.id
        }, follow=True)
        self.assertRedirects(response, self.url_list)
        self.assertContains(response, "Emprunt enregistré")
        emprunt = Emprunt.objects.get(emprunteur=self.membre_valide, media=self.media_valide)
        self.assertEqual(emprunt.statut, StatutEmprunt.EN_COURS)
        self.media_valide.refresh_from_db()
        self.assertFalse(self.media_valide.disponible)

    def test_fun_39_refus_media_non_empruntable_depuis_membre(self):
        media_non_consultable = Media.objects.get(pk=5)
        response = self.client.post(self.url_create_from_membre, data={
            "media": media_non_consultable.id
        })
        self.assertContains(response, "Ce média ne peut pas être emprunté")
        self.assertTemplateUsed(response, self.template_create)
