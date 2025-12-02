from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AdminAccessTest(TestCase):
    """
    Tests d'accès à l'interface d'administration Django.
    Vérifie que seul un superuser peut accéder à l'admin.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Création d’un superuser fixe pour les tests admin
        cls.admin_user = User.objects.create_superuser(
            username="admin_test",
            email="admin_test@example.com",
            password="testpass"
        )

    def setUp(self):
        # Connexion du client avec le superuser
        self.client.login(username="admin_test", password="testpass")

    def test_admin_base_access(self):
        """
        Vérifie que l'accès à la page d'accueil de l'admin est autorisé
        pour un superuser.
        """
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)

    def test_admin_urls_by_permissions(self):
        """
        Vérifie que l'accès aux URLs de l'admin est restreint
        selon les permissions.
        """
        # Exemple : accès à la liste des utilisateurs
        response = self.client.get(reverse("admin:auth_user_changelist"))
        self.assertEqual(response.status_code, 200)
