from django.test import TestCase
from django.urls import reverse

from bibliothecaire.models import Media, Livre, Dvd, Cd


class MediaListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.media = Media.objects.create(name="Test Media", theme="Test Thème")
        cls.livre = Livre.objects.create(
            name="Test Media-Livre", media_type="LIVRE", theme="Test Thème Media-Livre",
            auteur="Auteur Test Livre", resume="Résumé Test Livre"
        )
        cls.dvd = Dvd.objects.create(
            name="Test Media-Dvd", media_type="DVD", theme="Test Thème Media-Dvd",
            realisateur="Réalisateur Test Dvd", histoire="Histoire Test Dvd"
        )
        cls.cd = Cd.objects.create(
            name="Test Media-Cd", media_type="CD", theme="Test Thème Media-Cd",
            artiste="Artiste Test CD"
        )


    def test_vue_01_media_list_affichage(self):
        response = self.client.get(reverse('bibliothecaire:media_list'))
        self.assertContains(response, "Test Media (- sans -) - {consultable} - [disponible]")
        self.assertContains(response, "Test Media-Livre (LIVRE) - {consultable} - [disponible]")
        self.assertContains(response, "Test Media-Dvd (DVD) - {consultable} - [disponible]")
        self.assertContains(response, "Test Media-Cd (CD) - {consultable} - [disponible]")

    def test_vue_02_media_list_champs_generiques(self):
        response = self.client.get(reverse('bibliothecaire:media_list'))
        self.assertNotContains(response, "Histoire Test Dvd")
        self.assertNotContains(response, "Test Thème Media-Livre")
        # Vérifie que les champs typés ne sont pas affichés
        self.assertNotContains(response, "Auteur Test Livre")
        self.assertNotContains(response, "Réalisateur Test Dvd")
        self.assertNotContains(response, "Artiste Test CD")

