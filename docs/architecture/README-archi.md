# 🏗️ Architecture du projet – Médiathèque Django

Ce document décrit d’abord l’architecture **initiale** (une seule app), puis l’architecture **revisitée** en trois pôles, avant de présenter les composants, le flux de données et le modèle MVC.

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

## 🔄 2. Architecture révisée (3 pôles)

Pour clarifier les responsabilités et faciliter la maintenance, le projet a été scindé en trois pôles :

```text
Médiathèque Django (v2)
├── mediatheque/           # Couche centrale
│   ├── settings.py        # DB, langue, timezone
│   ├── urls.py            # Routage global
│   ├── views.py           # Page d’accueil et redirections
│   └── templates/         # Layouts communs
├── bibliothecaire/        # Gestion des membres et des emprunts
│   ├── models.py          # Livre, Emprunt, Retour…
│   ├── views.py           # CRUD membres et médias
│   └── urls.py
├── membre/                # Consultation seule des médias
│   ├── views.py           # Liste des médias
│   └── urls.py
└── requirements.txt
```

Avantages :

- Séparation nette des responsabilités  
- Réduction de la taille et de la complexité des modules  
- Tests unitaires spécifiques et isolés par app  
- Meilleure évolutivité pour l’ajout de fonctionnalités  

---

## 🧱 3. Composants principaux

- **Models** : définition des entités métier (`Livre`, `Usager`, `Emprunt`)  
- **Views** : traitement des requêtes et logique métier  
- **Templates** : rendu HTML côté client  
- **URLs** : routage par application  
- **Admin** : interface d’administration Django  

---

## 🔄 4. Flux de données

1. L’utilisateur envoie une requête HTTP  
2. Le **routage global** (`mediatheque/urls.py`) oriente vers l’app adéquate  
3. La **view** traite la logique métier  
4. Le **model** interagit avec la base de données  
5. La réponse est rendue via un **template**  

---

## 🧩 5. Modèle MVC dans Django

| Composant Django | Rôle MVC classique |
|------------------|--------------------|
| Models           | Modèle             |
| Views            | Contrôleur         |
| Templates        | Vue                |

> Django suit le pattern MTV (Model-Template-View), équivalent au MVC adapté au web.

---

## 📎 6. Liens vers la documentation

- [README principal du projet](../../README.md)
- [README général de la documentation](../README.md)
- [Suivi du développement](../developpement/README-dev.md)
- [Architecture du projet](../architecture/README-archi.md)
- [Spécifications fonctionnelles](../fonctionnel/README-fonct.md)  
- [Documentation technique](../technique/README-tech.md)
- [Rapport de projet](../../delivery/rapport/rapport-projet.md)

---
