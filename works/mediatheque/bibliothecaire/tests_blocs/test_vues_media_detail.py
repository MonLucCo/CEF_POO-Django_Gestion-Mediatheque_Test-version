from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Media, Livre, Dvd, Cd


class MediaDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.media = Media(name="Test Media", theme="Test Thème")
        cls.media.full_clean()
        cls.media.save()
        cls.livre = Livre(
            name="Test Media-Livre", media_type="LIVRE", theme="Test Thème Media-Livre",
            auteur="Auteur Test Livre", resume="Résumé Test Livre"
        )
        cls.livre.full_clean()
        cls.livre.save()
        cls.dvd = Dvd(
            name="Test Media-Dvd", media_type="DVD", theme="Test Thème Media-Dvd",
            realisateur="Réalisateur Test Dvd", histoire="Histoire Test Dvd"
        )
        cls.dvd.full_clean()
        cls.dvd.save()
        cls.cd = Cd(
            name="Test Media-Cd", media_type="CD", theme="Test Thème Media-Cd",
            artiste="Artiste Test Cd"
        )
        cls.cd.full_clean()
        cls.cd.save()

    def test_vue_03_media_detail_vue_type(self):
        # Vue de détail des objets typés (Livre, Dvd et Cd)
        responseLivre = self.client.get(reverse('bibliothecaire:media_detail', args=[self.livre.pk]))
        self.assertContains(responseLivre, "Auteur Test Livre")
        self.assertContains(responseLivre, "Test Thème Media-Livre")
        self.assertNotContains(responseLivre, "Année")
        responseDvd = self.client.get(reverse('bibliothecaire:media_detail', args=[self.dvd.pk]))
        self.assertContains(responseDvd, "Réalisateur Test Dvd")
        self.assertContains(responseDvd, "Test Thème Media-Dvd")
        self.assertNotContains(responseDvd, "Année")
        responseCd = self.client.get(reverse('bibliothecaire:media_detail', args=[self.cd.pk]))
        self.assertContains(responseCd, "Artiste Test Cd")
        self.assertContains(responseCd, "Test Thème Media-Cd")
        self.assertNotContains(responseCd, "Année")

    def test_vue_04a_media_detail_instance_type_livre(self):
        response = self.client.get(reverse('bibliothecaire:media_detail', args=[self.livre.pk]))
        media_obj = response.context['media']
        # Vérification du contenu
        self.assertEqual(type(media_obj).__name__, "Livre")
        self.assertEqual(media_obj.name, "Test Media-Livre")
        self.assertEqual(media_obj.annee_edition, None)
        self.assertEqual(media_obj.consultable, True)
        self.assertEqual(media_obj.disponible, True)
        self.assertEqual(media_obj.theme, "Test Thème Media-Livre")
        self.assertEqual(media_obj.media_type, "LIVRE")
        self.assertEqual(media_obj.auteur, "Auteur Test Livre")
        self.assertEqual(media_obj.nb_page, None)
        self.assertEqual(media_obj.resume, "Résumé Test Livre")
        # Vérification de l'affichage détaillé
        self.assertContains(response, "<th>Titre</th>")
        self.assertContains(response, f"<td>{media_obj.name}</td>")
        self.assertContains(response, "<th>Type</th>")
        self.assertContains(response, f"<td>{media_obj.media_type}</td>")
        self.assertNotContains(response, "<th>Année</th>")
        self.assertContains(response, "<th>Disponible</th>")
        expected_consultable = "Oui" if media_obj.consultable else "Non"
        self.assertContains(response, f"<td>{expected_consultable}</td>")
        self.assertContains(response, "<th>Thème</th>")
        self.assertContains(response, f"<td>{media_obj.theme}</td>")
        self.assertContains(response, "<th>Disponible</th>")
        expected_disponible = "Oui" if media_obj.disponible else "Non"
        self.assertContains(response, f"<td>{expected_disponible}</td>")
        self.assertContains(response, "<th>Auteur</th>")
        self.assertContains(response, f"<td>{media_obj.auteur}</td>")
        self.assertContains(response, "<th>Nombre de pages</th>")
        expected_nb_page = media_obj.nb_page if media_obj.nb_page else "non saisie"
        self.assertContains(response, f"<td>{expected_nb_page}</td>")
        self.assertContains(response, "<th>Résumé</th>")
        self.assertContains(response, f"<td>{media_obj.resume}</td>")

    def test_vue_04b_media_detail_instance_type_dvd(self):
        response = self.client.get(reverse('bibliothecaire:media_detail', args=[self.dvd.pk]))
        media_obj = response.context['media']
        # Vérification du contenu
        self.assertEqual(type(media_obj).__name__, "Dvd")
        self.assertEqual(media_obj.name, "Test Media-Dvd")
        self.assertEqual(media_obj.annee_edition, None)
        self.assertEqual(media_obj.consultable, True)
        self.assertEqual(media_obj.disponible, True)
        self.assertEqual(media_obj.theme, "Test Thème Media-Dvd")
        self.assertEqual(media_obj.media_type, "DVD")
        self.assertEqual(media_obj.realisateur, "Réalisateur Test Dvd")
        self.assertEqual(media_obj.duree, None)
        self.assertEqual(media_obj.histoire, "Histoire Test Dvd")
        # Vérification de l'affichage détaillé
        self.assertContains(response, "<th>Titre</th>")
        self.assertContains(response, f"<td>{media_obj.name}</td>")
        self.assertContains(response, "<th>Type</th>")
        self.assertContains(response, f"<td>{media_obj.media_type}</td>")
        self.assertNotContains(response, "<th>Année</th>")
        self.assertContains(response, "<th>Disponible</th>")
        expected_consultable = "Oui" if media_obj.consultable else "Non"
        self.assertContains(response, f"<td>{expected_consultable}</td>")
        self.assertContains(response, "<th>Thème</th>")
        self.assertContains(response, f"<td>{media_obj.theme}</td>")
        self.assertContains(response, "<th>Disponible</th>")
        expected_disponible = "Oui" if media_obj.disponible else "Non"
        self.assertContains(response, f"<td>{expected_disponible}</td>")
        self.assertContains(response, "<th>Réalisateur</th>")
        self.assertContains(response, f"<td>{media_obj.realisateur}</td>")
        self.assertContains(response, "<th>Durée</th>")
        expected_duree = f"{media_obj.duree} minute(s)" if media_obj.duree else "non saisie"
        self.assertContains(response, f"<td>{expected_duree}</td>")
        self.assertContains(response, "<th>Histoire</th>")
        self.assertContains(response, f"<td>{media_obj.histoire}</td>")

    def test_vue_04c_media_detail_instance_type_cd(self):
        response = self.client.get(reverse('bibliothecaire:media_detail', args=[self.cd.pk]))
        media_obj = response.context['media']
        # Vérification du contenu
        self.assertEqual(type(media_obj).__name__, "Cd")
        self.assertEqual(media_obj.name, "Test Media-Cd")
        self.assertEqual(media_obj.annee_edition, None)
        self.assertEqual(media_obj.consultable, True)
        self.assertEqual(media_obj.disponible, True)
        self.assertEqual(media_obj.theme, "Test Thème Media-Cd")
        self.assertEqual(media_obj.media_type, "CD")
        self.assertEqual(media_obj.artiste, "Artiste Test Cd")
        self.assertEqual(media_obj.nb_piste, 1)
        self.assertEqual(media_obj.duree_ecoute, None)
        # Vérification de l'affichage détaillé
        self.assertContains(response, "<th>Titre</th>")
        self.assertContains(response, f"<td>{media_obj.name}</td>")
        self.assertContains(response, "<th>Type</th>")
        self.assertContains(response, f"<td>{media_obj.media_type}</td>")
        self.assertNotContains(response, "<th>Année</th>")
        self.assertContains(response, "<th>Disponible</th>")
        expected_consultable = "Oui" if media_obj.consultable else "Non"
        self.assertContains(response, f"<td>{expected_consultable}</td>")
        self.assertContains(response, "<th>Thème</th>")
        self.assertContains(response, f"<td>{media_obj.theme}</td>")
        self.assertContains(response, "<th>Disponible</th>")
        expected_disponible = "Oui" if media_obj.disponible else "Non"
        self.assertContains(response, f"<td>{expected_disponible}</td>")
        self.assertContains(response, "<th>Artiste</th>")
        self.assertContains(response, f"<td>{media_obj.artiste}</td>")
        self.assertContains(response, "<th>Nombre de pistes</th>")
        self.assertContains(response, f"<td>{media_obj.nb_piste}</td>")
        self.assertContains(response, "<th>Durée d'écoute</th>")
        expected_duree_ecoute = f"{media_obj.duree_ecoute} minute(s)" if media_obj.duree_ecoute else "non saisie"
        self.assertContains(response, f"<td>{expected_duree_ecoute}</td>")

    def test_vue_05_media_detail_vue_sans_type(self):
        # Vue de détail d'un objet non typé (Media)
        responseMedia = self.client.get(reverse('bibliothecaire:media_detail', args=[self.media.pk]))
        media_obj = responseMedia.context['media']
        expected_media_type = media_obj.media_type if media_obj.media_type != 'NON_DEFINI' else "Non défini"
        self.assertContains(responseMedia, f"<td>{expected_media_type}</td>")
        self.assertNotContains(responseMedia, "Auteur Test Livre")
        self.assertNotContains(responseMedia, "Résumé Test Livre")
        self.assertNotContains(responseMedia, "Année")