from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import admin

class AdminAccessTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        # Crée un superuser de test avec nom unique
        base_username = 'test_admin'
        suffix = 0
        while True:
            self.test_admin_username = f"{base_username}_{suffix}" if suffix > 0 else base_username
            if not User.objects.filter(username=self.test_admin_username).exists():
                break
            suffix += 1

        self.test_admin_password = 'testpass'
        self.test_admin = User.objects.create_superuser(
            username=self.test_admin_username,
            email='test_admin@example.com',
            password=self.test_admin_password
        )
        self.client.login(username=self.test_admin_username, password=self.test_admin_password)

    def tearDown(self):
        # Supprime le superuser de test après exécution
        User.objects.filter(username=self.test_admin_username).delete()

    def test_admin_base_access(self):
        """
        T-ADM-01 : Vérifie l'accès à l'URL de l'accueil (`/admin`) et aux URLs des applications
        (`/admin/bibliothecaire`) exposées dans l'administration
        """
        url_admin_index = reverse('admin:index')  # '/admin/'
        response_root = self.client.get(url_admin_index)
        self.assertEqual(response_root.status_code, 200, "Accès à /admin KO")

        # Parcours des apps exposées dans l'admin
        app_labels = set()
        for model in admin.site._registry:
            app_labels.add(model._meta.app_label)

        for app_label in app_labels:
            url_app_index = f"{url_admin_index}{app_label}/"
            response_app = self.client.get(url_app_index)
            self.assertEqual(response_app.status_code, 200, f"Accès à {url_admin_index}{app_label}/ KO")

    def test_admin_urls_by_permissions(self):
        """
        T-ADM-02 : Vérifie les URLs admin selon les permissions déclarées dans ModelAdmin
        """

        # Obtention d'un objet `request` avec l'utilisateur défini comme le superuser de tests.
        factory = RequestFactory()
        mock_request = factory.get('/')
        mock_request.user = self.test_admin

        for model, model_admin in admin.site._registry.items():
            model_name = model._meta.model_name
            app_label = model._meta.app_label

            # Vérifie has_view_permission → changelist
            if model_admin.has_view_permission(mock_request):
                url_changelist = reverse(f'admin:{app_label}_{model_name}_changelist')
                response = self.client.get(url_changelist)
                self.assertEqual(response.status_code, 200, f"Changelist KO pour {model_name}")

            # Vérifie has_add_permission → add
            if model_admin.has_add_permission(mock_request):
                url_add = reverse(f'admin:{app_label}_{model_name}_add')
                response = self.client.get(url_add)
                self.assertEqual(response.status_code, 200, f"Add KO pour {model_name}")

            # Vérifie has_change_permission → change
            if model_admin.has_change_permission(mock_request):
                obj = model.objects.first()
                if obj:
                    url_change = reverse(f'admin:{app_label}_{model_name}_change', args=[obj.pk])
                    response = self.client.get(url_change)
                    self.assertEqual(response.status_code, 200, f"Change KO pour {model_name}")

            # Vérifie has_delete_permission → delete
            if model_admin.has_delete_permission(mock_request):
                obj = model.objects.first()
                if obj:
                    url_delete = reverse(f'admin:{app_label}_{model_name}_delete', args=[obj.pk])
                    response = self.client.get(url_delete)
                    self.assertEqual(response.status_code, 200, f"Delete KO pour {model_name}")
