from django.test import TestCase
from django.urls import reverse

from bibliothecaire.tests import LoginRequiredTestCase


class NavigationTests(LoginRequiredTestCase):
    def test_nav_01_accueil_accessible(self):
        response = self.client.get(reverse('bibliothecaire:accueil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bibliothecaire/accueil.html')

    def test_nav_02_media_list_accessible(self):
        response = self.client.get(reverse('bibliothecaire:media_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bibliothecaire/medias/media_list.html')

    def test_nav_03_media_detail_accessible(self):
        # Préparer un media
        from bibliothecaire.models import Media
        media = Media.objects.create(name="Test", media_type="LIVRE", theme="Test")
        response = self.client.get(reverse('bibliothecaire:media_detail', args=[media.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bibliothecaire/medias/media_detail.html')

    def test_nav_04_media_detail_404(self):
        response = self.client.get(reverse('bibliothecaire:media_detail', args=[999]))
        self.assertEqual(response.status_code, 404)
