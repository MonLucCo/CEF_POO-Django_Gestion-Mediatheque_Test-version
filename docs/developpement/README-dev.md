# 🛠️ Suivi du développement – Projet Médiathèque Django

Ce document centralise le suivi des **issues**, des **branches**, des **commits**, et des **étapes techniques** du 
projet Django de gestion de médiathèque.

Il sert de point d’entrée pour :
- comprendre la progression du projet par issue,
- accéder aux documents techniques associés à chaque étape,
- faciliter la relecture pédagogique ou technique.

Les documents de référence du développement du projet sont regroupés dans le dossier `/docs/developpement/dev-docs`.

---

## 🧭 Sommaire

1. [📌 Principes du développement](#1-principes-du-développement)
    - [1.1 Finalité du document de suivi](#11-finalité-du-document-de-suivi)
    - [1.2 Méthodologie de structuration par issues et branches](#12-méthodologie-de-structuration-par-issues-et-branches)
2. [📋 Issues traitées](#-2-issues-traitées)
    - [2.1 Version initiale du Plan de développement](#21-version-initiale-du-plan-de-développement)
    - [2.2 Version en cours du plan de développement](#22-version-2-du-plan-de-développement)
3. [📘 Étapes de développement documentées](#-3-étapes-de-développement-documentées)
    - [3.1 Issue #3 – Application fonctionnelle Bibliothécaire](#31-issue-3--application-fonctionnelle-bibliothécaire)
    - [3.2 Issue #4 – Application fonctionnelle Membre](#32-issue-4--application-fonctionnelle-de-consultation)
    - [3.3 Issue #5 – Authentification et sécurité](#33-issue-5--authentification-et-sécurité)
4. [🧪 Branches](#-4-branches)
5. [📂 Historique des commits](#-5-historique-des-commits)
6. [📎 Liens vers la documentation](#-6-liens-vers-la-documentation)

---

##  1. Principes du développement

###  1.1 Finalité du document de suivi

Ce document centralise le suivi des issues, des branches, des commits et des étapes techniques du projet Django de 
gestion de médiathèque. 

Il sert de point d’entrée pour :
- comprendre la progression du projet par issue,
- accéder aux documents techniques associés à chaque étape,
- faciliter la relecture pédagogique ou technique.

Les documents de référence du développement sont regroupés dans le dossier `/docs/developpement/dev-docs/`.

### 1.2 Méthodologie de structuration par issues et branches

Le développement est structuré en plusieurs issues successives, chacune correspondant à une phase métier ou technique 
clairement identifiée.  
La progression est documentée à travers une main-courante vivante, mise à jour dans les sous-branches `update-technical` 
de chaque issue.  
La branche `update-documentation` est réservée à la mise à jour du rapport du projet.

Cette organisation permet :
- une traçabilité claire des choix techniques,
- une séparation entre développement et documentation finale,
- une continuité documentaire entre les issues.

Le rapport s’appuie sur cette démarche pour expliciter les décisions prises, les priorités retenues et les évolutions à 
venir.

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

> Cette version du plan de développement a été remplacée pour permettre un développement du projet par applications.

### 2.2 Version 2 du plan de développement

|  Issue  |  Parent  | Branche associée | Titre de l’issue                                               | Objectif              | Statut       |
|:-------:|:--------:|------------------|----------------------------------------------------------------|-----------------------|--------------|
|   #1    |          | MonLucCo/issue1  | Préparation de l’environnement                                 | Projet                | ✅ Clôturée   |
|   #2    |          | MonLucCo/issue2  | Initialisation du projet et configuration centrale             | Django, `mediatheque` | ✅ Clôturée   |
|   #3    |          | MonLucCo/issue3  | Développement de l’application fonctionnelle bibliothécaire    | Métier `bibliotheque` | 🕒 En cours  |
|   #4    |          | MonLucCo/issue4  | Développement de l’application fonctionnelle de consultation   | Métier `consultation` | 🚧 À engager |
|   #5    |          | MonLucCo/issue5  | Authentification, autorisation et sécurité                     | Couche `mediatheque`  | ⏳ À venir    |
|   #6    |          | MonLucCo/issue6  | Tests et validation                                            | Application           | ⏳ À venir    |
|   #7    |          | MonLucCo/issue7  | Rapport final et livraison                                     | Projet                | ⏳ À venir    |
|   #12   |    #1    | MonLucCo/issue12 | Actualisation de la documentation et réorganisation des issues | Projet                | ✅ Clôturée   |

> Cette version du plan de développement a été remplacée pour permettre le développement séparé des fonctionnalités et 
> des travaux d'intégration dans les applications du projet.

### 2.3 Version 3 (en cours) du plan de développement

|  Issue  |  Parent  | Branche associée | Titre de l’issue                                               | Objectif                      | Statut       |
|:-------:|:--------:|------------------|----------------------------------------------------------------|-------------------------------|--------------|
|   #1    |          | MonLucCo/issue1  | Préparation de l’environnement                                 | Projet                        | ✅ Clôturée   |
|   #2    |          | MonLucCo/issue2  | Initialisation du projet et configuration centrale             | Django, `mediatheque`         | ✅ Clôturée   |
|   #3    |          | MonLucCo/issue3  | Développement de l’application fonctionnelle bibliothécaire    | Métier `bibliotheque`         | 🕒 En cours  |
|   #4    |          | MonLucCo/issue4  | Développement de l’application fonctionnelle de consultation   | Métier `consultation`         | 🚧 À engager |
|   #5    |          | MonLucCo/issue5  | Applications, Authentification, autorisation et sécurité       | Applications et sécurité      | ⏳ À venir    |
|   #6    |          | MonLucCo/issue6  | Finition applications (UX, affichages), Tests et validation    | Applications UX et validation | ⏳ À venir    |
|   #7    |          | MonLucCo/issue7  | Rapport final et livraison                                     | Projet                        | ⏳ À venir    |
|   #12   |    #1    | MonLucCo/issue12 | Actualisation de la documentation et réorganisation des issues | Projet                        | ✅ Clôturée   |

> Les documents associés aux développements techniques sont nommés selon leur fonction transverse à chaque issue.

> 🔗 [Voir les issues sur GitHub](https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version/issues)

---

## 📘 3. Étapes de développement documentées

| Issue | Étape | Description technique                                     | Document initial                                                                                                                                                     | Document actualisé ou associé                                                                                                                                                                                                  |
|-------|-------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #1    | - ✅   | Préparation de l'environnement                            | _non documenté spécifiquement_                                                                                                                                       | -                                                                                                                                                                                                                              |
| #2    | - ✅   | Initialisation du projet et réorganisation des issues     | [`Initialisation-Projet-et-Configuration-EDI.md`](issue2/Installation-Projet-et-Configuration-EDI.md)                                                                | -                                                                                                                                                                                                                              |
| #3    | 1 ✅   | Création des modèles métier                               | [`Analyse-Modèle.md`](issue3/task1/Analyse-Modele.md) et [`model.py_indexA.txt`](issue3/task1/models.py_indexA.txt)                                                  | [`models.py_indexH.txt`](issue3/task1/models.py_indexH.txt)                                                                                                                                                                    |
| #3    | 2 ✅   | Création du jeu de données initial                        | [`Analyse-initial_data.md`](issue3/task2/Analyse-initial_data.md) et [`initial_data.json_indexA.txt`](issue3/task2/initial_data.json_indexA.txt)                     | [`initial_data.json_indexB.txt`](issue3/task4/initial_data.json_indexB.txt)                                                                                                                                                    |
| #3    | 3 ✅   | Enregistrement des entités dans l’admin                   | [`admin.py_indexA.txt`](issue3/task3/admin.py_indexA.txt)                                                                                                            | [`admin.py_indexH.txt`](issue3/task4/admin.py_indexH.txt)                                                                                                                                                                      |
| #3    | 4 ✅   | Personnalisation complète de l’interface admin            | [`_Admin-main-courante.md`](issue3/task4/_Admin-main-courante.md)                                                                                                    | -                                                                                                                                                                                                                              |
| #3    | 5 ✅   | Développement fonctionnel initial - Médias                | [`_Frontend-main-courante.md` (index G-10)](issue3/task5/_Frontend-main-courante_indexG-10.md), [`tests-plan.md` (index G-10)](issue3/task5/tests-plan_indexG-10.md) | [`Analyse_LifeCycle_Medias.md` (index G-10)](issue3/task5/Analyse_LifeCycle_Medias_indexG-10.md), [`Analyse_Fonctionnalites_Bibliothecaire.md` (index G-10)](issue3/task5/Analyse_Fonctionnalites_Bibliothecaire_indexG-10.md) |
| #3    | 6 ✅   | Développement fonctionnel initial - Membre et Emprunt     | [`_Frontend-main-courante.md`](issue3/task6/_Frontend-main-courante.md), [`tests-plan.md`](issue3/task6/tests-plan.md)                                               | **Renommage des documents de développement sans indexation des versions**                                                                                                                                                      |
| #4    | - ⏳   | Développement fonctionnel complémentaire - Consultation   |                                                                                                                                                                      |                                                                                                                                                                                                                                |
| #5    | - ⏳   | Applications,- Authentification, autorisation et sécurité |                                                                                                                                                                      |                                                                                                                                                                                                                                |
| #6    | - ⏳   | Applications (UX et fonctions) - Tests et validation      |                                                                                                                                                                      |                                                                                                                                                                                                                                |
| #7    | - ⏳   | Rapport final et livraison                                |                                                                                                                                                                      |                                                                                                                                                                                                                                |

> Mise en place (fin issue #3 - plan de développement version 2) d'une documentation transversale regroupée dans le 
> `/docs/developpement/dev-docs/` :
> - `devMC.md` : **main-courante** du développement (nommage précédent : `_Frontend-main-courante.md`).
> - `devAFBib.md` : **analyse des fonctionnalités** du Bibliothécaire (nommage précédent : `Analyse_Fonctionnalités_Bibliothecaire.md`).
> - `devALCBib.md` : **analyse du cycle de vie des entités** du Bibliothécaire (nommage précédent `Analyse_LifeCycle_Bibliothecaire.md`).
> - `devTests.md` : **plan de tests du projet** (nommage précédent : `tests-plan.md`).
> - `devReport.md` : **rapports de tests unitaires** du projet (nommage précédent : `test_report.txt`).

> À partir de l'issue #4, les documents sont nommés selon leur fonction transversale de documentation du développement 
> pour garantir leur réutilisation dans les issues suivantes.
>
> L'issue #3 a servi de référence initiale pour chaque document de la documentation transversale. 

### 3.1 Issue #3 – Application fonctionnelle Bibliothécaire

📌 Objectif : développer les fonctionnalités de l'application Bibliothécaire en trois blocs :
- Bloc 1 : Modélisation des entités de l'application `bibliothecaire` et fonction `administrateur`.
- Bloc 2 : Modélisation `Media`, fonctions métier et typage différé (`Media`, `Livre`, `Dvd`, `Cd`).
- Bloc 3 : Modélisation et fonctions métier Membre et Emprunt (`Membre`, `Emprunt`, `Retour`).

📁 Dossier : `/docs/developpement/issue3/`

#### 🔹 Bloc 1 – Modèle Bibliothécaire et Administration
- Création des entités `Media`, `Livre`, `Dvd`, `Cd`, `JeuDePlateau`, `Emprunt`, `Membre`, `Bibliothecaire`.
- Enregistrement dans l’admin Django.
- Vue LIST pour les médias.
- Tests fonctionnels validés : ✅ 5 tests.
- Index de révision : de A à C.

> ➡️ Voir : [`_Admin-main-courante.md`](issue3/task4/_Admin-main-courante.md)

#### 🔹 Bloc 2 – Médias
- Vues CRUD pour les médias et ses sous-types.
- Typage différé et rollback métier.
- Cycle de vie métier formalisé.
- Tests fonctionnels validés : ✅ 47 tests.
- Index de révision : de D-3 à G-10.
- Documents figés : _main-courante_, _analyse fonctionnelle_ (AFBib), _analyse Life-Cycle_ (ALCBib) et _plan de test_.

> ➡️ Voir : [`_Frontend-main-courante.md` (index G-10)](issue3/task5/_Frontend-main-courante_indexG-10.md)

#### 🔹 Bloc 3 – Membre et Emprunt
- Vues CRUD pour les membres et les emprunts.
- Historique, filtrage, retour, statut.
- Finalisation des fonctionnalités métier.
- Tests fonctionnels validés : ✅ 136 tests.
- Index de révision : de H-1 à H-11.
- Documents figés : **aucun, tous les documents sont actualisés pour couvrir tout le développement de façon transversale 
aux issues de développement**.

> ➡️ Voir : [`_Frontend-main-courante.md` (index H)](issue3/task6/_Frontend-main-courante.md)  
> ➡️ Voir : [`devMC.md` **création**](dev-docs/devMC.md)

### 3.2 Issue #4 – Application fonctionnelle de consultation

- À engager après la finalisation de l’issue #3.
- Portera sur les vues accessibles au profil Membre.
- Inclura les restrictions d’accès, consultation de l'entité `Support`, et gestion de l'entité `JeuDePlateau`.

### 3.3 Issue #5 – Authentification et sécurité

- Gestion des rôles et permissions.
- Accès conditionnel aux vues et formulaires.
- Intégration des mécanismes de login, logout, et filtrage.
- Intégration des fonctionnalités Métier dans les applications `Bibliothécaire` et `Consultation`.

---

## 🧪 4. Branches

- `main` : branche stable  
- `MonLucCo/issueX` : branches de développement liées aux issues avec  
  - sous-branche `MonLucCo/issueX/update-technical` : développement technique du code.
  - sous-branche `MonLucCo/issueX/update-documentation` : actualisation du **rapport du projet**.

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
