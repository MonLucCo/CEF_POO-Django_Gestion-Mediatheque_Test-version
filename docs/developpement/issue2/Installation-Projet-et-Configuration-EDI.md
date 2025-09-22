# 🧾 Synthèse – Installation et configuration du projet Django avec PyCharm

> Ce document doit être intégré dans le dépôt ou le rapport dans le cadre de la branche `MonLucCo/issue2/update-rapport`.

## 📦 Partie 1 : Installation du projet Django (from scratch)

### 🔹 Objectifs :
- Initialiser un projet Django localement
- Préparer l’environnement virtuel
- Installer les dépendances nécessaires

### 🔹 Étapes :

1. **Cloner le dépôt du projet**
   ```bash
   git clone https://github.com/[utilisateur]/CEF_POO-Django_Gestion-Mediatheque_Test-version.git
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l’environnement virtuel**

   - Sous Windows :
     ```bash
     venv\Scripts\activate
     ```
   - Sous macOS/Linux :
     ```bash
     source venv/bin/activate
     ```

4. **Installer Django**
   ```bash
   pip install django
   ```

5. **Vérifier l’installation**
   ```bash
   python -m django --version
   ```

6. **Lancer le serveur Django**
   ```bash
   python manage.py runserver 8900
   ```

> Le port 8900 est utilisé pour éviter les conflits avec Apache (par défaut sur 8000)

---

## 🖥️ Partie 2 : Configuration locale de l’EDI PyCharm

### 🔹 Objectifs :
- Synchroniser PyCharm avec l’environnement virtuel
- Activer les fonctionnalités Django (si version Pro)
- Préparer l’environnement de développement

### 🔹 Étapes :

1. **Sélectionner l’interpréteur Python**
   - `File > Settings > Project: [nom du projet] > Python Interpreter`
   - ⚙️ > `Add...` > `Add Local Interpreter...`
   - Choisir `Existing environment`
   - Sélectionner : `works/venv/Scripts/python.exe`

2. **Marquer le dossier source**
   - Clic droit sur `/works/mediatheque`
   - `Mark Directory as > Sources Root`

3. **Activer le support Django** *(PyCharm Pro uniquement)*
   - `File > Settings > Languages & Frameworks > Django`
   - Cocher `Enable Django Support`
   - Renseigner :
     - Django project root : `works/mediatheque`
     - Settings : `mediatheque/settings.py`
     - Manage.py : `works/mediatheque/manage.py`
   - Laisser décoché : `Do not use Django test runner`
   - Laisser vide : `Environment variables` (sauf besoin spécifique)
   - Laisser vide ou définir : `Folder pattern to track files` (ex. `*.py:templates/*:static/*`)

---

## 🧠 Remarque sur Visual Studio Code (VSC)

Si l’EDI utilisé est **VSC au lieu de PyCharm**, la configuration reste nécessaire :

- Sélection de l’interpréteur Python via `Python: Select Interpreter`
- Installation des extensions :
  - **Python** (obligatoire)
  - **Django** (optionnelle mais utile)
- Configuration du dossier racine dans `.vscode/settings.json` si besoin

---
