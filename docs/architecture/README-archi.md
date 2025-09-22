# 🏗️ Architecture du projet – Médiathèque Django

Ce document présente l’évolution de l’architecture du projet Django de gestion de médiathèque. Il décrit :
- l’organisation initiale en une seule application,
- la refonte en quatre pôles spécialisés,
- les composants techniques,
- le découpage backend/frontend,
- le flux de données,
- le modèle MVC adapté à Django.

Ce fichier fait partie du dossier `/docs/architecture/` et sert de référence pour comprendre la structure technique du projet.

---

## 🧭 Sommaire

1. [Architecture initiale](#1-architecture-initiale)
2. [Architecture révisée (4 pôles)](#2-architecture-révisée-4-pôles)
3. [Composants principaux](#3-composants-principaux)
4. [Diagramme UML (à insérer)](#4-diagramme-uml-à-insérer)
5. [Flux de données](#5-flux-de-données)
6. [Modèle MVC dans Django](#6-modèle-mvc-dans-django)
7. [Liens vers la documentation](#7-liens-vers-la-documentation)

---

## 🏛️ 1. Architecture initiale

Au démarrage, toutes les fonctionnalités étaient regroupées dans une seule application Django `mediatheque/` :

```text
Médiathèque Django (v1)
└── mediatheque/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    ├── static/
    └── tests.py
```

Limites de ce modèle :

- Fichiers volumineux et responsabilités multiples dans `mediatheque/`  
- Difficulté à isoler l’authentification de la logique métier  
- Tests unitaires peu ciblés et code moins évolutif  

---

## 🔄 2. Architecture révisée (4 pôles)

Pour clarifier les responsabilités et faciliter la maintenance, le projet a été scindé en quatre pôles :

```text
Médiathèque Django (v2)
├── mediatheque/           # Couche centrale
│   ├── settings.py        # DB, langue, timezone
│   └── urls.py            # Routage global
├── accounts/              # Gestion de l'accueil (passerelle d'orientation)
│   ├── urls.py            # Routage spécifique d'orientation
│   ├── views.py           # Page d’accueil et redirections
│   └── templates/         # Layouts de l'accueil
├── bibliothecaire/        # Gestion des membres et des emprunts (par les bibliothécaires)
│   ├── models.py          # Livre, Emprunt, Retour…
│   ├── views.py           # CRUD membres et médias
│   └── urls.py            # Routage spécifique des bibliothécaires
├── membre/                # Consultation seule des supports consultables (par les membres)
│   ├── views.py           # Liste des supports consultables
│   └── urls.py            # Routage spécifique de la consultation
├── db.sqlite3             # Base de données du projet
└── manage.py              # Management de Django
```

Avantages :

- Séparation nette des responsabilités  
- Réduction de la taille et de la complexité des modules  
- Tests unitaires spécifiques et isolés par app  
- Meilleure évolutivité pour l’ajout de fonctionnalités  

> 🔄 **Découpage technique : Backend / Frontend**
>
> - Le **backend** regroupe les modèles (`models.py`), les vues métier (`views.py`), l’interface admin (`admin.py`), et les fichiers de configuration (`settings.py`, `urls.py`).  
> - Le **frontend** correspond aux templates HTML (`templates/`), aux formulaires, et à l’interaction utilisateur via les vues Django.  
> - Chaque pôle (app Django) contient à la fois des composants backend et frontend, mais leur rôle est spécialisé :
>   - `bibliothecaire/` : backend métier (modèles, logique d’emprunt) + frontend de gestion
>   - `membre/` : frontend de consultation publique
>   - `accounts/` : frontend d’accueil et de redirection
>   - `mediatheque/` : backend central (routage, configuration)

---

## 🧱 3. Composants principaux

- **Models** : définition des entités métier  
- **Views** : traitement des requêtes et logique métier  
- **Templates** : rendu HTML côté client  
- **URLs** : routage par application  
- **Admin** : interface d’administration Django  

---

## 📐 4. Diagramme UML (à insérer)

> Un diagramme UML des entités métier sera intégré dans le dossier `/docs/architecture/` une fois stabilisé.  
> Il représentera les relations entre `Support`, `Media`, `Livre`, `Emprunt`, `Membre`, etc.

---

## 🔄 5. Flux de données

1. L’utilisateur envoie une requête HTTP  
2. Le **routage global** (`mediatheque/urls.py`) oriente vers l’app adéquate  
3. La **view** traite la logique métier  
4. Le **model** interagit avec la base de données  
5. La réponse est rendue via un **template**  

---

## 🧩 6. Modèle MVC dans Django

| Composant Django | Rôle MVC classique |
|------------------|--------------------|
| Models           | Modèle             |
| Views            | Contrôleur         |
| Templates        | Vue                |

> Django suit le pattern MTV (Model-Template-View), équivalent au MVC adapté au web.

---

## 📎 7. Liens vers la documentation

- [README principal du projet](../../README.md)
- [README général de la documentation](../README.md)
- [Suivi du développement](../developpement/README-dev.md)
- [Architecture du projet](../architecture/README-archi.md)
- [Spécifications fonctionnelles](../fonctionnel/README-fonct.md)  
- [Documentation technique](../technique/README-tech.md)
- [Rapport de projet](../../delivery/rapport/rapport-projet.md)

---
