from django.urls import reverse
from bibliothecaire.tests import LoginRequiredTestCase


class BaseSecuriteTestCase(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # crée Superuser, Staff, BibAdmin, BibGestion

        cls.url_admin = reverse("admin:index")
        cls.url_accueil_bib = reverse("bibliothecaire:accueil")
        cls.url_accueil_consult = reverse("consultation:accueil")


# 🧭 Navigation – SECURITE-UC-NAVIGATION
class TestNavigationSecurite(BaseSecuriteTestCase):
    def test_sec_01_superuser_acces_admin(self):
        self.login_as(self.RoleTest.SUPERADMIN)
        response = self.client.get(self.url_admin)
        self.assertEqual(response.status_code, 200)

    def test_sec_02_staff_acces_admin_limite(self):
        self.login_as(self.RoleTest.STAFF)
        response = self.client.get(self.url_admin)
        self.assertEqual(response.status_code, 200)
        # Vérifie que le modèle Bibliothecaire n’est pas listé
        self.assertNotContains(response, "Bibliothecaire")


# 🧪 Fonctionnel – SECURITE-UC-PERMISSIONS
class TestFonctionnelSecurite(BaseSecuriteTestCase):
    def test_sec_03_bibadmin_acces_complet_bibliothecaire(self):
        self.login_as(self.RoleTest.ADMIN)
        response = self.client.get(self.url_accueil_bib)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'menu-bibliothecaire')

    def test_sec_04_membre_ou_anonyme_refus_bibliothecaire(self):
        self.logout()
        response = self.client.get(self.url_accueil_bib)
        self.assertEqual(response.status_code, 302)
        # Vérifie la redirection
        self.assertRedirects(response, reverse("accounts:403"))
        # Puis suit la redirection
        response_follow = self.client.get(reverse("accounts:403"))
        self.assertEqual(response_follow.status_code, 200)
        self.assertTemplateUsed(response_follow, "accounts/403.html")

    def test_sec_05_membre_acces_consultation(self):
        self.logout()
        response = self.client.get(self.url_accueil_consult)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "consultation/accueil.html")

    def test_sec_06_superuser_refus_bibliothecaire(self):
        self.login_as(self.RoleTest.SUPERADMIN)
        response = self.client.get(self.url_accueil_bib)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:403"))

    def test_sec_07_staff_refus_bibliothecaire(self):
        self.login_as(self.RoleTest.STAFF)
        response = self.client.get(self.url_accueil_bib)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:403"))
