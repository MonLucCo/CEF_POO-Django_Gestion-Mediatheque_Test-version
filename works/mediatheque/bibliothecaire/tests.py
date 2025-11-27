"""
📁 Fichier d’entrée – tests.py

Les tests en "blocs unitaires" sont organisés dans le dossier :
    bibliothecaire/tests_blocs/

Voir le plan complet :
    /docs/developpement/dev-docs/devTests.md
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.db import models

from bibliothecaire.models import Bibliothecaire, RoleBibliothecaire


class LoginRequiredTestCase(TestCase):
    """
    Base de tests avec gestion de connexion/déconnexion.

    @class LoginRequiredTestCase
    @description
    @description
     - Crée et expose tous les comptes utilisables en login: Superuser, Staff, BibAdmin, BibGestion.
     - Connecte par défaut BibGestion avant chaque test.
     - Fournit des helpers centralisés (login/logout/current_user).

    @methods
     - login_as(role): Connecte selon le rôle demandé (RoleTest.GESTION, ADMIN, SUPERADMIN, STAFF).
     - logout(): Déconnecte l'utilisateur connecté.
     - current_user(): Retourne le nom de l’utilisateur connecté ou None.
    """
    class RoleTest(models.IntegerChoices):
        ADMIN = 1, "Admin"
        GESTION = 2, "Gestion"
        SUPERADMIN = 3, "Superadmin"
        STAFF = 4, "Staff"

    @classmethod
    def setUpTestData(cls):
        # Création des comptes User de test
        cls.user_gestion = User.objects.create_user(
            username="testbib_gestion", password="secret", email="gestion@example.com"
        )
        cls.user_admin = User.objects.create_user(
            username="testbib_admin", password="secret", email="admin@example.com"
        )
        cls.user_superadmin = User.objects.create_superuser(
            username="superadmin", password="secret", email="superadmin@example.com"
        )
        cls.user_staff = User.objects.create_user(
            username="staff", password="secret", email="staff@example.com", is_staff=True
        )
        # Création des comptes Bibliothécaires de test
        cls.bib_gestion = Bibliothecaire.objects.create(
            name="BibGestion", user=cls.user_gestion, role=cls.RoleTest.GESTION
        )
        cls.bib_admin = Bibliothecaire.objects.create(
            name="BibAdmin", user=cls.user_admin, role=cls.RoleTest.ADMIN
        )

    def setUp(self):
        # Connexion par défaut : BibGestion
        self.login_as(self.RoleTest.GESTION)

    # --- Helpers génériques ---
    def login_as(self, role: RoleTest):
        """Connecte le client selon le rôle demandé."""
        if role == self.RoleTest.GESTION:
            ok = self.client.login(username="testbib_gestion", password="secret")
        elif role == self.RoleTest.ADMIN:
            ok = self.client.login(username="testbib_admin", password="secret")
        elif role == self.RoleTest.SUPERADMIN:
            ok = self.client.login(username="superadmin", password="secret")
        elif role == self.RoleTest.STAFF:
            ok = self.client.login(username="staff", password="secret")
        else:
            raise ValueError(f"Rôle inconnu: {role}")

        assert ok, f"Échec de connexion pour le rôle {role.label}"

    def logout(self):
        """Déconnecte l'utilisateur'."""
        self.client.logout()

    def current_user(self):
        """Retourne le nom de l’utilisateur connecté ou None."""
        uid = self.client.session.get("_auth_user_id")
        return User.objects.get(pk=uid).username if uid else None


class BibliothecaireAccessTest(LoginRequiredTestCase):
    def test_access_with_login(self):
        response = self.client.get(reverse("bibliothecaire:accueil"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'table id="menu-bibliothecaire"')
