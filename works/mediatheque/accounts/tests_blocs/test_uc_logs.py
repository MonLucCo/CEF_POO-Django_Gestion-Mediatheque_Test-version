from pathlib import Path
from django.conf import settings
from django.urls import reverse
from bibliothecaire.tests import LoginRequiredTestCase


class BaseLogsTestCase(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url_login = reverse("accounts:login")
        cls.url_logout = reverse("accounts:logout")
        cls.url_accueil_bib = reverse("bibliothecaire:accueil")
        cls.log_file = Path(settings.BASE_DIR) / "mediatheque_test.log"

        # On remet le fichier à zéro pour éviter le bruit des tests précédents
        cls.log_file.write_text("", encoding="utf-8")

    def read_log(self) -> str:
        """Retourne le contenu du fichier de log en UTF-8 (chaîne vide si absent)."""
        try:
            return self.log_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return ""

    def read_last_log_line(self) -> str:
        """Retourne uniquement la dernière ligne du fichier de log (ou chaîne vide si absent)."""
        try:
            with self.log_file.open(encoding="utf-8") as f:
                lines = f.readlines()
                return lines[-1].strip() if lines else ""
        except FileNotFoundError:
            return ""


# 🧪 Fonctionnel – UC-LOGS
class TestLogs(BaseLogsTestCase):

    def test_log_01_fichier_log_cree_et_alimente(self):
        """T-LOG-01 : Vérifie la création et l’alimentation du fichier mediatheque.log."""
        self.logout(url=True)
        self.assertTrue(self.log_file.exists(), "Le fichier mediatheque.log n'existe pas.")
        content = self.read_log()
        self.assertTrue(len(content) > 0, "Le fichier mediatheque.log est vide.")

    def test_log_02_connexion_genere_un_log_LOGIN(self):
        """T-LOG-02 : Vérifie qu’une connexion génère un message [LOGIN]."""
        self.logout()
        self.login_as(self.RoleTest.STAFF, url=True)
        content = self.read_log()
        self.assertIn("[LOGIN]", content, "Aucun [LOGIN] dans le fichier de logs.")

    def test_log_03_deconnexion_genere_un_log_LOGOUT(self):
        """T-LOG-03 : Vérifie qu’une déconnexion génère [LOGOUT] ou [LOGOUT_INVALID]."""
        self.logout()
        self.login_as(self.RoleTest.SUPERADMIN, url=True)
        self.client.post(self.url_logout)
        last_line = self.read_last_log_line()
        self.assertTrue(
            "[LOGOUT]" in last_line or "[LOGOUT_INVALID]" in last_line,
            "La dernière ligne ne contient pas [LOGOUT] ou [LOGOUT_INVALID]."
        )

    def test_log_04_acces_refuse_genere_un_log_ACCESS_DENIED(self):
        """T-LOG-04 : Vérifie qu’un accès refusé génère [ACCESS_DENIED]."""
        self.logout()
        self.client.get(self.url_accueil_bib)
        content = self.read_log()
        self.assertIn("[ACCESS_DENIED]", content, "Aucun [ACCESS_DENIED] dans le fichier de logs.")

    def test_log_05_acces_accepte_genere_un_log_ACCESS_GRANTED(self):
        """T-LOG-05 : Vérifie qu’un accès accordé génère [ACCESS_GRANTED]."""
        self.logout()
        self.login_as(self.RoleTest.ADMIN, url=True)
        self.client.get(self.url_accueil_bib)
        content = self.read_log()
        self.assertIn("[ACCESS_GRANTED]", content, "Aucun [ACCESS_GRANTED] dans le fichier de logs.")
