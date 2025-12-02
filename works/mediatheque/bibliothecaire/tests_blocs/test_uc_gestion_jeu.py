from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command

from bibliothecaire.models import JeuDePlateau
from bibliothecaire.tests import LoginRequiredTestCase


class BaseJeuTestCase(LoginRequiredTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # IMPORTANT: crée user+bibliothecaire

        call_command('loaddata', 'jeux_test.json', verbosity=0)
        cls.jeu = JeuDePlateau.objects.first()

        cls.url_list = reverse("bibliothecaire:jeu_list")
        cls.url_detail = reverse("bibliothecaire:jeu_detail", args=[cls.jeu.pk])
        cls.url_create = reverse("bibliothecaire:jeu_create")
        cls.url_update = reverse("bibliothecaire:jeu_update", args=[cls.jeu.pk])

        cls.template_list = "bibliothecaire/jeux/jeu_list.html"
        cls.template_detail = "bibliothecaire/jeux/jeu_detail.html"
        cls.template_form = "bibliothecaire/jeux/jeu_form.html"


# 🧭 Navigation
class TestNavigationJeu(BaseJeuTestCase):
    def test_nav_28_acces_liste_jeux(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_list)

    def test_nav_29_acces_detail_jeu(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_detail)

    def test_nav_30_acces_creation_jeu(self):
        response = self.client.get(self.url_create)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_form)

    def test_nav_31_acces_modification_jeu(self):
        response = self.client.get(self.url_update)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_form)


# 🧪 Fonctionnel
class TestFonctionnelJeu(BaseJeuTestCase):
    def test_fun_42_creation_jeu_valide(self):
        response = self.client.post(self.url_create, {
            "name": "Nouveau Jeu",
            "annee_edition": 2020,
            "consultable": True,
            "createur": "Mon créateur",
            "categorie": "Famille",
            "duree_partie": 60,
            "nb_joueur_min": 2,
            "nb_joueur_max": 4,
            "age_min": 10,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nouveau Jeu")

    def test_fun_43_modification_jeu(self):
        response = self.client.post(self.url_update, {
            "name": "Jeu Modifié",
            "annee_edition": self.jeu.annee_edition,
            "consultable": self.jeu.consultable,
            "createur": self.jeu.createur,
            "categorie": self.jeu.categorie,
            "duree_partie": self.jeu.duree_partie,
            "nb_joueur_min": self.jeu.nb_joueur_min,
            "nb_joueur_max": self.jeu.nb_joueur_max,
            "age_min": self.jeu.age_min,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.jeu.refresh_from_db()
        self.assertEqual(self.jeu.name, "Jeu Modifié")

    def test_fun_44_liste_cliquable(self):
        response = self.client.get(self.url_list)
        self.assertContains(response, reverse("bibliothecaire:jeu_detail", args=[self.jeu.pk]))

    def test_fun_45_indicateurs_accueil(self):
        url_accueil = reverse("bibliothecaire:accueil")
        response = self.client.get(url_accueil)
        self.assertContains(response, "Jeux enregistrés")
        self.assertContains(response, "— consultables")
