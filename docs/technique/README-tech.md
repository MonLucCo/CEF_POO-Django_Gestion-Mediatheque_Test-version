# ⚙️ Documentation technique – Projet Médiathèque Django

Ce document regroupe les **commandes**, **paramètres**, et **procédures techniques** utilisées dans le projet.

---

## 🧭 Sommaire

- [📦 Environnement de développement](#-environnement-de-développement)
- [🚀 Lancement du serveur Django](#-lancement-du-serveur-django)
- [🧾 Commandes Git utiles](#-commandes-git-utiles)
- [🔄 Clonage du dépôt GitHub](#-clonage-du-dépôt-github)
- [📎 Liens vers la documentation](#-liens-vers-la-documentation)

---

## 📦 Environnement de développement

- **Python** : 3.13.7  
- **Django** : 5.2.6  
- **IDE** : PyCharm  
- **Environnement virtuel** : `works/venv`

---

## 🚀 Lancement du serveur Django

```bash
cd works
.\\venv\\Scripts\\activate
cd mediatheque
python manage.py runserver 8900
```

Accès local : [http://127.0.0.1:8900](http://127.0.0.1:8900)

> ℹ️ Le port `8900` est utilisé pour éviter les conflits avec WampServer (Apache sur le port 8000).  
> Le fichier `manage.py` reste inchangé pour une configuration minimaliste.

---

## 🧾 Commandes Git utiles

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

## 🔄 Clonage du dépôt GitHub

```bash
git clone https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version.git
cd CEF_POO-Django_Gestion-Mediatheque_Test-version
```

> 💡 Pour cloner une branche spécifique :
```bash
git clone -b MonLucCo/issue2 https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version.git
```

---

## 📎 Liens vers la documentation

- [README principal du projet](../../README.md)
- [README général de la documentation](../README.md)
- [Suivi du développement](../developpement/README-dev.md)
- [Architecture du projet](../architecture/README-archi.md)
- [Spécifications fonctionnelles](../fonctionnel/README-fonct.md)  
- [Documentation technique](../technique/README-tech.md)
- [Rapport de projet](../../delivery/rapport/rapport-projet.md)

---
