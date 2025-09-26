# 🧠 Memento Django – Balises `{% ... %}` et Filtres `|...`

Ce mémento regroupe les éléments essentiels du langage de template Django utilisés dans le projet **bibliothécaire**, avec des exemples courts et des cas d’usage typiques.

---

## Sommaire

1. [📚 Références utiles](#-1-références-utiles)
2. [🔧 Balises `{% ... %}` – Logique de présentation](#-2-balises-----logique-de-présentation)
3. [🧩 Filtres `|...` – Transformation de variables](#-3-filtres---transformation-de-variables)
4. [🧠 Cas d’usage dans le projet](#-4-cas-dusage-dans-le-projet)
5. [🧪 Filtres personnalisés](#-5-filtres-personnalisés)
6. [🧱 Structure des templates](#-6-structure-des-templates)
7. [🧪 Tests de rendu de templates](#-7-tests-de-rendu-de-templates)
8. [📦 Autres thèmes à envisager pour compléter ce mémento](#-8-thèmes-complémentaires-à-documenter)
---

## 📚 1. Références utiles

- [Documentation Django – Balises et Filtres intégrés](https://docs.djangoproject.com/fr/5.2/ref/templates/builtins/)
- [Tutoriel Django – Templates](https://docs.djangoproject.com/fr/5.2/intro/tutorial03/)
- [Guide PyCharm – Templates Django](https://blog.jetbrains.com/fr/pycharm/2025/09/le-guide-ultime-des-templates-django/)
- [Créer des filtres personnalisés](https://runebook.dev/fr/docs/django/howto/custom-template-tags)

---

## 🔧 2. Balises `{% ... %}` – Logique de présentation

| Balise          | Usage                             |   Emploi    | Exemple                                                |
|-----------------|-----------------------------------|:-----------:|--------------------------------------------------------|
| `{% extends %}` | Hérite d’un template parent       |  Structure  | `{% extends '_base.html' %}`                           |
| `{% block %}`   | Zone remplaçable dans le parent   |  Structure  | `{% block content %}...{% endblock %}`                 |
| `{% include %}` | Insère un fragment de template    |  Structure  | `{% include 'partials/menu.html' %}`                   |
| `{% comment %}` | Commente du code Django           |  Structure  | `{% comment %} désactivé {% endcomment %}`             |
| `{% if %}`      | Condition logique                 |  Contrôle   | `{% if media.disponible %}Oui{% else %}Non{% endif %}` |
| `{% for %}`     | Boucle sur une liste              |  Contrôle   | `{% for membre in membres %}...{% endfor %}`           |
| `{% empty %}`   | Alternative si la boucle est vide |  Contrôle   | `{% empty %}Aucun résultat{% endempty %}`              |
| `{% url %}`     | Génère une URL nommée             | Navigation  | `{% url 'bibliothecaire:media_list' %}`                |
| `{% static %}`  | Fichier statique (image, CSS...)  | Navigation  | `{% static 'images/logo.png' %}`                       |

---

## 🧩 3. Filtres `|...` – Transformation de variables

| Filtre             | Effet                        | Exemple                                      |
|--------------------|------------------------------|----------------------------------------------|
| `lower`            | Minuscules                   | `{{ media.titre\|lower }}`                   |
| `upper`            | Majuscules                   | `{{ membre.nom\|upper }}`                    |
| `length`           | Taille d’une liste ou chaîne | `{{ emprunts\|length }}`                     |
| `date:"d/m/Y"`     | Formatage de date            | `{{ emprunt.date_emprunt\|date:"d/m/Y" }}`   |
| `default:"..."`    | Valeur par défaut si vide    | `{{ media.theme\|default:"Non renseigné" }}` |
| `truncatechars:50` | Coupe après n caractères     | `{{ media.description\|truncatechars:50 }}`  |
| `yesno:"Oui,Non"`  | Affichage booléen            | `{{ media.disponible\|yesno:"Oui,Non" }}`    |
| `join:", "`        | Concatène une liste          | `{{ membre.tags\|join:", " }}`               |
| `safe`             | Rend le HTML non échappé     | `{{ media.contenu_html\|safe }}`             |

---

## 🧠 4. Cas d’usage dans le projet

- `accueil.html` : `{% block content %}`, `{% extends %}`
- `media_list.html` : `{% for media in medias %}`, `{{ media.titre|upper }}`
- `media_detail.html` : `{{ media.disponible|yesno:"Oui,Non" }}`
- `_base.html` : `{% block title %}`, `{% url %}` vers les vues principales

---

## 🧪 5. Filtres personnalisés

Les filtres personnalisés permettent d’ajouter des transformations spécifiques à ton projet, directement dans les templates.

### 📁 Structure recommandée

Créer un dossier `templatetags/` dans ton application :

```
bibliothecaire/
├── templatetags/
│   ├── __init__.py
│   └── media_filters.py
```

### 🧱 Exemple simple

```python
# media_filters.py
from django import template

register = template.Library()

@register.filter
def majuscule(valeur):
    return valeur.upper()
```

Dans le template :

```django
{% load media_filters %}
{{ media.titre|majuscule }}
```

### 🔐 Bonnes pratiques

- Utiliser `@stringfilter` si le filtre attend une chaîne
- Gérer les cas d’erreur sans lever d’exception
- Redémarrer le serveur après ajout du module

---

## 🧱 6. Structure des templates

Organiser les templates par entité améliore la lisibilité et la maintenabilité du projet.

### 📁 Arborescence recommandée

```
templates/
└── bibliothecaire/
    ├── _base.html
    ├── accueil.html
    ├── medias/
    │   ├── list.html
    │   ├── detail.html
    ├── emprunts/
    │   ├── list.html
    ├── membres/
    │   ├── list.html
    ├── jeux/
        ├── list.html
```

### 🧠 Avantages

- Clarifie les responsabilités par entité
- Facilite l’héritage et la modularité
- Permet des inclusions ciblées (`{% include 'bibliothecaire/medias/card.html' %}`)

---

## 🧪 7. Tests de rendu de templates

Les tests de rendu permettent de vérifier que les templates s’affichent correctement avec les bons contextes.

### 🧱 Exemple avec `Client`

```python
from django.test import TestCase
from django.urls import reverse

class MediaViewTests(TestCase):
    def test_media_list_rendu(self):
        response = self.client.get(reverse('bibliothecaire:media_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bibliothecaire/medias/list.html')
```

### 🧠 Conseils

- Tester les templates critiques (accueil, listes, formulaires)
- Vérifier les blocs (`{% block content %}`) et les inclusions
- Utiliser `assertContains()` pour tester le contenu HTML

---

## 🧩 8. Thèmes complémentaires à documenter

D’autres thèmes liés au moteur de template Django pourront être ajoutés selon les besoins du développement. Ce mémento est évolutif et s’enrichira au fil des fonctionnalités du projet.

| 🧱 Thème                               | Description concrète et intérêt projet                                                               |
|----------------------------------------|------------------------------------------------------------------------------------------------------|
| ⚙️ Context processors                  | Injecter des variables globales dans tous les templates (ex. utilisateur connecté, notifications)    |
| 🧩 Balises personnalisées              | Créer des balises `{% ... %}` spécifiques pour encapsuler des blocs logiques ou du HTML réutilisable |
| 🔐 Contrôle d’accès dans les templates | Afficher ou masquer des blocs selon les permissions ou rôles utilisateur (`{% if user.is_staff %}`)  |

---
