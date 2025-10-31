from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Membre, StatutMembre
from datetime import datetime


# 🧪 Navigation
class TestNavigationMembreUcCreate(TestCase):
    def test_nav_14_acces_vue_creation_membre(self):
        response = self.client.get(reverse("bibliothecaire:membre_create"))
        self.assertEqual(response.status_code, 200)

    def test_nav_15_acces_vue_creation_emprunteur(self):
        response = self.client.get(reverse("bibliothecaire:membre_create_emprunteur"))
        self.assertEqual(response.status_code, 200)


# 🧪 Entités
class TestEntitesMembreUcCreate(TestCase):
    def test_ent_13_creation_membre_standard_compte_exact(self):
        nom = "Alice Dupont"
        annee = datetime.now().year
        prefixe = f"{annee}_{nom[:30].replace(' ', '_')}_"
        data = {"name": nom}
        self.client.post(reverse("bibliothecaire:membre_create"), data)
        membre = Membre.objects.get(name=nom)
        self.assertEqual(membre.statut, StatutMembre.MEMBRE)
        self.assertEqual(membre.compte, f"{prefixe}1")

    def test_ent_14_creation_membre_emprunteur_compte_exact(self):
        nom = "Bob Martin"
        annee = datetime.now().year
        prefixe = f"{annee}_{nom[:30].replace(' ', '_')}_"
        data = {"name": nom}
        self.client.post(reverse("bibliothecaire:membre_create_emprunteur"), data)
        membre = Membre.objects.get(name=nom)
        self.assertEqual(membre.statut, StatutMembre.EMPRUNTEUR)
        self.assertEqual(membre.compte, f"{prefixe}1")


# 🧪 Vues
class TestVuesMembreUcCreate(TestCase):
    def test_vue_16_titre_dynamique_selon_contexte(self):
        response_membre = self.client.get(reverse("bibliothecaire:membre_create"))
        self.assertContains(response_membre, "Créer un Membre (sans droit d'emprunt)")

        response_emprunteur = self.client.get(reverse("bibliothecaire:membre_create_emprunteur"))
        self.assertContains(response_emprunteur, "Créer un Membre-Emprunteur")


# 🧪 Formulaires
class TestFormulairesMembreUcCreate(TestCase):
    def test_form_04_champ_name_visible_et_label(self):
        response = self.client.get(reverse("bibliothecaire:membre_create"))
        self.assertContains(response, "Nom du Membre")
        self.assertContains(response, 'name="name"')
        self.assertNotContains(response, 'name="statut"')
        self.assertNotContains(response, 'name="compte"')


# 🧪 Fonctionnel
class TestFonctionnelMembreUcCreate(TestCase):
    def test_fun_14_uc_create_01_incrementation_membre_standard(self):
        nom = "Claire Lemoine"
        annee = datetime.now().year
        prefixe = f"{annee}_{nom[:30].replace(' ', '_')}_"

        for i in range(1, 4):
            with self.subTest(compteur=i):
                self.client.post(reverse("bibliothecaire:membre_create"), {"name": nom})
                compte_attendu = f"{prefixe}{i}"
                membre = Membre.objects.get(compte=compte_attendu)
                self.assertEqual(membre.name, nom)
                self.assertEqual(membre.statut, StatutMembre.MEMBRE)

    def test_fun_15_uc_create_02_incrementation_membre_emprunteur(self):
        nom = "David Morel"
        annee = datetime.now().year
        prefixe = f"{annee}_{nom[:30].replace(' ', '_')}_"

        for i in range(1, 4):
            with self.subTest(compteur=i):
                self.client.post(reverse("bibliothecaire:membre_create_emprunteur"), {"name": nom})
                compte_attendu = f"{prefixe}{i}"
                membre = Membre.objects.get(compte=compte_attendu)
                self.assertEqual(membre.name, nom)
                self.assertEqual(membre.statut, StatutMembre.EMPRUNTEUR)