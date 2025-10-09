# 📘 Analyse des fonctionnalités – Bibliothécaire  

📁 `/docs/developpement/issue3/task5/Analyse_Fonctionnalites.md`  

📌 Version : index F-3 (issue #3 – étape 5)

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
- [`tests-plan.md`](tests-plan.md)  
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
| Ajouter un média             | ✅ Demandée     | Création d’un média typé ou non typé                      | UC-CREATE   | 🟡 Formulaires à créer            | `T-VUE-06` (à définir) |
| Modifier un média            | 🔸 Souhaitable | Mise à jour des champs métier                             | UC-UPDATE   | 	⚪ Non commencé                   | —                      |
| Supprimer / masquer un média | 🔸 Souhaitable | Retrait d’un média du catalogue sans suppression physique | UC-DELETE   | 	⚪ Non commencé                   | —                      |

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
> [Difficulté 10 – Organisation du routage lié aux médias](../../../developpement/issue3/_Frontend-main-courante.md#910-difficulté-10--organisation-et-clarté-du-routage-lié-aux-médias).  
> 🔹 Chaque UC dispose d’une route dédiée, d’une vue spécifique et d’un bloc de test fonctionnel (`T-FUN-*`).

#### 🧠 Analyse technique associée

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
  - [Difficulté 11](_Frontend-main-courante.md#911-difficulté-11--visualisation-des-contraintes-du-formulaire) : 
    visualisation des contraintes dans le formulaire (fonctionnalités vs Design UX/UI).


#### 🔧 Impacts techniques

- Vues : `MediaCreateView`, `LivreCreateView`, etc.  
- Templates : `media_form.html` + templates typés si besoin  
- Tests : `T-VUE-06`, `T-FORM-01`, `T-FORM-02` à prévoir

---

### 3.3. Cas d’usage (souhaitables) – Modification et suppression 

| ID           | Description métier                           | Statut         | Vue cible         | Avancement     |
|--------------|----------------------------------------------|----------------|-------------------|----------------|
| UC-UPDATE-01 | Modifier un média typé ou non typé           | 🔸 Souhaitable | `MediaUpdateView` | ❌ Non commencé |
| UC-DELETE-01 | Masquer un média (sans suppression physique) | 🔸 Souhaitable | `MediaDeleteView` | ❌ Non commencé |

> Ces cas d’usage peuvent être développés ultérieurement ou en fin de l'issue #3.

---

## 4. Liaison technique

| Élément            | Source technique                                                                |
|--------------------|---------------------------------------------------------------------------------|
| Modèle             | `Media`, `Livre`, `Dvd`, `Cd`                                                   |
| Vue                | `MediaListView`, `MediaDetailView`, `MediaCreateView`                           |
| Template           | `media_list.html`, `media_detail.html`, `media_form.html`                       |
| Formulaire         | `MediaForm`, `LivreForm`, `DvdForm`, `CdForm`                                   |
| Tests techniques   | `test_vues_media_list.py`, `test_vues_media_detail.py`, `test_entites_media.py` |
| tests fonctionnels | `test_uc_list_media.py`, `test_uc_create_media.py`                              |

---
