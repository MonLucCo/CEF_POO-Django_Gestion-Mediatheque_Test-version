# 📊 Analyse du jeu de données initial – `initial_data.json`

Ce document analyse le contenu, les objectifs et la portée du jeu de données initial utilisé dans le projet Django de gestion de médiathèque. Il accompagne le fichier `initial_data.json` versionné dans `/docs/developpement/issue3/task4/`.

Ce jeu de données a été :
- **créé à l’étape 2** de l’issue #3 pour valider les modèles initiaux,
- **mis à jour à l’étape 4** pour refléter les enrichissements du backend (typages, champs, logique métier).

---

## 🧭 Sommaire

1. [Objectifs du jeu de données](#1-objectifs-du-jeu-de-données)  
2. [Structure des entités couvertes](#2-structure-des-entités-couvertes)  
3. [Cas de test simulés](#3-cas-de-test-simulés)  
4. [Évolution entre version initiale et finale](#4-évolution-entre-version-initiale-et-finale)  
5. [Fichiers associés](#5-fichiers-associés)  
6. [Remarques et limites](#6-remarques-et-limites)
7. [Perspectives pour les tests fonctionnels](#7-perspectives-pour-les-tests-fonctionnels)

---

## 1. Objectifs du jeu de données

- ✅ Valider la structure des modèles et leur enregistrement dans l’admin
- ✅ Simuler des cas métier : emprunt, retour, retard, blocage
- ✅ Tester les filtres, tris et recherches dans l’interface admin
- ✅ Préparer le socle pour les vues frontend à venir

---

## 2. Structure des entités couvertes

### 2.1 Description des entités du jeu de données initial

| Entité           | Volume | Champs clés présents                                                 | Particularités                          |
|------------------|--------|----------------------------------------------------------------------|-----------------------------------------|
| `Livre`          | 5      | `titre`, `auteur`, `nb_page`, `resume`                               | Hérite de `Media`                       |
| `Dvd`            | 5      | `titre`, `realisateur`, `duree`, `histoire`                          | Hérite de `Media`                       |
| `Cd`             | 5      | `titre`, `artiste`, `nb_piste`, `duree_ecoute`                       | Hérite de `Media`                       |
| `JeuDePlateau`   | 5      | `createur`, `categorie`, `nb_joueur_min`, `nb_joueur_max`, `age_min` | Non empruntable                         |
| `Membre`         | 5      | `nom`, `compte`, `bloque`                                            | Statuts variés                          |
| `Bibliothecaire` | 2      | `nom`                                                                | Interface admin simple                  |
| `Emprunt`        | 5      | `media`, `emprunteur`, `date_emprunt`, `date_retour`, `statut`       | Statuts typés                           |
| `Media`          | 15     | Support aux entités `Livre`, `Dvd` et `Cd`                           | Hérite de `Support`                     |
| `Utilisateur`    | (7)    | Abstrait                                                             | Hérité par `Membre` et `Bibliothecaire` |
| `Support`        | (20)   | Abstrait                                                             | Hérité par `Media` et `JeuDeplateau`    |

> ℹ️ **Note sur les entités abstraites**  
> Les classes `Utilisateur` et `Support` sont définies comme **abstraites** dans le modèle Django.  
> Elles ne sont pas instanciées directement dans le jeu de données, mais servent de base d’héritage :
> - `Utilisateur` est hérité par `Membre` et `Bibliothecaire`
> - `Support` est hérité par `Livre`, `Dvd`, `Cd`, `JeuDePlateau`

### 2.2 🔗 Relations entre entités

Les entités du jeu de données sont liées par des relations `ForeignKey` qui reflètent la logique métier :

- `Emprunt` → `Media` : chaque emprunt est associé à un média empruntable (`Livre`, `Dvd`, `Cd`)
- `Emprunt` → `Membre` : chaque emprunt est réalisé par un membre
- `Media` → `Support` : les types de média héritent de la structure commune `Support`
- `Membre`, `Bibliothecaire` → `Utilisateur` : les utilisateurs sont spécialisés selon leur rôle

Ces relations permettent de tester l’intégrité des données, les jointures dans l’admin, et les filtres dans les vues.

---

## 3. Cas de test simulés

- Emprunts :
  - En cours (`statut = EN_COURS`)
  - Rendus (`statut = RENDU`)
  - En retard (`statut = RETARD`)
- Médias de tous types (`Livre`, `Dvd`, `Cd`, `JeuDePlateau`)
- Membre bloqué avec emprunt actif (test de cohérence)
- Emprunt sans `date_retour` (retard implicite)
- Emprunt avec `date_retour` passée (retard explicite)

---

## 4. Évolution entre version initiale et finale

| Modification                                                     | Étape   | Description                                        |
|------------------------------------------------------------------|---------|----------------------------------------------------|
| Passage de `TextChoices` à `IntegerChoices` pour `StatutEmprunt` | Étape 4 | Permet le tri métier (`retard → en cours → rendu`) |
| Typage du champ `statut` en `IntegerField` dans `Emprunt`        | Étape 4 | Alignement avec l’énumération                      |
| Ajout des champs spécifiques à `JeuDePlateau`                    | Étape 4 | `categorie`, `règle`, `joueurs`, `durée`, `âge`    |
| Mise à jour des emprunts dans `initial_data.json`                | Étape 4 | Révision des statuts et dates                      |
| Ajout de `__str__()` et `verbose_name_plural` dans les modèles   | Étape 4 | Amélioration de l’affichage admin                  |

---

## 5. Fichiers associés

- `initial_data.json_indexH.txt` – version finale du jeu de données
- `models.py_indexH-final.txt` – modèle final validé
- `_Admin-main-courante.md` – documentation de l’interface admin
- `Analyse-initial_data.md` – présent document

---

## 6. Remarques et limites

> Ce jeu de données est conçu pour un usage en développement et validation.  
> Il ne couvre pas tous les cas limites métier (ex. : emprunt simultané, quotas, réservations).  
> Ces cas seront simulés dans les tests unitaires de l’étape 6 de l’issue #3.

---

## 7. Perspectives pour les tests fonctionnels

Les données simulées dans `initial_data.json` permettent de préparer une série de tests fonctionnels qui seront développés dans l’étape 6 de l’issue #3. Ces tests viseront à valider les règles métier, les comportements attendus et les cas limites.

### 7.1 Tests sur les emprunts

- ✅ Création d’un emprunt valide par un membre actif
- ❌ Refus d’un emprunt par un membre bloqué
- ❌ Refus d’un emprunt si le membre dépasse `MAX_EMPRUNTS`
- ❌ Refus d’un emprunt si le membre a des retards (`nb_retards > MAX_RETARDS`)
- ✅ Passage automatique du statut `EN_COURS` à `RETARD` si `date_retour` dépassée
- ✅ Passage du statut `EN_COURS` à `RENDU` avec `date_retour` renseignée

### 7.2 Tests sur les médias

- ✅ Vérification que seuls les médias disponibles peuvent être empruntés
- ✅ Vérification que les jeux de plateau ne sont pas empruntables
- ✅ Vérification du champ `consultable` dans les vues publiques

### 7.3 Tests sur les membres

- ✅ Calcul des propriétés `nb_emprunts_en_cours` et `nb_retards`
- ✅ Évaluation de la méthode `peut_emprunter()`
- ✅ Affichage correct dans l’admin (`__str__()`)

### 7.4 Tests d’intégrité et de cohérence

- ✅ Cohérence des relations `ForeignKey` (`Emprunt` → `Media`, `Membre`)
- ✅ Vérification des types et des choix (`media_type`, `statut`)
- ✅ Chargement et rechargement du jeu de données sans erreur

---

> Ces tests seront formalisés dans le fichier `tests.py` de l’application `bibliothecaire/`, avec des cas unitaires et fonctionnels.  
> Ils permettront de valider la robustesse du backend avant l’intégration frontend.

---
