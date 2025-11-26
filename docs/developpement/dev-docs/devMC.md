# 🧾 Main courante – Développement fonctionnel initial Bibliothecaire

Cette main-courante documente les étapes de l’issue #3 du projet Médiathèque : le développement fonctionnel initial de 
l’application dédiée au profil bibliothécaire.

Elle vise à :
- Structurer les actions techniques à réaliser
- Identifier les entités concernées et leurs fonctionnalités
- Clarifier les rôles utilisateurs et les accès
- Suivre les fichiers à produire et les tests à mettre en œuvre
- Documenter les difficultés rencontrées et les arbitrages méthodologiques
- Expliciter les décisions structurantes pour le développement
- Lister les documents techniques de référence.

La rédaction s’appuie sur le modèle métier du projet, les exigences explicites du sujet, et les bonnes pratiques Django 
issues de la documentation officielle.

---

📁 `/docs/developpement/dev-docs/devMC.md`  

> 📌 Ce document poursuit la main courante des étapes de l’issue #3, en ouvrant le **Bloc 3** du développement fonctionnel.

Il fait suite à la version figée à l’index H-11 ([`_Frontend-main-courante.md` (`/issue3/task6`)](../issue3/task6/_Frontend-main-courante.md) 
et couvre :
- Les entités `Membre`, `Emprunt`, `Retour`
- Les vues CRUD, les transitions métier, les historiques
- La préparation des tests fonctionnels et des fixtures

📌 Version : index K-2 (issue #5 – étape 2 - Bloc 5)

---

> 🔗 Liens utiles
>
>> - Description de l'issue #3 : [Issue #3 – Développement de l’application fonctionnelle bibliothécaire](https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version/issues/3)  
>> - Organisation du développement technique : [README-tech.md](../../technique/README-tech.md)  
>> - Analyse des fonctionnalités du projet : [Analyse_Fonctionnalites.md](../../fonctionnel/Analyse_Fonctionnalites.md)  
>> - Plan de tests du projet : [devTests.md](devTests.md)

---

## 📑 Sommaire

1. [🎯 Objectifs du document](#1--objectifs-du-document)
2. [📌 Fonctionnalités par entité – Profil Bibliothécaire](#2--fonctionnalités-par-entité--profil-bibliothécaire)
3. [🔐 Accès par profil utilisateur](#3--accès-par-profil-utilisateur)
4. [️🗂️ Fichiers concernés](#4--fichiers-concernés)
5. [🔁 Routage et vues à implémenter](#5--routage-et-vues-à-implémenter)
6. [🧩 Templates HTML à créer](#6--templates-html-à-créer)
7. [🧪 Tests unitaires et validation](#7--tests-unitaires-et-validation)
8. [📥 Fixtures de test à préparer](#8--fixtures-de-test-à-préparer)
9. [📌 Difficultés rencontrées](#9--difficultés-rencontrées)
   - [9.1 Difficulté 1 : organiser le développement avec une vue d'ensemble cohérente (main courante)](#91-difficulté-1--organiser-le-développement-avec-une-vue-densemble-cohérente---création-dune-main-courante-de-développement)
   - [9.2 Difficulté 2 : comprendre les mécanismes liés au moteur de template Django](#92-difficulté-2--comprendre-les-mécanismes-liés-au-moteur-de-template-django)
   - [9.3 Difficulté 3 : choix de la meilleure architecture de Vue](#93-difficulté-3--choix-de-la-meilleure-architecture-de-vue)
   - [9.4 Difficulté 4 : accéder aux données spécifiques de l’objet typé (héritage multi-table et ORM Django)](#94-difficulté-4--accéder-aux-données-spécifiques-de-lobjet-typé-héritage-multi-table-et-orm-django)
   - [9.5 Difficulté 5 : définir et structurer les tests unitaires](#95-difficulté-5--définir-et-structurer-les-tests-unitaires)
   - [9.6 Difficulté 6 : reprise de modélisation en cours de développement](#96-difficulté-6--reprise-de-modélisation-en-cours-de-développement)
   - [9.7 Difficulté 7 : gestion des contrôles de validité sur les champs numériques de données](#97-difficulté-7--gestion-des-contrôles-de-validité-sur-les-champs-numériques-de-données)
   - [9.8 Difficulté 8 : nommage des dossiers du projet](#98-difficulté-8--nommage-des-dossiers-du-projet)
   - [9.9 Difficulté 9 : interactions entre les tests unitaires techniques et fonctionnels métier](#99-difficulté-9--interactions-entre-les-tests-unitaires-techniques-et-fonctionnels-métier)
   - [9.10 Difficulté 10 : Organisation et clarté du routage lié aux médias](#910-difficulté-10--organisation-et-clarté-du-routage-lié-aux-médias)
   - [9.11 Difficulté 11 : Visualisation des contraintes du formulaire](#911-difficulté-11--visualisation-des-contraintes-du-formulaire)
   - [9.12 Difficulté 12 : Formalisation du cycle de vie initial et typé des médias](#912-difficulté-12--formalisation-du-cycle-de-vie-initial-et-typé-des-médias)
   - [9.13 Difficulté 13 : Définir ce que signifie “ajouter un média” – segmentation fonctionnelle, typage différé et structuration technique](#913-difficulté-13--définir-ce-que-signifie-ajouter-un-média--segmentation-fonctionnelle-typage-différé-et-structuration-technique)
   - [9.14 Difficulté 14 : Définition transversale du cycle de vie métier avant développement des UC](#914-difficulté-14--définition-transversale-du-cycle-de-vie-métier-avant-développement-des-uc)
   - [9.15 Difficulté 15 : Regroupement des tests techniques et fonctionnels dans un même groupe de tests](#915-difficulté-15--regroupement-des-tests-techniques-et-fonctionnels-dans-un-même-groupe-de-tests)
   - [9.16 Difficulté 16 : Redondance du champ `bloqué` et modélisation du blocage métier](#916-difficulté-16--redondance-du-champ-bloqué-et-modélisation-du-blocage-métier)
   - [9.17 Difficulté 17 : Cohérence UX et gestion du contexte métier via session](#917-difficulté-17--cohérence-ux-et-gestion-du-contexte-métier-via-session)
   - [9.18 Difficulté 18 : Appel implicite d’une méthode sans argument dans un template Django](#918-difficulté-18--appel-implicite-dune-méthode-sans-argument-dans-un-template-django)
   - [9.19 Difficulté 19 : Stylisation minimale des messages utilisateur](#919-difficulté-19--stylisation-minimale-des-messages-utilisateur)
   - [9.20 Difficulté 20 : Activation du calcul des retards des emprunts en cours](#920-difficulté-20--activation-du-calcul-des-retards-des-emprunts-en-cours)
   - [9.21 Difficulté 21 : Formalisation des méthodes métier et transitions d’état](#921-difficulté-21--formalisation-des-méthodes-métier-et-transitions-détat)
   - [9.22 Difficulté 22 : Gestion des messages d’incohérence (Logs) et d’information utilisateur (UX)](#922-difficulté-22--gestion-des-messages-dincohérence-logs-et-dinformation-utilisateur-ux)
   - [9.23 Difficulté 23 : Formalisation des scenarii métier](#923-difficulté-23--formalisation-des-scenarii-métier)
   - [9.24 Difficulté 24 : Traçabilité UX des actions métier et synchronisation du contexte d’affichage](#924-difficulté-24--traçabilité-ux-des-actions-métier-et-synchronisation-du-contexte-daffichage)
   - [9.25 Difficulté 25 : Choix du modèle de vue pour une confirmation métier liée à un objet](#925-difficulté-25--choix-du-modèle-de-vue-pour-une-confirmation-métier-liée-à-un-objet)
   - [9.26 Difficulté 26 : Réorganisation du plan de développement et de la documentation transverse](#926-difficulté-26--réorganisation-du-plan-de-développement-et-de-la-documentation-transverse)
   - [9.27 – Difficulté 27 : Modélisation de Bibliothécaire et accès restreint à l’application](#927--difficulté-27--modélisation-de-bibliothécaire-et-accès-restreint-à-lapplication)
10. [📌 Décisions structurantes du projet](#10--décisions-structurantes-du-projet)
    - [10.1 Décision 1 (D-01) – Structuration progressive du développement par blocs fonctionnels](#101-décision-1-d-01--structuration-progressive-du-développement-par-blocs-fonctionnels)
    - [10.2 Décision 2 (D-02) – Centralisation des vues sur l’entité Media avec typage différé](#102-décision-2-d-02--centralisation-des-vues-sur-lentité-media-avec-typage-différé)
    - [10.3 Décision 3 (D-03) – Gel de la première version avant _refactorisation_ métier](#103-décision-3-d-03--gel-de-la-première-version-avant-_refactorisation_-métier)
    - [10.4 Décision 4 (D-04) – Clarification du champ `Support.consultable` selon le sous-type](#104-décision-4-d-04--clarification-du-champ-supportconsultable-selon-le-sous-type)
    - [10.5 Décision 5 (D-05) – Stratégie de gestion des messages et des logs](#105-décision-5-d-05--stratégie-de-gestion-des-messages-et-des-logs)
    - [10.6 Décision 6 (D-06) – Structuration des scenarii métier](#106-décision-6-d-06--structuration-des-scenarii-métier)
    - [10.7 Décision 7 (D-07) - Reorganisation des documents techniques et du plan de développement (version 3)](#107-décision-7-d-07---reorganisation-des-documents-techniques-et-du-plan-de-développement-version-3)
11. [📚 Références techniques et documentaires](#11--références-techniques-et-documentaires)
    - [11.1 Documentation officielle (Django et Python)](#111-documentation-officielle-django-et-python)
    - [11.2 Structuration des modèles et logique métier](#112-structuration-des-modèles-et-logique-métier)
    - [11.3 Tests, fixtures et organisation du code](#113-tests-fixtures-et-organisation-du-code)
    - [11.4 Modélisation métier et architecture logicielle](#114-modélisation-métier-et-architecture-logicielle)
    - [11.5 Modélisation métier et architecture logicielle](#115-modélisation-métier-et-architecture-logicielle)

---

## 1. 🎯 Objectifs du document

Dans une démarche itérative et progressive d'une main-courante technique du développement :
- Implémenter les vues et les templates HTML pour les fonctionnalités accessibles aux applications de la médiathèque, 
du bibliothécaire et de la consultation.
- Couvrir les opérations CRUD sur les modèles : `Media`, `Emprunt`, `Retour`, `Membre`, `JeuDePlateau`.
- Préparer les tests unitaires et fonctionnels pour chaque vue.
- Organiser les accès et l'UX des applications.
- Documenter les choix techniques, les difficultés rencontrées et les écarts par rapport au périmètre du sujet.

---

## 2. 📌 Fonctionnalités par entité – Profil Bibliothécaire

Cette section distingue les fonctionnalités explicitement demandées dans le sujet (primordiales) de celles qui peuvent 
être ajoutées pour améliorer l’expérience ou démontrer la maîtrise technique (souhaitables).

### 2.1 🧭 Fonctionnalités primordiales (exigées dans le sujet)

| Entité      | Fonctionnalités exigées                            |
|-------------|----------------------------------------------------|
| **Media**   | Liste, Détail, Création, Modification, Suppression |
| **Emprunt** | Création, Retour, Liste                            |
| **Membre**  | Liste, Création, Modification, Suppression         |

> ℹ️ Les entités Livre, Dvd et Cd sont des spécialisations du modèle Media.  
> Les vues sont centralisées sur Media, avec affichage conditionnel selon le type.

### 2.2 ✨ Fonctionnalités souhaitables (complémentaires)

| Entité           | Fonctionnalités complémentaires                                            |
|------------------|----------------------------------------------------------------------------|
| **Media**        | Filtrage par type (`LIVRE`, `DVD`, `CD`), Recherche par titre ou thème     |
| **Emprunt**      | Filtrage par statut (`EN_COURS`, `RETARD`, `RENDU`), Historique par membre |
| **Membre**       | Affichage des emprunts en cours, Blocage/déblocage du compte               |
| **JeuDePlateau** | Liste consultable (non empruntable), Détail, Création, Modification        |

> ℹ️ Ces fonctionnalités ne sont pas exigées dans la grille d’évaluation du sujet, mais peuvent être intégrées pour 
> démontrer la modularité du projet et la capacité à étendre le périmètre fonctionnel.
>
> ℹ️ La suppression de `JeuDePlateau` est réservée à l’administrateur et n’est pas incluse dans cette étape.

---

## 3. 🔐 Accès par profil utilisateur

| Fonctionnalité        | Admin | Bibliothécaire | Membre |
|-----------------------|:-----:|:--------------:|:------:|
| CRUD Media            |   ✅   |       ✅        |   ❌    |
| CRUD JeuDePlateau     |   ✅   |       ✅        |   ❌    |
| CRUD Membre           |   ✅   |       ✅        |   ❌    |
| CRUD Emprunt / Retour |   ✅   |       ✅        |   ❌    |
| CRUD Bibliothecaire   |   ✅   |       ❌        |   ❌    |
| Consultation Support  |   ✅   |       ✅        |   ✅    |

> ℹ️ Seul le profil “Bibliothécaire” concerne les développements de cette étape.

---

## 4. 🗂️ Fichiers concernés

| Type              | Fichier / Dossier                           | Statut     |
|-------------------|---------------------------------------------|------------|
| Routage           | `/urls.py`                                  | ✅ En cours |
| Vues              | `/views.py`                                 | ✅ En cours |
| Templates         | `/templates/<application>/`                 | ✅ En cours |
| Tests             | `/tests.py` et `/tests_blocs/`              | ✅ En cours |
| Fixtures          | `/fixtures/*.json` et `/fixtures/scenarii/` | ✅ En cours |
| Documentation     | `/docs/developpement/dev-docs/devMC.md`     | ✅ En cours |
| Plan de test      | `/docs/developpement/dev-docs/devTests.md`  | ✅ En cours |
| AF Bibliothécaire | `/docs/developpement/dev-docs/devAFBib.md`  | ✅ En cours |

---

## 5. 🔁 Routage et vues à implémenter

### 5.1 🧭 Fonctionnalités primordiales

| Entité  | Vue à implémenter                                  | Classe Django recommandée                                          |
|---------|----------------------------------------------------|--------------------------------------------------------------------|
| Media   | Liste, Détail, Création, Modification, Suppression | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| Emprunt | Création, Retour, Liste                            | `CreateView`, `UpdateView`, `ListView`                             |
| Membre  | Liste, Création, Modification, Suppression         | `ListView`, `CreateView`, `UpdateView`, `DeleteView`               |

### 5.2 ✨ Fonctionnalités souhaitables

| Entité       | Vue complémentaire                                | Objectif                             |
|--------------|---------------------------------------------------|--------------------------------------|
| Media        | Vue filtrée par `media_type`                      | Affichage ciblé (livres, DVD, CD)    |
| Emprunt      | Vue filtrée par `statut`                          | Suivi des emprunts en cours / rendus |
| Membre       | Vue d’historique d’emprunts                       | Visualisation des prêts passés       |
| JeuDePlateau | Liste consultable, Détail, Création, Modification | Consultation sans emprunt            |

---

## 6. 🧩 Templates HTML à créer

### 6.1 🧭 Fonctionnalités primordiales

| Vue                  | Template associé              |
|----------------------|-------------------------------|
| Liste des médias     | `media_list.html`             |
| Détail d’un média    | `media_detail.html`           |
| Formulaire média     | `media_form.html`             |
| Liste des emprunts   | `emprunt_list.html`           |
| Formulaire emprunt   | `emprunt_form.html`           |
| Retour emprunt       | `emprunt_retour_form.html`    |
| Liste des membres    | `membre_list.html`            |
| Formulaire membre    | `membre_form.html`            |

### 6.2 ✨ Fonctionnalités souhaitables

| Vue complémentaire         | Template associé                   |
|----------------------------|------------------------------------|
| Filtrage par type média    | `media_list_filtered.html`         |
| Historique emprunts membre | `membre_emprunts.html`             |
| Liste des jeux de plateau  | `jeu_list.html`                    |
| Détail d'un jeu de plateau | `jeu_detail.html`                  |
| Formulaire jeu de plateau  | `jeu_form.html`                    |

---

## 7. 🧪 Tests unitaires et validation

### 7.1 🧭 Fonctionnalités primordiales

- [X] Tests de chaque vue CRUD pour `Media`, `Emprunt`, `Membre`
- [X] Vérification des modèles via shell Django
- [X] Tests de navigation et affichage dans le navigateur
- [X] Préparation du plan de test (`tests-plan.md`)
- [/] Validation des cas métier avec fixtures

### 7.2 ✨ Fonctionnalités souhaitables

- [X] Tests de filtrage par type et statut
- [ ] Tests d’accès conditionnel (ex. : membre bloqué)
- [ ] Tests d’affichage des historiques
- [ ] Tests de liste, d'affichage, de création, de mise à jour des jeux de plateaux
- [ ] Tests de consultation des jeux de plateau

---

## 8. 📥 Fixtures de test à préparer

### 8.1 🧭 Fonctionnalités primordiales

- [X] `media_test.json` (livres, DVD, CD)
- [X] `emprunts_test.json`
- [X] `retours_test.json`
- [X] `membres_test.json`

### 8.2 ✨ Fonctionnalités souhaitables

- [X] `media_filtre_test.json` (pour tests de type)
- [X] `emprunts_statut_test.json` (pour tests de statut)
- [ ] `historique_emprunts_test.json`
- [X] `jeux_test.json`

---

## 9. 📌 Difficultés rencontrées

> À compléter au fil du développement : erreurs, choix techniques, contournements, arbitrages entre exigences et extensions.

### 9.1 Difficulté 1 : organiser le développement avec une vue d'ensemble cohérente - création d'une main courante de développement

La réalisation de la main courante me permet de structurer le travail. 
Mais, pour une première réalisation avec Django cela se traduit par plusieurs complexités à organiser :
- identification des fonctionnalités
- compréhension des fichiers à coder
- ordonnancement du développement
- relation backend-frontend
- mise en place des tests fonctionnels

À partir du site de référence [`Django - Documentation`](https://docs.djangoproject.com/fr/5.2/intro/), j'ai pu synthétiser 
une ligne directrice pour réaliser le développement fonctionnel initial de l'application Bibliothécaire.

### 9.2 Difficulté 2 : comprendre les mécanismes liés au moteur de template Django

Lors de la réalisation de template, Django exploite des mécanismes qui peuvent perturber l'interprétation du code HTML.
Par exemple, la mise en commentaire d'une ligne de code HTML n'était pas pris en compte sans l'insertion d'une commande 
`{% comment %} ... {% endcomment %}`.

> `{% comment %} ... {% endcomment %}` est interprété **par le moteur Django**, contrairement à `<!-- ... -->` qui est 
> ignoré **par le navigateur**.

Après lecture du [tutorial (partie 3) de la documentation de Django] (https://docs.djangoproject.com/fr/5.2/intro/tutorial03/), 
j'ai compris qu'il me fallait comprendre les mécanismes de Django pour interpréter les templates.
De ces lectures, j'ai créé un [_memento_](../../technique/Memento_Django-Balises-Filtres.md) pour une exploitation dans 
mon développement.

> Ce mémento est appelé à évoluer au fil du développement, notamment avec les _filtres personnalisés_ et les _tests de rendu_.

### 9.3 Difficulté 3 : choix de la meilleure architecture de Vue

Cette difficulté s'est avérée la plus complexe à expliciter, car elle apparaît anodine dans sa formulation tout en étant 
liée à de nombreux sujets impactés par la résolution choisie. Par conséquent, elle est développée pour parcourir les 
différentes facettes.

Sa résolution m'a permis de :
- prendre du recul sur les différentes solutions possibles entre le backend (le modèle de données) et le frontend 
(les templates)
- consolider le modèle et d'orienter précisément la suite des développements et la structure du code.

#### a) Contexte de la difficulté

Lors de la mise en œuvre des vues liées à l’entité `Media` (et ses spécialisations `Livre`, `Dvd`, `Cd`), une difficulté 
majeure est apparue : **quelle structure adopter pour les vues ?**  
Le sujet impose certaines fonctionnalités (liste, ajout), mais laisse ouvertes d’autres (détail, suppression). Cette 
situation a révélé que **le périmètre fonctionnel influence directement l’architecture technique**.

#### b) Deux architectures possibles

**1. Architecture centralisée sur `Media`**  
- Une seule vue générique (`MediaDetailView`, `MediaCreateView`, etc.) gère tous les types de médias.  
- Le template (`media_detail.html`) adapte l’affichage via des blocs conditionnels (`{% if media.media_type == "LIVRE" %}`, etc.).  
- Conforme au sujet, qui préconise une centralisation des vues.  
- Facile à mettre en place pour un périmètre fonctionnel limité.

**2. Architecture spécialisée par sous-type**  
- Une vue et un template distincts pour chaque type (`LivreDetailView`, `DvdDetailView`, etc.).  
- Permet d’utiliser des formulaires et des affichages spécifiques sans logique conditionnelle.  
- Favorise la modularité, la traçabilité, et l’extensibilité.  
- Plus adaptée si le projet évolue vers des entités supplémentaires ou des comportements spécifiques.

#### c) Critères de choix

Le choix architectural dépend de plusieurs facteurs :

| Critère                 | Architecture centralisée        | Architecture spécialisée           |
|-------------------------|---------------------------------|------------------------------------|
| Respect du sujet        | ✅                               | ⚠️ non exigée                      |
| Complexité du périmètre | ✅ adaptée à un périmètre réduit | ⚠️ surdimensionnée si peu de types |
| Évolutivité             | ⚠️ difficile à maintenir        | ✅ extensible par entité            |
| Clarté documentaire     | ⚠️ logique dispersée            | ✅ traçabilité par type             |
| Tests unitaires         | ⚠️ plus complexes à isoler      | ✅ ciblés et modulaires             |

#### d) Décision retenue

Pour répondre strictement au sujet, l’architecture centralisée est retenue pour l’étape 5.  
Cependant, la structure du projet est pensée pour **permettre une bascule vers une architecture spécialisée** si le 
périmètre fonctionnel s’élargit (ajout de nouveaux types, logique métier plus fine).

#### e) Importance de l’architecture technique des vues

Le choix de l’architecture des vues impacte :

- La **lisibilité du code** et des templates
- La **modularité** du projet
- La **qualité des tests** (unitaires et fonctionnels)
- La **documentation** et la traçabilité des comportements
- La **capacité à intégrer de nouveaux besoins** sans refactorisation lourde

Ce choix doit donc être **documenté, justifié, et réévalué** à chaque évolution du modèle métier.

#### f) Autres aspects à considérer

- **Organisation des templates** : par entité ou centralisé
- **Gestion des formulaires** : spécifiques ou génériques
- **Routage des URLs** : explicite par type ou générique
- **Tests de rendu** : par vue ou par type
- **Documentation technique** : alignée sur l’architecture retenue

### 9.4 Difficulté 4 : accéder aux données spécifiques de l’objet typé (héritage multi-table et ORM Django)

Cette difficulté, bien que discrète (aucune erreur explicite à l’exécution), s’est révélée déterminante pour garantir un 
affichage complet des données dans les vues. Elle ne relève pas d’un choix stratégique, mais d’un **problème technique lié 
au polymorphisme et à l’héritage multi-table dans Django**, combiné aux mécanismes internes de son ORM.

La documentation officielle aborde cette problématique de manière implicite, sans proposer de solution native pour “caster” 
automatiquement une instance de `Media` vers son sous-type (`Livre`, `Dvd`, `Cd`). Après avoir exploré les options de 
modélisation, j’ai orienté mes recherches vers les forums et les retours d’expérience communautaires, ce qui m’a permis 
d’identifier une **bonne pratique émergente**.

La résolution s’est faite en deux temps :
- Une **surcharge de la méthode `get_object()` dans la vue** pour accéder dynamiquement à l’objet typé, sans modifier le 
modèle.
- Une **éventuelle centralisation dans le modèle** via une méthode utilitaire (`get_real_instance()`), pour simplifier 
- et uniformiser le comportement dans toutes les vues concernées.

Cette difficulté illustre l’importance de comprendre non seulement la structure des modèles, mais aussi **la manière dont 
Django instancie et transmet les objets aux vues et aux templates**.

La résolution de cette difficulté m'a permis d'aller rechercher la solution dans les discussions en cours des forums.

#### a) Contexte de la difficulté

Le modèle de la médiathèque repose sur une classe mère `Media`, dont héritent les entités typées `Livre`, `Dvd`, `Cd`.  
Chaque sous-type possède des champs spécifiques (ex. : `auteur` pour `Livre`, `realisateur` pour `Dvd`, etc.), mais les 
vues sont centralisées sur `Media`.

Lors de l’affichage du détail d’un média, il est nécessaire d’accéder à la fois aux champs communs et aux champs 
spécifiques du type réel. Sinon, seules les données des champs communs sont affichés car accessibles.
Cette situation soulève une difficulté technique liée au **polymorphisme effectif** dans le cadre de l’**héritage 
multi-table Django**.

#### b) Problème rencontré

- Une instance récupérée via `Media.objects.get(pk=...)` est de type `Media` et **ne donne pas accès directement** aux 
champs spécifiques du sous-type.
- Les données typées sont stockées dans une table distincte, liée à `Media` via un champ `media_ptr_id`.
- Django ne permet pas d’accéder à `media.auteur` ou `media.realisateur` tant que l’objet n’est pas typé correctement.

#### c) Solution technique mise en œuvre

La méthode `get_object()` de la vue `MediaDetailView` a été **surchargée** pour retourner dynamiquement l’instance 
réelle du sous-type :

```python
def get_object(self):
    obj = super().get_object()
    if hasattr(obj, 'livre'):
        return obj.livre
    elif hasattr(obj, 'dvd'):
        return obj.dvd
    elif hasattr(obj, 'cd'):
        return obj.cd
    return obj
```

Cette logique exploite les **relations inverses automatiques** créées par Django (`media.livre`, `media.dvd`, etc.).  
Le template reçoit alors une instance typée, exposant à la fois les champs hérités et les champs spécifiques.

#### d) Enseignements et bonnes pratiques

- Cette difficulté est **technique**, non stratégique : elle découle du fonctionnement interne de l’ORM Django.
- Elle illustre le besoin de **maîtriser les mécanismes de l’héritage multi-table** pour accéder aux données de manière 
polymorphe.
- Il est recommandé de centraliser cette logique dans une méthode utilitaire (`get_real_instance()`) pour éviter la 
duplication et faciliter la maintenance.

#### e) Illustration schématique

```
Media (objet mère)
   ├── Livre (objet typé)  ← accès via obj.livre
   ├── Dvd   (objet typé)  ← accès via obj.dvd
   └── Cd    (objet typé)  ← accès via obj.cd
```

#### f) Conclusion

Cette difficulté, bien que discrète, est **fondamentale** pour garantir un affichage correct et complet des données dans 
une architecture Django orientée POO.  
Elle montre que le polymorphisme ne se résume pas à la structure des classes, mais dépend aussi de la **manière dont les 
objets sont instanciés et transmis aux vues/templates**.

### 9.5 Difficulté 5 : définir et structurer les tests unitaires

Cette difficulté a émergé non pas dans l’écriture des tests eux-mêmes, mais dans leur **organisation progressive** au 
sein du projet. Elle est directement liée à la montée en complexité du code, à la volonté de maintenir une traçabilité 
claire, et à l’exigence d’autonomie entre les modules anciens et les développements récents.

Elle prolonge les réflexions amorcées dans les sections 9.3 et 9.4 : après avoir clarifié l’architecture des vues et le 
typage des objets, il s’agissait ici de structurer les tests unitaires de manière à accompagner le développement de façon 
incrémentale, traçable et modulaire.

La résolution de cette difficulté m'a permis de structurer les tests unitaires et de préparer, puis réaliser le plan de 
tests dans une approche DRY (Don't Repeat Yourself) préconisée en POO. 

#### a) Nature de la difficulté
La documentation Django propose une structure minimale (`tests.py` à la racine de l’app), mais ne guide pas explicitement 
sur la **modularisation des tests** ni sur la manière de les organiser pour accompagner un développement incrémental. 
Il m’a fallu comprendre comment :
- Séparer les tests par fonctionnalité (accueil, liste, détail, etc.)
- Maintenir une cohérence entre les tests et les étapes du développement
- Faciliter la lecture et la contribution future par d’autres développeurs

#### b) Démarche exploratoire
Après avoir étudié les pratiques communautaires (forums, documentation officielle, guides structurés), j’ai adopté une 
organisation modulaire :

- Création d’un dossier `bibliothecaire/tests_blocs/` avec des fichiers dédiés :
  - `test_accueil.py`
  - `test_media_list.py`
  - `test_media_detail.py`
- Ajout d’un fichier `__init__.py` pour rendre le dossier détectable par Django
- Conservation du fichier `tests.py` comme **point d’entrée documentaire**, contenant :
  - Un test minimal (`test_environment`) pour valider l’environnement
  - Des commentaires orientant vers le dossier `tests_blocs/` et le fichier `tests-plan.md`

#### c) Compréhension à l’issue
- La **décomposition en structure** permet une lisibilité et une autonomie très forte entre les tests anciens et les 
ajouts récents.
- Le fichier `tests.py` joue un rôle de **pivot technique et pédagogique**, utile pour la mise en œuvre et la relecture.
- La rédaction d’un fichier `tests-plan.md` est une **bonne pratique essentielle** pour formaliser les objectifs, les 
cas de test, et la couverture attendue.

#### d) Documentation associée
- [Django – Tests unitaires](https://docs.djangoproject.com/fr/5.2/internals/contributing/writing-code/unit-tests/)
- [CodezUp – Django Testing Best Practices](https://codezup.com/django-testing-best-practices-unit-tests-integration-tests/)
- [Dev.to – Writing Scalable Unit Tests in Django](https://dev.to/shreyash_jhon_doe/writing-scalable-maintainable-unit-tests-in-django-a-practical-guide-with-real-examples-47a4)

Ces ressources me confirment que la modularisation des tests, l’usage de `setUpTestData()`, et la documentation parallèle 
sont des pratiques reconnues pour maintenir la qualité et la scalabilité du code.

### 9.6 Difficulté 6 : reprise de modélisation en cours de développement

Cette difficulté concerne la traçabilité et la lisibilité des développements. 
Elle est apparue lors de la mise en œuvre des premiers tests unitaires et l'analyse qui a découlé de l'identification 
de la cause d'une erreur lors d'un test (ou de sa mise au point).

La solution a consisté en trois points d'organisation :
- la création d'une note technique qui :
  - identifie les erreurs de modélisation.
  - propose au moins une analyse ou une proposition de résolution.
  - identifie les tests unitaires à reprendre après correction.
- l'indexation du plan de tests (contenu et rapport des tests) pour permettre sa reprise et mise à jour.
- la création de points de sauvegarde (Git) pour tracer les documents techniques et le code.

La résolution de cette difficulté a démontré :
- l'importance de coder au plus tôt les tests unitaires sur les objets du modèle.
- qu'un test unitaire peut fonctionner correctement tout en étant "non vérifié" (Ko) lors de la découverte d'une erreur 
(bogue).
- l'efficacité d'une démarche itérative qui reprend tous les tests unitaires.

### 9.7 Difficulté 7 : gestion des contrôles de validité sur les champs numériques de données

Cette difficulté concerne le contrôle des bornes (limites de validité) des champs numériques du modèle de données. 
Lors de la correction du champ `annee_edition` de l'entité `Support`, j'ai cherché à assurer dans le modèle une séparation 
claire et précise entre la structure du modèle et les méthodes de validation de la donnée.

La solution identifiée dans un premier temps, mais non retenue, a consisté à définir une propriété 
`Validators(MinValueValidator(valueMin),MaxValueValidator(valueMax))` dans la structure du modèle.
Mais cette propriété étant statique lors du chargement du module au démarrage du serveur, 
j'ai ensuite (second temps) mis en œuvre une définition dynamique et définissant une surcharge de la méthode `clean()` 
de l'entité du modèle (il s'agissait de `Support`).
Ceci m'a conduit à distinguer la portée de cette définition du contrôle de validité. 
Soit définir un contrôle centralisé métier dans l'entité _mère_ (`Media`), soit dans les entités typées (`Livre`, `Dvd` 
et `Cd`). 

Cette mise en évidence de la logique métier de validation m'a conduit à la solution finale retenue consistant à reporter 
la logique métier de contrôle de validité de la donnée dans les formulaires, 
au lieu de l'intégrer dans la modélisation du champ de l'entité du modèle. 

La solution retenue est un modèle simple concernant la définition des champs des entités du modèle avec un report dans 
les formulaires des méthodes de validation métier de la donnée.

La résolution de cette difficulté a démontré :
- l'importance d'une responsabilité claire en évitant la duplication des contrôles dans plusieurs entités héritées.
- l'intérêt de centraliser la logique métier dans les formulaires ou service, et de garder le modèle structurellement 
simple.
- la cohérence à conserver entre :
  - les bornes **stables** qui peuvent être définies dans le modèle via **Validators**.
  - les bornes **dynamiques** (ie. année courante) qui doivent être définies dans un formulaire ou une méthode `clean()`.
- l'importance de garantir l'intégrité métier avec une structure des données toujours cohérente.

### 9.8 Difficulté 8 : nommage des dossiers du projet

Lors de la création de dossiers dans la structure du projet, il est essentiel de vérifier qu’ils ne sont pas exclus par 
le fichier `.gitignore`.
Le dossier `media/` est un exemple typique : il est ignoré par défaut, car utilisé pour les fichiers uploadés.

La solution appliquée est d'utiliser le **nom des entités au pluriel pour les dossiers de templates** (medias/, livres/, 
membres/, etc.).

Cette correction a permis d’explorer l’interface de _refactorisation_ de PyCharm, notamment la _preview_ des impacts et 
l’exclusion sélective de fichiers sensibles (`.gitignore`, `migrations`).

### 9.9 Difficulté 9 : interactions entre les tests unitaires techniques et fonctionnels métier

Lors de la reprise des développements fonctionnels, après la correction du modèle (Bloc 1), il a été difficile de 
caractériser un test unitaire fonctionnel (métier) dans une catégorie technique (`NAV`, `ENT` ou `VUE`).
Une analyse fonctionnelle basée sur les cas d'usage du rôle de Bibliothécaire a permis d'identifier les différentes 
fonctionnalités à réaliser et à tester.

Pour éviter une liaison entre les tests unitaires et conserver ainsi une autonomie entre les tests, la solution a consisté 
à créer une nouvelle catégorie de tests unitaires (T-FUN) qui sont définis de manière spécifique.
Les tests techniques et fonctionnels sont regroupés dans une classe de **tests du cas d'usage** pour une facilité de 
développement et de maintenance.

Cette correction a permis d'approfondir cette démarche de tests unitaires à la fois pour des validations techniques, mais 
aussi pour des validations fonctionnelles, dans un cadre commun des tests de cas d'usage.

---

### 9.10 Difficulté 10 : Organisation et clarté du routage lié aux médias

#### a) Contexte de la difficulté

Lors de la mise en œuvre des vues liées à l’entité `Media`, une complexité est apparue concernant la **structuration des 
routes**. 
Le sujet impose plusieurs cas d’usage distincts :
- Affichage de la **liste complète** des médias
- Affichage des **médias disponibles** pour l’emprunt
- Création d’un emprunt ou d’un média (selon des critères métier).

Ces cas d'usage induisent des fonctions complémentaires :
- Affichage des **médias par type** (`LIVRE`, `DVD`, `CD`)

Cette diversité fonctionnelle soulève une question centrale : **comment organiser les routes de manière claire, cohérente 
et extensible**, sans créer d’ambiguïté entre les vues ni de duplication technique.

#### b) Problème rencontré

La route `/medias/` est déjà utilisée pour UC-LIST-01 (consultables).  
Ajouter des paramètres GET (`?type=...`, `?disponible=True`) sur cette route aurait permis un filtrage dynamique, mais 
aurait introduit une **ambiguïté métier** :
- `/medias/?type=LIVRE` : est-ce une vue typée ou une vue consultable filtrée ?
- `/medias/?disponible=True` : est-ce UC-LIST-02 ou une extension de UC-LIST-01 ?

Cette situation rend difficile la lecture du code, la documentation des cas d’usage, et la maintenance des tests.

#### c) Résolution retenue

Pour garantir une **clarté fonctionnelle et une traçabilité technique**, les routes ont été **scindées en trois chemins 
indépendants** :

| Route                       | Cas d’usage associé | Vue Django                 | Filtrage appliqué                     |
|-----------------------------|---------------------|----------------------------|---------------------------------------|
| `/medias/`                  | ----                | `MediaListView`            | ----                                  |
| `/medias/consultables/`     | UC-LIST-01          | `MediaConsultableListView` | `consultable=True`                    |
| `/medias/disponibles/`      | UC-LIST-02          | `MediaDisponibleListView`  | `consultable=True`, `disponible=True` |
| `/medias/types/?type=LIVRE` | UC-LIST-03          | `MediaTypeListView`        | `media_type='LIVRE'`                  |

> 🔹 Chaque route correspond à un **filtrage métier explicite**, testé et documenté séparément.  
> 🔹 Le routage est **orthogonal** : chaque chemin est indépendant, mais peut être enrichi par des paramètres GET (`theme`, 
> `statut`, etc.).

#### d) Enjeux techniques et fonctionnels

- **Lisibilité du code** : chaque vue est dédiée à un cas d’usage métier
- **Modularité des tests** : chaque UC possède ses propres tests (`T-NAV`, `T-ENT`, `T-VUE`, `T-FUN`)
- **Extensibilité** : chaque route peut évoluer sans impacter les autres
- **Documentation claire** : chaque route est associée à une UC dans `Analyse_Fonctionnalites_Bibliothecaire.md`

#### e) Enseignements

- Le routage n’est pas qu’un choix technique : il reflète la **logique métier** du projet.
- Il doit être pensé en fonction des **cas d’usage**, des **tests**, et de la **documentation**.
- Une route unique avec des paramètres GET peut sembler plus compacte, mais devient vite difficile à maintenir si elle 
couvre plusieurs logiques métier.

#### f) Conclusion

La scission des routes `/medias/` en trois chemins indépendants permet :
- Une **navigation claire** pour le bibliothécaire
- Une **architecture modulaire** pour le développeur
- Une **documentation traçable** pour le mainteneur

Cette difficulté m'a permis de comprendre et illustre l’importance de **penser le routage comme un outil métier**, et 
non comme une simple convention technique.

---

### 9.11 Difficulté 11 : Visualisation des contraintes du formulaire

#### a) Problématique

Lors de la mise en œuvre de UC-CREATE-01, le formulaire de création d’un média non typé repose sur un `ModelForm` Django.  
Les champs obligatoires sont correctement validés côté serveur, mais **aucun indicateur visuel (`*`, couleur, icône)** 
n’est affiché dans le template `media_form.html`.

#### b) Analyse technique

- Le formulaire utilise `form.as_p`, qui génère automatiquement les balises HTML sans personnalisation.
- Les attributs `required` sont bien présents dans le HTML, mais **non stylisés ni signalés visuellement**.
- Django permet de personnaliser les libellés (`label`) et les aides (`help_text`), mais cela relève du **design UX/UI**, 
non du périmètre fonctionnel.

#### c) Arbitrage

🔹 Le choix de ne pas afficher d’indicateur visuel d’obligation est **volontaire et justifié** :
- Les validations fonctionnelles sont présentes et testées.
- Le design sera revu ultérieurement par un designer.
- Le formulaire reste conforme aux exigences du sujet.

#### d) Résolution

- Le formulaire conserve une structure générique (`form.as_p`) pour faciliter la reprise.
- Aucun indicateur visuel n’est ajouté dans cette version.
- Le bloc de test `T-FORM-01` valide la logique métier sans test UX visuel.

#### e) Conclusion

Cette réflexion m'a permis :
- d'approfondir les fonctionnalités offertes par les formulaires génériques de Django.
- de clarifier la frontière entre le développement fonctionnel et les choix relevant du design UX/UI.

---

### 9.12 Difficulté 12 : Formalisation du cycle de vie initial et typé des médias

#### a) Contexte de la difficulté

Cette difficulté est apparue lors de la création des formulaires des médias typés (`Livre`, `DVD`, `CD`) en identifiant 
une ambiguïté sur la définition de l'état (et surtout initial) d'un média.  
Elle a révélé un besoin métier fondamental : **stabiliser les états initiaux des objets `Media`** typés, afin de 
garantir une cohérence entre les données créées, les transitions métier, et les vues exposées.

Le cycle de vie métier, modélisé dans le document d'analyse du cycle de vie d'un média ([devALCBibMedias.md](assets/technique/devALCBibMedias.md)), 
a permis d’identifier un **état initial explicite** :  
> **État 0** (début) → `consultable=False`, `disponible=False`

Ce point de départ est essentiel pour permettre au bibliothécaire de déclencher les transitions métier vers des états 
stables (création, empruntable, emprunté, hors gestion, etc.).

#### b) Problèmes identifiés

- Le modèle `Media` définissait par défaut `consultable=True`, `disponible=True`, ce qui plaçait les objets directement 
  en **état 3 (empruntable)**, sans validation métier.
- Les vues typées forçaient `disponible=True` sans cohérence avec la logique de `consultable`, créant des états instables.
- Le champ `consultable` était exposé dans le formulaire, mais parfois écrasé dans la vue, ce qui brouillait la 
  responsabilité métier.

#### c) Résolution apportée

La résolution s’est articulée autour de trois axes :

1. **Modèle** :  
   - Correction des valeurs par défaut :
     ```python
     consultable = models.BooleanField(default=False)
     disponible = models.BooleanField(default=False)
     ```
   - Alignement structurel avec l’état 0 du cycle de vie.

2. **Vues typées** :  
   - Mise en œuvre d’une méthode `set_lifecycle_flags()` pour initier les états métier selon le type.
   - Clarification des transitions vers l’état 1 ou 3 selon les cas d’usage.

3. **Documentation** :  
   - Rédaction du document [devALCBibMedias.md](assets/technique/devALCBibMedias.md) pour formaliser les états, 
     transitions, et impacts techniques.
   - Intégration dans le [Plan de tests](devTests.md) (`T-FUN-xx` à `T-FUN-yy`) pour valider les transitions métier.

   > Le document [devALCBibMedias.md](assets/technique/devALCBibMedias.md) défini les principes retenus pour le 
   > développement et les tests dans l'ensemble du projet, alors que le [Plan de tests](devTests.md) décrits les tests 
   > mis en œuvre.  

#### d) Enjeux et bénéfices

- **Cohérence métier** : chaque média typé entre dans le cycle de vie avec un état stable et explicite.
- **Clarté technique** : les vues ne surchargent plus arbitrairement les champs, mais respectent les transitions métier.
- **Traçabilité documentaire** : chaque état et transition est formalisé, testé, et documenté.
- **Extensibilité** : le cycle de vie peut être enrichi sans refactorisation lourde.

La transition (0) du cycle de vie est désormais formalisée comme : 
- Création technique → Initialisation métier → Passage à l’état "Attente" (État 1).
Les autres transitions du cycle de vie de l'objet `Media` typé (`Livre`, `Dvd`, `Cd`) sont explicites avec les 
- _cheminements_ autorisés ou interdits.

#### e) Conclusion

La Difficulté 12 constitue un **nœud central du projet**, car elle relie :
- la modélisation métier (`Analyse_LifeCycle_Medias.md`)
- la structure technique (`models.py`, `views.py`)
- la logique fonctionnelle (`formulaires`, `tests`, `templates`)

Sa résolution a permis de transformer une ambiguïté technique en **levier de stabilité et de scalabilité**, en posant 
les fondations d’un cycle de vie métier robuste et extensible pour le projet.
Cette clarification stabilise les vues de création, les tests fonctionnels et le cycle de vie global du modèle `Media`. 
Elle m'a permis de poursuivre le développement plus facilement en utilisant une description explicite, tout en ayant du 
recul entre les notions d'**objets** (modélisation), de structure **technique** (framework Django) et la logique 
**fonctionnelle** (le besoin métier). 

---

### 9.13 Difficulté 13 : Définir ce que signifie “ajouter un média” – segmentation fonctionnelle, typage différé et structuration technique

#### a) Contexte de la difficulté

La fonctionnalité “ajouter un média” semble triviale dans sa formulation, mais elle recouvre en réalité **plusieurs cas 
d’usage distincts**, selon que le média est typé dès sa création ou non. Cette ambiguïté a nécessité une clarification 
métier et technique pour garantir une couverture fonctionnelle cohérente.

#### b) Problème rencontré

Le terme “ajouter” peut désigner :
- la **création directe** d’un média typé (`Livre`, `Dvd`, `Cd`)
- la **création différée** d’un média non typé (`Media` avec `media_type='NON_DEFINI'`), suivi d’un typage ultérieur

Cette dualité impose de **lier la création à la mise à jour**, et de prévoir des cas spécifiques pour :
- la modification d’un média typé
- la modification d’un média non typé
- le typage d’un média non typé vers un type réel
- l’annulation d’un typage en cours

#### c) Résolution adoptée

La fonctionnalité “ajouter un média” a été **décomposée en 12 fonctions élémentaires** :

| Action         | Type ciblé                     |
|----------------|--------------------------------|
| Ajouter        | Livre, Dvd, Cd, Média non typé |
| Modifier       | Livre, Dvd, Cd, Média non typé |
| Typer          | Livre, Dvd, Cd                 |
| Annuler typage | Média non typé                 |

Cette segmentation permet de couvrir tous les cas d’usage métier, tout en assurant une traçabilité technique claire dans 
les vues, les formulaires et les tests.

#### d) Enseignements techniques

La résolution de cette difficulté a permis de :

- **Structurer les routes** de manière explicite pour chaque cas fonctionnel :
  - `/ajouter/<type>` pour les créations typées
  - `/modifier/` pour les mises à jour d'un média non typé
  - `<type>/modifier/` pour les mises à jour d'un média typé
  - `/modifier/<type>` pour les typages
  - `/annuler_typage/` pour les rollbacks

  > Cette clarté dans le routage facilite la maintenance, la compréhension globale et la documentation.

- **Enrichir le modèle** avec des méthodes utilitaires :
  - `mutate_to_typed()` pour la création typée
  - `get_real_instance()` pour le typage polymorphe
  - `get_update_url_name()` et `get_typage_url_name()` pour le routage dynamique
  - `get_specific_fields()` dans chaque sous-type pour centraliser les champs spécifiques
  
  > Ces ajouts rendent le modèle plus expressif, plus autonome et plus lisible pour les développeurs.

- **Segmenter les données de contexte** dans les vues et les templates (`is_typage`, `is_update`, `is_<type>`) pour 
éviter une complexité excessive dans le modèle tout en assurant une logique métier claire et testable.

#### e) Impacts sur le projet

- Création des vues `MediaTypage<Type>View` et `MediaCancelTypingView`
- Mise à jour des templates pour gérer les cas de typage et d’annulation
- Définition des tests fonctionnels `T-FUN-08` à `T-FUN-10`
- Documentation enrichie dans `Analyse_Fonctionnalites_Bibliothecaire.md`, `Analyse_LifeCycle_Medias.md` et `tests-plan.md`

> Cette difficulté m'a permis de comprendre comment derrière une fonctionnalité métier simple, peut se cacher une 
> **complexité technique structurante**, qui doit être anticipée, documentée et testée pour garantir la robustesse du projet.

---

### 9.14 Difficulté 14 : Définition transversale du cycle de vie métier avant développement des UC

#### a) Contexte de la difficulté

Après la validation du cycle de vie des entités `Media` dans [`devALCBibMedias.md`](assets/technique/devALCBibMedias.md), 
il est apparu nécessaire de formaliser **les interactions métier entre les entités `Media`, `Membre`, et `Emprunt`** avant 
de poursuivre le développement des fonctionnalités associées aux UC-MEMBRE et UC-EMPRUNT.

#### b) Résolution adoptée

Cette difficulté a conduit à la rédaction d’un document transversal :

➡️ Analyse du cycle de vie des entités de Bibliothécaire : [`devALCBib.md`](devALCBib.md)

Ce document :
- Définit les **vecteurs de contexte** de chaque entité
- Clarifie les **transitions typées** (saisie, fonction métier, DDM)
- Formalise les **règles DDM** qui automatisent les états métier
- Présente les **interactions croisées** entre les objets manipulés par le profil Bibliothécaire

Il constitue une **base métier stable** pour la validation des UC et la rédaction des tests fonctionnels du Bloc 3.

> 📌 Ce document est rattaché à la task6 et figé à l’index H-1.

#### c) Conclusion

La résolution de cette difficulté a permis de poser une **architecture métier claire et cohérente** avant toute 
implémentation technique.  
En définissant les vecteurs de contexte, les transitions typées et les règles DDM, le document `devALCBib.md` 
offre :

- Une **vision unifiée** du fonctionnement des entités `Media`, `Membre`, et `Emprunt`
- Une **base stable** pour la validation des UC-MEMBRE et UC-EMPRUNT
- Une **réduction des ambiguïtés fonctionnelles** en amont du développement
- Une **structuration méthodologique** utile à mes futurs développements.


> 📌 Cette difficulté a permis de stabiliser les fondations métier du Bloc 3.  
> Elle garantit que les développements des UC-MEMBRE et UC-EMPRUNT reposent sur une logique métier claire, testable et extensible.  
> Elle constitue l'application des difficultés 12 et 13 précédentes.

---

### 9.15 Difficulté 15 : Regroupement des tests techniques et fonctionnels dans un même groupe de tests

#### a) Contexte de la difficulté

Lors du développement de l’UC MEMBRE-UC-LIST, pour faciliter leur définition, les tests ont été regroupés dans un fichier 
unique `test_uc_list_membre.py`, incluant à la fois :
- des tests techniques (modèle, vue, template)
- des tests fonctionnels (filtrage métier, affichage conditionnel).

Ce choix diffère de l’organisation adoptée pour les UC liées à `Media`, où les tests sont répartis par typologie 
(`test_entites_media.py`, `test_vues_media_list.py`, etc.).

#### b) Analyse et décision

📌 Avantages :
- Regroupement homogène par UC
- Lecture métier facilitée
- Maintenance localisée

📌 Inconvénients :
- Typologie technique moins explicite
- Asymétrie documentaire entre entités
- Risque de confusion dans l’indexation des tests

📌 Décision :
Le regroupement est conservé pour les UC `Membre` et `Emprunt`, afin de favoriser la lisibilité métier et la validation 
incrémentale par commit. Chaque test portera dans sa dénomination l'identifiant (catégorie et index) définie dans 
le [plan de tests](devTests.md).  
Une harmonisation documentaire pourra être envisagée avec les tests des UC `Media`pourra être envisagée ultérieurement. 
Toutefois, la nature indépendante de chaque test permet une poursuite du projet sans _refactorisation_ de ces tests.

#### c) Résolution adoptée

Pour répondre à la difficulté de structuration des tests identifiée dans cette UC, une organisation modulaire a été mise 
en place dans le fichier `test_uc_list_membre.py`, selon les principes suivants :

##### 🔹 Dénomination explicite des tests
Chaque méthode de test est nommée selon le schéma `test_aaa_xx_description`, où :
- `aaa` est le préfixe de catégorie (`nav`, `ent`, `vue`, `fun`)
- `xx` est l’identifiant du test tel que défini dans `tests-plan.md`
- `description` est un résumé fonctionnel du test

> Exemple : `test_fun_11_uc_list_01_membres_non_archives`

Cette convention garantit une traçabilité directe entre le plan de test et le code source.

##### 🔹 Regroupement par catégorie dans des classes dédiées
Les tests sont répartis dans des classes distinctes selon leur nature :

| Classe de test                | Catégorie couverte              |
|-------------------------------|---------------------------------|
| `TestNavigationMembreUcList`  | Navigation (`T-NAV-xx`)         |
| `TestEntitesMembreUcList`     | Modèle / Entités (`T-ENT-xx`)   |
| `TestVuesMembreUcList`        | Vues / Templates (`T-VUE-xx`)   |
| `TestFonctionnelMembreUcList` | Fonctionnel métier (`T-FUN-xx`) |

Cette segmentation permet une exécution ciblée, une maintenance facilitée et une documentation alignée.

##### 🔹 Création d’une classe de base pour le jeu de données
Une classe `BaseMembreTestCaseData` a été introduite pour centraliser le chargement des données via `setUpTestData()` :

```python
class BaseMembreTestCaseData(TestCase):
    @classmethod
    def setUpTestData(cls):
        ...
```

Les classes `ENT`, `VUE` et `FUN` héritent de cette base, garantissant la cohérence du jeu de données tout en évitant 
les duplications.

##### 🔹 Maintien de l’indépendance des tests unitaires
Chaque méthode de test :
- est autonome et isolée
- ne dépend pas de l’ordre d’exécution
- ne modifie pas l’état global partagé
- respecte les bonnes pratiques Django (`TestCase`, `setUpTestData`, assertions explicites)

#### d) Conclusion

La résolution de cette difficulté (mineure) est suffisamment significative pour refléter une problématique liée à la 
prolifération des fichiers de code et de documentation. La démarche des tests indépendants m'a permis de changer la 
structure des tests sans action de _refactorisation_ technique et documentaire. 

Cette mise en œuvre d'une structure organisationnelle des fichiers de tests m'a permis d'améliorer mes connaissances dans 
la mise en œuvre des tests, tout en les rendant plus lisible pour la suite du développement. Elle constitue le lien entre 
les analyses fonctionnelles, le plan de tests et la validation technique et fonctionnelle du code.

Cette difficulté, bien que mineure en apparence, m'a permis de consolider la cohérence entre les documents d’analyse, les 
conventions de nommage du code, et la structure des tests. Elle constitue un point d’ancrage méthodologique pour les UC 
suivantes du Bloc 3.

---

### 9.16 Difficulté 16 : Redondance du champ `bloqué` et modélisation du blocage métier

#### a) Contexte de la difficulté

Cette difficulté est apparue lors de l'analyse de la modélisation issue du modèle initial de l’entité `Membre`, pour 
développer les fonctionnalités du Bibliothécaire liées aux membres de la médiathèque.
La première version du modèle de l'entité `Membre` s'appuie sur la réutilisation du code à reprendre qui introduit un champ
`bloqué` sans typage ni logique métier associée à un _Emprunteur_. Ce champ suggérait une suspension manuelle du droit 
d’emprunter pour un membre de la médiathèque.
Le cycle de vie des fonctionnalités métier du projet (cf. Difficulté 14) permet une gestion dynamique de la capacité 
d'emprunter du membre de la médiathèque. Ainsi la modélisation nécessaire pour développer les fonctions métier du 
Bibliothécaire a dû être reprise pour éviter un conflit avec les règles métier dynamiques déjà définies dans le modèle 
`Membre`.

#### b) Nature de la difficulté

Le champ `bloqué` était censé représenter un état d’interdiction d’emprunt. Or, cette logique est déjà encapsulée dans 
la méthode `peut_emprunter()` du modèle `Membre`, qui prend en compte :
- les retards en cours,
- le quota d’emprunts autorisés,
- le statut du membre (`EMPRUNTEUR`, `ARCHIVE`, etc.).

Ainsi, cela se traduit par :
- Risque de **redondance fonctionnelle** : deux mécanismes pour une même logique métier.
- Risque d’**incohérence** : un membre pourrait être marqué comme `bloqué=True` tout en étant autorisé à emprunter
selon `peut_emprunter()`.
- Absence de typage ou de validation sur le champ `bloqué`.

#### c) Résolution mise en œuvre

La méthode `peut_emprunter()` encapsule les contraintes métier (retards, quota, statut), ce qui rend inutile toute 
persistance d’un état `bloqué`. Ce champ introduit une duplication de logique et une source potentielle de divergence 
entre l’état stocké et l’état calculé.

✅ Le champ `bloqué` a été **supprimé** du modèle final.  
✅ Le blocage est désormais **géré exclusivement** par les règles métier dynamiques dans `peut_emprunter()`.

#### d) Enseignements et bonnes pratiques

- La logique métier doit être **centralisée** dans des méthodes explicites (`peut_emprunter()`), et non dispersée dans 
des champs de contrôle.
- Les états fonctionnels doivent être **déduits** à partir des données métier, et non stockés de manière redondante.
- Cette approche garantit :
  - une **cohérence fonctionnelle**,
  - une **traçabilité claire**,
  - une **extensibilité** du modèle sans duplication.

#### e) Impact technique

- Suppression du champ `bloqué` dans le modèle `Emprunteur`.
- Renforcement de la méthode `peut_emprunter()` comme point d’entrée métier.
- Mise à jour des vues et des tests pour s’appuyer sur cette logique dynamique.

#### f) Conclusion

La résolution de cette difficulté (mineure) est suffisamment significative pour refléter une problématique majeure liée 
à la cohérence entre la modélisation d'une entité et les fonctionnalités métier associées. Cela s'est traduit par une 
simplification de la structure du modèle de l'entité `Membre` associé à des méthodes centralisées dans son modèle. 
Le contrôle du droit d'emprunter est désormais centralisé dans `peut_emprunter()`, ce qui garantit une cohérence métier 
sans surcharge technique.
Ainsi la base de données est allégée (suppression du champ `bloque`) au profit de méthodes et de contrôles dynamiques 
associés aux fonctionnalités du Bibliothécaire.

Cette difficulté, bien que mineure en apparence, m'a permis de consolider la cohérence entre les champs de données d'une 
entité et ses méthodes centralisées dans la modélisation. Cette suppression m'a permis de simplifier la logique des vues, 
des formulaires et des templates. 

---

### 9.17 Difficulté 17 : Cohérence UX et gestion du contexte métier via session

#### a) Contexte de la difficulté

Cette difficulté est apparue lors de la mise en œuvre de la navigation entre les vues de liste (`MembreListView`) et les 
vues de détail ou de modification (`MembreDetailView`, `MembreUpdateView`) tout en recherchant à préserver le contexte 
métier d’origine (ex. : liste des membres en gestion), sans recourir à des paramètres visibles dans l’URL. 
Le but visé est que ce contexte permette une redirection cohérente après modification, même en cas de rupture UX (accès 
direct, historique, menu).

Cette volonté d'une cohérence de gestion métier et d'UX s'est accompagnée de contraintes techniques et de sécurité :
- Pour permettre un retour fluide vers la liste initiale après modification.
- Pour éviter d’exposer des paramètres dans l’URL.
- Pour tolérer les ruptures UX (accès direct, absence de contexte).

#### b) Nature de la difficulté

- Le contexte de navigation (`liste_origine`) n’est pas toujours disponible.
- Les vues doivent être **résilientes** à l’absence de contexte.
- Le moteur de template doit pouvoir injecter dynamiquement les liens de retour (`Annuler`, `Retour à la liste`).

#### c) Résolution mise en œuvre

✅ Création d’un **mixin `OrigineSessionMixin`** :
- Injecte l’origine de navigation dans la session (`liste_origine`).
- Utilisé dans `MembreListView`, `MembreDetailView`, `MembreUpdateView`.

✅ Nettoyage explicite du contexte dans les vues de sortie métier :
- Réinitialisation à l’accueil si navigation directe.
- Fallback vers `membre_list_gestion` en cas de rupture.

#### d) Enseignements et bonnes pratiques

- L’usage de **mixins** permet une propagation invisible du contexte UX.
- La session est un vecteur robuste pour maintenir la continuité métier.
- Il est essentiel de :
  - injecter le contexte à l’entrée,
  - le nettoyer à la sortie,
  - prévoir des comportements par défaut en cas de rupture.

#### e) Impact technique

- Création du mixin `OrigineSessionMixin`.
- Mise à jour des vues pour intégrer le mixin et gérer le contexte.
- Injection des liens dynamiques dans `get_context_data()`.
- Tests validés (`T-VUE-16`, `T-VUE-18`, `T-FUN-18`) avec navigation cohérente.

#### f) Conclusion

La résolution de cette difficulté masquée (pas de difficulté technique, mais une volonté de cohérence Métier et UX) est 
suffisamment significative pour refléter une problématique majeure qui m'a conduit à revoir la gestion des contextes 
techniques et d'exploitation de l'application.

Cette difficulté m'a été compliquée à résoudre pour maintenir en cohérence :
- la logique métier basé sur le cycle de vie des entités avec un contexte dynamique de gestion
- la sécurité et le routage avec des URLs sans paramètre apparent
- la logique de développement et de maintenance du code des vues, des formulaires et des templates de l'application.

La mise en œuvre de la solution technique de _contexte de session_ associé à la technique de _multi-héritage_ m'a permis 
de proposer dans un fichier `mixins.py` une solution complète et extensible pour la cohérence métier et la maîtrise du 
contexte d'UX.

Cette difficulté m'a conduit à revoir la notion de contexte, à maîtriser la gestion des URLs et à exploiter l'architecture 
d'héritage et d'ORM de Django.

---

### 9.18 Difficulté 18 : Appel implicite d’une méthode sans argument dans un template Django

#### a) Contexte de la difficulté

Lors de l’implémentation de `MEMBRE-UC-DELETE`, la logique métier repose sur la méthode `Membre.peut_etre_supprime()` pour 
déterminer si un membre peut être supprimé (aucun emprunt actif, statut non ARCHIVE). Cette méthode est utilisée dans le 
template `membre_detail.html` pour conditionner l’affichage du lien “Supprimer ce membre”.
La difficulté est apparue lors de l'emploi de la méthode `{% if membre.peut_etre_supprime() %}`, comme condition d'affichage 
du lien de suppression. En effet, ce codage lève une erreur conformément à la documentation de référence Django. 
Alors une correction simple consistant à supprimer les arguments, conduit à un fonctionnement totalement satisfaisant, mais 
complètement incohérent _a priori_ avec les particularités d'une méthode.
Cette difficulté reflète l'analyse menée pour comprendre et mettre en place une solution robuste et conforme à ma 
compréhension de Python et de Django.

#### b) Problème identifié

Dans les templates Django, l’expression `{% if membre.peut_etre_supprime %}` fonctionne **même si la méthode n’est pas 
décorée avec `@property`**, ce qui semble contre-intuitif. En réalité, Django tente d’appeler implicitement toute méthode 
**callable sans argument**, et utilise son résultat comme valeur de vérité.

Ce comportement :
- n’est pas explicitement garanti par la documentation officielle.
- dépend de la signature exacte de la méthode.
- peut être cassé par des décorateurs, des arguments, ou un changement de moteur de template.

#### c) Décision technique
Pour garantir la robustesse du projet :
- La méthode `peut_etre_supprime()` reste une méthode explicite dans le modèle `Membre`, sans `@property`, afin de préserver 
sa sémantique métier.
- Un **contexte explicite** est injecté dans les vues concernées (`MembreDetailView`, etc.) via un mixin dédié 
(`MembreSuppressionContextMixin`) qui ajoute `peut_etre_supprime` au dictionnaire de contexte.
- Le template utilise alors `{% if peut_etre_supprime %}` au lieu d’un appel implicite.

#### d) Justification
Cette approche :
- évite les effets de bord liés à l’appel implicite.
- respecte les conventions Python/Django.
- facilite les tests unitaires et fonctionnels.
- prépare une _refactorisation_ modulaire du projet.

#### e) Références
- [Django Templates – Variables](https://docs.djangoproject.com/en/stable/topics/templates/#variables) : “If a variable 
is callable, the template system will try calling it with no arguments.”
- [Stack Overflow – How to call model methods in template](https://stackoverflow.com/questions/54340703/how-to-call-model-methods-in-template) : exemple 
de codage du contexte pour éviter l’appel implicite.
- [Stavros.io – Function calls in Django templates](https://www.stavros.io/posts/function-calls-in-django-templates/) : 
analyse des appels implicites et des effets de bord.

#### f) Conclusion

La résolution de cette difficulté m'a conduit à rechercher une cohérence technique dans l'emploi des méthodes d'une entité.
J'ai pu identifier des subtilités dues à la capacité que le système de modèle de Django offre concernant les _appelables 
sans argument_ dans les templates. Cette compréhension permise par les documents de référence m'a conduit à préférer une 
solution explicite utilisant des variables de contexte que j'utilise comme un dictionnaire dynamique pour conditionner le 
rendu du template.

Ainsi bien que la première solution consistant à exploiter une méthode d'une entité sans expliciter ses arguments fonctionne,
la solution consistant à exploiter des variables de contexte m'est apparu plus robuste et maintenable, tout en étant conforme
à la fois à l'emploi et l'appel de méthode, ainsi qu'aux principes de Python et de Django.

Cette difficulté m'est apparue comme une synthèse des différentes difficultés précédemment vues (cf. Difficultés 11, 13, 
14, 15, 16 et 17) qui conduisent à revoir la notion de contexte, à maîtriser la gestion des URLs et à exploiter l'architecture 
d'héritage et d'ORM de Django.

La résolution de cette difficulté m'a conduit à la décision de prévoir une `refactorisation` complète du développement pour 
reprendre selon ces orientations le code établi dans le développement fonctionnel initial de l'application Bibliothécaire.

---

### 9.19 Difficulté 19 : Stylisation minimale des messages utilisateur

#### a) Contexte de la difficulté

Lors de l’implémentation de `MEMBRE-UC-DELETE` et de `MEMBRE-UC-UPDATE`, des messages métier ont été ajoutés pour informer 
l’utilisateur du résultat de l’action (succès, erreur, alerte).  
Le sujet impose une interface **basique**, mais précise que le design sera repris par un designer web (§3.2 des exigences).  
Il est donc nécessaire de proposer une **stylisation minimale, fonctionnelle et facilement remplaçable**.

#### b) Problème rencontré

- Les messages Django (`messages.success()`, `messages.error()`, etc.) sont affichés via `{{ message.tags }}` dans le 
template.
- Sans stylisation, ces messages sont invisibles ou peu lisibles.
- Une stylisation trop poussée risquerait de figer des choix graphiques et de gêner le travail du designer.

#### c) Solution technique mise en œuvre

Un bloc CSS minimal a été ajouté dans `_base.html` :

```html
<style>
  .messages { list-style: none; padding: 0; margin: 10px 0; }
  .messages li { padding: 6px 12px; margin-bottom: 5px; border-radius: 4px; font-weight: bold; }
  .success { background-color: #e6ffe6; color: #2d662d; }
  .error   { background-color: #ffe6e6; color: #992d2d; }
  .warning { background-color: #fff8e6; color: #996600; }
</style>
```

Ce style :
- rend les messages visibles et compréhensibles
- respecte une logique métier (succès, erreur, alerte)
- peut facilement être remplacé par une feuille de style CSS dédiée

#### d) Justification

- Répond à l’exigence primordiale du sujet : interface fonctionnelle, stylisation remplaçable
- Permet une UX cohérente sans surcharger le design
- Compatible avec les balises `{{ message.tags }}` et le système de messages Django

#### e) Documentation associée

- [Django – Messages framework](https://docs.djangoproject.com/fr/5.2/ref/contrib/messages/)
- [Django – Templates variables](https://docs.djangoproject.com/fr/5.2/topics/templates/#variables)

#### f) Conclusion

Cette stylisation minimale permet de respecter les contraintes du sujet tout en assurant une UX fonctionnelle.  
Elle prépare le terrain pour une reprise graphique par un designer, sans bloquer les choix visuels futurs.

Cette difficulté m'a permis de mettre en œuvre une stylisation minimaliste pour que l'UX conserve ses fonctionnalités 
sans figer la conception ultérieure d'un designer.

---

### 9.20 Difficulté 20 : Activation du calcul des retards des emprunts en cours

Cette difficulté est apparue lors de la mise en œuvre des UC liées à l’entité `Emprunt`, en particulier `EMPRUNT-UC-CREATE`.  
Le sujet impose que les membres ne puissent emprunter que s’ils ne sont pas en retard.  
Il est donc nécessaire de disposer d’un mécanisme de **mise à jour quotidienne** du statut des emprunts (`EN_COURS` → 
`RETARD`) avant toute opération métier.

#### a) Contexte de la difficulté

Le calcul du retard repose sur une comparaison entre la date de retour prévue (`date_retour`) et la date du jour.  
Ce calcul doit être effectué **une fois par jour**, idéalement à la première connexion du bibliothécaire, pour éviter 
les traitements automatiques non maîtrisés.  
Il doit également être **accessible manuellement** pour vérification ou relance.

#### b) Problème rencontré

- Django ne propose pas de tâche planifiée native (cron, scheduler) dans le périmètre du sujet.
- Le calcul doit être déclenché sans dépendance serveur, mais avec une garantie de fréquence (une fois par jour).
- Le déclenchement doit être **invisible ou intégré naturellement** dans l’interface métier.

#### c) Solution technique mise en œuvre

- Création d’une méthode `Emprunt.marquer_retards()` qui parcourt les emprunts `EN_COURS` et met à jour leur statut si 
`date_retour < date.today()`.
- Stockage dans la session Django (`request.session`) d’une clé `retard_last_check_date`.
- Vérification à chaque connexion du bibliothécaire :
  - Si la date est différente de `date.today()`, la méthode est déclenchée et la session est mise à jour.
- Ajout d’un bouton manuel dans `accueil.html` pour relancer la vérification si nécessaire.

#### d) Enseignements et bonnes pratiques

- L’usage de la session permet une activation **simple, traçable et sans dépendance externe**.
- Le déclenchement à la première connexion garantit une **cohérence métier** sans surcharge serveur.
- La commande manuelle permet une **vérification explicite** par le bibliothécaire.
- Cette logique doit être mise en œuvre **avant** les UC `EMPRUNT-UC-CREATE`, car elle conditionne la validité de 
`peut_emprunter()`.

#### e) Illustration schématique

```txt
Connexion du bibliothécaire →
  Vérification de session →
    Si date ≠ aujourd’hui →
      Appel Emprunt.marquer_retards() →
      Mise à jour des statuts →
      Mise à jour session
```

#### f) Conclusion

Cette difficulté m'a permis de formaliser un mécanisme métier essentiel, en conciliant :
- les exigences du sujet (pas de tâche planifiée en Django, codage en Django uniquement)
- la logique métier (retard = blocage d’emprunt)
- une UX fluide et invisible pour l’utilisateur

Elle constitue un prérequis technique et fonctionnel primordial pour la mise en œuvre des UC liées aux emprunts.

Elle m'a permis de mettre en application l'exploitation des contextes métier et de session (cf. Difficulté 17) dans une 
approche UX fluide qui ne met pas de solution technique complexe.

---

### 9.21 Difficulté 21 : Formalisation des méthodes métier et transitions d’état

Cette difficulté est apparue à mesure que les UC liées aux entités `Emprunt`, `Media` et `Membre` se sont précisées.  
Contrairement aux premières difficultés rencontrées pendant le codage, celle-ci s’est imposée **en amont**, lors de la 
modélisation métier.  
Elle concerne la nécessité de **formaliser les méthodes d’état et d’action** dans les modèles, afin de structurer les 
transitions métier avant toute implémentation technique.

#### a) Contexte de la difficulté

Le projet repose sur des entités dont le comportement métier dépend de leur état :
- Un `Emprunt` peut être en cours, rendu ou en retard
- Un `Media` peut être disponible, consultable, empruntable
- Un `Membre` peut emprunter ou non, selon ses emprunts et retards

Ces états ne sont pas toujours stockés directement dans les champs du modèle, mais sont souvent **calculés dynamiquement** 
via des méthodes métier (`peut_emprunter()`, `est_empruntable()`, `est_en_retard()`, etc.).

#### b) Problème rencontré

- Sans formalisation préalable, la logique métier risque d’être dispersée dans les vues, les formulaires ou les templates.
- Les transitions d’état (ex. : retour d’un emprunt) impliquent plusieurs entités, et doivent être synchronisées.
- La documentation fonctionnelle de Bibliothecaire ([devAFBib](devAFBib.md)) ne prévoyait initialement pas de section 
dédiée aux méthodes métier.

#### c) Solution mise en œuvre

- Ajout de méthodes métier dans les modèles :
  - `Membre.peut_emprunter()`
  - `Media.est_empruntable()`
  - `Emprunt.rendre()`, `Emprunt.est_en_retard()`, `Emprunt.date_retour_prévu`.
- Centralisation des transitions dans des méthodes d’action :
  - `Emprunt.rendre()` encapsule la mise à jour du statut et du média.
- Révision de l’analyse fonctionnelle Bibliothécaire ([devAFBib](devAFBib.md)) pour intégrer ces méthodes dans 
les UC, sans détailler leur logique interne.
- Alignement avec les DDM et vecteurs d’état définis dans le cycle de vie des entités ([devALCBib](devALCBib.md)).

#### d) Enseignements et bonnes pratiques

- Formaliser les méthodes métier **avant le codage** permet :
  - une meilleure traçabilité des UC
  - une simplification du code des vues
  - une documentation plus claire et modulaire.
- Cette approche s’inscrit dans une démarche de **modélisation orientée métier**, proche du Domain-Driven Design (DDD).
- Les transitions métier doivent être **encapsulées dans les modèles**, et non dispersées dans les vues.
- L'analyse fonctionnelle Bibliothécaire ([devAFBib](devAFBib.md)) doit prévoir une annexe “Méthodes métier par entité” 
ou les intégrer directement dans les UC.

#### e) Illustration schématique

```txt
Emprunt
   ├── date_retour_prévu = date_emprunt + DELAI_EMPRUNT
   ├── est_en_retard() → bool
   ├── rendre() → met à jour statut + média
Media
   ├── est_empruntable() → bool
Membre
   ├── peut_emprunter() → bool
```

#### f) Référence conceptuelle associée

La formalisation des méthodes métier et des transitions d’état s’appuie sur des principes issus de la modélisation orientée 
métier, notamment ceux décrits dans le **catalogue EAA (Enterprise Application Architecture)** de Martin Fowler.

Ce catalogue présente les grands patterns de structuration métier :
- Domain Model
- Service Layer
- Transaction Script
- Repository
- Identity Map
- Unit of Work

Ces concepts ont guidé la structuration des entités `Emprunt`, `Media` et `Membre`, ainsi que la définition des méthodes 
métier (`peut_emprunter()`, `est_empruntable()`, `rendre()`, etc.).

> 🔗 Référence guide : [Catalogue EAA – Martin Fowler](https://martinfowler.com/eaaCatalog/)
   >> 🔸 Référence utilisée pour formaliser les transitions métier, les vecteurs d’état, et les méthodes d’action dans les 
   >> entités.

Cette référence permet de situer les choix de modélisation dans une démarche reconnue, tout en les adaptant aux contraintes 
du projet Django et aux exigences du sujet. 

Ainsi, cette référence est utilisée comme guide de structuration métier, permettant d’adapter les patterns à la logique 
Django et aux contraintes du sujet. Elle est venue structurer comme un guide les références Django associées suivantes 
pour lesquelles :
- la formalisation des méthodes métier dans les modèles Django est une pratique recommandée par la communauté et la 
documentation spécialisée.  
- elle permet de centraliser les règles métier, de simplifier les vues, et de garantir une architecture maintenable.

> 🔗 Référence Django : [Django Best Practices: Models – LearnDjango.com](https://learndjango.com/tutorials/django-best-practices-models)  
> 🔗 Référence Django : [Separation of Business Logic and Data Access – GeeksforGeeks](https://www.geeksforgeeks.org/python/separation-of-business-logic-and-data-access-in-django/)  
> 🔗 Référence Django : [Django Models Best Practices – CodezUp](https://codezup.com/django-models-best-practices-for-scalable-applications/)

#### g) Conclusion

Cette difficulté marque une **évolution méthodologique** dans le développement du projet :  
- les premières difficultés (Difficultés 1 à 13) étaient techniques et survenaient pendant le codage ou en synthèse 
documentaire (pour le `commit` vers GitHub).  
- les dernières (à partir de Difficulté 14) sont **conceptuelles**, anticipées en amont, et structurent le développement.  
La formalisation des méthodes métier et des transitions d’état me permet un codage plus fluide, plus robuste et plus cohérent.

Le traitement de cette difficulté m'a permis de réorganiser ma méthode de développement, d'améliorer ma compréhension de 
la modélisation orientée métier en associant la modélisation de base de données à l'encapsulation des méthodes métier dans 
la structure (modèle, url, vue, template) du projet.

---

### 9.22 Difficulté 22 : Gestion des messages d’incohérence (Logs) et d’information utilisateur (UX)

#### a) Contexte de la difficulté

Cette difficulté est apparue lors de la formalisation du rendu d’un emprunt (`Emprunt.rendre()`), qui met en cohérence 
plusieurs éléments du modèle :
- l’état du média (`Media.disponible`).
- la date de retour (`Emprunt.date_retour`).
- le statut de l’emprunt (`StatutEmprunt`).

La combinaison de ces éléments a révélé la nécessité de :
- signaler les incohérences métier (ex. : média déjà disponible alors que l’emprunt est encore actif).
- informer l’utilisateur via des messages UX clairs.
- tracer les anomalies via des messages de log (`warnings.warn()` ou `logger.warning()`).

Cette difficulté, bien que tardivement identifiée, est au cœur de la robustesse métier du projet.

#### b) Nature de la difficulté

- Le sujet du projet mentionne la journalisation des actions, mais sans en préciser le périmètre ni le moment 
d’implémentation.
- Les incohérences métier ne doivent pas bloquer l’exécution, mais doivent être visibles pour le développeur et 
l’utilisateur.
- La gestion des logs ne peut pas être rétroactive sur les issues déjà développées sans casser la traçabilité.

#### c) Analyse

Deux types de messages doivent être distingués :
- **Messages UX** : affichés dans les vues ou les templates pour informer l’utilisateur (ex. : “Ce média est déjà 
disponible”).
- **Messages de log** : enregistrés dans les logs techniques pour tracer les anomalies ou incohérences 
(ex. : `warnings.warn()`).

#### d) Résolution

- Intégration progressive des messages :
  - Dans les méthodes métier du modèle : ajout de `warnings.warn()` pour les incohérences détectées.
  - Dans les vues : ajout de messages UX via `messages.warning()` ou `messages.info()` pour informer l’utilisateur.
- Centralisation de la journalisation complète dans l’issue #6, lors de la phase de validation finale.

> 🔸 Cette difficulté est transversale et impacte toutes les entités métier.  
> 🔸 Elle est documentée pour garantir la cohérence des données et la traçabilité des actions métier.

#### e) Références techniques

- [Python – Module `warnings`](https://docs.python.org/3/library/warnings.html)  
  > 🔹 Utilisé pour émettre des messages d’avertissement non bloquants dans les méthodes métier du modèle.

- [Django – Framework messages](https://docs.djangoproject.com/fr/5.2/ref/contrib/messages/)  
  > 🔹 Permet d’afficher des messages UX dans les vues et les templates (`messages.info()`, `messages.warning()`).

- [Django – Logging configuration](https://docs.djangoproject.com/fr/5.2/topics/logging/)  
  > 🔹 Guide pour configurer la journalisation technique dans `settings.py` (niveaux, formats, handlers).

> 🔸 Ces références sont à exploiter dans l’issue #6 pour la centralisation de la journalisation et la validation des 
> logs.

#### f) Conclusion

La gestion des messages métier (logs et UX) est une composante transversale du projet, apparue tardivement, mais 
essentielle pour :
- garantir la cohérence des données.
- informer l’utilisateur de manière claire.
- tracer les anomalies pour le développeur.

Cette difficulté a été identifiée lors du développement de la méthode `Emprunt.rendre()`, qui cristallise les enjeux de
cohérence métier.  
Elle a conduit à une stratégie en deux phases :
- intégration progressive dans les méthodes et vues (issues #3 à #5).
- centralisation et validation dans l’issue #6.

> 🔹 Cette approche permet de respecter la traçabilité pédagogique tout en assurant la robustesse fonctionnelle du projet.

Cette difficulté m'a permis de compléter ma connaissance dans les méthodes utilisées en Python et par Django pour gérer 
les logs d'une application. Sa résolution m'a permis de revoir et de consolider le plan de développement des issues 
(GitHub), sans rompre la traçabilité et la logique initiale du développement.

---

### 9.23 Difficulté 23 : Formalisation des scenarii métier

#### a) Contexte de la difficulté

Cette difficulté est apparue lors des premiers tests de validation de la fonction de _marquage des retards_. La situation 
dépendait, par choix fonctionnel, de données non saisissables et ni modifiables par l'administrateur. Ainsi, pour pouvoir 
mener des tests de validation en exploitant l'UI/UX de l'application et la base de données, j'ai dû mettre en place une 
solution reproductible et contrôlée.

La difficulté porte sur la nécessité de disposer de scenarii métier pour tester les fonctions d’emprunt, notamment celles 
qui exploitent des dates système (`auto_now_add`) ou des champs non saisissables par l’utilisateur. Ces fonctions ne 
peuvent pas être testées directement via l’interface sans attendre des jours réels pour constater des retards ou des 
transitions d’état.

#### b) Problème rencontré

Les tests fonctionnels deviennent difficilement réalisables sans injection directe de données. Or, les fixtures permettent 
de créer un contexte métier en base, avec des dates simulées, des statuts précis, et des emprunts typés. La définition 
du contenu des fixtures devient alors un **scénario métier**, qui permet une mise en œuvre immédiate dans l’UX et une 
validation reproductible.

#### c) Solution mise en œuvre

Chaque scénario est structuré dans un dossier `scenarii/scenar_X/` contenant :
- les fixtures `medias`, `membres`, `emprunts`, `superuser`
- un contexte métier simulé
- un effet attendu sur l’UX ou les fonctions métier

Un fichier `README.md` minimal est placé dans `/works/.../fixtures/scenarii/scenar_X/`, pointant vers la documentation 
complète dans `/docs/fonctionnel/scenarii/scenar_X.md`.

#### d) Extension du périmètre

Ce besoin, non explicitement formulé dans le sujet, devient transversal à toutes les applications du projet. Il constitue 
les prémisses de l’issue #6, qui vise à compléter les tests fonctionnels développés selon l’[devAFBib](devAFBib.md) et 
le [plan de tests](devTests.md).

#### e) Justification de la formalisation

La charge de travail induite est significative. Elle justifie une structuration documentaire dédiée, sans remettre en 
cause les développements antérieurs. La formalisation permet une validation fonctionnelle reproductible, une traçabilité 
des cas métier, et une extension progressive.

#### f) Références techniques

La formalisation des scenarii métier s’appuie sur plusieurs sources techniques et communautaires :

- [Django – Fixtures](https://docs.djangoproject.com/fr/5.2/topics/db/fixtures/)  
  > 🔹 Documentation officielle sur les formats (`JSON`, `XML`, `YAML`), les commandes `dumpdata` et `loaddata`, et les 
  > emplacements reconnus (`fixtures/`, `FIXTURE_DIRS`).

- [Django – Tests](https://docs.djangoproject.com/fr/5.2/topics/testing/)  
  > 🔹 Guide sur l’utilisation des fixtures dans les tests unitaires (`fixtures = [...]`), la préparation de l’état de 
  > la base, et la validation des comportements métier.

- [RealPython – Django Pytest Fixtures](https://realpython.com/django-pytest-fixtures/)  
  > 🔹 Tutoriel sur l’usage de `pytest` et de fixtures modulaires pour tester des modèles Django avec des données 
  > injectées.

- [Dev.to – Writing Scalable Unit Tests in Django](https://dev.to/shreyash_jhon_doe/writing-scalable-maintainable-unit-tests-in-django-a-practical-guide-with-real-examples-47a4)  
  > 🔹 Guide communautaire sur la structuration des tests, la modularisation, et la réutilisation des fixtures dans des 
  > cas métier.

Ces références m'ont confirmé que la structuration des scenarii métier est une bonne pratique pour garantir la 
reproductibilité des tests, la traçabilité des cas métier, et l’extensibilité du projet.

#### g) Conclusion

Cette difficulté m'a permis de reprendre la notion de tests fonctionnels dans une situation _bloquée_ du fait d'une 
impossibilité de saisir des données en base. La mise en place de scenarii m'a conduit à étendre ma compréhension des 
fixtures et à comprendre les notions de **sérialisation** associées à la production de ces fichiers à partir des données
de la base de données.
La résolution de cette difficulté m'a permis de réaliser et de reproduire tous les types de tests fonctionnels à partir 
de l'UI/UX de l'application (Bibliothecaire).

---

### 9.24 Difficulté 24 : Traçabilité UX des actions métier et synchronisation du contexte d’affichage

Cette difficulté est apparue lors de la mise en œuvre de l’UC `EMPRUNT-UC-RETARD`, en prolongement direct de la 
difficulté 17 (gestion du contexte métier via session).  
Elle concerne la **traçabilité UX des actions métier** (marquage des retards) et la **synchronisation du contexte 
d’affichage** dans une logique de persistance utilisateur de la page d'accueil du profil Bibliothecaire.

#### a) Contexte de la difficulté

L’UC `EMPRUNT-UC-RETARD` repose sur une action métier automatique (détection des retards) déclenchée une fois par jour.  
Cette action doit être **visible et compréhensible** par le bibliothécaire, sans recalcul ni perte d’information.  
La difficulté est apparue dans la gestion du **message UX**, du **tableau des emprunts marqués**, et du **bouton 
d’affichage conditionnel**, tous dépendants d’un contexte partagé entre session et vue.

#### b) Problèmes rencontrés

- Confusion entre `self.request.session[...]` (persistant) et `context[...]` (temporaire).
- Perte du message UX après navigation ou affichage conditionnel.
- Absence de nettoyage du contexte UX avant réinjection.
- Risque de désynchronisation entre les emprunts marqués et le message affiché.
- Besoin de mémoriser l’état d’affichage (`affiche_table`) sans exposer de paramètre GET.

#### c) Résolution technique

- Stockage explicite des clés UX dans la session : `retard_message`, `emprunts_marques_ids`, `affiche_table`.
- Injection systématique dans le contexte de la vue à chaque appel.
- Nettoyage préventif des clés UX avant marquage quotidien.
- Passage à un contrôle POST pour l’affichage conditionnel (évite les paramètres GET).
- Découplage clair entre logique métier (marquage) et logique UX (affichage).

#### d) Enseignements et bonnes pratiques

- La session est un outil puissant pour **mémoriser l’état UX**, mais nécessite une gestion rigoureuse.
- Le découplage entre logique métier et logique UX permet une meilleure traçabilité.
- Le bouton POST est préférable au paramètre GET pour éviter les fuites d’état dans l’URL.
- Le nettoyage du contexte UX avant injection garantit la cohérence des données affichées.
- Cette difficulté illustre l’importance de **formaliser les transitions UX** dans les vues métier.

#### e) Illustration UX

L'analyse fonctionnelle (devAFBib) illustre le cas d'usage avec les UX associés :
- Exemple 1 : [marquage automatique à la première connexion (message et tableau affichés)](devAFBib.md#-marquage-automatique---exemple-dux-obtenus-avec-le-scenario-scenar_01)
- Exemple 2 : [marquage manuel via commande dédiée (message injecté, tableau affiché)](devAFBib.md#-marquage-manuel---exemple-dux-obtenus-avec-le-scenario-scenar_01)

#### f) Conclusion

Cette difficulté est une extension directe de la 
[difficulté 17](#917-difficulté-17--cohérence-ux-et-gestion-du-contexte-métier-via-session), appliquée à une UC métier. 
Elle combine des enjeux techniques (session, injection de contexte) et UX (affichage conditionnel, lisibilité des 
actions). C'est pourquoi j'ai choisi une formalisation spécifique pour documenter les choix de traçabilité UX et de 
synchronisation du contexte.

La recherche d'une solution pour réaliser à la fois une action automatisée (marquage des retards) et de disposer d'une 
persistance UX des résultats de ce traitement dans la page d'accueil, ma permis d'exploiter plus précisément les capacités 
de gestion du contexte de Django en distinguant particulièrement le contexte de session et le contexte de la vue.

La recherche d'une solution pour disposer d'URLs propres (sans paramètre GET) m'a permis de mieux exploiter les méthodes 
GET et POST dans les templates.

Associé à une optimisation des méthodes (méthodes de classe) des entités de la base, cette solution technique m'a permis 
de développer le cas d'usage du marquage des retards d'emprunt (EMPRUNT-UC-RETARD) dans un code très épuré et sans 
répétition (concept DRY de la POO).

La résolution de cette difficulté m'a permis de capitaliser dans le codage de ce cas d'usage (EMPRUNT-UC-RETARD) 
l'expérience de développement issue des difficultés précédentes.

---

### 9.25 Difficulté 25 : Choix du modèle de vue pour une confirmation métier liée à un objet

Cette difficulté est apparue lors de la mise en œuvre de la vue `EmpruntRetourConfirmView`, qui doit permettre au 
bibliothécaire de confirmer le retour d’un emprunt sans modifier les champs résultants de sélections antérieures.
La recherche d'une solution de modélisation (architecture) m'a conduit à rejeter la solution à partir d'un modèle 
`UpdateView` pour me concentrer sur une modélisation basée sur `FormView`.

#### a) Contexte de la difficulté

La confirmation d’un retour est une action métier :
- elle ne modifie pas les champs via formulaire.
- elle repose sur une instance existante (`Emprunt`).
- elle doit afficher les données de l’objet (`media`, `emprunteur`, `date_emprunt`) dans le template.

Le besoin est donc :
- un formulaire statique (sans champs éditables).
- un accès à l’objet métier (`self.object` ou `get_object()`).

#### b) Problème rencontré

Le modèle `FormView` ne fournit pas `get_object()` ni `self.object` par défaut.  
Cela empêche l’accès aux données de l’objet `Emprunt` dans le template ou dans la logique métier.

#### c) Solution retenue

Ajout du mixin `SingleObjectMixin` à la vue :

```python
class EmpruntRetourConfirmView(SingleObjectMixin, FormView):
    model = Emprunt
    ...
```

Ce mixin permet :
- d’accéder à `self.object` dans `get()`, `form_valid()`, `get_context_data()`.
- d’utiliser `get_object()` sans redéfinition manuelle.

La vue devient ainsi capable :
- d’afficher les données de l’objet dans le template.
- d’exécuter la logique métier (`enregistrer_retour()`).
- de rediriger selon le contexte UX.

#### d) Enseignement

Le mixin `SingleObjectMixin` est indispensable pour toute **vue de confirmation métier liée à un objet**, lorsqu’on 
utilise `FormView`.  
Il permet de respecter la séparation des responsabilités :
- le formulaire reste statique.
- la logique métier reste dans la vue.
- l’accès aux données reste encapsulé.

Cette difficulté a également permis de clarifier le rôle des mixins :
- ils doivent **compléter** les vues, sans empiéter sur leur logique métier.
- ils ne doivent pas effectuer de calculs de redirection (`reverse()`), qui relèvent de la vue.

> 🔹 Cette clarification est intégrée dans l’AFBib (section 3.3.1.3 – UC-RETOUR)  
> 🔹 Elle permet de structurer les futures vues de confirmation (suppression, archivage, etc.)

#### e) Alternatives envisagées

Une alternative envisagée était l’utilisation de `UpdateView`, qui permet d’accéder à `get_object()` et `self.object` 
nativement.  
Cependant, cette classe est conçue pour des **vues de modification** de champs via formulaire, ce qui ne correspond pas 
au besoin métier ici.

Dans le cas de `EmpruntRetourConfirmView`, aucun champ n’est modifié par l’utilisateur :
- le formulaire est statique (pas de saisie).
- la logique métier est déclenchée par validation (`enregistrer_retour()`).

Utiliser `UpdateView` aurait impliqué :
- une surcharge inutile du comportement de mise à jour.
- une confusion sur l’intention métier (édition vs confirmation).

La solution `FormView` + `SingleObjectMixin` est donc plus adaptée :
- elle permet un formulaire statique.
- elle donne accès à l’objet métier.
- elle respecte la séparation des responsabilités.

> 🔹 Cette clarification permet de poser une convention pour les vues de confirmation métier :  
> 👉 **Utiliser `FormView` + `SingleObjectMixin` pour les actions métier sans édition de champs**.

#### f) Conclusion

La solution retenue résulte d’une recherche d’adéquation entre le besoin métier — une confirmation d’action sans 
modification de données — et les modèles de vue proposés par Django.  
Plutôt que d’utiliser `UpdateView`, conçu pour des formulaires évolutifs et des mises à jour de champs, le choix s’est 
porté sur `FormView` associé à `SingleObjectMixin`, permettant de gérer un formulaire statique tout en accédant à 
l’objet métier via `get_object()`.

Ce choix, qui peut sembler _puriste_ dans une première approche, a été déterminant pour approfondir ma compréhension des 
**Mixins**.  
Il illustre leur rôle fondamental : **étendre les capacités d’une vue sans en altérer la logique métier**, en injectant 
des comportements ciblés par héritage.  
L’exemple de `SingleObjectMixin`, qui ajoute l’accès à l’objet sans modifier le code existant, démontre la puissance de 
cette approche non intrusive.

Cette difficulté m’a permis :
- de clarifier les responsabilités entre vue, formulaire et modèle.
- de structurer une architecture extensible pour les confirmations métier.
- d’éviter toute _refactorisation_ des vues antérieures, conformément à la 
[décision D-03](#103-décision-3-d-03--gel-de-la-première-version-avant-_refactorisation_-métier).

Elle constitue un **point d’inflexion dans le raisonnement architectural** du projet, et mérite d’être documentée comme 
un fait marquant du développement.

---

### 9.26 Difficulté 26 : Réorganisation du plan de développement et de la documentation transverse

Cette difficulté est apparue à la fin du développement des entités principales de l’application Bibliothécaire (`Media`, 
`Membre`, `Emprunt`).  
La question s’est posée de savoir si les entités `JeuDePlateau` et `Support` relevaient de l’issue #3 (Bibliothécaire) 
ou de l’issue #4 (Consultation).

Cette interrogation a révélé un besoin plus profond : **réorganiser le contenu fonctionnel de chaque issue** pour 
clarifier leur périmètre et leur articulation.  
Elle a conduit à la définition d’une **version 3 du plan de développement**, fondée sur les principes suivants :

- Les issues **#3 et #4** sont dédiées au développement des **fonctions métier**, sans viser une intégration finale dans 
les applications.
- L’issue **#5** est consacrée à l’**intégration des fonctions dans les applications** (`Bibliothecaire`, `Consultation`) 
et à la mise en place des **accès et de la sécurité**.
- L’issue **#6** regroupe les travaux de finition UX, les filtrages, les messages cohérents et les validations 
fonctionnelles.

Cette réorganisation fonctionnelle a mis en évidence une difficulté sous-jacente :  
> Comment structurer la documentation technique pour qu’elle accompagne durablement toutes les issues du projet ?

La réponse a été la mise en place d’une **documentation transverse**, regroupée dans le dossier 
`/docs/developpement/dev-docs/`, avec des fichiers renommés selon leur fonction :

| Fonction              | Ancien nom (initial)                        | Nouveau nom (final) |
|-----------------------|---------------------------------------------|---------------------|
| Main-courante         | `_Frontend-main-courante.md`                | `devMC.md`          |
| Analyse fonctionnelle | `Analyse_Fonctionnalites_Bibliothecaire.md` | `devAFBib.md`       |
| Cycle de vie métier   | `Analyse_LifeCycle_Bibliothecaire.md`       | `devALCBib.md`      |
| Plan de tests         | `tests-plan.md`                             | `devTests.md`       |
| Rapport de tests      | `test_report_indexH-11.txt`                 | `devReport.md`      |

Cette documentation est mise à jour dans les branches `update-technical` de chaque issue, et poursuivie dans les 
branches `update-documentation` pour la rédaction du rapport final.

> Cette difficulté a permis de stabiliser une organisation documentaire durable, modulaire et extensible, garantissant 
> la traçabilité des choix techniques et la continuité du projet.
> 
> D'autre part, l'issue #3 doit contenir les deux rédactions (initiale et finale) pour assurer la continuité du 
> développement.

Cette réorganisation documentaire s’accompagne d’une refonte du plan de développement (version 3), qui segmente les 
issues par application (`bibliothecaire`, `consultation`, `mediatheque`) et par rôle métier.

---

### 9.27 – Difficulté 27 : Modélisation de Bibliothécaire et accès restreint à l’application

Cette difficulté est apparue lors de l’intégration de l’authentification et de la restriction des accès à l’application 
`bibliothecaire`.  

L’enjeu était de reprendre les développements antérieurs sans modifier les fonctionnalités existantes (une fois 
connecté), tout en garantissant la bonne exécution des tests unitaires associés. Les fonctionnalités de l’application 
se répartissent entre :

- primordiales, correspondant aux besoins de gestion courante des bibliothécaires ;
- importantes, non demandées explicitement, mais nécessaires pour l’administration et le bon fonctionnement global.

Cette dualité qui se retrouve dans les développements et les exigences fonctionnelles du projet, se traduit par une 
interface double relative à plusieurs rôles de Bibliothécaire. Ces rôles métiers de bibliothécaire sont :
- **BibAdmin**, le **bibliothécaire administrateur** qui accède à toutes les fonctions disponibles avec un affichage 
technique complet.
- **BibGestion**, le **bibliothécaire gestionnaire** qui n'accède qu'aux fonctions primordiales demandées pour le projet 
avec un affichage opérationnel. 

L'application Django prévoit l'utilisation d'un site d'administration accessible par un utilisateur `superuser` ou 
`staff`. Cette capacité fonctionnelle et technique intégrée dans le framework Django doit être conservé sans intervenir 
dans le fonctionnement de l'application. Cette indépendance doit être conservée. 

#### a) Contexte fonctionnel et technique

La mise en place de l’application `bibliothecaire` nécessite une gestion stricte des accès.  
Seuls les utilisateurs authentifiés doivent pouvoir accéder aux vues, avec une distinction entre les rôles internes 
(BibAdmin et BibGestion).  
Les membres de la médiathèque ne sont pas concernés par cette authentification.

Le développement des fonctions doit être revu pour ajouter les restrictions d'accès à chaque route fonctionnelle.

Le développement des tests doit être repris pour ajouter la contrainte de connexion et pour s'assurer des redirections 
prévues.

#### b) Description

La difficulté réside dans la modélisation de l’entité `Bibliothecaire` et son articulation avec `auth.User`.  
Deux approches étaient envisageables (modèle étendu via `AbstractUser` ou modèle lié via `OneToOneField`).  
Le choix retenu est de relier `Bibliothecaire` à `User` par un champ `OneToOneField`, avec un attribut `role` pour 
distinguer `BibAdmin` et `BibGestion`.  

Il est nécessaire de restreindre toutes les URLs de l’application `bibliothecaire` via `login_required` ou 
`LoginRequiredMixin`.

Il est nécessaire de compléter tous les tests de l'application bibliothecaire pour s'assurer de la connexion et de la 
bonne gestion des redirections. 

#### c) Impact

- Les tests existants doivent être adaptés pour gérer la connexion préalable.  
- Les rôles métier (BibAdmin/BibGestion) sont séparés des rôles techniques (`superuser`, `staff`).  
- Les membres restent des entités métier sans compte `User`.
- Les URLs associées à l'application Bibliothecaire sont à accès restreint.
- Les tests doivent prévoir une connexion et la bonne gestion des redirections.

#### d) Solution

- Ajout du champ `Bibliothecaire.user = OneToOneField(User, ...)`.  
- Ajout du champ `Bibliothecaire.role` avec valeurs `ADMIN` et `GESTION`.  
- Restriction des URLs de `bibliothecaire` via `login_required`.  
- Création d’une classe de test commune (`LoginRequiredTestCase`) pour factoriser la logique de connexion.  
- Vérification des redirections vers `/accounts/login/` pour les utilisateurs non connectés.

#### f) Conclusion

Cette difficulté a marqué un tournant dans l’intégration architecturale du projet. La solution retenue, basée sur une 
relation OneToOneField entre Bibliothecaire et User, s’est révélée explicite, non intrusive et facilement maintenable, 
tout en respectant les développements déjà réalisés.  

Elle a permis d’ajouter une fonctionnalité majeure (accès restreint) avec un minimum d’impact, d’exploiter pleinement le 
modèle User de Django et de renforcer la cohérence des tests. Ce choix constitue un **point d’inflexion fonctionnel et 
technique**, documenté comme un fait marquant du développement

Ainsi, devant agir sur plusieurs axes en parallèle (le modèle, les routes, les UX et les tests), la résolution de cette 
difficulté m’a permis :
- d'ajouter une fonctionnalité majeure au projet tout en reprenant avec un minimum d'impact les codes déjà réalisés.
- d'exploiter le modèle User de Django et de mieux comprendre les impacts des restrictions d'accès.
- d'exploiter dans les fonctions et les tests les principes de la POO pour intégrer avec un minimum d'impact la 
fonctionnalité d'accès restreint dans le projet.

---

### 9.28 – Difficulté 28 : Gestion des accès restreints et du template 403

Cette difficulté est apparue lors de la mise en place du décorateur `bibliothecaire_required` et de la gestion des accès 
restreints à l’application `bibliothecaire`.  
L’enjeu était de distinguer clairement les situations d’accès non autorisé (utilisateur non connecté ou connecté sans 
rôle Bibliothécaire) tout en garantissant une cohérence des URLs et une expérience utilisateur explicite.

#### a) Contexte fonctionnel et technique

La logique d’accès devait répondre à deux cas distincts :  
- **Utilisateur non connecté** : accès refusé, invitation à se connecter.  
- **Utilisateur connecté sans rôle Bibliothécaire** : accès refusé, retour vers l’accueil.  
- **Utilisateur connecté avec rôle Bibliothécaire** : accès autorisé.  

Le décorateur devait gérer ces situations sans dépendre de `login_required`, afin de conserver des URLs propres et 
éviter l’ajout automatique de paramètres `?next`.  
La difficulté s’est également posée sur le positionnement du template `403.html`, qui devait idéalement être placé dans 
`/accounts/templates/accounts/` pour rester cohérent avec les autres templates liés à l’authentification.

#### b) Description

La difficulté réside dans l’articulation entre :  
- La logique Django standard (`login_required`) qui redirige vers `/login?next=...` pour les utilisateurs non connectés.  
- La logique projet, qui privilégie une approche simple et cohérente : lever `PermissionDenied` et afficher une page 403 
avec des liens explicites.  

Deux problèmes ont été rencontrés :  
1. L’utilisation de `login_required` empêchait l’affichage du template 403 pour les utilisateurs non connectés.  
2. Le template `403.html` n’était reconnu que s’il était placé dans `mediatheque/templates/`, alors que la cohérence 
fonctionnelle demandait son placement dans `accounts/templates/accounts/`.

#### c) Impact

- Les utilisateurs non connectés étaient redirigés directement vers `/login`, ce qui contredisait l’esprit du 403 dans 
le projet.  
- Les URLs comportaient des paramètres `?next`, jugés peu élégants et non nécessaires dans ce contexte.  
- Le template 403 devait être déplacé dans `mediatheque/templates`, ce qui brouillait la séparation entre erreurs 
globales et erreurs liées aux accès utilisateurs.  
- La documentation devait clarifier cette divergence entre logique Django standard et logique projet.

#### d) Solution

- Suppression de l’appel à `login_required` dans le décorateur.  
- Mise en place d’un décorateur personnalisé qui lève `PermissionDenied` pour les cas non connectés et non autorisés.  
- Création d’un template `403.html` avec messages différenciés selon l’état de l’utilisateur (non connecté ou connecté 
sans rôle).  
- Définition d’un `handler403` dans `urls.py` racine pour permettre l’utilisation d’un template placé dans 
`/accounts/templates/accounts/403.html`.  

#### f) Conclusion

Cette difficulté a permis de clarifier la distinction entre logique technique (FBV avec `login_required`) et logique 
métier (CBV avec `RedirectURLMixin`).  
Le choix retenu – un décorateur personnalisé sans `login_required` – garantit des URLs propres, une expérience 
utilisateur explicite et une cohérence avec les règles du projet.  

Ce choix est **non standard Django**, mais il est adapté au cadre du projet :  
- Il respecte la consigne fonctionnelle (accès réservé aux utilisateurs connectés).  
- Il simplifie la logique en évitant les redirections automatiques et les paramètres `?next`.  
- Il documente clairement la divergence avec la pratique Django standard, afin que les futurs contributeurs puissent 
comprendre et éventuellement réintroduire `login_required` dans des projets ultérieurs.  

Cette résolution constitue un **point d’inflexion architectural** : elle illustre la capacité à adapter les conventions 
Django aux besoins spécifiques du projet, tout en maintenant une documentation claire et transmissible.

---

## 10. 📌 Décisions structurantes du projet

Cette section regroupe les décisions techniques et méthodologiques prises au cours du développement, en complément des 
difficultés rencontrées.  
Chaque décision est identifiée par un code (`D-01`, `D-02`, etc.) et documentée pour être auto-porteuse selon le même 
format que les difficultés : objectif, constat, décision.

---

### 10.1 Décision 1 (D-01) – Structuration progressive du développement par blocs fonctionnels

#### 🎯 Objectif  
Organiser le développement de l’application Bibliothécaire en blocs fonctionnels cohérents, traçables et pédagogiques.

#### 🔍 Constat  
- Le sujet impose plusieurs entités avec des UC distinctes.
- Le développement initial ne peut pas être linéaire : certaines entités dépendent d’autres.
- Une structuration par blocs permet de segmenter les étapes, documenter les difficultés, valider les UC progressivement.

#### 🧠 Décision  
- Le développement est organisé en blocs :
  - Bloc 1 : structuration du projet et des entités
  - Bloc 2 : développement des vues et formulaires de base
  - Bloc 3 : transitions métier et tests fonctionnels
- Chaque bloc est indexé dans la main-courante (ex. : G-10, H-9).
- Les difficultés sont rattachées au bloc concerné.

---

### 10.2 Décision 2 (D-02) – Centralisation des vues sur l’entité Media avec typage différé

#### 🎯 Objectif  
Respecter les exigences du sujet tout en assurant une architecture extensible pour les entités typées (`Livre`, `Dvd`, 
`Cd`).

#### 🔍 Constat  
- Le sujet impose une centralisation des vues sur `Media`.
- Les sous-types ont des champs spécifiques, mais partagent une logique commune.
- Le typage différé permet de créer un `Media` non typé, puis de le transformer.

#### 🧠 Décision  
- Les vues CRUD sont centralisées sur `Media`, avec affichage conditionnel.
- Le typage différé est géré via :
  - le champ `media_type`
  - la méthode `mutate_to_typed()` dans `Media`
- Les vues de typage sont ajoutées comme extensions, sans modifier la logique centrale.

---

### 10.3 Décision 3 (D-03) – Gel de la première version avant _refactorisation_ métier

#### 🎯 Objectif  
Garantir la traçabilité pédagogique en distinguant la première version livrable des améliorations métier postérieures.

#### 🔍 Constat  
- Le modèle métier évolue avec l’analyse métier.
- Ces évolutions impliquent des ajouts de méthodes métier, mais ne modifient pas les résultats fonctionnels.
- Une _refactorisation_ anticipée perturberait la traçabilité du développement.

#### 🧠 Décision  
- Aucune _refactorisation_ avant la finalisation complète de la version relative à l'issue #3 (développement fonctionnel 
initial de l'application `bibliothecaire`).
- Les ajouts métier seront :
  - intégrés dans `models.py_indexJ-5` (et suivant si besoin).
  - documentés dans AFBib (section 3.4).
  - exploités sans modifier les résultats fonctionnels existants.

---

### 10.4 Décision 4 (D-04) – Clarification du champ `Support.consultable` selon le sous-type

#### 🎯 Objectif  
Définir clairement le sens métier du champ `consultable` selon l’entité héritière (`Media` ou `JeuDePlateau`).

#### 🔍 Constat  
- Le champ `consultable` est défini dans `Support`, mais son interprétation dépend du sous-type.
- Pour `Media`, il signifie “visible à la consultation et empruntable”.
- Pour `JeuDePlateau`, il pourrait signifier “règle disponible”, mais ce sens n’est pas requis par le sujet.

#### 🧠 Décision  
- Le champ `consultable` reste dans `Support` comme capacité technique.
- La méthode `is_consultable()` est définie dans `Support`, mais son usage métier est limité à `Media`.
- La méthode `rendre_consultable()` est définie dans `Media` uniquement.
- L’application Consultation n’affichera que les instances de `Media` consultables.

---

### 10.5 Décision 5 (D-05) – Stratégie de gestion des messages et des logs

#### 🎯 Objectif

Définir une stratégie cohérente pour :
- la gestion des messages d’information utilisateur (UX).
- la journalisation des incohérences métier (logs techniques).

Cette décision garantit une traçabilité pédagogique, une UX cohérente, et une journalisation technique conforme aux 
exigences du projet.

#### 🔍 Constat

- Le sujet du projet mentionne la journalisation, mais sans spécifier son intégration dans les étapes de développement.
- La détection d’incohérences métier (ex. : tentative de rendu sur un média déjà disponible) nécessite une double 
signalisation :
  - à l’utilisateur (UX).
  - au développeur (logs).

#### 🧠 Décision

- **Phase 1 – Développement (issues #3 à #5)** :
  - Ajouter des `warnings.warn()` dans les méthodes métier du modèle pour tracer les incohérences.
  - Ajouter des messages UX dans les vues (`messages.warning()`, `messages.info()`) pour informer l’utilisateur.

- **Phase 2 – Validation (issue #6)** :
  - Centraliser la configuration du module `logging` dans `settings.py`.
  - Uniformiser les niveaux (`INFO`, `WARNING`, `ERROR`) et les formats.
  - Vérifier la cohérence des logs générés lors des tests fonctionnels.
  - Documenter les cas de journalisation dans la main-courante.

> 🔸 Cette stratégie permet de respecter la traçabilité pédagogique tout en assurant la robustesse métier du projet.

---

### 10.6 Décision 6 (D-06) – Structuration des scenarii métier

#### 🎯 Objectif de la décision

Formaliser la structuration des scenarii métier comme projet-support interne au sein du projet principal, pour accompagner 
le développement, les tests et la validation fonctionnelle.

#### 🔍 Contenu de chaque scénario

Chaque scénario contient :
- des fixtures injectables (`medias`, `membres`, `emprunts`, `superuser`)
- un contexte métier simulé
- un effet attendu sur l’UX ou les fonctions métier

#### 🧠 Décision

##### Organisation documentaire

La documentation des scenarii est placée dans :

```txt
/docs/fonctionnel/scenarii/
├── README_scenar.md
├── scenar_01.md
├── scenar_02.md
└── ...
```

Un fichier `README.md` minimal est placé dans :

```txt
/works/.../fixtures/scenarii/scenar_X/
```

Ce fichier contient un résumé du scénario et un lien vers la documentation fonctionnelle.

##### Portée de la décision

Cette structuration permet :
- une validation fonctionnelle reproductible
- une traçabilité des cas métier
- une extension progressive sans impact sur les développements antérieurs

Elle est volontairement minimaliste pour être exploitée dans la suite du développement sans avoir à reprendre les sujets 
antérieurs.

---

### 10.7 Décision 7 (D-07) - Reorganisation des documents techniques et du plan de développement (version 3)

À la suite de la Difficulté 26, une décision structurante a été prise pour garantir la continuité documentaire et la 
lisibilité du projet sur l’ensemble des issues à venir.

Deux axes ont été retenus :
- structuration de la documentation technique.
- organisation du plan de développement.

#### 🔹 1. Renommage des documents techniques de développement

Les documents produits dans l’issue #3 ont été renommés selon leur fonction transverse, et non plus selon leur index de 
version.  
Ils sont désormais regroupés dans le dossier `/docs/developpement/dev-docs/` :

| Nouveau nom    | Ancien nom                                  | Fonction                       |
|----------------|---------------------------------------------|--------------------------------|
| `devMC.md`     | `_Frontend-main-courante.md`                | Main-courante du développement |
| `devAFBib.md`  | `Analyse_Fonctionnalites_Bibliothecaire.md` | Analyse des fonctionnalités    |
| `devALCBib.md` | `Analyse_LifeCycle_Bibliothecaire.md`       | Analyse du cycle de vie métier |
| `devTests.md`  | `tests-plan.md`                             | Plan de tests                  |
| `devReport.md` | `test_report_indexH-11.txt`                 | Rapport de tests               |

Cette organisation permet :
- une réutilisation directe dans les issues suivantes.
- une maintenance facilitée.
- une séparation claire entre développement (`update-technical`) et rapport final (`update-documentation`).

#### 🔹 2. Structuration du plan de développement – Version 3

Le plan de développement a été redéfini pour clarifier le rôle de chaque issue :

- **Issue #3** : développement des fonctions métier de l’application `bibliothecaire` (sans finalisation UX).
- **Issue #4** : développement des fonctions métier de l’application `consultation` (sans finalisation UX).
- **Issue #5** : intégration des fonctions dans les applications (`bibliothecaire`, `consultation`) avec gestion des 
accès et de la sécurité.
- **Issue #6** : finition UX, filtrages, messages, validation fonctionnelle.
- **Issue #7** : rédaction du rapport final et livraison.

Cette structuration permet de :
- valider les traitements métier de manière robuste avant toute intégration UX.
- isoler les responsabilités techniques (métier, sécurité, UX).
- garantir une progression modulaire et traçable du projet.

> Cette décision marque la clôture technique de l’issue #3 et prépare la continuité documentaire et fonctionnelle du 
> projet dans les issues suivantes.

---

## 11. 📚 Références techniques et documentaires

Cette section regroupe les ressources utilisées pour guider le développement, la modélisation métier, la structuration 
des vues, et les bonnes pratiques Django.  
Elles ont été mobilisées à différentes étapes du projet, notamment pour résoudre les difficultés, formaliser les UC, et 
structurer les méthodes métier.
Elles sont rappelées dans cette section pour constituer un regroupement des documents principaux qui m'ont été utiles à 
la structuration de ma compréhension et à l'application des techniques et concepts employés.

---

### 11.1 Documentation officielle (Django et Python)

- [Django – Documentation officielle (version 5.2)](https://docs.djangoproject.com/fr/5.2/)
- [Django – Tutoriel d’introduction](https://docs.djangoproject.com/fr/5.2/intro/tutorial01/)
- [Python – Documentation officielle](https://docs.python.org/3/)

- [Python – Module `warnings`](https://docs.python.org/3/library/warnings.html)  
- [Django – Framework messages](https://docs.djangoproject.com/fr/5.2/ref/contrib/messages/)  
- [Django – Logging configuration](https://docs.djangoproject.com/fr/5.2/topics/logging/)  
- [Django – Tests](https://docs.djangoproject.com/fr/5.2/topics/testing/)

---

### 11.2 Structuration des modèles et logique métier

- [Django – Modèles et ORM](https://docs.djangoproject.com/fr/5.2/topics/db/models/)
- [Django – Héritage multi-table](https://docs.djangoproject.com/fr/5.2/topics/db/models/#multi-table-inheritance)
- [Django – Relations inverses et accès typé](https://docs.djangoproject.com/fr/5.2/ref/models/relations/)

- [LearnDjango – Django Best Practices: Models](https://learndjango.com/tutorials/django-best-practices-models)
- [GeeksforGeeks – Separation of Business Logic and Data Access in Django](https://www.geeksforgeeks.org/python/separation-of-business-logic-and-data-access-in-django/)
- [CodezUp – Django Models Best Practices](https://codezup.com/django-models-best-practices-for-scalable-applications)

---

### 11.3 Tests, fixtures et organisation du code

#### a) Tests unitaires et fonctionnels

- [Django – Tests](https://docs.djangoproject.com/fr/5.2/topics/testing/)
- [Django – Tests unitaires (contribution)](https://docs.djangoproject.com/fr/5.2/internals/contributing/writing-code/unit-tests/)
- [CodezUp – Django Testing Best Practices](https://codezup.com/django-testing-best-practices-unit-tests-integration-tests/)

- [Dev.to – Writing Scalable Unit Tests in Django](https://dev.to/shreyash_jhon_doe/writing-scalable-maintainable-unit-tests-in-django-a-practical-guide-with-real-examples-47a4)
- [Dev.to – Testing in Django (Ifihanagbara Olusheye)](https://dev.to/ifihan/testing-in-django-26e5)
- [TestDriven.io – Django Unit Testing Guide](https://testdriven.io/blog/django-unit-testing/) **(avec abonnement)**
- [LearnDjango – Django Testing Tutorial](https://learndjango.com/tutorials/django-testing-tutorial)


#### b) Fixtures et scenarii métier

- [Django – Fixtures](https://docs.djangoproject.com/fr/5.2/topics/db/fixtures/)
- [RealPython – Django Pytest Fixtures](https://realpython.com/django-pytest-fixtures/)

---

### 11.4 Modélisation métier et architecture logicielle

- [Django – Vue générique basée sur les classes](https://docs.djangoproject.com/fr/5.2/topics/class-based-views/)
- [Django – Routage et URLconf](https://docs.djangoproject.com/fr/5.2/topics/http/urls/)
- [Django – Templates et moteur de rendu](https://docs.djangoproject.com/fr/5.2/topics/templates/)
- [Django – Bonnes pratiques de structuration](https://docs.djangoproject.com/fr/5.2/misc/design-philosophies/)

---

### 11.5 Modélisation métier et architecture logicielle

- [Martin Fowler – Catalogue EAA (Enterprise Application Architecture)](https://martinfowler.com/eaaCatalog/)

---

## > Fin de document - lien vers le [sommaire](#-sommaire)

---
