from django.test import TestCase
from bibliothecaire.models import Media, Livre


class MediaEntityTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Création d’un Media seul
        cls.monMedia = Media(name="Test Media", media_type="LIVRE", theme="Test Theme Media")
        cls.monMedia.full_clean()
        cls.monMedia.save()

    def test_ent_01_media_livre_creation(self):
        self.assertEqual(self.monMedia.name, "Test Media")
        self.assertEqual(self.monMedia.annee_edition, None)
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

    def test_ent_04a_media_avec_sous_type_livre(self):
        # Création d’un Livre (lié au Media)
        from bibliothecaire.models import Livre

        titreLivre = "Test Media-Livre"
        monLivre = Livre(
            name=titreLivre, media_type="LIVRE", theme="Test Theme Media-Livre",
            auteur="Auteur-Livre", resume="Résumé-Livre"
        )
        monLivre.full_clean()
        monLivre.save()

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
        # Vérifie que le Livre avec pk=2 est un sous-type avec le champ hérité 'annee_edition' vide
        self.assertEqual(Livre.objects.get(pk=2).annee_edition, None)
        # Vérifie que le Livre avec pk=2 est un sous-type avec le champ 'nb_page' vide
        self.assertEqual(Livre.objects.get(pk=2).nb_page, None)

    def test_ent_04b_media_avec_sous_type_dvd(self):
        # Création d’un Dvd (lié au Media)
        from bibliothecaire.models import Dvd

        titreDvd = "Test Media-Dvd"
        monDvd = Dvd(
            name=titreDvd, media_type="DVD", theme="Test Theme Media-Dvd",
            realisateur="Realisateur-Dvd", histoire="Histoire-Dvd"
        )
        monDvd.full_clean()
        monDvd.save()

        # Assertions sur tables en base de données
        self.assertTrue(Media.objects.count() == 2)
        self.assertTrue(Dvd.objects.count() == 1)

        # Assertions sur la table Media
        self.assertEqual(Media.objects.get(pk=1).name, "Test Media")
        self.assertEqual(Media.objects.get(pk=2).name, titreDvd)

        # Assertions sur la table Dvd
        # Vérifie que le Media avec pk=1 n’a pas de sous-type Dvd (et qu'une exception est bien levée)
        with self.assertRaises(Dvd.DoesNotExist):
            Dvd.objects.get(pk=1)
        # Vérifie que le Dvd avec pk=2 est bien un sous-type Dvd de Media et qu'il a la même valeur
        self.assertEqual(Dvd.objects.get(pk=2).name, titreDvd)
        # Vérifie que le Dvd avec pk=2 est un sous-type avec le champ hérité 'annee_edition' vide
        self.assertEqual(Dvd.objects.get(pk=2).annee_edition, None)
        # Vérifie que le Dvd avec pk=2 est un sous-type avec le champ 'duree' vide
        self.assertEqual(Dvd.objects.get(pk=2).duree, None)

    def test_ent_04c_media_avec_sous_type_cd(self):
        # Création d’un Dvd (lié au Media)
        from bibliothecaire.models import Cd

        titreCd = "Test Media-Cd"
        monCd = Cd(
            name=titreCd, media_type="CD", theme="Test Theme Media-Cd",
            artiste="Artiste-Cd"
        )
        monCd.full_clean()
        monCd.save()

        # Assertions sur tables en base de données
        self.assertTrue(Media.objects.count() == 2)
        self.assertTrue(Cd.objects.count() == 1)

        # Assertions sur la table Media
        self.assertEqual(Media.objects.get(pk=1).name, "Test Media")
        self.assertEqual(Media.objects.get(pk=2).name, titreCd)

        # Assertions sur la table Cd
        # Vérifie que le Media avec pk=1 n’a pas de sous-type Cd (et qu'une exception est bien levée)
        with self.assertRaises(Cd.DoesNotExist):
            Cd.objects.get(pk=1)
        # Vérifie que le Cd avec pk=2 est bien un sous-type Cd de Media et qu'il a la même valeur
        self.assertEqual(Cd.objects.get(pk=2).name, titreCd)
        # Vérifie que le Cd avec pk=2 est un sous-type avec le champ hérité 'annee_edition' vide
        self.assertEqual(Cd.objects.get(pk=2).annee_edition, None)
        # Vérifie que le Cd avec pk=2 est un sous-type avec le champ 'nb_piste' avec la valeur par défaut '1'
        self.assertEqual(Cd.objects.get(pk=2).nb_piste, 1)
        # Vérifie que le Dvd avec pk=2 est un sous-type avec le champ 'duree_ecoute' vide
        self.assertEqual(Cd.objects.get(pk=2).duree_ecoute, None)
