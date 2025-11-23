from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class BaseAccountsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Création des données pour les tests
        cls.admin = User.objects.create_superuser(
            username="admin",
            email="admin.test@localhost",
            password="admin-MdP"
        )
        cls.url_accueil = reverse("accounts:accueil")
        cls.url_login = reverse("accounts:login")
        cls.url_logout = reverse("accounts:logout")
        cls.url_bib_accueil = reverse("bibliothecaire:accueil")
        cls.url_consult_accueil = reverse("consultation:accueil")

        cls.template_accueil = "accounts/accueil.html"
        cls.template_login = "accounts/login.html"
        cls.template_logout = "accounts/logout.html"

    def login_admin(self):
        return self.client.post(
            self.url_login,
            {"username": "admin", "password": "admin-MdP"},  # mot de passe de l'admin créé pour le test
            follow=True
        )

    def logout_admin(self):
        return self.client.post(self.url_logout, follow=True)


# 🧭 Navigation – ACCUEIL-UC-NAVIGATION
class TestNavigationAccueil(BaseAccountsTestCase):
    def test_nav_38_acces_accueil_mediatheque(self):
        response = self.client.get(self.url_accueil)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_accueil)

    def test_nav_39_lien_bibliothecaire(self):
        response = self.client.get(self.url_bib_accueil)
        self.assertEqual(response.status_code, 200)

    def test_nav_40_lien_consultation(self):
        response = self.client.get(self.url_consult_accueil)
        self.assertEqual(response.status_code, 200)

    def test_nav_41_lien_connexion_affiche_si_non_connecte(self):
        response = self.client.get(self.url_login)
        self.assertContains(response, "Connexion")

    def test_nav_42_lien_deconnexion_affiche_si_connecte(self):
        self.login_admin()
        response = self.client.get(self.url_accueil)
        self.assertContains(response, "Déconnexion (admin)")


# 🧪 Fonctionnel – COMPTE-UC-GESTION
class TestFonctionnelAccounts(BaseAccountsTestCase):
    def test_fun_52_connexion_valide_redirige_accueil(self):
        response = self.login_admin()
        self.assertRedirects(response, self.url_accueil)

    def test_fun_53_connexion_invalide_affiche_erreur(self):
        response = self.client.post(
            self.url_login,
            {"username": "admin", "password": "mauvais"},
            follow=True
        )
        self.assertContains(response, "Saisissez un nom d’utilisateur et un mot de passe valides")

    def test_fun_54_deconnexion_redirige_accueil_bibliothecaire(self):
        self.login_admin()
        response = self.logout_admin()
        self.assertRedirects(response, self.url_accueil)

    def test_fun_55_menu_affiche_connexion_ou_deconnexion_selon_etat(self):
        # Non connecté
        response = self.client.get(self.url_accueil)
        self.assertContains(response, "Connexion")
        # Connecté
        self.login_admin()
        response = self.client.get(self.url_accueil)
        self.assertContains(response, "Déconnexion (admin)")

    def test_fun_56_affichage_nom_utilisateur_connecte(self):
        self.login_admin()
        response = self.client.get(self.url_accueil)
        self.assertContains(response, "Déconnexion (admin)")
