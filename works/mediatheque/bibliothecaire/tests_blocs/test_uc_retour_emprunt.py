from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from django.utils.formats import date_format

from bibliothecaire.models import Emprunt, Membre, Media, StatutEmprunt


class BaseEmpruntRetourTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'membres_test.json', verbosity=0)
        call_command('loaddata', 'medias_test.json', verbosity=0)
        call_command('loaddata', 'emprunts_test.json', verbosity=0)

        cls.emprunt = Emprunt.objects.get(pk=2)  # Emprunt en cours
        cls.media = cls.emprunt.media
        cls.membre = cls.emprunt.emprunteur

        cls.url_rendre = reverse("bibliothecaire:emprunt_rendre")
        cls.url_confirm = reverse("bibliothecaire:emprunt_retour_confirm", args=[cls.emprunt.pk])
        cls.url_list = reverse("bibliothecaire:emprunt_list")
        cls.url_from_media = reverse("bibliothecaire:media_detail", args=[cls.media.pk])

        cls.template_form = "bibliothecaire/emprunts/emprunt_form.html"
        cls.template_confirm = "bibliothecaire/emprunts/emprunt_retour_confirm.html"

    def post_selection(self, emprunt_id, follow=False):
        return self.client.post(self.url_rendre, data={"emprunt": emprunt_id}, follow=follow)

    def post_confirmation(self, follow=False):
        return self.client.post(self.url_confirm, follow=follow)


# 🧭 Navigation
class TestNavigationEmpruntRetour(BaseEmpruntRetourTestCase):
    def test_nav_24_acces_vue_selection_retour(self):
        response = self.client.get(self.url_rendre)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_form)

    def test_nav_25_acces_vue_confirmation_retour(self):
        response = self.client.get(self.url_confirm)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_confirm)

    def test_nav_26_acces_vue_retour_depuis_media(self):
        url = reverse("bibliothecaire:media_rendre", args=[self.media.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.url_confirm)


# 🧪 Vues
class TestVuesEmpruntRetour(BaseEmpruntRetourTestCase):
    def test_vue_32_formulaire_retour_affiche_champs(self):
        response = self.client.get(self.url_rendre)
        self.assertContains(response, 'name="emprunt"')
        self.assertContains(response, 'id="id_media"')
        self.assertContains(response, 'id="id_emprunteur"')
        self.assertContains(response, 'disabled')

    def test_vue_33_script_js_synchronise_champs(self):
        response = self.client.get(self.url_rendre)
        self.assertContains(response, 'document.addEventListener')
        self.assertContains(response, 'empruntData')

    def test_vue_34_affichage_confirmation_retour(self):
        response = self.client.get(self.url_confirm)
        self.assertContains(response, str(self.emprunt.media))
        self.assertContains(response, str(self.emprunt.emprunteur))
        date_affichee = date_format(self.emprunt.date_emprunt, format='DATE_FORMAT', use_l10n=True)
        self.assertContains(response, date_affichee)

    def test_vue_35_redirection_retour_depuis_media(self):
        url = reverse("bibliothecaire:media_rendre", args=[self.media.pk])
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, self.url_confirm)
        self.assertTemplateUsed(response, self.template_confirm)


# 🧪 Fonctionnel
class TestFonctionnelEmpruntRetour(BaseEmpruntRetourTestCase):
    def test_fun_37_selection_emprunt_redirige_confirmation(self):
        response = self.post_selection(self.emprunt.pk)
        self.assertRedirects(response, self.url_confirm)

    def test_fun_38_confirmation_retour_met_a_jour_emprunt(self):
        response = self.post_confirmation(follow=True)
        self.assertRedirects(response, self.url_list)
        self.assertContains(response, "Emprunt rendu ")
        self.emprunt.refresh_from_db()
        self.assertEqual(self.emprunt.statut, StatutEmprunt.RENDU)
        self.assertIsNotNone(self.emprunt.date_retour)
        self.media.refresh_from_db()
        self.assertTrue(self.media.disponible)

    def test_fun_39_retour_depuis_media_met_a_jour_emprunt(self):
        # Simule le parcours depuis media_detail
        url = reverse("bibliothecaire:media_rendre", args=[self.media.pk])
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, self.url_confirm)

        # Confirmation du retour
        response = self.post_confirmation(follow=True)
        self.assertRedirects(response, self.url_from_media)
        self.assertContains(response, "Emprunt rendu")
        self.emprunt.refresh_from_db()
        self.assertEqual(self.emprunt.statut, StatutEmprunt.RENDU)
        self.assertIsNotNone(self.emprunt.date_retour)
        self.media.refresh_from_db()
        self.assertTrue(self.media.disponible)
