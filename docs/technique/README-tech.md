
# ⚙️ Documentation technique – Médiathèque Django

Ce document regroupe les commandes, paramètres, scripts et procédures techniques utilisées dans le projet Django de gestion de médiathèque.  
Il est complété par deux mémos spécialisés :
- [`Memento_Systeme_Scripts-terminal.md`](Memento_Systeme_Scripts-terminal.md) – scripts shell pour automatiser les tâches
- [`Memento_Technique_Commandes-migration.md`](Memento_Technique_Commandes-migration.md) – commandes Django liées aux migrations

---

## 🧭 Sommaire

1. [📦 Environnement de développement](#-1-environnement-de-développement)  
2. [🚀 Lancement du serveur Django](#-2-lancement-du-serveur-django)  
3. [🧾 Commandes Git utiles](#-3-commandes-git-utiles)  
4. [🔄 Clonage du dépôt GitHub](#-4-clonage-du-dépôt-github)  
5. [📥 Chargement et réinitialisation des données](#-5-chargement-et-réinitialisation-des-données)  
6. [🧩 Mémentos techniques associés](#-6-mémentos-techniques-associés)  
7. [📎 Liens vers la documentation](#-7-liens-vers-la-documentation)

---

## 📦 1. Environnement de développement

- **Python** : 3.13.7  
- **Django** : 5.2.6  
- **IDE** : PyCharm  
- **Environnement virtuel** : `works/venv`

---

## 🚀 2. Lancement du serveur Django

```bash
cd works
.\\venv\\Scripts\\activate
cd mediatheque
python manage.py runserver 8900
```

Accès local : [http://127.0.0.1:8900](http://127.0.0.1:8900)

> ℹ️ Le port `8900` est utilisé pour éviter les conflits avec WampServer (Apache sur le port 8000).

---

## 🧾 3. Commandes Git utiles

- Initialisation du dépôt :
  ```bash
  git init
  git remote add origin <url>
  ```

- Création de branche :
  ```bash
  git checkout -b MonLucCo/issueX
  ```

- Commit et push :
  ```bash
  git add .
  git commit -m "Message"
  git push -u origin MonLucCo/issueX
  ```

---

## 🔄 4. Clonage du dépôt GitHub

```bash
git clone https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version.git
cd CEF_POO-Django_Gestion-Mediatheque_Test-version
```

> 💡 Pour cloner une branche spécifique :
```bash
git clone -b MonLucCo/issue2 https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version.git
```

---

## 📥 5. Chargement et réinitialisation des données

### 5.1 Chargement des données initiales

```bash
python manage.py loaddata bibliothecaire/fixtures/initial_data.json
```

### 5.2 Réinitialisation complète (base + données)

> Cette procédure permet de réinitialiser entièrement la base de données et de recharger les données initiales du projet.

```bash
# 1. Activation de l’environnement virtuel
cd works
.\venv\Scripts\activate

# 2. Accès au projet Django
cd mediatheque

# 3. Réinitialisation de la base
python manage.py flush

# 4. Application des migrations
python manage.py migrate

# 5. Chargement des données initiales
python manage.py loaddata bibliothecaire/fixtures/initial_data.json
```

> 💡 Cette commande recharge tous les objets nécessaires à la validation fonctionnelle (médias, membres, emprunts, etc.).

### 5.3 Réinitialisation minimale (superuser uniquement)

> Cette procédure permet de réinitialiser la base sans charger les données métier, uniquement pour créer un superutilisateur.

```bash
# 1. Activation de l’environnement virtuel
cd works
.\venv\Scripts\activate

# 2. Accès au projet Django
cd mediatheque

# 3. Réinitialisation de la base
python manage.py flush

# 4. Application des migrations
python manage.py migrate

# 5. Création du superutilisateur
python manage.py createsuperuser
```

> 📌 Utile pour tester l’interface admin ou démarrer une nouvelle série de tests sans données préchargées.

---

## 🧩 6. Mémentos techniques associés

- [`Memento_Systeme_Scripts-terminal.md`](Memento_Systeme_Scripts-terminal.md) – scripts shell pour initialisation et réinitialisation
- [`Memento_Technique_Commandes-migration.md`](Memento_Technique_Commandes-migration.md) – commandes Django pour gérer les migrations

---

## 📎 7. Liens vers la documentation

- [README principal du projet](../../README.md)  
- [README général de la documentation](../README.md)  
- [Suivi du développement](../developpement/README-dev.md)  
- [Architecture du projet](../architecture/README-archi.md)  
- [Spécifications fonctionnelles](../fonctionnel/README-fonct.md)  
- [Rapport de projet](../../delivery/rapport/rapport-projet.md)

---
