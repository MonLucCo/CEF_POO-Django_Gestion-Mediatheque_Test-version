from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Membre, StatutMembre
from datetime import datetime

from bibliothecaire.tests import LoginRequiredTestCase


class BaseMembreUpdateTestCase(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        cls.membre = Membre.objects.create(
            name="Élodie Martin",
            compte="2025_Élodie_Martin_1",
            statut=StatutMembre.MEMBRE
        )


# 🧪 Navigation
class TestNavigationMembreUcUpdate(BaseMembreUpdateTestCase):
    def test_nav_16_acces_vue_update_membre(self):
        response = self.client.get(reverse("bibliothecaire:membre_update", kwargs={"pk": self.membre.pk}))
        self.assertEqual(response.status_code, 200)

    def test_nav_17_acces_vue_activation_emprunteur(self):
        response = self.client.get(reverse("bibliothecaire:membre_activate_emprunteur", kwargs={"pk": self.membre.pk}))
        self.assertEqual(response.status_code, 200)


# 🧪 Entités
class TestEntitesMembreUcUpdate(BaseMembreUpdateTestCase):
    def test_ent_15_modification_nom_membre(self):
        data = {"name": "Élodie M."}
        self.client.post(reverse("bibliothecaire:membre_update", kwargs={"pk": self.membre.pk}), data)
        self.membre.refresh_from_db()
        self.assertEqual(self.membre.name, "Élodie M.")

    def test_ent_16_activation_statut_emprunteur(self):
        self.client.post(reverse("bibliothecaire:membre_activate_emprunteur", kwargs={"pk": self.membre.pk}))
        self.membre.refresh_from_db()
        self.assertEqual(self.membre.statut, StatutMembre.EMPRUNTEUR)


# 🧪 Vues
class TestVuesMembreUcUpdate(BaseMembreUpdateTestCase):
    def test_vue_17_formulaire_update_affiche_nom(self):
        response = self.client.get(reverse("bibliothecaire:membre_update", kwargs={"pk": self.membre.pk}))
        self.assertContains(response, "Nom du Membre")
        self.assertContains(response, f'value="{self.membre.name}"')

    def test_vue_18_page_activation_emprunteur(self):
        response = self.client.get(reverse("bibliothecaire:membre_activate_emprunteur", kwargs={"pk": self.membre.pk}))
        self.assertEqual(response.status_code, 200)

        # Vérifie le titre principal
        self.assertContains(response, "<h2>Activer le statut emprunteur</h2>")

        # Vérifie les données du membre affichées
        self.assertContains(response, f"<li><strong>Nom :</strong> {self.membre.name}</li>")
        self.assertContains(response, f"<li><strong>Compte :</strong> {self.membre.compte}</li>")

        # Vérifie le message d’alerte en rouge
        self.assertContains(response, '<p style="color: red;"><strong>Attention :</strong> cette opération est <u>irréversible</u>.</p>')


# 🧪 Formulaires
class TestFormulairesMembreUcUpdate(BaseMembreUpdateTestCase):
    def test_form_05_champ_name_visible_et_modifiable(self):
        response = self.client.get(reverse("bibliothecaire:membre_update", kwargs={"pk": self.membre.pk}))
        self.assertContains(response, 'name="name"')
        self.assertNotContains(response, 'name="statut"')
        self.assertNotContains(response, 'name="compte"')

    def test_form_06_champ_statut_non_expose(self):
        response = self.client.get(reverse("bibliothecaire:membre_update", kwargs={"pk": self.membre.pk}))
        self.assertNotContains(response, 'name="statut"')


# 🧪 Fonctionnel
class TestFonctionnelMembreUcUpdate(BaseMembreUpdateTestCase):
    def test_fun_16_uc_update_01_modifie_nom(self):
        data = {"name": "Élodie M."}
        response = self.client.post(reverse("bibliothecaire:membre_update", kwargs={"pk": self.membre.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.membre.refresh_from_db()
        self.assertEqual(self.membre.name, "Élodie M.")

    def test_fun_17_uc_update_02_active_emprunteur(self):
        response = self.client.post(reverse("bibliothecaire:membre_activate_emprunteur", kwargs={"pk": self.membre.pk}))
        self.assertEqual(response.status_code, 302)
        self.membre.refresh_from_db()
        self.assertEqual(self.membre.statut, StatutMembre.EMPRUNTEUR)

    def test_fun_18_uc_update_02_enchainement_activation_emprunteur(self):
        # Étape 1 : affichage de la page de confirmation
        response_get = self.client.get(reverse("bibliothecaire:membre_activate_emprunteur", kwargs={"pk": self.membre.pk}))
        self.assertEqual(response_get.status_code, 200)
        self.assertContains(response_get, "Confirmer l’activation")

        # Étape 2 : soumission du formulaire
        response_post = self.client.post(reverse("bibliothecaire:membre_activate_emprunteur", kwargs={"pk": self.membre.pk}))
        self.assertEqual(response_post.status_code, 302)

        # Étape 3 : vérification du statut et de la redirection
        self.membre.refresh_from_db()
        self.assertEqual(self.membre.statut, StatutMembre.EMPRUNTEUR)
