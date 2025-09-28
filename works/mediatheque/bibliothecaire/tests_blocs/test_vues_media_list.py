from django.test import TestCase
from django.urls import reverse

from bibliothecaire.models import Media, Livre, Dvd, Cd


class MediaListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.media = Media.objects.create(titre="Test Media", annee_edition=0, media_type="LIVRE", theme="Test Thème")
        cls.livre = Livre.objects.create(
            titre="Test Media-Livre", annee_edition=0, media_type="LIVRE", theme="Test Thème Media-Livre",
            auteur="Auteur Test Livre", nb_page=0, resume="Résumé Test Livre"
        )
        cls.dvd = Dvd.objects.create(
            titre="Test Media-Dvd", annee_edition=0, media_type="DVD", theme="Test Thème Media-Dvd",
            realisateur="Réalisateur Test Dvd", duree=0, histoire="Histoire Test Dvd"
        )
        cls.cd = Cd.objects.create(
            titre="Test Media-Cd", annee_edition=0, media_type="CD", theme="Test Thème Media-Cd",
            artiste="Artiste Test CD", nb_piste=0, duree_ecoute=0
        )


    def test_vue_01_media_list_affichage(self):
        response = self.client.get(reverse('bibliothecaire:media_list'))
        self.assertContains(response, "Test Media (LIVRE) - [disponible]")
        self.assertContains(response, "Test Media-Livre (LIVRE) - [disponible]")
        self.assertContains(response, "Test Media-Dvd (DVD) - [disponible]")
        self.assertContains(response, "Test Media-Cd (CD) - [disponible]")

    def test_vue_02_media_list_champs_generiques(self):
        response = self.client.get(reverse('bibliothecaire:media_list'))
        self.assertNotContains(response, 0)
        self.assertNotContains(response, 0)
        self.assertNotContains(response, "Test Thème Media-Livre")
        # Vérifie que les champs typés ne sont pas affichés
        self.assertNotContains(response, "Auteur Test Livre")
        self.assertNotContains(response, "Réalisateur Test Dvd")
        self.assertNotContains(response, "Artiste Test CD")

