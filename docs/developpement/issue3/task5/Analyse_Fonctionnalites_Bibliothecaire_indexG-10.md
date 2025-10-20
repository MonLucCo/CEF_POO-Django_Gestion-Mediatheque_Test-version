# 📘 Analyse des fonctionnalités – Bibliothécaire  

📁 `/docs/developpement/issue3/task5/Analyse_Fonctionnalites_indexG-10.md`  

📌 Version : index G-10 (issue #3 – étape 5)

---

## Sommaire

- [1. Objectif du document](#1-objectif-du-document)
- [2. Synthèse des fonctionnalités demandées](#2-synthèse-des-fonctionnalités-demandées)
- [3. Description des fonctionnalités](#3-description-des-fonctionnalités)
  - [3.1 Cas d’usage UC-LIST – Affichage de la liste des médias](#31-cas-dusage-uc-list--affichage-de-la-liste-des-médias)
  - [3.2 Cas d’usage UC-CREATE – Création d’un média](#32-cas-dusage-uc-create--création-dun-média)
  - [3.3. Cas d’usage (souhaitables) – Modification et suppression](#33-cas-dusage-souhaitables--modification-et-suppression-)
- [4. Liaison technique](#4-liaison-technique)

---

## 1. Objectif du document

Ce document formalise les cas d’usage fonctionnels liés au profil bibliothécaire, en cohérence avec les exigences du sujet et les choix techniques validés dans les documents :

- [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](Modelisation_correction-erreurs-suite-tests-unitaires.md)  
- [`tests-plan.md` (index G-10)](tests-plan_indexG-10.md)  
- [`Analyse_Fonctionnalites.md`](../../../fonctionnel/Analyse_Fonctionnalites.md)
- [`README-fonct.md`](../../../fonctionnel/README-fonct.md)

Il permet de :

- Définir les fonctionnalités minimales et souhaitables
- Identifier les vues, formulaires et templates à développer
- Structurer les tests fonctionnels à venir (`T-VUE-*`, `T-FORM-*`)
- Préparer l’intégration des contraintes métier et des filtres

---

## 2. Synthèse des fonctionnalités demandées

| Fonction                     | Statut         | Description                                               | Désignation | Avancement technique              | Tests associés         |
|------------------------------|----------------|-----------------------------------------------------------|-------------|-----------------------------------|------------------------|
| Afficher la liste des médias | ✅ Demandée     | Vue principale pour consultation du catalogue             | UC-LIST     | 🟢 Vue en place (`MediaListView`) | `T-VUE-01`, `T-VUE-02` |
| Ajouter un média             | ✅ Demandée     | Création d’un média typé ou non typé                      | UC-CREATE   | 🟢 Vue en place                   | `T-FUN-04`, `T-FUN-05` |
| Modifier un média            | 🔸 Souhaitable | Mise à jour des champs métier                             | UC-UPDATE   | 🟢 Vue en place                   | `T-FUN-10`             |
| Typer un média               | 🔸 Souhaitable | Transformation d’un média non typé en typé                | UC-TYPAGE   | 🟢 Vue en place                   | `T-FUN-08`             |
| Annuler un typage            | 🔸 Souhaitable | Rollback d’un typage en cours                             | UC-ROLLBACK | 🟢 Vue en place                   | `T-FUN-09`             |
| Supprimer / masquer un média | 🔸 Souhaitable | Retrait d’un média du catalogue sans suppression physique | UC-DELETE   | ⚪ Non commencé                    | —                      |

> 🔹 L’interface doit rester **basique**, sans mise en forme avancée : un designer Web prendra le relai.  
> 🔹 Les vues doivent être **fonctionnelles, testables et extensibles**.
> 
> Légende : 🟢 = implémenté ; 🟡 = en cours ; ⚪ = non commencé

---

## 3. Description des fonctionnalités

### 3.1 Cas d’usage UC-LIST – Affichage de la liste des médias

#### 🎯 Objectif métier  
Permettre au bibliothécaire de consulter les médias du catalogue selon des critères utiles à la gestion.

#### 🧩 Cas d’usage

| ID         | Description métier                            | Filtrage appliqué                                         | Avancement   |
|------------|-----------------------------------------------|-----------------------------------------------------------|--------------|
| UC-LIST-01 | Afficher tous les médias consultables         | `Media.objects.filter(consultable=True)`                  | ✅ Implémenté |
| UC-LIST-02 | Afficher tous les médias disponibles          | `Media.objects.filter(consultable=True, disponible=True)` | ✅ Implémenté |
| UC-LIST-03 | Afficher les médias par type (Livre, Dvd, Cd) | `Media.objects.filter(media_type='LIVRE')` (ou autre)     | ✅ Implémenté |
| UC-LIST-04 | Afficher les médias non typés (`NON_DEFINI`)  | `Media.objects.filter(media_type='NON_DEFINI')`           | ✅ Implémenté |                                               |                                                           |              |

> 🔹 La structuration des routes associées à ces cas d’usage a soulevé une difficulté métier importante, documentée dans la 
> [Difficulté 10 – Organisation du routage lié aux médias](_Frontend-main-courante_indexG-10.md#910-difficulté-10--organisation-et-clarté-du-routage-lié-aux-médias).  
> 🔹 Chaque UC dispose d’une route dédiée, d’une vue spécifique et d’un bloc de test fonctionnel (`T-FUN-*`).

#### 🧠 Analyse technique associée

- La mise en œuvre des UC-LIST-01 à UC-LIST-03 a nécessité de traiter deux difficultés majeures :
  - [Difficulté 9](_Frontend-main-courante_indexG-10.md#99-difficulté-9--interactions-entre-les-tests-unitaires-techniques-et-fonctionnels-métier) : distinction entre tests techniques et fonctionnels
  - [Difficulté 10](_Frontend-main-courante_indexG-10.md#910-difficulté-10--organisation-et-clarté-du-routage-lié-aux-médias) : clarification du routage des vues liées à `Media`

- La création d’un média non typé (`UC-CREATE-01`) implique la possibilité de le consulter.  
  Une nouvelle UC a donc été ajoutée pour le profil **Bibliothécaire uniquement** :

| ID         | Description métier                           | Filtrage appliqué                               |
|------------|----------------------------------------------|-------------------------------------------------|
| UC-LIST-04 | Afficher les médias non typés (`NON_DEFINI`) | `Media.objects.filter(media_type='NON_DEFINI')` |

> 🔹 Cette UC est exclue de l’application Membre.  
> 🔹 Elle permet au bibliothécaire de retrouver les médias en attente de typage ou de complétion.

#### 🔧 Impacts techniques

- Vue : `MediaListView` avec surcharge de `get_queryset()`  
- Template : `media_list.html` avec blocs conditionnels  
- Tests : `T-VUE-01`, `T-VUE-02`, `T-VUE-06` à prévoir

---

### 3.2 Cas d’usage UC-CREATE – Création d’un média

#### 🎯 Objectif métier  
Permettre au bibliothécaire d’ajouter un nouveau média au catalogue, avec ou sans typage immédiat.

#### 🧩 Cas d’usage

| ID           | Description métier                                    | Formulaire utilisé | Avancement              |
|--------------|-------------------------------------------------------|--------------------|-------------------------|
| UC-CREATE-01 | Ajouter un média non typé (`media_type='NON_DEFINI'`) | `MediaForm`        | ✅ Formulaire implémenté |
| UC-CREATE-02 | Ajouter un Livre                                      | `LivreForm`        | ✅ Formulaire implémenté |
| UC-CREATE-03 | Ajouter un Dvd                                        | `DvdForm`          | ✅ Formulaire implémenté |
| UC-CREATE-04 | Ajouter un Cd                                         | `CdForm`           | ✅ Formulaire implémenté |

> 🔸 Les vues `CreateView` typées ne sont pas encore développées.  
> 🔸 Les formulaires spécifiques sont à créer et à valider via `full_clean()`.  
> 📌 Aucun test `T-FORM-*` encore défini.

#### 🧠 Analyse technique associée

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
  - [Difficulté 11](_Frontend-main-courante_indexG-10.md#911-difficulté-11--visualisation-des-contraintes-du-formulaire) : 
    visualisation des contraintes dans le formulaire (fonctionnalités vs Design UX/UI).


#### 🔧 Impacts techniques

- Vues : `MediaCreateView`, `LivreCreateView`, etc.  
- Templates : `media_form.html` + templates typés si besoin  
- Tests : `T-VUE-06`, `T-FORM-01`, `T-FORM-02` à prévoir

---

### 3.3. Cas d’usage (souhaitables) – Modification et suppression 

| ID          | Description métier                           | Statut         | Vue cible         | Avancement     |
|-------------|----------------------------------------------|----------------|-------------------|----------------|
| UC-UPDATE-* | Modifier un média typé ou non typé           | 🔸 Souhaitable | `MediaUpdateView` | ✅ Implémenté   |
| UC-DELETE-* | Masquer un média (sans suppression physique) | 🔸 Souhaitable | `MediaDeleteView` | ❌ Non commencé |

> Ces cas d’usage _souhaitable_ ont pour vocation de compléter les cas d'usage de _création d'un média_ pour une 
> expérience utilisateur (UX) cohérente.

#### 3.3.1 Cas d’usage UC-UPDATE et UC-TYPAGE – Mise à jour et transformation d’un média

##### 🎯 Objectif métier  
Permettre au bibliothécaire de modifier un média existant, qu’il soit typé ou non, et de transformer un média non typé en un sous-type réel (`Livre`, `Dvd`, `Cd`).  
La logique métier impose une distinction entre mise à jour classique, typage différé et annulation de typage.

##### 🧩 Cas d’usage

| ID           | Description métier                                     | Vue utilisée            | Formulaire utilisé | Avancement     |
|--------------|--------------------------------------------------------|-------------------------|--------------------|----------------|
| UC-UPDATE-01 | Modifier un média typé (`Livre`, `Dvd`, `Cd`)          | `LivreUpdateView`, etc. | `LivreForm`, etc.  | ✅ Vue en place |
| UC-UPDATE-02 | Modifier un média non typé (`media_type='NON_DEFINI'`) | `MediaUpdateView`       | `MediaForm`        | ✅ Vue en place |
| UC-TYPAGE-01 | Typer un média en `Livre`                              | `MediaTypageLivreView`  | `LivreForm`        | ✅ Vue en place |
| UC-TYPAGE-02 | Typer un média en `Dvd`                                | `MediaTypageDvdView`    | `DvdForm`          | ✅ Vue en place |
| UC-TYPAGE-03 | Typer un média en `Cd`                                 | `MediaTypageCdView`     | `CdForm`           | ✅ Vue en place |
| UC-TYPAGE-04 | Annuler un typage en cours                             | `MediaCancelTypingView` | —                  | ✅ Vue en place |

> 🔹 Le typage est déclenché automatiquement depuis `MediaUpdateView` si le champ `media_type` est modifié.  
> 🔹 L’annulation du typage supprime le sous-type et réinitialise le champ `media_type` à `'NON_DEFINI'`.

#### 🧠 Analyse technique associée

- Le typage est réalisé via une méthode `mutate_to_typed()` dans le modèle `Media`, garantissant une création atomique du sous-type.
- Les champs spécifiques sont appliqués dynamiquement via `get_specific_fields()` dans chaque sous-type (`Livre`, `Dvd`, `Cd`).
- Le routage est explicite pour chaque cas :
  - `/ajouter/<type>` → création typée
  - `/modifier/` → mise à jour non typée
  - `/<type>/modifier/` → mise à jour typée
  - `/modifier/<type>` → typage
  - `/annuler_typage/` → rollback

> 🔹 Cette segmentation permet une traçabilité claire, une maintenance facilitée et une UX cohérente.


#### 3.3.2 Cas d’usage UC-DELETE – Masquer un média (sans suppression physique)

Cette fonctionnalité sera développée ultérieurement, car elle nécessite de prendre en considération la situation 
d'emprunt pour effectuer la modification du média.

Cette UC sera intégrée dans une future étape, en cohérence avec les transitions métier définies dans 
[Analyse_LifeCycle_Medias.md](Analyse_LifeCycle_Medias_indexG-10.md).

---

## 4. Liaison technique

| Élément            | Source technique                                                                                                           |
|--------------------|----------------------------------------------------------------------------------------------------------------------------|
| Modèle             | `Media`, `Livre`, `Dvd`, `Cd`                                                                                              |
| Vue                | `MediaListView`, `MediaDetailView`, `MediaCreateView`, `MediaUpdateView`, `MediaTypage<Type>View`, `MediaCancelTypingView` |
| Template           | `media_list.html`, `media_detail.html`, `media_form.html`                                                                  |
| Formulaire         | `MediaForm`, `LivreForm`, `DvdForm`, `CdForm`                                                                              |
| Tests techniques   | `test_vues_media_list.py`, `test_vues_media_detail.py`, `test_entites_media.py`                                            |
| Tests fonctionnels | `test_uc_list_media.py`, `test_uc_create_media.py`, `test_uc_typage_media.py`                                              |

---
