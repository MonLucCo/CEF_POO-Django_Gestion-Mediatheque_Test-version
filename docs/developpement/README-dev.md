# 🛠️ Suivi du développement – Projet Médiathèque Django

Ce document centralise le suivi des **issues**, des **branches**, des **commits**, et des **étapes techniques** du projet Django de gestion de médiathèque.

Il sert de point d’entrée pour :
- comprendre la progression du projet par issue,
- accéder aux documents techniques associés à chaque étape,
- faciliter la relecture pédagogique ou technique.

Les documents de référence sont regroupés dans le dossier `/docs/developpement/`.

---

## 🧭 Sommaire

1. [📌 Objectifs](#-1-objectifs)
2. [📋 Issues traitées](#-2-issues-traitées)
3. [📘 Étapes de développement documentées](#-3-étapes-de-développement-documentées)
4. [🧪 Branches](#-4-branches)
5. [📂 Historique des commits](#-5-historique-des-commits)
6. [📎 Liens vers la documentation](#-6-liens-vers-la-documentation)

---

## 📌 1. Objectifs

- Documenter les tâches réalisées et à venir  
- Suivre l’évolution du projet par branche et par issue  
- Faciliter la relecture pédagogique ou technique  

---

## 📋 2. Issues traitées

### 2.1 Version initiale du Plan de développement

| Numéro | Branche associée | Description                              |
|--------|------------------|------------------------------------------|
| #1     | MonLucCo/issue1  | Préparation de l’environnement           |
| #2     | MonLucCo/issue2  | Initialisation du projet Django          |
| #3     | À définir        | Modélisation des entités                 |
| #4     | À définir        | Développement des vues et logique métier |
| #5     | À définir        | Interfaces utilisateur et templates      |
| #6     | À définir        | Tests et validation                      |
| #7     | À définir        | Rapport final et livraison               |

### 2.2 Version en cours du plan de développement

| Issue | Parent) | Branche associée | Titre de l’issue                                               | Objectif              | Statut       |
|-------|---------|------------------|----------------------------------------------------------------|-----------------------|--------------|
| #1    |         | MonLucCo/issue1  | Préparation de l’environnement                                 | Projet                | ✅ Clôturée   |
| #2    |         | MonLucCo/issue2  | Initialisation du projet et configuration centrale             | Django, `mediatheque` | ✅ Clôturée   |
| #3    |         | MonLucCo/issue3  | Développement de l’application fonctionnelle bibliothécaire    | Métier `bibliotheque` | 🕒 Een cours |
| #4    |         | MonLucCo/issue4  | Développement de l’application fonctionnelle membre            | Métier `membre`       | 🚧 À engager |
| #5    |         | MonLucCo/issue5  | Authentification, autorisation et sécurité                     | Couche `mediatheque`  | ⏳ À venir    |
| #6    |         | MonLucCo/issue6  | Tests et validation                                            | Application           | ⏳ À venir    |
| #7    |         | MonLucCo/issue7  | Rapport final et livraison                                     | Projet                | ⏳ À venir    |
| #12   | #1      | MonLucCo/issue12 | Actualisation de la documentation et réorganisation des issues | Projet                | ✅ Clôturée   |


> 🔗 [Voir les issues sur GitHub](https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version/issues)

---

## 📘 3. Étapes de développement documentées

| Issue | Étape | Description technique                                 | Document initial                                                                                                                                 | Document actualisé                                                          |
|-------|-------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| #1    | - ✅   | Préparation de l'environnement                        | _non documenté spécifiquement_                                                                                                                   | -                                                                           |
| #2    | - ✅   | Initialisation du projet et réorganisation des issues | [`Initialisation-Projet-et-Configuration-EDI.md`](issue2/Installation-Projet-et-Configuration-EDI.md)                                            | -                                                                           |
| #3    | 1 ✅   | Création des modèles métier                           | [`Analyse-Modèle.md`](issue3/task1/Analyse-Modele.md) et [`model.py_indexA.txt`](issue3/task1/models.py_indexA.txt)                              | [`models.py_indexH.txt`](issue3/task1/models.py_indexH.txt)                 |
| #3    | 2 ✅   | Création du jeu de données initial                    | [`Analyse-initial_data.md`](issue3/task2/Analyse-initial_data.md) et [`initial_data.json_indexA.txt`](issue3/task2/initial_data.json_indexA.txt) | [`initial_data.json_indexB.txt`](issue3/task4/initial_data.json_indexB.txt) |
| #3    | 3 ✅   | Enregistrement des entités dans l’admin               | [`admin.py_indexA.txt`](issue3/task3/admin.py_indexA.txt)                                                                                        | [`admin.py_indexH.txt`](issue3/task4/admin.py_indexH.txt)                   |
| #3    | 4 ✅   | Personnalisation complète de l’interface admin        | [`_Admin-main-courante.md`](issue3/task4/_Admin-main-courante.md)                                                                                |                                                                             |
| #3    | 5 ⏳   | Développement fonctionnel initial (vues, templates)   | [`_Frontend-main-courante.md`](issue3/task5/_Frontend-main-courante.md) *(à venir)*                                                              |                                                                             |

---

## 🧪 4. Branches

- `main` : branche stable  
- `MonLucCo/issueX` : branches de développement liées aux issues  

---

## 📂 5. Historique des commits

Utiliser la commande suivante pour afficher un historique condensé :

```bash
git log --oneline
```

Ou bien consulter directement l’interface GitHub pour une vue détaillée des commits.

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
