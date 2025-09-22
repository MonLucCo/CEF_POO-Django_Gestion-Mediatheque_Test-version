# 🛠️ Mémento – Scripts système pour terminal

Ce mémento regroupe les commandes du terminal utilisées pour lancer, réinitialiser ou tester le projet Django.  
Chaque commande est présentée en deux variantes : Windows (PowerShell / terminal PyCharm) et Linux/macOS (bash).  
Les sections sont organisées par usage et liées aux issues correspondantes du projet.

---

## 🧭 Sommaire

1. [📦 Démarrage du projet](#-1-démarrage-du-projet)
2. [🔄 Réinitialisation complète avec données](#-2-réinitialisation-complète-avec-données)
3. [🧼 Réinitialisation minimale (superuser uniquement)](#-3-réinitialisation-minimale-superuser-uniquement)
4. [🧪 Vérification technique](#-4-vérification-technique)
5. [👤 Création et gestion des utilisateurs [`issue #5`] (à compléter)](#-5-création-et-gestion-des-utilisateurs-issue-5-à-compléter)
6. [📥 Chargement de données spécifiques [`issue #6`] (à compléter)](#-6-chargement-de-données-spécifiques-issue-6-à-compléter)
7. [🧪 Tests unitaires et fonctionnels [`issue #6`] (à compléter)](#-7-tests-unitaires-et-fonctionnels-issue-6-à-compléter)
8. [💾 Exportation et sauvegarde de la base [`issue #7`] (à compléter)](#-8-exportation-et-sauvegarde-de-la-base-issue-7-à-compléter)
9. [🚀 Déploiement local ou distant [issue _hors projet_] (à compléter)](#-9-déploiement-local-ou-distant-issue-_hors-projet_-à-compléter)

---

## 📦 1. Démarrage du projet

### ▶️ Windows

```powershell
cd works
.\venv\Scripts\activate
cd mediatheque
python manage.py runserver 8900
```

### 🐧 Linux / macOS

```bash
cd works
source venv/bin/activate
cd mediatheque
python manage.py runserver 8900
```

---

## 🔄 2. Réinitialisation complète avec données

> Supprime toutes les données, applique les migrations, recharge `initial_data.json`.

### ▶️ Windows

```powershell
cd works
.\venv\Scripts\activate
cd mediatheque
python manage.py flush
python manage.py migrate
python manage.py loaddata bibliothecaire/fixtures/initial_data.json
```

### 🐧 Linux / macOS

```bash
cd works
source venv/bin/activate
cd mediatheque
python manage.py flush
python manage.py migrate
python manage.py loaddata bibliothecaire/fixtures/initial_data.json
```

---

## 🧼 3. Réinitialisation minimale (superuser uniquement)

> Supprime les données, applique les migrations, crée un superutilisateur.

### ▶️ Windows

```powershell
cd works
.\venv\Scripts\activate
cd mediatheque
python manage.py flush
python manage.py migrate
python manage.py createsuperuser
```

### 🐧 Linux / macOS

```bash
cd works
source venv/bin/activate
cd mediatheque
python manage.py flush
python manage.py migrate
python manage.py createsuperuser
```

---

## 🧪 4. Vérification technique

> Commandes utiles pour inspecter l’état du projet.

### Universel (Windows / Linux / macOS)

```bash
python manage.py check
python manage.py showmigrations
python manage.py sqlmigrate bibliothecaire 0001
```
 
---

## 👤 5. Création et gestion des utilisateurs [issue #5] (à compléter)

Cette section regroupera les commandes liées à la création de comptes, à la gestion des rôles (`membre`, `bibliothecaire`) et à l’activation/désactivation.

---

## 📥 6. Chargement de données spécifiques [issue #6] (à compléter)

Cette section regroupera les commandes pour charger des jeux de données ciblés (ex. : emprunts, membres bloqués, tests de retard).

---

## 🧪 7. Tests unitaires et fonctionnels [issue #6] (à compléter)

Cette section regroupera les commandes pour exécuter les tests (`manage.py test`), inspecter la couverture (`coverage`) et valider les cas métier.

---

## 💾 8. Exportation et sauvegarde de la base [issue #7] (à compléter)

Cette section regroupera les commandes pour exporter la base (`dumpdata`), sauvegarder les fixtures, ou réinjecter des données.

---

## 🚀 9. Déploiement local ou distant [issue _hors projet_] (à compléter)

Cette section regroupera les commandes pour préparer le projet à un déploiement (ex. : `collectstatic`, configuration de serveur, environnement distant).

---
