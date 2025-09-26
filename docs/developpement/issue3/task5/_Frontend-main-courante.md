# 🧾 Main courante – Étape 5 : Développement fonctionnel initial

Cette main-courante documente l’étape 5 de l’issue #3 du projet Médiathèque : le développement fonctionnel initial de l’application dédiée au profil bibliothécaire.

Elle vise à :
- Structurer les actions techniques à réaliser
- Identifier les entités concernées et leurs fonctionnalités
- Clarifier les rôles utilisateurs et les accès
- Suivre les fichiers à produire et les tests à mettre en œuvre
- Documenter les difficultés rencontrées et les arbitrages méthodologiques

La rédaction s’appuie sur le modèle métier du projet, les exigences explicites du sujet, et les bonnes pratiques Django issues de la documentation officielle.

---

## 📑 Sommaire

1. [🎯 Objectifs de l’étape](#1--objectifs-de-létape)
2. [📌 Fonctionnalités par entité – Profil Bibliothécaire](#2--fonctionnalités-par-entité--profil-bibliothécaire)
3. [🔐 Accès par profil utilisateur](#3--accès-par-profil-utilisateur)
4. [️🗂️ Fichiers concernés](#4--fichiers-concernés)
5. [🔁 Routage et vues à implémenter](#5--routage-et-vues-à-implémenter)
6. [🧩 Templates HTML à créer](#6--templates-html-à-créer)
7. [🧪 Tests unitaires et validation](#7--tests-unitaires-et-validation)
8. [📥 Fixtures de test à préparer](#8--fixtures-de-test-à-préparer)
9. [📌 Difficultés rencontrées](#9--difficultés-rencontrées)
10. [🔗 Liens utiles](#10--liens-utiles)

---

## 1. 🎯 Objectifs de l’étape

- Implémenter les vues et les templates HTML pour les fonctionnalités accessibles au profil bibliothécaire
- Couvrir les opérations CRUD sur les modèles : `Media`, `Emprunt`, `Retour`, `Membre`
- Préparer les tests unitaires et fonctionnels pour chaque vue
- Documenter les choix techniques, les difficultés rencontrées et les écarts par rapport au périmètre du sujet

---

## 2. 📌 Fonctionnalités par entité – Profil Bibliothécaire

Cette section distingue les fonctionnalités explicitement demandées dans le sujet (primordiales) de celles qui peuvent être ajoutées pour améliorer l’expérience ou démontrer la maîtrise technique (souhaitables).

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

> ℹ️ Ces fonctionnalités ne sont pas exigées dans la grille d’évaluation du sujet, mais peuvent être intégrées pour démontrer la modularité du projet et la capacité à étendre le périmètre fonctionnel.
>
> ℹ️ La suppression de `JeuDePlateau` est réservée à l’administrateur et n’est pas incluse dans cette étape.

---

## 3. 🔐 Accès par profil utilisateur

| Fonctionnalité        | Admin | Bibliothécaire | Membre |
|-----------------------|:-----:|:--------------:|:------:|
| CRUD Media            |   ✅   |       ✅        |   ❌    |
| Consultation Media    |   ✅   |       ✅        |   ✅    |
| CRUD JeuDePlateau     |   ✅   |       ✅        |   ❌    |
| CRUD Membre           |   ✅   |       ✅        |   ❌    |
| CRUD Bibliothecaire   |   ✅   |       ❌        |   ❌    |
| CRUD Emprunt / Retour |   ✅   |       ✅        |   ❌    |

> ℹ️ Seul le profil “Bibliothécaire” concerne les développements de cette étape.

---

## 4. 🗂️ Fichiers concernés

| Type          | Fichier / Dossier                                       | Statut         |
|---------------|---------------------------------------------------------|----------------|
| Routage       | `bibliothecaire/urls.py`                                | 🆕 À créer     |
| Vues          | `bibliothecaire/views.py`                               | 🔄 À compléter |
| Templates     | `bibliothecaire/templates/bibliothecaire/`              | 🆕 À créer     |
| Tests         | `bibliothecaire/tests.py`                               | 🔄 À compléter |
| Fixtures      | `bibliothecaire/fixtures/*.json`                        | 🆕 À créer     |
| Documentation | `/docs/developpement/issue3/_Frontend-main-courante.md` | ✅ En cours     |
| Plan de test  | `/docs/tests/tests-plan.md`                             | 🆕 À créer     |

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

- [ ] Tests de chaque vue CRUD pour `Media`, `Emprunt`, `Membre`
- [ ] Vérification des modèles via shell Django
- [ ] Tests de navigation et affichage dans le navigateur
- [ ] Préparation du plan de test (`tests-plan.md`)
- [ ] Validation des cas métier avec fixtures

### 7.2 ✨ Fonctionnalités souhaitables

- [ ] Tests de filtrage par type et statut
- [ ] Tests d’accès conditionnel (ex. : membre bloqué)
- [ ] Tests d’affichage des historiques
- [ ] Tests de liste, d'affichage, de création, de mise à jour des jeux de plateaux
- [ ] Tests de consultation des jeux de plateau

---

## 8. 📥 Fixtures de test à préparer

### 8.1 🧭 Fonctionnalités primordiales

- [ ] `media_test.json` (livres, DVD, CD)
- [ ] `emprunts_test.json`
- [ ] `retours_test.json`
- [ ] `membres_test.json`

### 8.2 ✨ Fonctionnalités souhaitables

- [ ] `media_filtre_test.json` (pour tests de type)
- [ ] `emprunts_statut_test.json` (pour tests de statut)
- [ ] `historique_emprunts_test.json`
- [ ] `jeux_test.json`

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

À partir du site de référence [`Django - Documentation`](https://docs.djangoproject.com/fr/5.2/intro/), j'ai pu synthétiser une ligne directrice pour réaliser le développement fonctionnel initial de l'application Bibliothécaire.

### 9.2 Difficulté 2 : comprendre les mécanismes liés au moteur de template Django

Lors de la réalisation de template, Django exploite des mécanismes qui peuvent perturber l'interprétation du code HTML.
Par exemple, la mise en commentaire d'une ligne de code HTML n'était pas pris en compte sans l'insertion d'une commande `{% comment %} ... {% endcomment %}`.

> `{% comment %} ... {% endcomment %}` est interprété **par le moteur Django**, contrairement à `<!-- ... -->` qui est ignoré **par le navigateur**.

Après lecture du [tutorial (partie 3) de la documentation de Django] (https://docs.djangoproject.com/fr/5.2/intro/tutorial03/), j'ai compris qu'il me fallait comprendre les mécanismes de Django pour interpréter les templates.
De ces lectures, j'ai créé un [_memento_](../../../technique/Memento_Django-Balises-Filtres.md) pour une réexploitation dans mon développement.

> Ce mémento est appelé à évoluer au fil du développement, notamment avec les _filtres personnalisés_ et les _tests de rendu_.

### 9.3 Difficulté 3 : choix de la meilleure architecture de Vue

Cette difficulté s'est avérée la plus complexe à expliciter, car elle apparaît anodine dans sa formulation tout en étant liée à de nombreux sujets impactés par la résolution choisie. Par conséquent, elle est développée pour parcourir les différentes facettes.

Sa résolution m'a permis de :
- prendre du recul sur les différentes solutions possibles entre le backend (le modèle de données) et le frontend (les templates)
- consolider le modèle et d'orienter précisément la suite des développements et la structure du code.

#### a) Contexte de la difficulté

Lors de la mise en œuvre des vues liées à l’entité `Media` (et ses spécialisations `Livre`, `Dvd`, `Cd`), une difficulté majeure est apparue : **quelle structure adopter pour les vues ?**  
Le sujet impose certaines fonctionnalités (liste, ajout), mais laisse ouvertes d’autres (détail, suppression). Cette situation a révélé que **le périmètre fonctionnel influence directement l’architecture technique**.

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
Cependant, la structure du projet est pensée pour **permettre une bascule vers une architecture spécialisée** si le périmètre fonctionnel s’élargit (ajout de nouveaux types, logique métier plus fine).

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

Cette difficulté, bien que discrète (aucune erreur explicite à l’exécution), s’est révélée déterminante pour garantir un affichage complet des données dans les vues. Elle ne relève pas d’un choix stratégique, mais d’un **problème technique lié au polymorphisme et à l’héritage multi-table dans Django**, combiné aux mécanismes internes de son ORM.

La documentation officielle aborde cette problématique de manière implicite, sans proposer de solution native pour “caster” automatiquement une instance de `Media` vers son sous-type (`Livre`, `Dvd`, `Cd`). Après avoir exploré les options de modélisation, j’ai orienté mes recherches vers les forums et les retours d’expérience communautaires, ce qui m’a permis d’identifier une **bonne pratique émergente**.

La résolution s’est faite en deux temps :
- Une **surcharge de la méthode `get_object()` dans la vue** pour accéder dynamiquement à l’objet typé, sans modifier le modèle.
- Une **éventuelle centralisation dans le modèle** via une méthode utilitaire (`get_real_instance()`), pour simplifier et uniformiser le comportement dans toutes les vues concernées.

Cette difficulté illustre l’importance de comprendre non seulement la structure des modèles, mais aussi **la manière dont Django instancie et transmet les objets aux vues et aux templates**.

La résolution de cette difficulté m'a permis d'aller rechercher la solution dans les discussions en cours des forums.

#### a) Contexte de la difficulté

Le modèle de la médiathèque repose sur une classe mère `Media`, dont héritent les entités typées `Livre`, `Dvd`, `Cd`.  
Chaque sous-type possède des champs spécifiques (ex. : `auteur` pour `Livre`, `realisateur` pour `Dvd`, etc.), mais les vues sont centralisées sur `Media`.

Lors de l’affichage du détail d’un média, il est nécessaire d’accéder à la fois aux champs communs et aux champs spécifiques du type réel. Sinon, seules les données des champs communs sont affichés car accessibles.
Cette situation soulève une difficulté technique liée au **polymorphisme effectif** dans le cadre de l’**héritage multi-table Django**.

#### b) Problème rencontré

- Une instance récupérée via `Media.objects.get(pk=...)` est de type `Media` et **ne donne pas accès directement** aux champs spécifiques du sous-type.
- Les données typées sont stockées dans une table distincte, liée à `Media` via un champ `media_ptr_id`.
- Django ne permet pas d’accéder à `media.auteur` ou `media.realisateur` tant que l’objet n’est pas typé correctement.

#### c) Solution technique mise en œuvre

La méthode `get_object()` de la vue `MediaDetailView` a été **surchargée** pour retourner dynamiquement l’instance réelle du sous-type :

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
- Elle illustre le besoin de **maîtriser les mécanismes de l’héritage multi-table** pour accéder aux données de manière polymorphe.
- Il est recommandé de centraliser cette logique dans une méthode utilitaire (`get_real_instance()`) pour éviter la duplication et faciliter la maintenance.

#### e) Illustration schématique

```
Media (objet mère)
   ├── Livre (objet typé)  ← accès via obj.livre
   ├── Dvd   (objet typé)  ← accès via obj.dvd
   └── Cd    (objet typé)  ← accès via obj.cd
```

#### f) Conclusion

Cette difficulté, bien que discrète, est **fondamentale** pour garantir un affichage correct et complet des données dans une architecture Django orientée POO.  
Elle montre que le polymorphisme ne se résume pas à la structure des classes, mais dépend aussi de la **manière dont les objets sont instanciés et transmis aux vues/templates**.

---

## 10. 🔗 Liens utiles

- [Issue #3 – Développement de l’application fonctionnelle bibliothécaire](https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version/issues/3)  
- [README-tech.md](../../technique/README-tech.md)  
- [Analyse_Fonctionnalites.md](../../fonctionnel/Analyse_Fonctionnalites.md)  
- [tests-plan.md](../../tests/tests-plan.md) *(à créer)*

---
