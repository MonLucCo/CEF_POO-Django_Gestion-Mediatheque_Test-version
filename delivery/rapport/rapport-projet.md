# Rapport de projet – Application Médiathèque Django

| Élément           | Détail                                                                  |
|-------------------|-------------------------------------------------------------------------|
| **Nom du projet** | Gestion de médiathèque avec Django                                      |
| **Date**          | Septembre 2025                                                          |
| **Rédacteur**     | `Luc PERARD` / micro-entreprise `PerLucCo`                              |
| **Formation**     | CEF – Développement Web et Web Mobile – Module POO                      |
| **Avancement**    | ✔️ Done : #1, #12 • 🚧 En cours : #2 • ⏳ À venir : #3, #4, #5, #6, #7  |

> Cette rédaction du rapport est incrémentale et les paragraphes absents seront intégrés lors de la réalisation du développement.
> 
> Dans le dépôt GitHub du projet, chaque issue du plan de développement prévoit les sections concernées par la mise à jour du présent document.

---

## Sommaire

- [1. Introduction](#1-introduction)
- [3. Architecture du projet et mise en place](#3-architecture-du-projet-et-mise-en-place)
  - [3.1 Organisation des dossiers](#31-organisation-des-dossiers)
  - [3.2 Plan de développement et réorganisation des issues](#32-plan-de-développement-et-réorganisation-des-issues)
  - [3.4 Couche centrale du projet Django](#34-couche-centrale-du-projet-django)
- [7. Mode d’installation et d’exécution](#7-mode-dinstallation-et-dexécution)
  - [7.1 Prérequis](#71-prérequis)
  - [7.2 Commandes pas à pas](#72-commandes-pas-à-pas)
- [8. Démarche de travail et traçabilité](#8-démarche-de-travail-et-traçabilité)
  - [8.1 Workflow GitHub](#81-workflow-github)
  - [8.3 Difficultés rencontrées et leçons apprises](#83-difficultés-rencontrées-et-leçons-apprises)
- [Annexes](#annexes)
  - [Annexe C – Arborescence du projet](#annexe-c--arborescence-du-projet)

---

## 1. Introduction

Ce projet s’inscrit dans le cadre du devoir du module Programmation Orientée Objet (POO) avec Python. Il vise à mettre en œuvre une application Django simulant la gestion d’une médiathèque, en respectant des contraintes métier précises.

Les objectifs pédagogiques sont :
- Appliquer les principes de la POO dans un projet concret
- Structurer une application Django avec plusieurs composants
- Implémenter des fonctionnalités métier réalistes
- Mettre en place une stratégie de tests
- Documenter la démarche et livrer un projet complet

Le livrable final comprend :
- Un dépôt GitHub structuré et développé à partir de huit (8) issues
- Un rapport de projet rédigé en Markdown et exporté en PDF

---

## 3. Architecture du projet et mise en place

### 3.1 Organisation des dossiers

Le dépôt est structuré en trois zones distinctes :

- `works/`  
  - `mediatheque/` : projet Django (`manage.py`, `db.sqlite3`, apps…)  
  - `venv/` : environnement virtuel Python  
- `docs/` : documentation fonctionnelle et technique (`README-*.md`, diagrammes…)  
- `delivery/` : livrables finaux (`rapport-projet.md`, `rapport-projet.pdf`)

Cette séparation garantit une clarté immédiate entre le code, la documentation évolutive et les artefacts remis.

### 3.2 Plan de développement et réorganisation des issues

#### 3.2.1 Version initiale

La première mouture du projet s’appuyait sur sept issues linéaires, imaginées pour une unique application Django.

| Issue | Branche associée | Titre de l’issue                                   | Objectif            |
|-------|------------------|----------------------------------------------------|---------------------|
| #1    | MonLucCo/issue1  | Préparation de l’environnement                     | Projet              |
| #2    | MonLucCo/issue2  | Initialisation du projet et configuration centrale | Django, Application |
| #3    | À définir        | Modélisation des entités                           | Application         |
| #4    | À définir        | Développement des vues et logique métier           | Application         |
| #5    | À définir        | Interfaces utilisateur et templates                | Application         |
| #6    | À définir        | Tests et validation                                | Application         |
| #7    | À définir        | Rapport final et livraison                         | Projet              |

Cette organisation a rapidement montré ses limites face au besoin de deux applications métier distinctes.

#### 3.2.2 Version révisée

Sous l’égide de l’issue #12 (Actualisation de la documentation et réorganisation des issues), le plan a été repensé en trois pôles :

| Issue | Parent) | Branche associée | Titre de l’issue                                               | Objectif              |
|-------|---------|------------------|----------------------------------------------------------------|-----------------------|
| #1    |         | MonLucCo/issue1  | Préparation de l’environnement                                 | Projet                |
| #2    |         | MonLucCo/issue2  | Initialisation du projet et configuration centrale             | Django, `mediatheque` |
| #3    |         | MonLucCo/issue3  | Développement de l’application fonctionnelle bibliothécaire    | Métier `bibliotheque` |
| #4    |         | MonLucCo/issue4  | Développement de l’application fonctionnelle membre            | Métier `membre`       |
| #5    |         | MonLucCo/issue5  | Authentification, autorisation et sécurité                     | Couche `mediatheque`  |
| #6    |         | MonLucCo/issue6  | Tests et validation                                            | Application           |
| #7    |         | MonLucCo/issue7  | Rapport final et livraison                                     | Projet                |
| #12   | #1      | MonLucCo/issue12 | Actualisation de la documentation et réorganisation des issues | Projet                |

Ce découpage, effectué avant tout développement, a clarifié les responsabilités de chaque composant :  
- **mediatheque** (application : couche centrale)  
- **bibliothecaire** (application métier : gestion des emprunts et des membres)  
- **membre** (application métier : consultation des médias)  

Il a aussi permis de planifier chaque étape technique avec précision et d’assurer une traçabilité optimale via GitHub.

### 3.4 Couche centrale du projet Django

La couche centrale du projet (mediatheque) est responsable de la configuration globale, du routage, de la vue d’accueil et de la gestion des rôles. Elle agit comme point d’entrée unique, redirigeant les utilisateurs vers l’application correspondant à leur profil.

Définie lors de la réorganisation des issues (cf. issue #12), la couche `mediatheque` sert de point d’entrée unique et assure :

- Configuration globale (`settings.py`) : base de données, langue, timezone  
- Vue d’accueil protégée et redirection selon le rôle utilisateur  
- Routage principal (`urls.py`) pour coordonner les deux sous-applications  
- Gestion des sessions et des permissions pour sécuriser l’accès

---

## 7. Mode d’installation et d’exécution

### 7.1 Prérequis

- Python 3.13.7
- pip 25.2
- Environnement virtuel (`venv`)
- Django 5.2.6

Ces versions précises garantissent la reproductibilité et la compatibilité du projet.

### 7.2 Commandes pas à pas

Cette procédure est destinée à toute personne souhaitant tester le projet localement à partir du dépôt GitHub. Elle permet de :

- Cloner le dépôt contenant le projet
- Activer l’environnement virtuel préconfiguré
- Lancer l’application Django en local

> ℹ️ **Nom du dépôt** : `CEF_POO-Django_Gestion-Mediatheque_Test-version`  
> Ce dépôt contient l’ensemble du projet, y compris le code source, la documentation et les livrables.

> 📁 **Dossier `works/`** : contient le code source et l’environnement virtuel  
> └── `mediatheque/` : dossier du projet Django (avec `manage.py`, `db.sqlite3`, etc.)  
> └── `venv/` : environnement virtuel Python contenant Django et les dépendances

> ⚠️ **Port utilisé** : le serveur Django est lancé sur le port `8900`, car le port `8000` est occupé par Apache sur le poste de développement.

---

#### 📦 Étapes communes

1. Cloner le dépôt GitHub :

```bash
git clone https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version.git
cd CEF_POO-Django_Gestion-Mediatheque_Test-version
```

2. Se placer dans le dossier de travail :

```bash
cd works
```

---

### 🪟 Sous Windows

```bash
# Activer l’environnement virtuel
venv\Scripts\activate

# Vérifier que Django est bien installé
python -m django --version

# Se placer dans le projet Django
cd mediatheque

# Lancer le serveur
python manage.py runserver
```

---

### 🐧 Sous Unix/macOS

```bash
# Activer l’environnement virtuel
source venv/bin/activate

# Vérifier que Django est bien installé
python3 -m django --version

# Se placer dans le projet Django
cd mediatheque

# Lancer le serveur
python3 manage.py runserver
```

> ✅ Une fois le serveur lancé, l’application est accessible à l’adresse : [http://127.0.0.1:8000](http://127.0.0.1:8000)

> ℹ️ **Note** : Si le port 8000 est déjà utilisé (par exemple par Apache), vous pouvez spécifier un autre port lors du lancement :  
> `python manage.py runserver 127.0.0.1:8900`  
> L’application sera alors accessible via [http://127.0.0.1:8900](http://127.0.0.1:8900)

---

## 8. Démarche de travail et traçabilité

### 8.1 Workflow GitHub

Le projet utilise GitHub pour assurer la traçabilité du développement et la séparation entre les tâches techniques et la rédaction du rapport.

Le workflow adopté repose sur les principes suivants :
- Une branche principale : `main`
- Des branches de travail nommées selon le schéma :  
  - `MonLucCo/issue[n]/update-technical` pour les développements techniques  
  - `MonLucCo/issue[n]/update-report` pour la rédaction du rapport
  - `MonLucCo/isue[n]/[dénomination-spécifique]` pour des tâches spécifiques
- Chaque issue GitHub (#1 à #7, #12) correspond à une étape du projet
- Les branches sont fusionnées via des `Pull Requests` (PR), puis supprimées une fois validées

> ℹ️ **Note** : Ce workflow n’a pas été appliqué dès le début du projet.  
> Lors du traitement de l’issue #1, l’organisation des branches a évolué progressivement, en parallèle de la prise en main de l’interface de l’EDI PyCharm.  
> Certaines premières branches ne respectent pas entièrement la convention de nommage, ce qui reflète une phase d’apprentissage et d’ajustement.

Ce processus garantit une traçabilité claire entre les tâches, les commits, les issues et les livrables, tout en facilitant les revues de code et la rédaction du rapport.

> ⚠️ **Remarque** : Une branche dédiée à la mise à jour documentaire a été créée pour l’issue #12 : `MonLucCo/issue12/update-documentation`. Cette branche regroupe les modifications du README `/docs/developpement`, du plan du rapport et des titres d’issues. Elle illustre l’importance d’un travail préparatoire structuré avant le développement technique.

### 8.3 Difficultés rencontrées et leçons apprises

#### 8.3.1 Difficulté d'un bon plan de développement

L'origine de ce problème est l'apparition d'une incohérence d'organisation et d'architecture à l'engagement de la réalisation de l'issue #2 selon la version initiale du plan de développement.

La mise à jour des issues a représenté une difficulté notable, notamment pour comprendre la logique de découpage fonctionnel qui distingue :
- une couche centrale d'authentification (médiathèque)
- deux applications métier (bibliothécaire et membre).

Cette étape - à la fois d'architecture, d'organisation, de technique - a permis de mieux anticiper les tâches techniques à réaliser, en distinguant clairement les rôles métier et les responsabilités de chaque application. Elle a également facilité la rédaction du rapport et la cohérence du projet dans son ensemble.

---

## Annexes

### Annexe C – Arborescence du projet

```text
CEF_POO-Django_Gestion-Mediatheque_Test-version/
├── works/
│   ├── mediatheque/
│   │   ├── db.sqlite3
│   │   ├── manage.py
│   │   └── ...
│   └── venv/
│       ├── Include/
│       ├── Lib/
│       ├── Scripts/
│       └── pyvenv.cfg
├── docs/
│   ├── architecture/
│   ├── fonctionnel/
│   ├── technique/
│   └── README-dev.md
├── delivery/
│   └── rapport/
│       ├── rapport-projet.md
│       └── rapport-projet.pdf
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
---
