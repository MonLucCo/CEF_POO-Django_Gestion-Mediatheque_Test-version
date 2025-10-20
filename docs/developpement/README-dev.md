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
    - [2.1 Version initiale du Plan de développement](#21-version-initiale-du-plan-de-développement)
    - [2.2 Version en cours du plan de développement](#22-version-en-cours-du-plan-de-développement)
3. [📘 Étapes de développement documentées](#-3-étapes-de-développement-documentées)
    - [3.1 📘 Issue #3 – Application fonctionnelle Bibliothécaire](#31--issue-3--application-fonctionnelle-bibliothécaire)
    - [3.2 📘 Issue #4 – Application fonctionnelle Membre](#32--issue-4--application-fonctionnelle-membre)
    - [3.3 📘 Issue #5 – Authentification et sécurité](#33--issue-5--authentification-et-sécurité)
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

| Issue | Parent) | Branche associée | Titre de l’issue                                               | Objectif              | Statut      |
|-------|---------|------------------|----------------------------------------------------------------|-----------------------|-------------|
| #1    |         | MonLucCo/issue1  | Préparation de l’environnement                                 | Projet                | ✅ Clôturée  |
| #2    |         | MonLucCo/issue2  | Initialisation du projet et configuration centrale             | Django, `mediatheque` | ✅ Clôturée  |
| #3    |         | MonLucCo/issue3  | Développement de l’application fonctionnelle bibliothécaire    | Métier `bibliotheque` | 🕒 En cours |
| #4    |         | MonLucCo/issue4  | Développement de l’application fonctionnelle membre            | Métier `membre`       | 🚧 À engager |
| #5    |         | MonLucCo/issue5  | Authentification, autorisation et sécurité                     | Couche `mediatheque`  | ⏳ À venir   |
| #6    |         | MonLucCo/issue6  | Tests et validation                                            | Application           | ⏳ À venir   |
| #7    |         | MonLucCo/issue7  | Rapport final et livraison                                     | Projet                | ⏳ À venir   |
| #12   | #1      | MonLucCo/issue12 | Actualisation de la documentation et réorganisation des issues | Projet                | ✅ Clôturée  |


> 🔗 [Voir les issues sur GitHub](https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version/issues)

---

## 📘 3. Étapes de développement documentées

| Issue | Étape | Description technique                                 | Document initial                                                                                                                                        | Document actualisé ou associé                                                                                                                                                                                                  |
|-------|-------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #1    | - ✅   | Préparation de l'environnement                        | _non documenté spécifiquement_                                                                                                                          | -                                                                                                                                                                                                                              |
| #2    | - ✅   | Initialisation du projet et réorganisation des issues | [`Initialisation-Projet-et-Configuration-EDI.md`](issue2/Installation-Projet-et-Configuration-EDI.md)                                                   | -                                                                                                                                                                                                                              |
| #3    | 1 ✅   | Création des modèles métier                           | [`Analyse-Modèle.md`](issue3/task1/Analyse-Modele.md) et [`model.py_indexA.txt`](issue3/task1/models.py_indexA.txt)                                     | [`models.py_indexH.txt`](issue3/task1/models.py_indexH.txt)                                                                                                                                                                    |
| #3    | 2 ✅   | Création du jeu de données initial                    | [`Analyse-initial_data.md`](issue3/task2/Analyse-initial_data.md) et [`initial_data.json_indexA.txt`](issue3/task2/initial_data.json_indexA.txt)        | [`initial_data.json_indexB.txt`](issue3/task4/initial_data.json_indexB.txt)                                                                                                                                                    |
| #3    | 3 ✅   | Enregistrement des entités dans l’admin               | [`admin.py_indexA.txt`](issue3/task3/admin.py_indexA.txt)                                                                                               | [`admin.py_indexH.txt`](issue3/task4/admin.py_indexH.txt)                                                                                                                                                                      |
| #3    | 4 ✅   | Personnalisation complète de l’interface admin        | [`_Admin-main-courante.md`](issue3/task4/_Admin-main-courante.md)                                                                                       | -                                                                                                                                                                                                                              |
| #3    | 5 ✅   | Développement fonctionnel initial - Médias            | [`_Frontend-main-courante.md` (index G-10)](issue3/task5/_Frontend-main-courante_indexG-10.md), [`tests-plan.md` (index G-10)](issue3/task5/tests-plan_indexG-10.md) | [`Analyse_LifeCycle_Medias.md` (index G-10)](issue3/task5/Analyse_LifeCycle_Medias_indexG-10.md), [`Analyse_Fonctionnalites_Bibliothecaire.md` (index G-10)](issue3/task5/Analyse_Fonctionnalites_Bibliothecaire_indexG-10.md) |
| #3    | 6 ⏳   | Développement fonctionnel initial - Membre et Emprunt | [`_Frontend-main-courante.md` *(à venir)*](issue3/task5/_Frontend-main-courante.md), [`tests-plan.md` *(à venir)*](issue3/task6/tests-plan.md)                      |                                                                                                                                                                                                                                |

### 3.1 📘 Issue #3 – Application fonctionnelle Bibliothécaire

📌 Objectif : développer les fonctionnalités de l'application Bibliothécaire en trois blocs :
- Bloc 1 : Modélisation des entités de l'application `bibliothecaire` et fonction àdministrateur`.
- Bloc 2 : Modélisation `Media`, fonctions métier et typage différé (`Media`, `Livre`, `Dvd`, `Cd`).
- Bloc 3 : Modélisation et fonctions métier Membre et Emprunt (`Membre`, `Emprunt`, `Retour`).

📁 Dossier : `/docs/developpement/issue3/`

#### 🔹 Bloc 1 – Modèle Bibliothécaire et Administration
- Création des entités `Media`, `Livre`, `Dvd`, `Cd`, `JeuDePlateau`, `Emprunt`, `Membre`, `Bibliothecaire`
- Enregistrement dans l’admin Django
- Vue LIST pour les médias
- Tests fonctionnels validés : ✅ 5 tests
- Index de révision : A à C

➡️ Voir : [`_Admin-main-courante.md`](issue3/task4/_Admin-main-courante.md)

#### 🔹 Bloc 2 – Médias
- Vues CRUD pour les médias et ses sous-types
- Typage différé et rollback métier
- Cycle de vie métier formalisé
- Tests fonctionnels validés : ✅ 47 tests
- Index de révision : D-3 à G-10
- Documents figés : _main-courante_ et _plan de test_

➡️ Voir : [`_Frontend-main-courante.md` (index G-10)](issue3/task5/_Frontend-main-courante_indexG-10.md)

#### 🔹 Bloc 3 – Membre et Emprunt
- Vues CRUD pour les membres et emprunts
- Historique, filtrage, retour, statut
- Finalisation des fonctionnalités métier
- Index de révision prévu : H

➡️ Voir : [`_Frontend-main-courante.md` (index H)](issue3/task6/_Frontend-main-courante.md)

### 3.2 📘 Issue #4 – Application fonctionnelle Membre

- À engager après la finalisation de l’issue #3
- Portera sur les vues accessibles au profil Membre
- Inclura les restrictions d’accès, consultation, et emprunt

### 3.3 📘 Issue #5 – Authentification et sécurité

- Gestion des rôles et permissions
- Accès conditionnel aux vues et formulaires
- Intégration des mécanismes de login, logout, et filtrage

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
