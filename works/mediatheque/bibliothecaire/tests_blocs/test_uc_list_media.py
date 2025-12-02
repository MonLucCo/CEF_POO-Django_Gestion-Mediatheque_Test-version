from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from bibliothecaire.tests import LoginRequiredTestCase


class MediaConsultableViewTests(LoginRequiredTestCase):
    fixtures = ['medias_test.json']

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        cls.url = reverse('bibliothecaire:media_list_consultables')

    def setUp(self):
        super().setUp() # exécute la connexion BibGestion

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

class MediaDisponibleViewTests(LoginRequiredTestCase):
    fixtures = ['medias_test.json']

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        cls.url = reverse('bibliothecaire:media_list_disponibles')

    def setUp(self):
        super().setUp() # exécute la connexion BibGestion

        self.response = self.client.get(self.url)

    def test_nav_06_url_and_template(self):
        """T-NAV-06 : Accès à la vue disponible et vérification du template"""
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

class MediaTypeViewTests(LoginRequiredTestCase):
    fixtures = ['medias_test.json', 'media_untyped_fixture.json']

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        cls.url = reverse('bibliothecaire:media_list_by_type')

    def setUp(self):
        super().setUp() # exécute la connexion BibGestion

        self.media_types = ['LIVRE', 'DVD', 'CD']
        self.expected_titles = {
            'LIVRE': 'Liste des livres',
            'DVD': 'Liste des DVD',
            'CD': 'Liste des CD'
        }

    def test_nav_07_url_and_template(self):
        """T-NAV-07 : Vérifie l’accès et le template pour chaque type"""
        for media_type in self.media_types:
            with self.subTest(media_type=media_type):
                response = self.client.get(f"{self.url}?type={media_type}")
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'bibliothecaire/medias/media_list.html')

    def test_ent_07_type_objects_only(self):
        """T-ENT-07 : Vérifie que tous les objets affichés ont le bon media_type"""
        for media_type in self.media_types:
            with self.subTest(media_type=media_type):
                response = self.client.get(f"{self.url}?type={media_type}")
                for media in response.context['medias']:
                    self.assertEqual(media.media_type, media_type)

    def test_vue_08_title_displayed(self):
        """T-VUE-08 : Vérifie que le titre <h2> correspond au type demandé"""
        for media_type in self.media_types:
            with self.subTest(media_type=media_type):
                response = self.client.get(f"{self.url}?type={media_type}")
                self.assertContains(response, f"<h2>{self.expected_titles[media_type]}</h2>")

    def test_fun_03_uc_list_03_verification(self):
        """
        T-FUN-03 : Vérifie la cohérence fonctionnelle de UC-LIST-03
        - Accès OK
        - Template utilisé
        - Titre affiché
        - Objets filtrés correctement
        """
        for media_type in self.media_types:
            with self.subTest(media_type=media_type):
                response = self.client.get(f"{self.url}?type={media_type}")
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'bibliothecaire/medias/media_list.html')
                self.assertContains(response, f"<h2>{self.expected_titles[media_type]}</h2>")
                for media in response.context['medias']:
                    self.assertEqual(media.media_type, media_type)

class MediaNonTypeViewTests(LoginRequiredTestCase):
    fixtures = ['medias_test.json', 'media_untyped_fixture.json']

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        cls.url = reverse('bibliothecaire:media_list_non_types')

    def setUp(self):
        super().setUp() # exécute la connexion BibGestion

        self.media_types = ['NON_DEFINI']
        self.expected_titles = {
            'NON_DEFINI': 'Liste des médias "non définis" (en attente de définition)'
        }

    def test_nav_09_url_and_template(self):
        """T-NAV-09 : Vérifie l’accès et le template pour chaque type"""
        for media_type in self.media_types:
            with self.subTest(media_type=media_type):
                response = self.client.get(f"{self.url}?type={media_type}")
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'bibliothecaire/medias/media_list.html')

    def test_ent_09_type_objects_only(self):
        """T-ENT-09 : Vérifie que tous les objets affichés ont le bon media_type"""
        for media_type in self.media_types:
            with self.subTest(media_type=media_type):
                response = self.client.get(f"{self.url}?type={media_type}")
                for media in response.context['medias']:
                    self.assertEqual(media.media_type, media_type)

    def test_vue_10_title_displayed(self):
        """T-VUE-10 : Vérifie que le titre <h2> correspond au type demandé"""
        for media_type in self.media_types:
            with self.subTest(media_type=media_type):
                response = self.client.get(f"{self.url}?type={media_type}")
                self.assertContains(response, f"<h2>{self.expected_titles[media_type]}</h2>")

    def test_fun_06_uc_list_06_verification(self):
        """
        T-FUN-06 : Vérifie la cohérence fonctionnelle de UC-LIST-04
        - Accès OK
        - Template utilisé
        - Titre affiché
        - Objets filtrés correctement
        """
        for media_type in self.media_types:
            with self.subTest(media_type=media_type):
                response = self.client.get(f"{self.url}?type={media_type}")
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'bibliothecaire/medias/media_list.html')
                self.assertContains(response, f"<h2>{self.expected_titles[media_type]}</h2>")
                for media in response.context['medias']:
                    self.assertEqual(media.media_type, media_type)