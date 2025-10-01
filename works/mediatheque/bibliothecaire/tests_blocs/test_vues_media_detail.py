from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Media, Livre, Dvd, Cd


class MediaDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.media = Media.objects.create(name="Test Media", media_type="LIVRE", theme="Test Thème")
        cls.livre = Livre.objects.create(
            name="Test Media-Livre", media_type="LIVRE", theme="Test Thème Media-Livre",
            auteur="Auteur Test Livre", nb_page=0, resume="Résumé Test Livre"
        )
        cls.dvd = Dvd.objects.create(
            name="Test Media-Dvd", annee_edition=2000, media_type="DVD", theme="Test Thème Media-Dvd",
            realisateur="Réalisateur Test Dvd", duree=0, histoire="Histoire Test Dvd"
        )
        cls.cd = Cd.objects.create(
            name="Test Media-Cd", annee_edition=2021, media_type="CD", theme="Test Thème Media-Cd",
            artiste="Artiste Test CD", nb_piste=0, duree_ecoute=0
        )

    def test_vue_03_media_detail_vue_type(self):
        # Vue de détail des objets typés (Livre, Dvd et Cd)
        responseLivre = self.client.get(reverse('bibliothecaire:media_detail', args=[self.livre.pk]))
        self.assertContains(responseLivre, "Auteur Test Livre")
        self.assertContains(responseLivre, "Test Thème Media-Livre")
        self.assertNotContains(responseLivre, "Année")
        responseDvd = self.client.get(reverse('bibliothecaire:media_detail', args=[self.dvd.pk]))
        self.assertContains(responseDvd, "Réalisateur Test Dvd")
        self.assertContains(responseDvd, "Test Thème Media-Dvd")
        self.assertContains(responseDvd, "Année")
        responseCd = self.client.get(reverse('bibliothecaire:media_detail', args=[self.cd.pk]))
        self.assertContains(responseCd, "Artiste Test CD")
        self.assertContains(responseCd, "Test Thème Media-Cd")
        self.assertContains(responseCd, "Année")

    def test_vue_04_media_detail_instance_type(self):
        response = self.client.get(reverse('bibliothecaire:media_detail', args=[self.livre.pk]))
        media_obj = response.context['media']
        self.assertEqual(type(media_obj).__name__, "Livre")
        self.assertEqual(media_obj.auteur, "Auteur Test Livre")
        self.assertEqual(media_obj.nb_page, 0)
        self.assertNotContains(response, "Année")

    def test_vue_05_media_detail_vue_sans_type(self):
        # Vue de détail d'un objet non typé (Media)
        responseMedia = self.client.get(reverse('bibliothecaire:media_detail', args=[self.media.pk]))
        self.assertContains(responseMedia, "LIVRE")
        self.assertNotContains(responseMedia, "Auteur Test Livre")
        self.assertNotContains(responseMedia, "Résumé Test Livre")
        self.assertNotContains(responseMedia, "Année")