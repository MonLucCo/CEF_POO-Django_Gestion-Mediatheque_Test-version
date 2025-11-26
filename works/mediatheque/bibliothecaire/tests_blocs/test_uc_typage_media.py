from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Media, Livre, Dvd, Cd
from bibliothecaire.tests import LoginRequiredTestCase


class TypageMediaTest(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        cls.media = Media.objects.create(
            name="À typer",
            theme="Roman",
            media_type="NON_DEFINI"
        )

    def test_typage_en_livre(self):
        self.assertTrue(Media.objects.filter(pk=self.media.pk).exists())
        self.assertEqual(Media.objects.get(pk=self.media.pk).media_type, 'NON_DEFINI')

        url = reverse('bibliothecaire:media_typage_livre', kwargs={'pk': self.media.pk})
        data = {
            'name': self.media.name,
            'theme': self.media.theme,
            'annee_edition': 2020,
            'consultable': True,
            'auteur': "Auteur Test",
            'nb_page': 123,
            'resume': "Résumé test"
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('bibliothecaire:media_list'))
        self.assertTrue(Livre.objects.filter(pk=self.media.pk).exists())
        self.assertEqual(Media.objects.get(pk=self.media.pk).media_type, 'LIVRE')


class RollbackTypageTest(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        cls.media = Media.objects.create(
            name="À annuler",
            theme="Essai",
            media_type="DVD"
        )
        # Mutation typée via méthode métier
        cls.media = cls.media.mutate_to_typed()
        # Mise à jour des champs spécifiques
        Dvd.objects.filter(pk=cls.media.pk).update(
            realisateur="Réalisateur",
            duree=90,
            histoire="Histoire"
        )

    def test_annulation_typage(self):
        self.assertTrue(Media.objects.filter(pk=self.media.pk).exists())
        self.assertTrue(Dvd.objects.filter(pk=self.media.pk).exists())
        self.assertEqual(Media.objects.get(pk=self.media.pk).media_type, 'DVD')

        url = reverse('bibliothecaire:media_cancel_typing', kwargs={'pk': self.media.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('bibliothecaire:media_list'))
        self.assertFalse(Dvd.objects.filter(pk=self.media.pk).exists())
        self.assertTrue(Media.objects.filter(pk=self.media.pk).exists())
        self.assertEqual(Media.objects.get(pk=self.media.pk).media_type, 'NON_DEFINI')


class RedirectionTypageDepuisUpdateTest(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        cls.media = Media.objects.create(
            name="À rediriger",
            theme="Science",
            media_type="NON_DEFINI"
        )

    def test_redirection_vers_typage_cd(self):
        url = reverse('bibliothecaire:media_update', kwargs={'pk': self.media.pk})
        data = {
            'name': self.media.name,
            'theme': self.media.theme,
            'media_type': 'CD'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('bibliothecaire:media_typage_cd', kwargs={'pk': self.media.pk}))
