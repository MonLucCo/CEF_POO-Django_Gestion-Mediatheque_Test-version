from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Media
from bibliothecaire.tests import LoginRequiredTestCase


class MediaCreateTests(LoginRequiredTestCase):
    fixtures = []

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire
        cls.url = reverse('bibliothecaire:media_create')

    def test_nav_08_access_create_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_vue_09_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'bibliothecaire/medias/media_form.html')

    def test_ent_08_created_media_has_expected_values(self):
        data = {
            'name': 'Média temporaire',
            'theme': 'À classer'
        }
        self.client.post(self.url, data)
        media = Media.objects.get(name='Média temporaire')
        self.assertEqual(media.media_type, 'NON_DEFINI')
        self.assertFalse(media.consultable)
        self.assertFalse(media.disponible)
        self.assertIsNone(media.annee_edition)

    def test_form_01_fields_present(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'name')
        self.assertContains(response, 'theme')
        self.assertContains(response, 'annee_edition')

    def test_form_02_labels_customized(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'Titre du média')
        self.assertContains(response, 'Thématique')
        self.assertContains(response, "Année d'édition")

    def test_form_03_required_and_optional_fields(self):
        response = self.client.get(self.url)
        form = response.context['form']
        self.assertTrue(form.fields['name'].required)
        self.assertTrue(form.fields['theme'].required)
        self.assertFalse(form.fields['annee_edition'].required)

    def test_fun_04_valid_creation_redirects(self):
        data = {
            'name': 'Validé',
            'theme': 'Test T-FUN-04',
        }
        response = self.client.post(self.url, data)

        # Vérifie la redirection attendue après la validation correcte du formulaire
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('bibliothecaire:media_list'))

        # Vérifie la bonne création de l'objet Media
        media_qs = Media.objects.filter(**data)
        self.assertEqual(media_qs.count(), 1)

        # Vérifie le contenu correct de l'objet Media (non typé) en base
        media = media_qs.first()
        self.assertEqual(media.media_type, 'NON_DEFINI')
        self.assertFalse(media.consultable)
        self.assertFalse(media.disponible)
        self.assertIsNone(media.annee_edition)

    def test_fun_05_missing_required_field_name(self):
        data = {
            'theme': 'Thème Test T-FUN-05'
        }
        response = self.client.post(self.url, data)

        # Vérifie le rendu d'un formulaire qui n'a pas été validé
        self.assertEqual(response.status_code, 200)

        # Vérifie que le formulaire est bien dans le contexte
        form = response.context.get('form')
        self.assertIsNotNone(form)
        self.assertTrue(form.is_bound)

        # Vérifie l’erreur sur le champ 'name'
        self.assertIn('name', form.errors)
        self.assertIn('Ce champ est obligatoire.', form.errors['name'])

        # Vérifie qu’aucun objet Media n’a été créé
        self.assertFalse(Media.objects.filter(**data).exists())

    def test_fun_07_creation_typage_etat_metier(self):
        """
        T-FUN-07 : Vérifie la transition métier (0) et (0+1) pour chaque média typé (Livre, Dvd, Cd)
        Le test utilise les vues typées de création et remplit les champs spécifiques requis.
        Il valide que :
         - un média créé avec consultable=False est en état 1 (disponible=True).
         - un média créé avec consultable=True est en état 3 (disponible=True).
        """

        # Initial State : état 0 (début)
        types = {
            'livre': {'auteur': 'Auteur Test', 'resume': 'Résumé Test'},
            'dvd': {'realisateur': 'Réalisateur Test', 'histoire': 'Histoire Test'},
            'cd': {'artiste': 'Artiste Test', 'nb_piste' : 1}
        }

        for media_type, specific_fields in types.items():
            with self.subTest(media_type=media_type):
                url = reverse(f'bibliothecaire:media_create_{media_type}')

                # Création en état 1 : consultable=False
                data_attente = {
                    'name': f'Média {media_type} attente',
                    'theme': 'Test T-FUN-07',
                    'media_type': media_type,
                    'consultable': False,
                    **specific_fields
                }
                response = self.client.post(url, data_attente)
                self.assertEqual(response.status_code, 302)
                media = Media.objects.get(name=data_attente['name'])
                self.assertFalse(media.consultable)
                self.assertTrue(media.disponible)

                # Création en état 3 : consultable=True
                data_empruntable = {
                    'name': f'Média {media_type} prêt',
                    'theme': 'Test T-FUN-07',
                    'media_type': media_type,
                    'consultable': True,
                    **specific_fields
                }
                response = self.client.post(url, data_empruntable)
                self.assertEqual(response.status_code, 302)
                media = Media.objects.get(name=data_empruntable['name'])
                self.assertTrue(media.consultable)
                self.assertTrue(media.disponible)
