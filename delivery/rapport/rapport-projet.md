# Rapport de projet – Application Médiathèque Django

| Élément       | Détail                                                                 |
|---------------|------------------------------------------------------------------------|
| **Nom du projet** | Gestion de médiathèque avec Django                                     |
| **Date**          | Septembre 2025                                                        |
| **Rédacteur**     | Luc PERARD / PerLucCo                                                 |
| **Formation**     | CEF – Développement Web et Web Mobile – Module POO                   |

---

## Sommaire

- [1. Introduction](#1-introduction)
- [3. Architecture du projet et mise en place](#3-architecture-du-projet-et-mise-en-place)
  - [3.1 Organisation des dossiers](#31-organisation-des-dossiers)
- [7. Mode d’installation et d’exécution](#7-mode-dinstallation-et-dexécution)
  - [7.1 Prérequis](#71-prérequis)
  - [7.2 Commandes pas à pas](#72-commandes-pas-à-pas)
- [8. Démarche de travail et traçabilité](#8-démarche-de-travail-et-traçabilité)
  - [8.1 Workflow GitHub](#81-workflow-github)
- [Annexes](#annexes)
  - [Annexe C – Arborescence du projet](#annexe-c--arborescence-du-projet)

---

## 1. Introduction

Ce projet s’inscrit dans le cadre du devoir 12 du module Programmation Orientée Objet (POO) avec Python. Il vise à mettre en œuvre une application Django simulant la gestion d’une médiathèque, en respectant des contraintes métier précises.

Les objectifs pédagogiques sont :
- Appliquer les principes de la POO dans un projet concret
- Structurer une application Django avec plusieurs composants
- Implémenter des fonctionnalités métier réalistes
- Mettre en place une stratégie de tests
- Documenter la démarche et livrer un projet complet

Le livrable final comprend :
- Un dépôt GitHub structuré
- Un rapport de projet rédigé en Markdown et exporté en PDF

---

## 3. Architecture du projet et mise en place

### 3.1 Organisation des dossiers

Le projet est structuré en trois répertoires principaux :

- `works/` : contient le code source et l’environnement virtuel  
  - `mediatheque/` : projet Django principal (`manage.py`, `db.sqlite3`, etc.)  
  - `venv/` : environnement virtuel Python avec Django et les dépendances  
- `docs/` : documentation technique, fonctionnelle et architecture  
  - Tous les fichiers `README.md` sont regroupés ici (aucun dans `works/`)  
- `delivery/` : livrables finaux, dont le rapport Markdown et son export PDF

Cette organisation permet de séparer clairement le code, la documentation et les livrables.

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
- Chaque issue GitHub (#1 à #7) correspond à une étape du projet
- Les branches sont fusionnées via des Pull Requests (PR), puis supprimées une fois validées

> ℹ️ Ce workflow n’a pas été appliqué dès le début du projet.  
> Lors du traitement de l’issue #1, l’organisation des branches a évolué progressivement, en parallèle de la prise en main de l’interface de l’EDI PyCharm.  
> Certaines premières branches ne respectent pas entièrement la convention de nommage, ce qui reflète une phase d’apprentissage et d’ajustement.

Ce processus garantit une traçabilité claire entre les tâches, les commits, les issues et les livrables, tout en facilitant les revues de code et la rédaction du rapport.

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
