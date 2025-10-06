from django.test import TestCase
from django.urls import reverse

class MediaConsultableViewTests(TestCase):
    fixtures = ['medias_test.json']

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('bibliothecaire:media_list_consultables')

    def setUp(self):
        self.response = self.client.get(self.url)


    def test_nav_05_url_and_template(self):
        """T-NAV-05 : Accès à la vue consultable et vérification du template"""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'bibliothecaire/medias/media_list.html')

    def test_ent_05_consultable_objects_only(self):
        """T-ENT-05 : Vérifie que tous les objets affichés ont consultable=True"""
        for media in self.response.context['medias']:
            self.assertTrue(media.consultable)

    def test_vue_06_title_displayed(self):
        """T-VUE-06 : Vérifie que le titre <h2> correspond à la vue consultable"""
        self.assertContains(self.response, '<h2>Liste des médias consultables</h2>')

    def test_fun_01_uc_list_01_verification(self):
        """
        T-FUN-01 : Vérification fonctionnelle du cas d’usage UC-LIST-01
        Ce test recoupe :
        - T-NAV-05 : accès et template
        - T-ENT-05 : objets consultables uniquement
        - T-VUE-06 : titre métier affiché
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'bibliothecaire/medias/media_list.html')
        self.assertContains(self.response, '<h2>Liste des médias consultables</h2>')
        for media in self.response.context['medias']:
            self.assertTrue(media.consultable)

class MediaDisponibleViewTests(TestCase):
    fixtures = ['medias_test.json']

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('bibliothecaire:media_list_disponibles')

    def setUp(self):
        self.response = self.client.get(self.url)

    def test_nav_06_url_and_template(self):
        """T-NAV-06 : Accès à la vue disponibles et vérification du template"""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'bibliothecaire/medias/media_list.html')

    def test_ent_06_disponible_objects_only(self):
        """T-ENT-06 : Vérifie que tous les objets affichés ont disponible=True"""
        for media in self.response.context['medias']:
            self.assertTrue(media.consultable)
            self.assertTrue(media.disponible)

    def test_vue_07_title_displayed(self):
        """T-VUE-07 : Vérifie que le titre <h2> correspond à la vue disponibles"""
        self.assertContains(self.response, '<h2>Liste des médias disponibles</h2>')

    def test_fun_02_uc_list_02_verification(self):
        """
        T-FUN-02 : Vérification fonctionnelle du cas d’usage UC-LIST-02
        Ce test recoupe :
        - T-NAV-06 : accès et template
        - T-ENT-06 : objets disponibles uniquement
        - T-VUE-07 : titre métier affiché
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'bibliothecaire/medias/media_list.html')
        self.assertContains(self.response, '<h2>Liste des médias disponibles</h2>')
        for media in self.response.context['medias']:
            self.assertTrue(media.consultable)
            self.assertTrue(media.disponible)