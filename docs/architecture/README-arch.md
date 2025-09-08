# 🏗️ Architecture du projet – Médiathèque Django

Ce document décrit l’architecture technique du projet, les composants principaux, et leur organisation au sein de l’application Django.

---

## 🧭 Sommaire

- [📁 Structure des dossiers](#-structure-des-dossiers)
- [🧱 Composants principaux](#-composants-principaux)
- [🔄 Flux de données](#-flux-de-données)
- [🧩 Modèle MVC dans Django](#-modèle-mvc-dans-django)
- [📎 Liens vers la documentation](#-liens-vers-la-documentation)

---

## 📁 Structure des dossiers

```
CEF_POO-Django_Gestion-Mediatheque_Test-version/
├── mediatheque/          # Application principale
│   ├── models.py         # Modèles de données
│   ├── views.py          # Logique métier
│   ├── templates/        # Fichiers HTML
│   └── urls.py           # Routage
├── manage.py             # Script de gestion Django
├── db.sqlite3            # Base de données locale
└── docs/                 # Documentation du projet
```

---

## 🧱 Composants principaux

- **Modèles** : Représentation des entités (Livre, Usager, Emprunt)
- **Vues** : Traitement des requêtes et logique métier
- **Templates** : Interface utilisateur en HTML
- **URLconf** : Définition des routes
- **Admin** : Interface d’administration Django

---

## 🔄 Flux de données

1. L’utilisateur interagit via l’interface HTML
2. Les vues traitent la requête
3. Les modèles accèdent à la base de données
4. La réponse est rendue via un template

---

## 🧩 Modèle MVC dans Django

| Composant Django | Rôle MVC classique |
|------------------|--------------------|
| Models           | Modèle             |
| Views            | Contrôleur         |
| Templates        | Vue                |

> Django suit une architecture MTV (Model-Template-View), qui est une variante du MVC adaptée au web.

---

## 📎 Liens vers la documentation

- [README principal du projet](../../README.md)
- [README général de la documentation](../README.md)
- [Spécifications fonctionnelles](../fonctionnel/README-fonct.md)
- [Documentation technique](../technique/README-tech.md)
- [Suivi du développement](../developpement/README-dev.md)

---
