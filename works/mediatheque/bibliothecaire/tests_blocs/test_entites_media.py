from django.test import TestCase
from bibliothecaire.models import Media, Livre


class MediaEntityTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Création d’un Media seul
        cls.monMedia = Media.objects.create(name="Test Media", annee_edition=0, media_type="LIVRE", theme="Test Theme Media")

    def test_ent_01_media_livre_creation(self):
        self.assertEqual(self.monMedia.name, "Test Media")
        self.assertEqual(self.monMedia.annee_edition, 0)
        self.assertEqual(self.monMedia.theme, "Test Theme Media")
        self.assertEqual(self.monMedia.media_type, "LIVRE")

    def test_ent_02_media_default_values(self):
        self.assertTrue(self.monMedia.consultable)
        self.assertTrue(self.monMedia.disponible)

    def test_ent_03_media_sans_sous_type(self):
        # Ce n'est pas une entité Livre (type)
        self.assertFalse(hasattr(self.monMedia, 'auteur'))
        self.assertFalse(hasattr(self.monMedia, 'nb_page'))
        self.assertFalse(hasattr(self.monMedia, 'resume'))
        # C'est une entité Media (héritage de Support)
        self.assertTrue(hasattr(self.monMedia, 'name'))
        self.assertTrue(hasattr(self.monMedia, 'annee_edition'))
        self.assertTrue(hasattr(self.monMedia, 'consultable'))
        # C'est une entité Media (type)
        self.assertTrue(hasattr(self.monMedia, 'disponible'))
        self.assertTrue(hasattr(self.monMedia, 'theme'))
        self.assertTrue(hasattr(self.monMedia, 'media_type'))

    def test_ent_04_media_avec_sous_type(self):
        # Création d’un Livre (lié au Media)
        from bibliothecaire.models import Livre

        titreLivre = "Test Media-Livre"
        monLivre = Livre.objects.create(
            name=titreLivre, annee_edition=1, media_type="LIVRE", theme="Test Theme Media-Livre",
            auteur="Auteur-Livre", resume="Résumé-Livre", nb_page=0
        )

        # Assertions sur tables en base de données
        self.assertTrue(Media.objects.count() == 2)
        self.assertTrue(Livre.objects.count() == 1)

        # Assertions sur la table Media
        self.assertEqual(Media.objects.get(pk=1).name, "Test Media")
        self.assertEqual(Media.objects.get(pk=2).name, titreLivre)

        # Assertions sur la table Livre
        # Vérifie que le Media avec pk=1 n’a pas de sous-type Livre (et qu'une exception est bien levée)
        with self.assertRaises(Livre.DoesNotExist):
            Livre.objects.get(pk=1)
        # Vérifie que le Livre avec pk=2 est bien un sous-type Livre de Media et qu'il a la même valeur
        self.assertEqual(Livre.objects.get(pk=2).name, titreLivre)
