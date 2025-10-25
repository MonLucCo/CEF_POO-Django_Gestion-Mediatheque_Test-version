# 📘 Analyse des fonctionnalités – Bibliothécaire

📁 `/docs/developpement/issue3/task5/Analyse_Fonctionnalites_indexH-4.md`  
📌 Version : index H-5 (issue #3 – Bloc 3 - étape 6)

---

## Sommaire

- [1. Objectif du document](#1-objectif-du-document)
- [2. Synthèse des fonctions demandées](#2-synthèse-des-fonctions-demandées)
- [3. Description des fonctionnalités](#3-description-des-fonctionnalités)
  - [3.1 Médias – Fonctionnalités associées directement](#31-médias--fonctionnalités-associées-directement)
    - [3.1.1 Fonctionnalités primordiales – Cas d’usage MEDIA-UC-LIST et MEDIA-UC-CREATE](#311-fonctionnalités-primordiales--cas-dusage-media-uc-list-et-media-uc-create)
      - [3.1.1.1 Cas d’usage MEDIA-UC-LIST – Affichage de la liste des médias](#3111-cas-dusage-media-uc-list--affichage-de-la-liste-des-médias)
      - [3.1.1.2 Cas d’usage MEDIA-UC-CREATE – Création d’un média](#3112-cas-dusage-uc-create--création-dun-média)
    - [3.1.2 Fonctionnalités souhaitables – Cas d’usage MEDIA-UC-UPDATE et MEDIA-UC-TYPAGE](#312-fonctionnalités-souhaitables--cas-dusage-media-uc-update-et-media-uc-typage)
      - [3.1.2.1 Cas d’usage MEDIA-UC-UPDATE et MEDIA-UC-TYPAGE – Mise à jour et transformation](#3121-cas-dusage-media-uc-update-et-media-uc-typage--mise-à-jour-et-transformation)
      - [3.1.2.2 Cas d’usage MEDIA-UC-DELETE – Masquer un média](#3122-cas-dusage-uc-delete--masquer-un-média-sans-suppression-physique)
  - [3.2 Membres – Fonctionnalités associées directement](#32-membres--fonctionnalités-associées-directement)
    - [3.2.1 Fonctionnalités primordiales – Cas d’usage MEMBRE-UC-LIST, MEMBRE-UC-CREATE, MEMBRE-UC-UPDATE et MEMBRE-UC-DELETE](#321-fonctionnalités-primordiales--cas-dusage-membre-uc-list-membre-uc-create-membre-uc-update-et-membre-uc-delete)
    - [3.2.2 Fonctionnalités souhaitables – Cas d’usage MEMBRE-UC-HISTORIQUE et MEMBRE-UC-ARCHIVE](#322-fonctionnalités-souhaitables--cas-dusage-membre-uc-historique-et-membre-uc-archive)
  - [3.3 Emprunts – Fonctionnalités associées directement](#33-emprunts--fonctionnalités-associées-directement)
    - [3.3.1 Fonctionnalités primordiales – Cas d’usage EMPRUNT-UC-CREATE, EMPRUNT-UC-RETOUR et EMPRUNT-UC-RETARD](#331-fonctionnalités-primordiales--cas-dusage-emprunt-uc-create-emprunt-uc-retour-et-emprunt-uc-retard)
    - [3.3.2 Fonctionnalités souhaitables – Cas d’usage EMPRUNT-UC-ARCHIVE](#332-fonctionnalités-souhaitables--cas-dusage-emprunt-uc-archive)
- [4. Liaison technique](#4-liaison-technique)
  - [4.1 Application Bibliothecaire](#41-application-bibliothecaire)
    - [4.1.1 Medias](#411-medias)
    - [4.1.2 Membres](#412-membres)
    - [4.1.3 Emprunts](#413-emprunts)
    - [4.1.4 Jeux](#414-jeux)
  - [4.2 Application Consultation](#42-application-consultation)
  - [4.3 Application Mediatheque](#43-application-mediatheque)
  - [4.4 Application Administration](#44-application-administration)
- [5. Liens documentaires](#5-liens-documentaires)

---

## 1. Objectif du document

Ce document formalise les cas d’usage fonctionnels liés au profil bibliothécaire, en cohérence avec les exigences du 
sujet et les choix techniques validés dans les documents :

- [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](../task5/Modelisation_correction-erreurs-suite-tests-unitaires.md)  
- [`tests-plan.md`](tests-plan.md)  
- [`Analyse_Fonctionnalites.md`](../../../fonctionnel/Analyse_Fonctionnalites.md)  
- [`README-fonct.md`](../../../fonctionnel/README-fonct.md)

Il permet de :
- Définir les fonctionnalités minimales et souhaitables
- Identifier les vues, formulaires et templates à développer
- Structurer les tests fonctionnels à venir (`T-VUE-*`, `T-FORM-*`)
- Préparer l’intégration des contraintes métier et des filtres

---

## 2. Synthèse des fonctions demandées

| Entité  | UC                   | Description métier                   | Statut         | Avancement technique |
|---------|----------------------|--------------------------------------|----------------|----------------------|
| Media   | MEDIA-UC-LIST        | Affichage filtré des médias          | ✅ Demandée     | 🟢 Implémenté        |
| Media   | MEDIA-UC-CREATE      | Création d’un média typé ou non typé | ✅ Demandée     | 🟢 Implémenté        |
| Media   | MEDIA-UC-UPDATE      | Modification d’un média              | 🔸 Souhaitable | 🟢 Implémenté        |
| Media   | MEDIA-UC-TYPAGE      | Transformation en sous-type          | 🔸 Souhaitable | 🟢 Implémenté        |
| Media   | MEDIA-UC-ROLLBACK    | Rollback d'un typage en cours        | 🔸 Souhaitable | 🟢 Implémenté        |
| Media   | MEDIA-UC-DELETE      | Suppression logique d'un média       | 🔸 Souhaitable | ⚪ À définir          |
| Membre  | MEMBRE-UC-LIST       | Affichage de la liste des membres    | ✅ Demandée     | ⚪ À développer       |
| Membre  | MEMBRE-UC-CREATE     | Création d’un membre                 | ✅ Demandée     | ⚪ À développer       |
| Membre  | MEMBRE-UC-UPDATE     | Mise à jour d’un membre              | ✅ Demandée     | ⚪ À développer       |
| Membre  | MEMBRE-UC-DELETE     | Suppression logique d’un membre      | ✅ Demandée     | ⚪ À développer       |
| Membre  | MEMBRE-UC-HISTORIQUE | Consultation des emprunts passés     | 🔸 Souhaitable | ⚪ À définir          |
| Membre  | MEMBRE-UC-ARCHIVE    | Archivage d’un membre                | 🔸 Souhaitable | ⚪ À définir          |
| Emprunt | EMPRUNT-UC-CREATE    | Création d’un emprunt                | ✅ Demandée     | ⚪ À développer       |
| Emprunt | EMPRUNT-UC-RETOUR    | Enregistrement du retour             | ✅ Demandée     | ⚪ À développer       |
| Emprunt | EMPRUNT-UC-RETARD    | Détection et marquage du retard      | ✅ Demandée     | ⚪ À développer       |
| Emprunt | EMPRUNT-UC-ARCHIVE   | Archivage d’un emprunt               | 🔸 Souhaitable | ⚪ À définir          |

> 🔹 L’interface doit rester **basique**, sans mise en forme avancée : un designer Web prendra le relai.  
> 🔹 Les vues doivent être **fonctionnelles, testables et extensibles**.
> 
> Légende : 🟢 = implémenté ; 🟡 = en cours ; ⚪ = non commencé

---

## 3. Description des fonctionnalités

### 3.1 Médias – Fonctionnalités associées directement

#### 3.1.1 Fonctionnalités primordiales – Cas d’usage MEDIA-UC-LIST et MEDIA-UC-CREATE

- Reprise intégrale des sections 3.1 et 3.2 de la version G-10 :
  - UC-LIST-01 à UC-LIST-04 → renommés MEDIA-UC-LIST-01 à 04
  - UC-CREATE-01 à UC-CREATE-04 → renommés MEDIA-UC-CREATE-01 à 04

##### 3.1.1.1 Cas d’usage MEDIA-UC-LIST – Affichage de la liste des médias

###### 🎯 Objectif métier  
Permettre au bibliothécaire de consulter les médias du catalogue selon des critères utiles à la gestion.

###### 🧩 Cas d’usage

| ID (MEDIA-*) | Description métier                            | Filtrage appliqué                                         | Avancement   |
|--------------|-----------------------------------------------|-----------------------------------------------------------|--------------|
| UC-LIST-01   | Afficher tous les médias consultables         | `Media.objects.filter(consultable=True)`                  | ✅ Implémenté |
| UC-LIST-02   | Afficher tous les médias disponibles          | `Media.objects.filter(consultable=True, disponible=True)` | ✅ Implémenté |
| UC-LIST-03   | Afficher les médias par type (Livre, Dvd, Cd) | `Media.objects.filter(media_type='LIVRE')` (ou autre)     | ✅ Implémenté |
| UC-LIST-04   | Afficher les médias non typés (`NON_DEFINI`)  | `Media.objects.filter(media_type='NON_DEFINI')`           | ✅ Implémenté |                                               |                                                           |              |

> 🔹 La structuration des routes associées à ces cas d’usage a soulevé une difficulté métier importante, documentée dans la 
> [Difficulté 10 – Organisation du routage lié aux médias](_Frontend-main-courante.md#910-difficulté-10--organisation-et-clarté-du-routage-lié-aux-médias).  
> 🔹 Chaque UC dispose d’une route dédiée, d’une vue spécifique et d’un bloc de test fonctionnel (`T-FUN-*`).

###### 🧠 Analyse technique associée

- La mise en œuvre des UC-LIST-01 à UC-LIST-03 a nécessité de traiter deux difficultés majeures :
  - [Difficulté 9](_Frontend-main-courante.md#99-difficulté-9--interactions-entre-les-tests-unitaires-techniques-et-fonctionnels-métier) : distinction entre tests techniques et fonctionnels
  - [Difficulté 10](_Frontend-main-courante.md#910-difficulté-10--organisation-et-clarté-du-routage-lié-aux-médias) : clarification du routage des vues liées à `Media`

- La création d’un média non typé (`UC-CREATE-01`) implique la possibilité de le consulter.  
  Une nouvelle UC a donc été ajoutée pour le profil **Bibliothécaire uniquement** :

| ID         | Description métier                           | Filtrage appliqué                               |
|------------|----------------------------------------------|-------------------------------------------------|
| UC-LIST-04 | Afficher les médias non typés (`NON_DEFINI`) | `Media.objects.filter(media_type='NON_DEFINI')` |

> 🔹 Cette UC est exclue de l’application Membre.  
> 🔹 Elle permet au bibliothécaire de retrouver les médias en attente de typage ou de complétion.

###### 🔧 Impacts techniques

- Vue : `MediaListView` avec surcharge de `get_queryset()`  
- Template : `media_list.html` avec blocs conditionnels  
- Tests : `T-VUE-01`, `T-VUE-02`, `T-VUE-06`

---

##### 3.1.1.2 Cas d’usage UC-CREATE – Création d’un média

###### 🎯 Objectif métier  
Permettre au bibliothécaire d’ajouter un nouveau média au catalogue, avec ou sans typage immédiat.

###### 🧩 Cas d’usage

| ID (MEDIA-*) | Description métier                                    | Formulaire utilisé | Avancement              |
|--------------|-------------------------------------------------------|--------------------|-------------------------|
| UC-CREATE-01 | Ajouter un média non typé (`media_type='NON_DEFINI'`) | `MediaForm`        | ✅ Formulaire implémenté |
| UC-CREATE-02 | Ajouter un Livre                                      | `LivreForm`        | ✅ Formulaire implémenté |
| UC-CREATE-03 | Ajouter un Dvd                                        | `DvdForm`          | ✅ Formulaire implémenté |
| UC-CREATE-04 | Ajouter un Cd                                         | `CdForm`           | ✅ Formulaire implémenté |

> 🔸 Les vues `CreateView` typées ne sont pas encore développées.  
> 🔸 Les formulaires spécifiques sont à créer et à valider via `full_clean()`.  
> 📌 Aucun test `T-FORM-*` encore défini.

###### 🧠 Analyse technique associée

- Le modèle `Media` repose sur une **structure en héritage multi-table**, imposée par l’ORM Django.  
  Chaque entité typée (`Livre`, `Dvd`, `Cd`) est liée à une instance `Media` via une clé primaire identique (`pk`).

- Cette organisation impose une **création en deux temps** :
  1. Création de l’objet `Media` (UC-CREATE-01)
  2. Création de l’objet typé (`Livre`, `Dvd`, `Cd`) selon `media_type` (UC-CREATE-02 à UC-CREATE-04)

> 🔹 Cette segmentation est **techniquement impérative**, non considérée comme une difficulté.  
> 🔹 Elle est conforme aux pratiques des ORM modernes pour gérer l’héritage.

- Particularité métier du champ `consultable` :
  - Un média **non typé** est **non consultable** par défaut.
  - Un média **typé** est selon les besoins métier :
    - en situation d'**attente** : **disponible par défaut** et **non consultable par défaut**
    - en situation **empruntable** : **disponible par défaut** et **consultable par saisie**


> 🔹 Cette logique permet de distinguer les médias en attente (non typés) des médias prêts à être empruntés ou consultés.

- La mise en œuvre des UC-CREATE a nécessité de traiter une difficulté majeure liée au formulaire :
  - [Difficulté 11](_Frontend-main-courante.md#911-difficulté-11--visualisation-des-contraintes-du-formulaire) : 
    visualisation des contraintes dans le formulaire (fonctionnalités vs Design UX/UI).

###### 🔧 Impacts techniques

- Vues : `MediaCreateView`, `LivreCreateView`, etc.  
- Templates : `media_form.html` + templates typés si besoin  
- Tests : `T-VUE-06`, `T-FORM-01`, `T-FORM-02` à prévoir

---

#### 3.1.2 Fonctionnalités souhaitables – Cas d’usage MEDIA-UC-UPDATE et MEDIA-UC-TYPAGE

- Reprise intégrale de la section 3.3.1 de la version G-10 :
  - UC-UPDATE-01 à 02 → renommés MEDIA-UC-UPDATE-01 à 02
  - UC-TYPAGE-01 à 04 → renommés MEDIA-UC-TYPAGE-01 à 04

| ID (MEDIA-*) | Description métier                           | Statut         | Vue cible         | Avancement     |
|--------------|----------------------------------------------|----------------|-------------------|----------------|
| UC-UPDATE-*  | Modifier un média typé ou non typé           | 🔸 Souhaitable | `MediaUpdateView` | ✅ Implémenté   |
| UC-DELETE-*  | Masquer un média (sans suppression physique) | 🔸 Souhaitable | `MediaDeleteView` | ❌ Non commencé |

> Ces cas d’usage _souhaitable_ ont pour vocation de compléter les cas d'usage de _création d'un média_ pour une 
> expérience utilisateur (UX) cohérente.

##### 3.1.2.1 Cas d’usage UC-UPDATE et UC-TYPAGE – Mise à jour et transformation d’un média

###### 🎯 Objectif métier :

Permettre au bibliothécaire de modifier un média existant, qu’il soit typé ou non, et de transformer un média non typé en un sous-type réel (`Livre`, `Dvd`, `Cd`).  
La logique métier impose une distinction entre mise à jour classique, typage différé et annulation de typage.

###### 🧩 Cas d’usage
    
| ID (MEDIA-*) | Description métier                                     | Vue utilisée            | Formulaire utilisé | Avancement     |
|--------------|--------------------------------------------------------|-------------------------|--------------------|----------------|
| UC-UPDATE-01 | Modifier un média typé (`Livre`, `Dvd`, `Cd`)          | `LivreUpdateView`, etc. | `LivreForm`, etc.  | ✅ Vue en place |
| UC-UPDATE-02 | Modifier un média non typé (`media_type='NON_DEFINI'`) | `MediaUpdateView`       | `MediaForm`        | ✅ Vue en place |
| UC-TYPAGE-01 | Typer un média en `Livre`                              | `MediaTypageLivreView`  | `LivreForm`        | ✅ Vue en place |
| UC-TYPAGE-02 | Typer un média en `Dvd`                                | `MediaTypageDvdView`    | `DvdForm`          | ✅ Vue en place |
| UC-TYPAGE-03 | Typer un média en `Cd`                                 | `MediaTypageCdView`     | `CdForm`           | ✅ Vue en place |
| UC-TYPAGE-04 | Annuler un typage en cours                             | `MediaCancelTypingView` | —                  | ✅ Vue en place |

> 🔹 Le typage est déclenché automatiquement depuis `MediaUpdateView` si le champ `media_type` est modifié.  
> 🔹 L’annulation du typage supprime le sous-type et réinitialise le champ `media_type` à `'NON_DEFINI'`.

###### 🧠 Analyse technique associée

- Le typage est réalisé via une méthode `mutate_to_typed()` dans le modèle `Media`, garantissant une création atomique du sous-type.
- Les champs spécifiques sont appliqués dynamiquement via `get_specific_fields()` dans chaque sous-type (`Livre`, `Dvd`, `Cd`).
- Le routage est explicite pour chaque cas :
  - `/ajouter/<type>` → création typée
  - `/modifier/` → mise à jour non typée
  - `/<type>/modifier/` → mise à jour typée
  - `/modifier/<type>` → typage
  - `/annuler_typage/` → rollback

    > 🔹 Cette segmentation permet une traçabilité claire, une maintenance facilitée et une UX cohérente.

##### 3.1.2.2 Cas d’usage UC-DELETE – Masquer un média (sans suppression physique)

Cette fonctionnalité sera développée ultérieurement, car elle nécessite de prendre en considération la situation 
d'emprunt pour effectuer la modification du média.

Cette UC sera intégrée dans une future étape, en cohérence avec les transitions métier définies dans 
[Analyse_LifeCycle_Medias.md](Analyse_LifeCycle_Medias.md).

---

### 3.2 Membres – Fonctionnalités associées directement

#### 3.2.1 Fonctionnalités primordiales – Cas d’usage MEMBRE-UC-LIST, MEMBRE-UC-CREATE, MEMBRE-UC-UPDATE et MEMBRE-UC-DELETE

- À rédiger dans la version H-5 à partir des vues `MembreListView`, `MembreCreateView`, etc.
- Structure attendue :
  - MEMBRE-UC-LIST : affichage filtré par statut
  - MEMBRE-UC-CREATE : initialisation du statut
  - MEMBRE-UC-UPDATE : modification du nom, compte, statut
  - MEMBRE-UC-DELETE : suppression logique (statut = ARCHIVE)

##### 3.2.1.1 Cas d’usage MEMBRE-UC-LIST – Affichage de la liste des membres

###### 🎯 Objectif métier  
Permettre au bibliothécaire de consulter les membres de la médiathèque selon des critères utiles à la gestion :
- en gestion : les membres abonnés et non-abonnés, soit les membres qui ne sont pas archivés (hors gestion).
- abonné : les membres qui peuvent emprunter.
- hors gestion : les membres supprimés (logiquement, car pas de suppression physique pour permettre une historisation 
des emprunts). 

###### 🧩 Cas d’usage

| ID (MEMBRE-*) | Description métier                   | Filtrage appliqué                          | Avancement     |
|---------------|--------------------------------------|--------------------------------------------|----------------|
| UC-LIST-01    | Afficher tous les membres de la base | `Membre.objects.all()`                     | ✅ Implémenté |
| UC-LIST-02    | Afficher tous les membres en gestion | `Membre.objects.exclude(statut=ARCHIVE)`   | ✅ Implémenté |
| UC-LIST-03    | Afficher tous les membres abonnés    | `Membre.objects.filter(statut=EMPRUNTEUR)` | ✅ Implémenté |
| UC-LIST-04    | Afficher tous les membres supprimés  | `Membre.objects.filter(statut=ARCHIVE)`    | ✅ Implémenté |

> Avancement : ⚪ À développer ou ✅ Implémenté

###### 🧠 Analyse technique associée

- chaque fonction est identifiée avec une route unique

###### 🔧 Impacts techniques

- Vue : `MembreListView` avec surcharge de `get_queryset()`  
- Template : `media_list.html` avec blocs conditionnels  
- Tests : `T-NAV-xx`, `T-ENT-xx`, `T-VUE-xx`, `T-FUN-xx` définis dans `test_uc_list_membre.py`.

---

#### 3.2.2 Fonctionnalités souhaitables – Cas d’usage MEMBRE-UC-HISTORIQUE et MEMBRE-UC-ARCHIVE

- À définir dans une version ultérieure
- Historique = vue des emprunts passés
- Archivage = transition métier complète (statut, désactivation)

---

### 3.3 Emprunts – Fonctionnalités associées directement

#### 3.3.1 Fonctionnalités primordiales – Cas d’usage EMPRUNT-UC-CREATE, EMPRUNT-UC-RETOUR et EMPRUNT-UC-RETARD

- À rédiger dans la version H-5
- Structure attendue :
  - EMPRUNT-UC-CREATE : création avec vérification `peut_emprunter()`
  - EMPRUNT-UC-RETOUR : mise à jour du statut et du média
  - EMPRUNT-UC-RETARD : marquage automatique (DDM ou tâche planifiée)

#### 3.3.2 Fonctionnalités souhaitables – Cas d’usage EMPRUNT-UC-ARCHIVE

- Archivage métier : passage à `statut = RENDU`, désactivation du lien

---

---

## 4. Liaison technique

### 4.1 Application Bibliothecaire

#### 4.1.1 Medias

| Élément            | Source technique                                                                                                           |
|--------------------|----------------------------------------------------------------------------------------------------------------------------|
| Modèle             | `Media`, `Livre`, `Dvd`, `Cd`                                                                                              |
| Vue                | `MediaListView`, `MediaDetailView`, `MediaCreateView`, `MediaUpdateView`, `MediaTypage<Type>View`, `MediaCancelTypingView` |
| Template           | `media_list.html`, `media_detail.html`, `media_form.html`                                                                  |
| Formulaire         | `MediaForm`, `LivreForm`, `DvdForm`, `CdForm`                                                                              |
| Tests techniques   | `test_vues_media_list.py`, `test_vues_media_detail.py`, `test_entites_media.py`                                            |
| Tests fonctionnels | `test_uc_list_media.py`, `test_uc_create_media.py`, `test_uc_typage_media.py`                                              |

#### 4.1.2 Membres

| Élément            | Source technique                                                                                               |
|--------------------|----------------------------------------------------------------------------------------------------------------|
| Modèle             | `Membre`                                                                                                       |
| Vue                | `MembreListView`, `MembreDetailView`, `MembreCreateView`, `MembreUpdateView`, `MembreSupprimeView`             |
| Template           | `membre_list.html`, `membre_detail.html`, `membre_form.html`                                                   |
| Formulaire         | `MembreForm`                                                                                                   |
| Tests techniques   | `test_vues_membre_list.py`, `test_vues_membre_detail.py`, `test_entites_membre.py`                             |
| Tests fonctionnels | `test_uc_list_membre.py`, `test_uc_create_membre.py`, `test_uc_update_membre.py`, `test_uc_supprime_membre.py` |

#### 4.1.3 Emprunts

Cette section sera complétée lors du développement applicatif prévu dans l'`issue #3`.

#### 4.1.4 Jeux

Cette section sera complétée lors du développement applicatif prévu dans l'`issue #3`.

### 4.2 Application Consultation

Cette section sera complétée lors du développement applicatif prévu dans l'`issue #4`.

### 4.3 Application Mediatheque

Cette section sera complétée lors du développement applicatif prévu dans l'`issue #5`.

### 4.4 Application Administration

Cette section sera complétée lors du développement applicatif prévu dans l'`issue #3`, l'`issue #4` et l'`issue #5`.

---

## 5. Liens documentaires

- [`Analyse_LifeCycle_Bibliothecaire.md`](Analyse_LifeCycle_Bibliothecaire.md)
- [`Analyse_LifeCycle_Membres.md`](Analyse_LifeCycle_Membres.md)
- [`Analyse_LifeCycle_Emprunts.md`](Analyse_LifeCycle_Emprunts.md)
- [`Analyse_LifeCycle_Medias.md`](Analyse_LifeCycle_Medias.md)
- [`tests-plan.md`](tests-plan.md)
