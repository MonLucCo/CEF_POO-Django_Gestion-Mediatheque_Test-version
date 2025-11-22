from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command

from bibliothecaire.models import Media, JeuDePlateau


class BaseSupportTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'medias_test.json', verbosity=0)
        call_command('loaddata', 'jeux_test.json', verbosity=0)

        cls.url_accueil = reverse("consultation:accueil")
        cls.url_supports = reverse("consultation:supports")
        cls.url_medias = reverse("consultation:supports_medias")
        cls.url_jeux = reverse("consultation:supports_jeux")
        cls.url_disponibles = reverse("consultation:supports_medias_disponibles")
        cls.url_vide = reverse("consultation:supports_vide")

        cls.template_accueil = "consultation/accueil.html"
        cls.template_supports = "consultation/supports/supports_list.html"


# 🧭 Navigation
class TestNavigationConsultation(BaseSupportTestCase):
    def test_nav_32_acces_accueil_consultation(self):
        response = self.client.get(self.url_accueil)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_accueil)

    def test_nav_33_acces_liste_supports(self):
        response = self.client.get(self.url_supports)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_supports)

    def test_nav_34_acces_liste_medias(self):
        response = self.client.get(self.url_medias)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_supports)

    def test_nav_35_acces_liste_jeux(self):
        response = self.client.get(self.url_jeux)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_supports)

    def test_nav_36_acces_liste_medias_disponibles(self):
        response = self.client.get(self.url_disponibles)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_supports)

    def test_nav_37_acces_liste_vide(self):
        response = self.client.get(self.url_vide)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucun support de consultable")


# 🧪 Fonctionnel
class TestFonctionnelConsultation(BaseSupportTestCase):
    def test_fun_46_filtrage_medias_consultables(self):
        response = self.client.get(self.url_medias)
        for media in Media.objects.filter(consultable=True):
            self.assertContains(response, media.name)

    def test_fun_47_filtrage_jeux_consultables(self):
        response = self.client.get(self.url_jeux)
        for jeu in JeuDePlateau.objects.filter(consultable=True):
            self.assertContains(response, jeu.name)

    def test_fun_48_filtrage_medias_disponibles(self):
        response = self.client.get(self.url_disponibles)
        for media in Media.objects.filter(consultable=True, disponible=True):
            self.assertContains(response, media.name)

    def test_fun_49_cas_liste_vide(self):
        response = self.client.get(self.url_vide)
        self.assertContains(response, "Aucun support de consultable")

    def test_fun_50_persistance_filtre(self):
        response = self.client.get(self.url_medias)
        self.assertContains(response, 'value="medias"')

    def test_fun_51_cta_accueil_consultation(self):
        response = self.client.get(self.url_accueil)
        self.assertContains(response, reverse("consultation:supports"))
