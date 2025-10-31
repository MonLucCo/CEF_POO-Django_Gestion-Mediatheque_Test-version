from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Membre, StatutMembre
from datetime import datetime


class BaseMembreDeleteTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.membre_sans_emprunt = Membre.objects.create(
            name="second membre *222",
            compte="2025_second_membre_222",
            statut=StatutMembre.EMPRUNTEUR
        )
        cls.membre_avec_emprunt = Membre.objects.create(
            name="Martin",
            compte="membre2",
            statut=StatutMembre.EMPRUNTEUR
        )
        # Simuler un emprunt actif
        from bibliothecaire.models import Media, Emprunt
        media = Media.objects.create(name="TestMedia", consultable=True, disponible=True, theme="Test")
        Emprunt.objects.create(media=media, emprunteur=cls.membre_avec_emprunt)


# 🧭 Navigation
class TestNavigationMembreUcDelete(BaseMembreDeleteTestCase):
    def test_nav_18_acces_vue_confirmation_suppression(self):
        response = self.client.get(reverse("bibliothecaire:membre_delete", kwargs={"pk": self.membre_sans_emprunt.pk}))
        self.assertEqual(response.status_code, 200)


# 🧪 Entités
class TestEntitesMembreUcDelete(BaseMembreDeleteTestCase):
    def test_ent_17_suppression_logique_membre_sans_emprunt(self):
        self.client.post(reverse("bibliothecaire:membre_delete", kwargs={"pk": self.membre_sans_emprunt.pk}))
        self.membre_sans_emprunt.refresh_from_db()
        self.assertEqual(self.membre_sans_emprunt.statut, StatutMembre.ARCHIVE)

    def test_ent_18_refus_suppression_membre_avec_emprunt(self):
        self.client.post(reverse("bibliothecaire:membre_delete", kwargs={"pk": self.membre_avec_emprunt.pk}))
        self.membre_avec_emprunt.refresh_from_db()
        self.assertNotEqual(self.membre_avec_emprunt.statut, StatutMembre.ARCHIVE)


# 🧪 Vues
class TestVuesMembreUcDelete(BaseMembreDeleteTestCase):
    def test_vue_19_lien_suppression_visible_si_autorisé(self):
        response = self.client.get(reverse("bibliothecaire:membre_detail", kwargs={"pk": self.membre_sans_emprunt.pk}))
        self.assertContains(response, "Supprimer ce membre")

    def test_vue_20_lien_suppression_non_visible_si_emprunt(self):
        response = self.client.get(reverse("bibliothecaire:membre_detail", kwargs={"pk": self.membre_avec_emprunt.pk}))
        self.assertNotContains(response, "Supprimer ce membre")


# 🧪 Formulaires
class TestFormulairesMembreUcDelete(BaseMembreDeleteTestCase):
    def test_form_07_confirmation_suppression_affiche_donnees(self):
        response = self.client.get(reverse("bibliothecaire:membre_delete", kwargs={"pk": self.membre_sans_emprunt.pk}))
        self.assertContains(response, self.membre_sans_emprunt.name)
        self.assertContains(response, self.membre_sans_emprunt.compte)
        self.assertContains(response, "Confirmer la suppression")


# 🧪 Fonctionnel
class TestFonctionnelMembreUcDelete(BaseMembreDeleteTestCase):
    def test_fun_19_suppression_reussie_membre_sans_emprunt(self):
        response = self.client.post(reverse("bibliothecaire:membre_delete", kwargs={"pk": self.membre_sans_emprunt.pk}))
        self.assertEqual(response.status_code, 302)
        self.membre_sans_emprunt.refresh_from_db()
        self.assertEqual(self.membre_sans_emprunt.statut, StatutMembre.ARCHIVE)

    def test_fun_20_suppression_refusee_membre_avec_emprunt(self):
        response = self.client.post(reverse("bibliothecaire:membre_delete", kwargs={"pk": self.membre_avec_emprunt.pk}))
        self.assertEqual(response.status_code, 302)
        self.membre_avec_emprunt.refresh_from_db()
        self.assertNotEqual(self.membre_avec_emprunt.statut, StatutMembre.ARCHIVE)
