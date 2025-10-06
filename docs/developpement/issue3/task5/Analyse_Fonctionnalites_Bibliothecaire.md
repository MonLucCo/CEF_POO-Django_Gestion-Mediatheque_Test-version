# 📘 Analyse des fonctionnalités – Bibliothécaire  

📁 `/docs/developpement/issue3/task5/Analyse_Fonctionnalites.md`  

📌 Version : index F-1 (issue #3 – étape 5)

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

| ID         | Description métier                            | Filtrage appliqué                                         | Avancement                                 |
|------------|-----------------------------------------------|-----------------------------------------------------------|--------------------------------------------|
| UC-LIST-01 | Afficher tous les médias consultables         | `Media.objects.filter(consultable=True)`                  | ✅ Implémenté                               |
| UC-LIST-02 | Afficher tous les médias disponibles          | `Media.objects.filter(consultable=True, disponible=True)` | 🔸 À intégrer dans get_queryset()          |
| UC-LIST-03 | Afficher les médias par type (Livre, Dvd, Cd) | `Media.objects.filter(media_type='LIVRE')` (ou autre)     | 🔸 À intégrer avec paramètre GET ou filtre |

> ✅ UC-LIST-01 est validé dans MediaListView et testé (`T-VUE-01`, `T-VUE-02`).   
> 🔸 UC-LIST-02 et UC-LIST-03 sont à intégrer dans la logique de filtrage dynamique.

#### 🔧 Impacts techniques

- Vue : `MediaListView` avec surcharge de `get_queryset()`  
- Template : `media_list.html` avec blocs conditionnels  
- Tests : `T-VUE-01`, `T-VUE-02`, `T-VUE-06` à prévoir

---

### 3.2 Cas d’usage UC-CREATE – Création d’un média

#### 🎯 Objectif métier  
Permettre au bibliothécaire d’ajouter un nouveau média au catalogue, avec ou sans typage immédiat.

#### 🧩 Cas d’usage

| ID           | Description métier                                    | Formulaire utilisé | Avancement            |
|--------------|-------------------------------------------------------|--------------------|-----------------------|
| UC-CREATE-01 | Ajouter un média non typé (`media_type='NON_DEFINI'`) | `MediaForm`        | 🔸 Formulaire à créer |
| UC-CREATE-02 | Ajouter un Livre                                      | `LivreForm`        | 🔸 Formulaire à créer |
| UC-CREATE-03 | Ajouter un Dvd                                        | `DvdForm`          | 🔸 Formulaire à créer |
| UC-CREATE-04 | Ajouter un Cd                                         | `CdForm`           | 🔸 Formulaire à créer |

> 🔸 Les vues `CreateView` typées ne sont pas encore développées.  
> 🔸 Les formulaires spécifiques sont à créer et à valider via `full_clean()`.  
> 📌 Aucun test `T-FORM-*` encore défini.

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

| Élément     | Source technique                     |
|-------------|--------------------------------------|
| Modèle      | `Media`, `Livre`, `Dvd`, `Cd`        |
| Vue         | `MediaListView`, `MediaDetailView`, `MediaCreateView` |
| Template    | `media_list.html`, `media_detail.html`, `media_form.html` |
| Formulaire  | `MediaForm`, `LivreForm`, `DvdForm`, `CdForm` |
| Tests       | `test_vues_media_list.py`, `test_vues_media_detail.py`, `test_entites_media.py` |

---
