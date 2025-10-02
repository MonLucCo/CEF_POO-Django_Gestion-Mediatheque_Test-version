# 🛠️ Modélisation – Corrections suite aux tests unitaires

📁 `/docs/developpement/issue3/task5/Modelisation_correction-erreurs-suite-tests-unitaires.md`  

📌 Version : indexE-5

---

## Sommaire

- [1. Introduction](#1-introduction)
  - [1.1 Objectif du document](#11-objectif-du-document)
  - [1.2 Positionnement du document dans le cycle de développement](#12--positionnement-du-document-dans-le-cycle-de-développement)
  - [1.3 Historique des corrections et versions du développement](#13-historique-des-corrections-et-versions-du-développement)
- [2. Synthèse des corrections à appliquer](#-2-synthèse-des-corrections-à-appliquer)
- [3. Descriptions des corrections](#-3-descriptions-des-corrections)
  - [3.1 Correction 1 – Renommage du champ `titre` → `name` dans `Support`](#31-correction-1--renommage-du-champ-titre--name-dans-support)
  - [3.2 Correction 2 – Renommage du champ `titre` → `name` dans `Utilisateur`](#32-correction-2--renommage-du-champ-titre--name-dans-utilisateur)
  - [3.3 Correction 3 – Redéfinition du champ `annee_edition` dans `Support`](#33-correction-3--redéfinition-du-champ-annee_edition-dans-support)
  - [3.4 Correction 4 – Ajout d’un choix `NON_DEFINI` à `media_type`](#34-correction-4--ajout-dun-choix-non_defini-à-media_type)
  - [3.5 Correction 5 – Validation des champs numériques métier](#35-correction-5--validation-des-champs-numériques-métier)
  - [3.6 Correction 6 – Centralisation du typage réel via `get_real_instance()`](#36-correction-6--centralisation-du-typage-réel-via-get_real_instance)
- [4. Suivi des tests après correction](#-4-suivi-des-tests-après-correction)

---

## 1. Introduction

### 1.1 Objectif du document

Ce document concerne les corrections à appliquer à la modélisation réalisée lors du développement de l'application Bibliothecaire.
Il est établi en plusieurs versions qui sont définies par une lettre d'index et un chiffre (**index** [**X**]-[**1**]).

Son objectif est de présenter les erreurs qui ont été identifiées lors des tests unitaires associés à différents éléments du codage (modèle, routage, vue, templates...) du projet.

### 1.2 – Positionnement du document dans le cycle de développement

Ce document intervient à la jonction entre la modélisation initiale et la validation par les tests unitaires. 
Il ne vise pas à redéfinir les modèles, mais à **documenter les ajustements nécessaires** pour que la modélisation soit conforme aux comportements attendus en test et en usage réel.

Il s’inscrit dans une logique de développement incrémental, où chaque série de tests permet de :

- **Révéler des incohérences** ou des oublis dans la modélisation
- **Proposer des corrections ciblées**, justifiées par des cas métier ou des erreurs techniques
- **Tracer les impacts sur les tests existants**, facilitant leur re-exécution ou leur adaptation

Ce document est donc un **outil de pilotage technique**, complémentaire à :

- [`tests-plan.md`](tests-plan.md), qui formalise les cas de test et leur état
- [`_Frontend-main-courante.md`](Modelisation_correction-erreurs-suite-tests-unitaires.md), qui consigne les difficultés rencontrées et les décisions prises

Chaque correction est présentée selon le triptyque :
**Justification – Action à mener – Tests impactés**

### 1.3 Historique des corrections et versions du développement

Les différentes versions, de l'index A à C, ont concerné le développement du code (Routage, Templates) de l'application Bibliothecaire.

Le présent document est créé dans sa première version, index D-1, lors du développement de la première série des tests unitaires.

La seconde version, index D-2, a conduit aux corrections du modèle C-MOD-01 à C-MOD-03 et qui ont été identifiées lors de la première validation d'ensemble des tests unitaires.

La troisième version, index D-3, a conduit à l'ajout des corrections C-MOD-04 à C-MOD-06. 
Ces ajouts ont été identifiés à partir de la première version stabilisée des tests unitaires du plan de tests. 
Les résultats de ces tests unitaires sont consignés dans le document [`test_report_indexD-3.txt`](test_report_indexD-3.txt) 

La quatrième version, index E-5, a conduit à la réalisation des corrections C-MOD-01, C-MOD-02, C-MOD-03 et C-MOD-05. 
Ces corrections ont conduit à l'ajout dans le **plan de tests** des tests du site d'administration (T-ADM-01 et T-ADM-02). 
Les résultats de ces tests unitaires sont consignés :
- Pour C-MOD-01 et C-MOD-02, dans le document [`test_report_indexE-3.txt`](test_report_indexE-3.txt) 
- Pour C-MOD-01, C-MOD-02 et C-MOD-03, dans le document [`test_report_indexE-4.txt`](test_report_indexE-4.txt) 
- Pour C-MOD-01, C-MOD-02, C-MOD-03 et C-MOD-05, dans le document [`test_report_indexE-5.txt`](test_report_indexE-5.txt) 

---

## 🔹 2. Synthèse des corrections à appliquer

| ID       | Correction identifiée                                   | Modèle concerné      | Type de correction     | Tests impactés à re-exécuter                                |
|----------|---------------------------------------------------------|----------------------|------------------------|-------------------------------------------------------------|
| C-MOD-01 | Renommer le champ `titre` en `name` dans `Support`      | `Support`            | Sémantique / cohérence | À définir dans les issues #2, #3 et #4                      |
| C-MOD-02 | Renommer le champ `nom` en `name` dans `Utilisateur`    | `Utilisateur`        | Sémantique / cohérence | À définir dans les issues #2, #3 et #4                      |
| C-MOD-03 | Redéfinir `annee_edition` dans `Media`                  | `Media`              | Validation / structure | `test_media_enregistrement`, `test_media_detail_accessible` |
| C-MOD-04 | Ajout d’un choix `NON_DEFINI` à `media_type`            | `Media`              | Sémantique / cohérence | `T-VUE-05`, `T-ENT-03`, `test_entites_media.py`             |
| C-MOD-05 | Validation des champs numériques métier                 | `Livre`, `Dvd`, `Cd` | validation / structure | `T-ENT-04`, `test_entites_media.py`, fixtures JSON          |
| C-MOD-06 | Centralisation du typage réel via `get_real_instance()` | `Media`              | Structure / cohérence  | `T-VUE-04`, `T-VUE-05`, `test_vues_media_detail.py`         |

---

## 🔧 3. Descriptions des corrections

### 3.1 Correction 1 – Renommage du champ `titre` → `name` dans `Support`

#### 🔸 Justification
- Le champ `titre` est ambigu pour un support technique ou physique.
- Le champ `name` est plus générique et cohérent avec les autres entités (`Membre`, `Jeu`, etc.).

#### 🔸 Action à réaliser
```python
# Avant
class Support(models.Model):
    titre = models.CharField(max_length=100)

# Après
class Support(models.Model):
    name = models.CharField(max_length=100)
```

#### 🔸 Tests impactés
- Tests T-NAV-03, T-ENT-xx, T-VUE-xx
- Prévoir des tests dans l’issue #4 ou lors de l’intégration des vues liées à `Support`

#### 🔸 Validation post correction
- Création des tests pour l'administration (T-ADM-01 et T-ADM-02) : `test_admin.py`
- Templates mis à jour : `media_list.html` et `media_detail.html`
- Tests corrigés : `test_urls.py`, `test_entites_mdeia.py`, `test_vues_media_list.py` et `test_vue_media_detail.py`
- Résultat : ✅ Tests passés avec succès (T-NAV-03 toujours en échec - attente correction 3) `test_report_indexE-4.txt`

---

### 3.2 Correction 2 – Renommage du champ `titre` → `name` dans `Utilisateur`

#### 🔸 Justification
- Le champ `nom` est cohérent.
- Le champ `name` est celui utilisé dans le sujet et cohérent avec les autres entités (`Support`, etc.).

#### 🔸 Action à réaliser
```python
# Avant
class Utilisateur(models.Model):
    titre = models.CharField(max_length=100)

# Après
class Utilisateur(models.Model):
    name = models.CharField(max_length=100)
```

#### 🔸 Tests impactés
- Tests T-NAV-03, T-ENT-xx, T-VUE-xx
- Prévoir des tests dans l’issue #4 ou lors de l’intégration des vues liées à `Support`

#### 🔸 Validation post correction
- Validation des tests pour l'administration (T-ADM-01 et T-ADM-02) : ✅ Tests passés avec succès
- Templates mis à jour : `media_list.html` et `media_detail.html`
- Tests corrigés : `test_urls.py`, `test_entites_mdeia.py`, `test_vues_media_list.py` et `test_vue_media_detail.py`
- Résultat : ✅ Tests passés avec succès (T-NAV-03 toujours en échec - attente correction 3) `test_report_indexE-3.txt`

---

### 3.3 Correction 3 – Redéfinition du champ `annee_edition` dans `Support`

#### 🔸 Problème détecté
- Le champ est requis à la création, ce qui bloque les tests si la valeur est absente.
- Aucun contrôle sur la cohérence temporelle (valeurs négatives ou futures possibles).

#### 🔸 Objectif
- Permettre une valeur vide (inconnue)
- Imposer une valeur positive si renseignée
- Limiter à l’année courante ou antérieure

#### 🔸 Proposition de champ
```python
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

annee_edition = models.PositiveIntegerField(
    null=True,
    blank=True,
    validators=[
        MinValueValidator(1000),
        MaxValueValidator(datetime.now().year)
    ],
    help_text="Année d’édition si connue. Sinon, laisser vide."
)
```

#### 🔸 Tests impactés
- `test_media_enregistrement` (dans `tests_blocs/test_accueil.py`)
- `test_media_detail_accessible` (dans `test_urls.py`) – actuellement KO
- Prévoir un test de validation explicite dans `test_entites_media.py`

#### 🔸 Synthèse des corrections retenues

- **Définition des contraintes dans `Support`**  
  Le champ `annee_edition` est une valeur vide ou positive garantissant une cohérence pour tous les types de support (médias ou jeux de plateau).

- **Reporter les contraintes métier dans le formulaire**  
  Le modèle doit être stable et les bornes de validité cohérentes dans le temps. Pour cela les contraintes évolutives liées au temps ne sont pas définies dans le modèle. 
  Cela se traduit par :
    - Suppression des validators et de la méthode `clean()` dans le modèle.
    - Ajout d’un `help_text` explicite : *"Année d’édition si connue. Sinon, laisser vide."*
    - Report du contrôle dynamique (borne supérieure = année courante) dans le formulaire associé.

- **Contenu des tests unitaires**  
  La validation étant déplacée dans les formulaires, les tests unitaires doivent prévoir un ciblage sur le contrôle de validité dans les `ModelForm` et non dans les modèles eux-mêmes

- **Adaptation du template de détail**  
  Le champ `annee_edition` est masqué dans le template si sa valeur est vide (`None`). 
  Cette décision évite l’affichage de données non renseignées et simplifie les tests de rendu.  
  Un filtre personnalisé (defaut_si_vide) a été envisagé pour afficher ‘non définie’ dans les templates, 
  mais n’a pas été retenu à ce stade pour limiter les impacts sur les tests. Cette option reste ouverte pour une correction ultérieure.

> Ce choix permet une validation claire, maintenable et cohérente. Elle laisse un modèle simple tout en garantissant une validation métier côté interface.

> Le template est associé à la logique de la donnée (masquage du champ si contenu vide) et des tests unitaires. Un filtre personnalisé reste à envisager pour rendre explicite le contenu des champs.

#### 🔸 Validation post correction
- Validation des tests pour l'administration (T-ADM-01 et T-ADM-02) : ✅ Tests passés avec succès
- Templates mis à jour : `media_detail.html` (masquage du champ **Année** si la valeur de `annee_edition` est vide)
- Tests corrigés : `test_entites_mdeia.py`, `test_vues_media_list.py` et `test_vue_media_detail.py`
- Résultat : ✅ Tests passés avec succès `test_report_indexE-4.txt`

---

### 3.4 Correction 4 – Ajout d’un choix `NON_DEFINI` à `media_type`

#### 🔸 Justification

Le champ `media_type` est requis, mais n’a pas de valeur par défaut. 
Cela empêche la création d’un objet `Media` non typé, ce qui est pourtant utile pour tester les cas limites ou initier des objets avant typage. 
De plus, la valeur seule ne garantit pas la présence d’un sous-type réel (`Livre`, `Dvd`, `Cd`), comme démontré dans `T-VUE-05`.

#### 🔸 Action à mener

Ajouter une valeur par défaut `'NON_DEFINI'` dans les choix du champ `media_type` :
```python
TYPE_CHOICES = [
    ('NON_DEFINI', 'Non défini'),
    ('LIVRE', 'Livre'),
    ('DVD', 'DVD'),
    ('CD', 'CD'),
]

media_type = models.CharField(
    max_length=10,
    choices=TYPE_CHOICES,
    default='NON_DEFINI',
    help_text="Type de média. 'NON_DEFINI' si aucun sous-type n’est instancié."
)
```

#### 🔸 Tests impactés

- `T-VUE-05` (vue de détail d’un Media non typé)  
- `T-ENT-03` (attributs accessibles selon typage)  
- `test_entites_media.py` (création de Media seul)

---

### 3.5 Correction 5 – Validation des champs numériques métier

#### 🔸 Justification
Les champs numériques `nb_page`, `duree`, `duree_ecoute` acceptent la valeur `0`, ce qui est incohérent avec leur sens métier. 
Un livre ne peut avoir 0 page, un DVD 0 minute, etc. 
Ces valeurs ont été utilisées dans les tests (lorsque la définition était impérative : _setUp_ d'un `@classmethod`), mais ne devraient pas être permises en production.

#### 🔸 Action à mener  

Ajouter un validateur `MinValueValidator(1)` sur chaque champ concerné :

```python
from django.core.validators import MinValueValidator

nb_page = models.PositiveIntegerField(
    validators=[MinValueValidator(1)],
    help_text="Nombre de pages (minimum 1)"
)

duree = models.PositiveIntegerField(
    validators=[MinValueValidator(1)],
    help_text="Durée du DVD en minutes (minimum 1)"
)

duree_ecoute = models.PositiveIntegerField(
    validators=[MinValueValidator(1)],
    help_text="Durée d’écoute du CD en minutes (minimum 1)"
)
```

#### 🔸 Tests impactés

- `T-ENT-04` (création d’un sous-type et vérification des champs)  
- `test_entites_media.py` (valeurs numériques dans les objets typés)  
- Fixtures `initial_data.json` à réviser

#### 🔸 Synthèse des corrections retenues

- **Ajout de `MinValueValidator(1)`** sur les champs numériques suivants :
  - `nb_page` dans `Livre`
  - `duree` dans `Dvd`
  - `duree_ecoute` dans `Cd`
  - `nb_piste` dans `Cd`, avec `default=1` pour garantir une valeur minimale même en création simplifiée

- **Respect de la logique métier** :
  - Un livre doit avoir au moins une page
  - Un CD doit contenir au moins une piste
  - Un DVD ou un CD doit avoir une durée d’écoute significative, sinon laissé vide

- **Template `media_detail.html` mis à jour** :
  - Affichage conditionnel des champs numériques avec unité (`minute(s)`)
  - Mention explicite `"non saisie"` si valeur absente
  - Ajout du champ `consultable` (oubli détecté lors des tests T-VUE-04abc)

- **Tests unitaires adaptés** :
  - Passage de `.create()` à `.full_clean()` + `.save()` pour déclencher les validators
  - Vérification du rendu HTML avec `assertContains()` et `assertNotContains()`
  - Calcul dynamique des valeurs affichées dans les tests (`Oui/Non`, `non saisie`, `X minute(s)`)

#### 🔸 Validation post correction

- **Modèle corrigé** dans `models.py_indexI-5` :
  - Tous les champs numériques métiers sont correctement validés
  - Le champ `nb_piste` est non nullable avec une valeur par défaut

- **Template corrigé** dans `media_detail.html_indexE-5` :
  - Ajout du champ `consultable`
  - Affichage conditionnel des champs numériques avec unité ou mention `"non saisie"`

- **Tests validés** :
  - `test_entites_media.py_indexE-5` : création et vérification des entités typées
  - `test_vues_media_detail.py_indexE-5` : vérification du rendu HTML pour chaque type (`Livre`, `Dvd`, `Cd`)
  - Tous les tests T-VUE-04abc passent avec succès, y compris les cas minimaux et enrichis

- **Résultat** : ✅ Correction C-MOD-05 validée et consolidée dans les modèles, templates et tests

---

### 3.6 Correction 6 – Centralisation du typage réel via `get_real_instance()`

#### 🔸 Justification

La logique de typage dynamique est actuellement dispersée dans les vues. Pour garantir une cohérence et faciliter les tests, il est préférable d’intégrer une méthode `get_real_instance()` directement dans le modèle `Media`. Cela permet d’accéder à l’objet typé (`Livre`, `Dvd`, `Cd`) à partir d’un `Media`, sans dépendre de la vue.

#### 🔸 Action à mener

Ajouter dans le modèle `Media` :

```python
def get_real_instance(self):
    if hasattr(self, 'livre'):
        return self.livre
    elif hasattr(self, 'dvd'):
        return self.dvd
    elif hasattr(self, 'cd'):
        return self.cd
    return self
 ```

#### 🔸 Tests impactés

- `T-VUE-04` (vérification du typage dans le contexte de la vue)  
- `T-VUE-05` (absence de typage malgré `media_type`)  
- `test_vues_media_detail.py` (accès aux champs spécifiques via `get_real_instance`)  
- `test_entites_media.py` (vérification du typage réel)

---

## 🧪 4. Suivi des tests après correction

Une fois les corrections appliquées :
- Réexécuter les tests impactés
- Documenter les résultats dans `test_report_index[X]-[0].txt`
- Mettre à jour le `tests-plan.md` pour refléter les changements de modèle

---
