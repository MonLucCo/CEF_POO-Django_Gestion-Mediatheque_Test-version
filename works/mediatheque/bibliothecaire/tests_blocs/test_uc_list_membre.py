from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Membre, StatutMembre


class BaseMembreTestCaseData(TestCase):
    @classmethod
    def setUpTestData(cls):
        Membre.objects.create(name="Alice", compte="alice01", statut=StatutMembre.EMPRUNTEUR)
        Membre.objects.create(name="Bob", compte="bob02", statut=StatutMembre.MEMBRE)
        Membre.objects.create(name="Charlie", compte="charlie03", statut=StatutMembre.ARCHIVE)


# 🧪 Navigation
class TestNavigationMembreUcList(TestCase):
    def test_nav_10_acces_vue_tous_les_membres(self):
        response = self.client.get(reverse("bibliothecaire:membre_list"))
        self.assertEqual(response.status_code, 200)

    def test_nav_11_acces_vue_membres_en_gestion(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_gestion"))
        self.assertEqual(response.status_code, 200)

    def test_nav_12_acces_vue_membres_emprunteurs(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_emprunteurs"))
        self.assertEqual(response.status_code, 200)

    def test_nav_13_acces_vue_membres_supprimes(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_archives"))
        self.assertEqual(response.status_code, 200)


# 🧪 Entités
class TestEntitesMembreUcList(BaseMembreTestCaseData):
    def test_ent_10_filtrage_statut_non_archive(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_gestion"))
        for membre in response.context["membres"]:
            self.assertNotEqual(membre.statut, StatutMembre.ARCHIVE)

    def test_ent_11_filtrage_statut_emprunteur(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_emprunteurs"))
        for membre in response.context["membres"]:
            self.assertEqual(membre.statut, StatutMembre.EMPRUNTEUR)

    def test_ent_12_filtrage_statut_archive(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_archives"))
        for membre in response.context["membres"]:
            self.assertEqual(membre.statut, StatutMembre.ARCHIVE)


# 🧪 Vues
class TestVuesMembreUcList(BaseMembreTestCaseData):
    def test_vue_11_tableau_colonnes_presentes(self):
        response = self.client.get(reverse("bibliothecaire:membre_list"))
        self.assertContains(response, "<th>Nom</th>")
        self.assertContains(response, "<th>Compte</th>")
        self.assertContains(response, "<th>Statut</th>")
        self.assertContains(response, "<th>Emprunts</th>")
        self.assertContains(response, "<th>Retards</th>")

    def test_vue_12_affichage_membres_non_archives(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_gestion"))
        self.assertContains(response, "Alice")
        self.assertContains(response, "Bob")
        self.assertNotContains(response, "Charlie")

    def test_vue_13_affichage_membres_emprunteurs(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_emprunteurs"))
        self.assertContains(response, "Alice")
        self.assertNotContains(response, "Bob")
        self.assertNotContains(response, "Charlie")

    def test_vue_14_affichage_membres_archives(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_archives"))
        self.assertContains(response, "Charlie")
        self.assertNotContains(response, "Alice")
        self.assertNotContains(response, "Bob")

    def test_vue_15_tableau_conditionnel_si_liste_vide(self):
        Membre.objects.all().delete()
        response = self.client.get(reverse("bibliothecaire:membre_list"))
        self.assertContains(response, "Aucun membre trouvé.")
        self.assertEqual(Membre.objects.count(), 0)
        self.assertNotContains(response, '<table id="liste-annuaire">')


# 🧪 Fonctionnel
class TestFonctionnelMembreUcList(BaseMembreTestCaseData):
    def test_fun_11_uc_list_02_membres_non_archives(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_gestion"))
        for membre in response.context["membres"]:
            self.assertNotEqual(membre.statut, StatutMembre.ARCHIVE)

    def test_fun_12_uc_list_03_membres_emprunteurs(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_emprunteurs"))
        for membre in response.context["membres"]:
            self.assertEqual(membre.statut, StatutMembre.EMPRUNTEUR)

    def test_fun_13_uc_list_04_membres_archives(self):
        response = self.client.get(reverse("bibliothecaire:membre_list_archives"))
        for membre in response.context["membres"]:
            self.assertEqual(membre.statut, StatutMembre.ARCHIVE)
