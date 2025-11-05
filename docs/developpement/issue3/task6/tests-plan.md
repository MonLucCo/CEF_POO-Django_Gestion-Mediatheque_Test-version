# ✅ Plan de test – Bibliothécaire

📁 `/docs/developpement/issue3/task5/tests-plan.md`  

📌 Version : index H-9 (issue #3 – étape 6 - Bloc 3)
- Rapport de tests associé : [`test_report_indexH-9.txt`](test_report_indexH-9.txt)

___

Ce document constitue le plan de test unitaire et fonctionnel de l’application dédiée au profil bibliothécaire. 
Il accompagne le développement progressif des fonctionnalités définies dans l’issue #3, en particulier l’étape 5, 
et sert de base extensible pour les étapes suivantes et les autres issues du projet.

Les tests ont été regroupé en **Bloc de tests** qui correspondent à des phases de développement de l'issue #3 :
- **Bloc 1** : Première correction majeure de la modélisation
- **Bloc 2** : développement fonctionnel de l'application bibliothécaire (entité `Media`).
- **Bloc 3** : développement fonctionnel des entités `Membre`, `Emprunt` et `JeuDePlateau` de l'application Bibliothecaire.

Il est conçu pour :
- Structurer les tests par catégorie (navigation, entités, fonctionnalités)
- Garantir une couverture minimale par vue, extensible selon les besoins
- Faciliter la lecture, la maintenance et l’enrichissement du projet
- Documenter les cas de test, les méthodes de validation et les liens techniques

📌 Version du document :  
- **Indexage** : 
  - index E-7 (index D-3, avec correction de la modélisation) pour le **Bloc 1** de correction
  - index G-10 (modification des médias non typés : fonction de typage des médias et rollback en média non typé) pour 
  le **Bloc 2** de correction, avec :
    - index F-1, reprise du développement fonctionnel
    - index F-3, fonctions de liste et de création d'un média non typé
    - index F-4, fonctions de création des médias typés. Intégration du cycle de vie de `Media`.
  - index H-9 (entités Emprunt) pour le **Bloc 3**, avec :
    - index H-1 à H-4, restructuration documentaire pour organiser toutes les entités.
    - Index H-5, fonctions de liste des membres et organisation de la navigation.
    - Index H-6, fonction de création des membres et correction du menu de navigation des Membres.
    - Index H-7, fonction de mise à jour des membres et gestion du contexte de session pour l'UX.
    - Index H-8, fonction de suppression (logique) des membres de la gestion du Bibliothécaire.
    - Index H-9, fonction de marquage du retard des emprunts avec une logique combinée `actions techniques` vs `UX`.
- **Périmètre couvert** : site administration, entité `Media` – vues `liste` et `détail`  
- **Niveau de couverture** : tests de niveau _minimum_ à _intermédiaire_  
- **Évolutivité prévue** :
  - entité `Media` - vues `mise à jour` et `supprime` (masque pour le bibliothécaire)
  - entités `Emprunt`, `Membre`, `JeuDePlateau` et vues CRUD

📌 Ce plan de test est spécifique aux étapes de l’issue #3.
Il pourra être déplacé ou indexé dans `/docs/tests/` (à créer) si une documentation globale est mise en place.
Chaque index de ce plan possède un rapport de tests nommé `tests_report_index[version].md`.

---

📁 `/docs/developpement/issue3/task6/tests-plan.md`  
- Rapport de tests associé : [`test_report_indexH-1.txt`](test_report_indexH-1.txt)

➡️ Ce document poursuit le plan de test figé à l’index G-10 ([`tests-plan_indexG-10.md` (`/task5`)](../task5/tests-plan_indexG-10.md))  
➡️ Il accompagne le développement des entités `Membre`, `Emprunt`, `Retour` dans le cadre du profil Bibliothécaire.

---

Ce plan de test couvre les fonctionnalités du **Bloc 3** de l’issue #3, en lien avec la main-courante 
[`_Frontend-main-courante.md`](_Frontend-main-courante.md).

Il est conçu pour :
- Structurer les tests unitaires et fonctionnels liés aux entités `Membre` et `Emprunt`
- Vérifier les transitions métier (création, retour, statut)
- Préparer les tests d’historique, filtrage, et blocage de compte
- Étendre la couverture des vues CRUD et des formulaires

📌 Indexage prévu :
- **Index H+** : développement fonctionnel des vues et modèles `Membre`, `Emprunt`, `Retour`
- **Bloc 3** : finalisation du cycle métier Bibliothécaire

📌 Évolutivité :
- Intégration des tests UC-EMPRUNT-01 à UC-EMPRUNT-05
- Intégration des tests UC-MEMBRE-01 à UC-MEMBRE-06
- Préparation des tests de permissions et accès conditionnels
- Tests de cohérence entre `Media` et `Emprunt` (statut, disponibilité)

📌 Documents associés :
- [`_Frontend-main-courante.md`](_Frontend-main-courante.md)
- [`Analyse_Fonctionnalites_Bibliothecaire.md`](Analyse_Fonctionnalites_Bibliothecaire.md)
- [`Analyse_LifeCycle_Emprunts.md`](Analyse_LifeCycle_Emprunts.md) *(à créer)*

---

## 📑 Sommaire

1. [🔹 Objectifs du plan de test](#-1-objectifs-du-plan-de-test)
2. [🔹 Organisation des tests](#-2-organisation-des-tests)
3. [🔹 Cas de test (Étape 5)](#-3-cas-de-test-étape-5)
   - [🧪 Navigation (`T-NAV-xxx`)](#-navigation-t-nav-xxx)
   - [🧪 Entités (`T-ENT-xxx`)](#-entités-t-ent-xxx)
   - [🧪 Vues (`T-VUE-xxx`)](#-vues-t-vue-xxx)
   - [🧪 Formulaires (`T-FORM-xxx`)](#-formulaires-t-form-xxx)
   - [🧪 Administration (`T-ADM-xxx`)](#-administration-t-adm-xxx)
   - [🧪 Fonctionnel (`T-FUN-xxx`)](#-fonctionnel-t-fun-xxx)
4. [🔹 Méthode de validation](#-4-méthode-de-validation)
5. [🔹 Couverture attendue](#-5-couverture-attendue)
6. [🔹 Liens vers les fichiers de test](#-6-liens-vers-les-fichiers-de-test)
7. [🔹 Évolutivité du plan](#-7-évolutivité-du-plan)
8. [🔹 Références](#-8-références)

---

## 🔹 1. Objectifs du plan de test

- Vérifier que chaque vue retourne un code HTTP 200
- Vérifier que les bons templates sont utilisés
- Vérifier que les données attendues sont affichées
- Vérifier que les champs spécifiques du type réel sont accessibles
- Structurer les tests pour faciliter leur extension et leur maintenance

---

## 🔹 2. Organisation des tests

Les tests sont répartis en cinq catégories :

| Catégorie      | Dossier / Fichier                           | Préfixe ID | Objectif principal                                 | Création |
|----------------|---------------------------------------------|------------|----------------------------------------------------|----------|
| Navigation     | `tests_blocs/test_urls.py`                  | `T-NAV-`   | Vérifier les accès, les routes, les redirections   | Initial  |
| Entités        | `tests_blocs/test_entites_media.py`, etc.   | `T-ENT-`   | Vérifier la cohérence des modèles et des données   | initial  |
| Vues           | `tests_blocs/test_vues_media_list.py`, etc. | `T-VUE-`   | Vérifier le comportement des vues et des templates | Initial  |
| Administration | `tests_blocs/test_admin.py`                 | `T-ADM-`   | Vérifier le site d'administration du projet        | Bloc 1   |
| Fonctionnel    | `tests_blocs/test_uc_list_media.py`, etc.   | `T-FUN-`   | Vérifier une fonctionnalité métier                 | Bloc 2   |

> Remarque : les catégories Permissions, Formulaires, Erreurs, Filtrages sont envisagées, mais n'ont pas été mises en 
> œuvre pour cette étape du développement.

---

## 🔹 3. Cas de test (Étape 5)

Chaque catégorie de tests est regroupée dans une sous-section spécifique avec une indication de son status :
- 🔄 À tester
- ❌ Echec
- ✅ Validé
- 🟡 Non implémenté

### 🧪 Navigation (`T-NAV-xxx`)

| Série  | ID Test  | Description                                   | URL ciblée                                         | Résultat attendu                                 | Statut   |
|--------|----------|-----------------------------------------------|----------------------------------------------------|--------------------------------------------------|----------|
| Bloc 1 | T-NAV-01 | Accès à la page d’accueil                     | `/bibliothecaire/`                                 | Code 200 + template accueil                      | ✅ Validé |
| Bloc 1 | T-NAV-02 | Accès à la liste des médias                   | `/bibliothecaire/media/`                           | Code 200 + template liste                        | ✅ Validé |
| Bloc 1 | T-NAV-03 | Accès au détail d’un média existant           | `/bibliothecaire/media/1/`                         | Code 200 + template détail                       | ✅ Validé |
| Bloc 1 | T-NAV-04 | Accès à un média inexistant                   | `/bibliothecaire/media/999/`                       | Code 404                                         | ✅ Validé |
| Bloc 2 | T-NAV-05 | Accès à la liste des médias consultables      | `/bibliothecaire/medias/consultables/`             | Code 200 + template liste                        | ✅ Validé |
| Bloc 2 | T-NAV-06 | Accès à la liste des médias disponibles       | `/bibliothecaire/medias/disponibles/`              | Code 200 + template liste                        | ✅ Validé |
| Bloc 2 | T-NAV-07 | Accès à la liste des médias par type          | `/bibliothecaire/medias/type/?type=LIVRE`          | Code 200 + template liste                        | ✅ Validé |
| Bloc 2 | T-NAV-08 | Accès à la création d'un média                | `/bibliothecaire/medias/ajouter/`                  | Code 200 + template liste                        | ✅ Validé |
| Bloc 2 | T-NAV-09 | Accès à la liste des médias non typés         | `/bibliothecaire/medias/non-types/`                | Code 200 + template liste                        | ✅ Validé |
| Bloc 3 | T-NAV-10 | Accès à la liste des membres (tous)           | `/bibliothecaire/membres/`                         | Code 200 + template liste membres                | ✅ Validé |
| Bloc 3 | T-NAV-11 | Accès à la liste des membres en gestion       | `/bibliothecaire/membres/gestion`                  | Code 200 + template liste membres                | ✅ Validé |
| Bloc 3 | T-NAV-12 | Accès à la liste des membres abonnés          | `/bibliothecaire/membres/emprunteurs`              | Code 200 + template liste membres                | ✅ Validé |
| Bloc 3 | T-NAV-13 | Accès à la liste des membres supprimés        | `/bibliothecaire/membres/supprimes`                | Code 200 + template liste membres                | ✅ Validé |
| Bloc 3 | T-NAV-14 | Accès à la création d’un membre standard      | `/bibliothecaire/membres/ajouter/`                 | Code 200 + formulaire affiché                    | ✅ Validé |
| Bloc 3 | T-NAV-15 | Accès à la création d’un membre emprunteur    | `/bibliothecaire/membres/ajouter/emprunteur`       | Code 200 + formulaire affiché                    | ✅ Validé |
| Bloc 3 | T-NAV-16 | Accès à la mise à jour d’un membre            | `/bibliothecaire/membres/<pk>/modifier/`           | Code 200 + formulaire affiché                    | ✅ Validé |
| Bloc 3 | T-NAV-17 | Accès à l’activation du statut emprunteur     | `/bibliothecaire/membres/<pk>/activer/emprunteur/` | Code 200 + page de confirmation                  | ✅ Validé |
| Bloc 3 | T-NAV-18 | Accès à la page de confirmation               | `/membres/<pk>/supprimer/`                         | Code 200 + template affiché                      | ✅ Validé |
| Bloc 3 | T-NAV-19 | Accès à la vue de marquage manuel des retards | `/bibliothecaire/emprunts/retard/`                 | Code 200 + template `emprunt_retard_result.html` | ✅ Validé |
| Bloc 3 | T-NAV-20 | Accès à la liste des emprunts                 | `/bibliothecaire/emprunts/`                        | Code 200 + template `emprunt_list.html`          | ✅ Validé |


> ❌ Le test T-NAV-03 a révélé une contrainte sur le champ `annee_edition` du modèle `Media`. ✅ Il a été repris 
> après correction du modèle de données.  
> 🔧 La correction a été intégrée et documentée dans [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](../task5/Modelisation_correction-erreurs-suite-tests-unitaires.md).  
> 📌 Aucun point technique à noter dans la main-courante pour la série du **Bloc 1**.

---

### 🧪 Entités (`T-ENT-xxx`)

| Série  | ID Test  | Description                                                              | Modèle testé    | Résultat attendu                                                        | Statut   |
|--------|----------|--------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------|----------|
| Bloc 1 | T-ENT-01 | Création d’un `Media` non typé (création minimaliste)                    | `Media`         | Attributs cohérents (`name`, `media_type`, `theme`, etc.)               | ✅ Validé |
| Bloc 1 | T-ENT-02 | Vérification des attributs par défaut                                    | `Media`         | `consultable=True`, `disponible=True`                                   | ✅ Validé |
| Bloc 1 | T-ENT-03 | Vérification des attributs accessibles selon le typage                   | `Media`         | Champs spécifiques (`auteur`, `resume`, etc.) absents si non typé       | ✅ Validé |
| Bloc 1 | T-ENT-04 | Vérification du typage multi-table et de la structure en base            | `Media → Livre` | `Media.count() == 2`, `Livre.count() == 1`, `Livre.pk == Media.pk`      | ✅ Validé |
| Bloc 2 | T-ENT-05 | Vérification de tous les objets affichés ont `consultable=True`          | `Media`         | `consultable=True` pour une sélection de `Media`                        | ✅ Validé |
| Bloc 2 | T-ENT-06 | Vérifie que tous les objets affichés ont `disponible=True`               | `Media`         | `disponible=True` (et `consultable=True`) pour une sélection de `Media` | ✅ Validé |
| Bloc 2 | T-ENT-07 | Vérifie que tous les objets affichés ont `media_type='LIVRE'`            | `Media`         | `media_type='LIVRE'` pour une sélection de `Media`                      | ✅ Validé |
| Bloc 2 | T-ENT-08 | Création d'un `Media` (non typé) avec des valeurs minimales              | `Media`         | Valeurs cohérentes avec la définition minimale d'un `Media` non typé    | ✅ Validé |
| Bloc 2 | T-ENT-09 | Vérifie que tous les objets affichés ont `media_type='NON_DEFINI'`       | `Media`         | Tous les objets de la vue ont `media_type='NON_DEFINI'`                 | ✅ Validé |
| Bloc 3 | T-ENT-10 | Vérifie que les membres affichés sont non archivés (`statut != ARCHIVE`) | `Membre`        | Tous les objets ont `statut` différent de `ARCHIVE`                     | ✅ Validé |
| Bloc 3 | T-ENT-11 | Vérifie que les membres affichés sont abonnés (`statut == EMPRUNTEUR`)   | `Membre`        | Tous les objets ont `statut == EMPRUNTEUR`                              | ✅ Validé |
| Bloc 3 | T-ENT-12 | Vérifie que les membres affichés sont archivés (`statut == ARCHIVE`)     | `Membre`        | Tous les objets ont `statut == ARCHIVE`                                 | ✅ Validé |
| Bloc 3 | T-ENT-13 | Création d’un membre standard : statut et compte                         | `Membre`        | `statut == MEMBRE`, `compte` généré correctement                        | ✅ Validé |
| Bloc 3 | T-ENT-14 | Création d’un membre emprunteur : statut et compte                       | `Membre`        | `statut == EMPRUNTEUR`, `compte` généré correctement                    | ✅ Validé |
| Bloc 3 | T-ENT-15 | Mise à jour du nom (informations générales) d’un membre                  | `Membre`        | Le champ `name` est modifié et persisté                                 | ✅ Validé |
| Bloc 3 | T-ENT-16 | Activation du statut emprunteur                                          | `Membre`        | `statut == EMPRUNTEUR` après appel à la vue dédiée                      | ✅ Validé |
| Bloc 3 | T-ENT-17 | Suppression logique d’un membre sans emprunt                             | `Membre`        | `statut == ARCHIVE` après suppression                                   | ✅ Validé |
| Bloc 3 | T-ENT-18 | Refus de suppression si emprunt en cours                                 | `Membre`        | `statut != ARCHIVE` + message d’erreur                                  | ✅ Validé |
| Bloc 3 | T-ENT-19 | Vérifie que le changement de statut lors du marquage du retard           | `Emprunt`       | `statut == EN_COURS` avant marquage, `statut == RETARD` avant marquage  | ✅ Validé |

> ✅ Les tests T-ENT-xx sont validés.  
> ✅ Les assertions couvrent la structure multi-table, les attributs hérités et typés, et la cohérence des enregistrements.  
> 🔧 Les corrections de modélisation ont été intégrées et documentées dans [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](../task5/Modelisation_correction-erreurs-suite-tests-unitaires.md).  
> 📌 Aucun point technique à noter dans la main-courante pour la série du **Bloc 1**.

---

### 🧪 Vues (`T-VUE-xxx`)

| Série  | ID Test  | Vue testée                                        | Description                                                              | Résultat attendu                                                       | Statut   |
|--------|----------|---------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|----------|
| Bloc 1 | T-VUE-01 | `MediaListView`                                   | Affichage des titres                                                     | Présence dans le HTML                                                  | ✅ Validé |
| Bloc 1 | T-VUE-02 | `MediaListView`                                   | Affichage du type et disponibilité                                       | Présence dans le HTML                                                  | ✅ Validé |
| Bloc 1 | T-VUE-03 | `MediaDetailView`                                 | Affichage des champs spécifiques du sous-type                            | Présence de `auteur`, `resume`, etc. si typé                           | ✅ Validé |
| Bloc 1 | T-VUE-04 | `MediaDetailView`                                 | Utilisation de l’objet typé dans le contexte                             | Instance héritée (`Livre`, `Dvd`, `Cd`) reçue                          | ✅ Validé |
| Bloc 1 | T-VUE-05 | `MediaDetailView`                                 | Affichage d’un objet non typé malgré `media_type` défini                 | Absence des champs spécifiques dans le HTML                            | ✅ Ajouté |
| Bloc 2 | T-VUE-06 | `MediaListConsultableView`                        | Le titre <`h2`> du template correspond à la vue consultable              | Présence dans le HTML                                                  | ✅ Validé |
| Bloc 2 | T-VUE-07 | `MediaDisponibleListView`                         | Le titre <`h2`> du template correspond à la vue disponibles              | Présence dans le HTML                                                  | ✅ Validé |
| Bloc 2 | T-VUE-08 | `MediaTypeListView`                               | Le titre <`h2`> du template correspond au type demandé                   | Présence dans le HTML                                                  | ✅ Validé |
| Bloc 2 | T-VUE-09 | `MediaCreateView`                                 | Affichage du formulaire `MediaForm` dans le template `media_form.html`   | Présence du template dans le HTML                                      | ✅ Validé |
| Bloc 2 | T-VUE-10 | `MediaNonTypeListView`                            | Le titre <`h2`> du template correspond à la vue des non typés            | Présence dans le HTML                                                  | ✅ Validé |
| Bloc 3 | T-VUE-11 | `MembreListView` (vue tous les membres)           | Affichage du tableau avec les colonnes attendues                         | Présence des colonnes `Nom`, `Compte`, `Statut`, `Emprunts`, `Retards` | ✅ Validé |
| Bloc 3 | T-VUE-12 | `MembreEnGestionView`                             | Affichage filtrée des membres non archivés                               | Présence des membres avec `statut != ARCHIVE`                          | ✅ Validé |
| Bloc 3 | T-VUE-13 | `MembreEmprunteursView`                           | Affichage filtrée des membres abonnés                                    | Présence des membres avec `statut == EMPRUNTEUR`                       | ✅ Validé |
| Bloc 3 | T-VUE-14 | `MembreArchivesView`                              | Affichage filtrée des membres supprimés                                  | Présence des membres avec `statut == ARCHIVE`                          | ✅ Validé |
| Bloc 3 | T-VUE-15 | `membre_list.html` (template)                     | Affichage conditionnel du tableau                                        | Tableau affiché uniquement si `membres` non vide                       | ✅ Validé |
| Bloc 3 | T-VUE-16 | `MembreCreateView` / `MembreCreateEmprunteurView` | Affichage du titre `<h2>` selon le contexte `is_emprunteur`              | Texte dynamique : “Créer un Membre…”                                   | ✅ Validé |
| Bloc 3 | T-VUE-17 | `MembreUpdateView`                                | Affichage du formulaire avec données préremplies                         | Formulaire affiché avec `name` initialisé                              | ✅ Validé |
| Bloc 3 | T-VUE-18 | `MembreActivateEmprunteurView`                    | Affichage de la page de confirmation d’activation                        | Présence du nom du membre et bouton de validation                      | ✅ Validé |
| Bloc 3 | T-VUE-19 | `MembreDetailView`                                | Affichage conditionnel du lien “Supprimer”                               | Présence si `peut_etre_supprime == True`                               | ✅ Validé |
| Bloc 3 | T-VUE-20 | `membre_supprime_confirm.html`                    | Affichage des données du membre + mise en garde                          | Présence du nom, compte, message d’alerte                              | ✅ Validé |
| Bloc 3 | T-VUE-21 | `AccueilBibliothecaireView`                       | Affichage du message UX de retard (`accueil.html`)                       | Message affiché si `retard_message` présent en session                 | ✅ Validé |
| Bloc 3 | T-VUE-22 | `AccueilBibliothecaireView`                       | Affichage conditionnel du tableau (`accueil.html`)                       | Tableau affiché si `affiche_table == True`                             | ✅ Validé |
| Bloc 3 | T-VUE-23 | `EmpruntRetardView`                               | Affichage du tableau des emprunts marqués (`emprunt_retard_result.html`) | Tableau affiché avec les emprunts marqués                              | ✅ Validé |
| Bloc 3 | T-VUE-24 | `emprunt_retard_marque_table.html`                | Affichage correct des colonnes  (`include`)                              | Colonnes : Membre, Média, Date emprunt, Date retour prévu              | ✅ Validé |

> ✅ La distinction entre typage réel et simple valeur `media_type` est désormais testée.  
> ✅ La logique de typage dynamique est assurée par la surcharge de `get_object()` dans `MediaDetailView`.  
> 📌 Le test `T-VUE-05` confirme que `media_type="LIVRE"` ne suffit pas sans sous-type instancié.
> 📌 Le test `T-VUE-15` nécessite un identifiant du tableau (`<table id="liste-annuaire">` pour simplifier le test.

---

### 🧪 Formulaires (`T-FORM-xxx`)

| Série  | ID Test   | Formulaire testé | Description                                                         | Résultat attendu                                                              | Statut   |
|--------|-----------|------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------|----------|
| Bloc 2 | T-FORM-01 | `MediaForm`      | Vérifie que les champs attendus sont présents dans le formulaire    | Champs `name`, `theme`, `annee_edition` visibles dans le HTML                 | ✅ Validé |
| Bloc 2 | T-FORM-02 | `MediaForm`      | Vérifie que les labels personnalisés sont affichés                  | `Titre du média`, `Thématique`, `Année d'édition` présents dans le formulaire | ✅ Validé |
| Bloc 2 | T-FORM-03 | `MediaForm`      | Vérifie les contraintes de validation (obligatoires vs facultatifs) | `name` et `theme` obligatoires, `annee_edition` facultatif                    | ✅ Validé |
| Bloc 3 | T-FORM-04 | `MembreForm`     | Vérifie que seul le champ `name` est exposé avec le bon label       | Champ `name` visible, label = “Nom du Membre”                                 | ✅ Validé |
| Bloc 3 | T-FORM-05 | `MembreForm`     | Vérifie que le champ `name` est prérempli et modifiable             | Champ visible, valeur initiale correcte                                       | ✅ Validé |
| Bloc 3 | T-FORM-06 | `MembreForm`     | Vérifie que le champ `statut` n’est pas exposé                      | Champ absent du formulaire HTML                                               | ✅ Validé |
| Bloc 3 | T-FORM-07 | `MembreForm`     | Formulaire de confirmation de suppression                           | Bouton “Confirmer” + lien “Annuler” présents                                  | ✅ Validé |

> 🔧 Ces tests permettent de valider la structure, la lisibilité et la robustesse du formulaire `MediaForm`, 
> indépendamment de la logique métier.  
> 🔹 Ils sont complémentaires aux tests fonctionnels (`T-FUN-*`) qui valident le cycle complet de création.  
> 🔹 Le test `T-FORM-03` confirme que les contraintes sont bien définies dans le modèle et respectées dans le 
> formulaire, sans dépendre du design visuel (cf. [Difficulté 11](_Frontend-main-courante.md#911-difficulté-11--visualisation-des-contraintes-du-formulaire)).

---

### 🧪 Administration (`T-ADM-xxx`)

| Série  | ID Test  | Description                                                                 | Cible                         | Résultat attendu                                           | Statut   |
|--------|----------|-----------------------------------------------------------------------------|-------------------------------|------------------------------------------------------------|----------|
| Bloc 1 | T-ADM-01 | Accès à l’interface admin et aux apps exposées (`/admin/{app_label}/`)      | `admin:index` + apps exposées | Code 200 pour chaque URL                                   | ✅ Validé |
| Bloc 1 | T-ADM-02 | Vérification des URLs admin selon les permissions déclarées dans ModelAdmin | `ModelAdmin` exposés          | Code 200 pour chaque vue autorisée (`add`, `change`, etc.) | ✅ Validé |

> 🔧 Les tests utilisent `RequestFactory` pour simuler une requête authentifiée (`mock_request`) et éviter les erreurs 
> liées à `self.client.request()`.  
> ✅ Le test T-ADM-02 est dynamique : il s’adapte aux permissions et à la présence d’objets pour chaque modèle.  
> 📌 Le modèle `Media` est exposé en lecture seule, ce qui est pris en compte dans le test.

---

### 🧪 Fonctionnel (`T-FUN-xxx`)

| Série  | ID Test  | Description                                                                                  | Résultat attendu                                                                                                            | Statut            |
|--------|----------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------|
| Bloc 2 | T-FUN-01 | Vérifie que la vue consultable respecte les règles métier définies (MEDIA-UC-LIST-01)        | Code 200 + template (T-NAV-05), Booléen vrai (T-ENT-05), Contenu HTML (T-VUE-06)                                            | ✅ Validé          |
| Bloc 2 | T-FUN-02 | Vérifie que la vue disponibles respecte les règles métier définies (MEDIA-UC-LIST-02)        | Code 200 + template (T-NAV-06), Booléen vrai (T-ENT-06), Contenu HTML (T-VUE-07)                                            | ✅ Validé          |
| Bloc 2 | T-FUN-03 | Vérifie que la vue par type respecte les règles métier définies (MEDIA-UC-LIST-03)           | Code 200 + template (T-NAV-07), Type exact (T-ENT-07), Contenu HTML (T-VUE-08)                                              | ✅ Validé          |
| Bloc 2 | T-FUN-04 | Création réussie d'un média (non typé) avec les données valides                              | Code 302 + Redirection finale correcte + Objet `Media` (non typé) créé en base                                              | ✅ Validé          |
| Bloc 2 | T-FUN-05 | Vérifie le refus de création d'un média (non typé) avec champ obligatoire manquant           | Code 200 + Template Form avec message d'erreur + Objet `Media` non créé en base                                             | ✅ Validé          |
| Bloc 2 | T-FUN-06 | Vérifie que la vue non typée respecte les règles métier définies (MEDIA-UC-LIST-04)          | Code 200 + template (T-NAV-09), Type exact (NON_DEFINI), Contenu HTML spécifique                                            | ✅ Validé          |
| Bloc 2 | T-FUN-07 | Vérifie la création d’un média typé selon l’état métier attendu                              | Création via formulaire : état 1 (`consultable=False`, `disponible=True`) ou état 3 (`consultable=True`, `disponible=True`) | ✅ Validé          |
| Bloc 2 | T-FUN-08 | Création d’un sous-type via typage (`MediaTypage<Type>View`)                                 | Objet typé créé, champs spécifiques appliqués, redirection vers la liste                                                    | ✅ Validé          |
| Bloc 2 | T-FUN-09 | Annulation du typage (`MediaCancelTypingView`)                                               | Sous-type supprimé, `media_type` réinitialisé à `'NON_DEFINI'`, redirection OK                                              | ✅ Validé          |
| Bloc 2 | T-FUN-10 | Redirection vers typage depuis `MediaUpdateView` si `media_type` modifié                     | Redirection vers la vue `MediaTypage<Type>View` sans enregistrement préalable                                               | ✅ Validé          |
| Bloc 3 | T-FUN-11 | Vérifie que la vue tous les membres respecte les règles métier (MEMBRE-UC-LIST-02)           | Code 200 + template + membres non archivés (`statut != ARCHIVE`)                                                            | ✅ Validé          |
| Bloc 3 | T-FUN-12 | Vérifie que la vue abonnés respecte les règles métier (MEMBRE-UC-LIST-03)                    | Code 200 + template + membres abonnés (`statut == EMPRUNTEUR`)                                                              | ✅ Validé          |
| Bloc 3 | T-FUN-13 | Vérifie que la vue supprimés respecte les règles métier (MEMBRE-UC-LIST-04)                  | Code 200 + template + membres archivés (`statut == ARCHIVE`)                                                                | ✅ Validé          |
| Bloc 3 | T-FUN-14 | Création de plusieurs membres standards avec données valides                                 | Redirection + `statut == MEMBRE` + `compte` généré                                                                          | ✅ Validé          |
| Bloc 3 | T-FUN-15 | Création de plusieurs membres emprunteurs avec données valides                               | Redirection + `statut == EMPRUNTEUR` + `compte` généré                                                                      | ✅ Validé          |
| Bloc 3 | T-FUN-16 | Mise à jour réussie du nom d’un membre (MEMBRE-UC-UPDATE-01)                                 | Redirection vers `membre_detail` + nom modifié visible                                                                      | ✅ Validé          |
| Bloc 3 | T-FUN-17 | Activation du statut emprunteur (MEMBRE-UC-UPDATE-02)                                        | Redirection vers `membre_detail` + `statut == EMPRUNTEUR` + message de succès                                               | ✅ Validé          |
| Bloc 3 | T-FUN-18 | Enchaînement métier complet d’activation emprunteur (affichage + confirmation + redirection) | Page affichée, bouton cliqué, redirection vers `membre_detail`, `statut == EMPRUNTEUR`                                      | ✅ Validé          |
| Bloc 3 | T-FUN-19 | Suppression réussie d’un membre sans emprunt                                                 | Redirection vers `membre_detail` + `statut == ARCHIVE` + message de succès                                                  | ✅ Validé          |
| Bloc 3 | T-FUN-20 | Suppression refusée si emprunt en cours                                                      | Redirection vers `membre_detail` + `statut != ARCHIVE` + message d’erreur                                                   | ✅ Validé          |
| Bloc 3 | T-FUN-21 | Marquage manuel des retards via vue dédiée (Accès à `EmpruntRetardView`)                     | Message UX affiché + tableau mis à jour                                                                                     | ✅ Validé          |
| Bloc 3 | T-FUN-22 | Marquage automatique à la première connexion (`retard_last_check_date` < aujourd’hui )       | Marquage déclenché + message et tableau affichés - Accès à `AccueilBibliothecaireView`                                      | ✅ Validé          |
| Bloc 3 | T-FUN-23 | Masquage du tableau via bouton POST (`affiche_table == True` - POST `toggle_table=false`)    | Tableau masqué, session mise à jour - Accès à `AccueilBibliothecaireView`                                                   | ✅ Validé          |
| Bloc 3 | T-FUN-24 | Affichage du tableau via bouton POST (`affiche_table == False` - POST `toggle_table=true`)   | Tableau affiché, session mise à jour - Accès à `AccueilBibliothecaireView`                                                  | ✅ Validé          |
| Bloc 3 | T-FUN-25 | Rejeu du marquage automatique via fonction de debug (`retard_last_check_date` modifiée)      | Marquage relancé, message et tableau mis à jour - Accès à `AccueilBibliothecaireView`                                       | 🟡 Non implémenté |

> 🔧 Les tests unitaires _fonctionnels_ sont définis pour être autonome. Ils peuvent se rapprocher de tests unitaires
> _techniques_ qui sont indiqués dans le _résultat attendu_. 
> Pour une facilité de développement et de maintenance, ils sont regroupés dans une classe de tests fonctionnels et techniques.  
> 🔹 Cette organisation permet de valider chaque UC dans une classe dédiée, tout en conservant la granularité des tests
> techniques pour le diagnostic.  

> 🔧 Les tests de création (T-FUN-04 et T-FUN-05) attendent : 
> - un code **HTTP 302** qui correspond à la _redirection automatique_ effectuée par Django après validation du 
> formulaire via `form_valid()`.
> - un code **HTTP 200** qui correspond à la page servie avec un _message d'erreur_ après l'invalidation du formulaire 
> via `form_invalid()`.   
> 
> Ce comportement est standard pour les vues génériques (CreateView) et confirme le succès de l’enregistrement ou 
> l'affichage d'une erreur dans le formulaire.


> 🔧 Les tests T-FUN-08 à T-FUN-10 valident la logique métier du typage différé, la cohérence des transitions, 
> et la robustesse des vues associées.  
> Ces tests consolident le fonctionnement de la fonction **ajouter un média**.

> 🔧 Les tests T-FUN-14 à T-FUN-15 valident la logique métier du compte défini automatiquement par une règle métier d'unicité, 
> la cohérence et la robustesse des créations sont réalisées dans une boucle de `subTest()`.  
> Ces tests consolident le fonctionnement de la fonction **créer un membre**.

> 🔧 Les tests T-FUN-18 valide l'enchaînement de la logique métier pour activer un membre-emprunteur. Il s'agit de la 
> validation de plusieurs fonctionnalités dans un bloc fonctionnel métier cohérent. 

> 🔧 Le test T-FUN-25 est volontairement laissé `🟡 Non implémenté` car il ne correspond pas à un cas d'usage métier 
> validé. Il concerne une fonctionnalité de rejeu de test de l'UX (debug). 

---

## 🔹 4. Méthode de validation

- Exécution des tests via :
  ```bash
  python manage.py test bibliothecaire
  ```
- Visualisation dans PyCharm :
  - Onglet “Run” avec icônes ✅ / ❌
  - Affichage des erreurs, lignes concernées, et liens vers le code
- Vérification manuelle dans le navigateur (complémentaire)

> ℹ️ Note : pour obtenir les résultats en redirigeant la sortie vers un fichier `test_report.txt`, il faut aussi rediger 
> le canal de sortie d'erreur (canal 2) vers le canal standard (canal 1).
> 
> Cette redirection permet de capturer les messages de test affichés dans le terminal, qui sont parfois envoyés sur le 
> canal d’erreur (stderr) par Django ou les frameworks de test. 
> Pour une analyse structurée, il faut utiliser `--verbosity=2` ou `--verbosity=3` selon le niveau de détail souhaité.

> La commande dans le terminal est :
> 
> ```bash
> python manage.py test bibliothecaire --verbosity=2 > test_report.txt 2>&1
> ```

> Utilisation de `subTest()` :  
> 🔹 Les tests UC-LIST-03 utilisent subTest() pour valider les trois types (LIVRE, DVD, CD) dans une boucle unique.  
> 🔹 Cette approche permet une couverture complète tout en conservant la lisibilité et la modularité des tests.

---

## 🔹 5. Couverture attendue

| Niveau de couverture | Description                                                      |
|----------------------|------------------------------------------------------------------|
| Minimum              | 1 test par vue (liste, détail, accueil)                          |
| Étendu               | Tests de contenu, modèle, navigation `avec variation paramétrée` |
| Futur                | Tests de création, modification, suppression, filtrage           |

---

## 🔹 6. Liens vers les fichiers de test

| Fichier                     | Fonctionnalité ciblée                                                      | Catégorie                |
|-----------------------------|----------------------------------------------------------------------------|--------------------------|
| `test_urls.py`              | Routage et accès (URLs locales)                                            | Navigation               |
| `test_entites_media.py`     | Modèle `Media` et sous-types                                               | Entités                  |
| `test_vues_media_detail.py` | Détail d’un média typé                                                     | Vues                     |
| `test_vues_media_list.py`   | Liste des médias                                                           | Vues                     |
| `test_admin.py`             | Interface d’administration                                                 | Administration           |
| `test_uc_list_media.py`     | Cas d’usage des listes de médias (consultables, disponibles, typés)        | Fonctionnel              |
| `test_uc_create_media.py`   | Cas d'usage des créations de médias (non typé, livre, dvd, cd)             | Fonctionnel              |
| `test_uc_typage_media.py`   | Cas d’usage du typage et rollback des médias non typés                     | Fonctionnel              |
| `test_uc_list_membre.py`    | Cas d'usage des listes des membres (membres, emprunteurs, supprimés, tous) | Technique et Fonctionnel |
| `test_uc_create_membre.py`  | Cas d'usage de création des membres (membre, emprunteur)                   | Technique et Fonctionnel |
| `test_uc_update_membre.py`  | Cas d'usage de modification des membres (membre, emprunteur)               | Technique et Fonctionnel |
| `test_uc_delete_membre.py`  | Cas d'usage de suppression des membres (membre, emprunteur) de la gestion  | Technique et Fonctionnel |

> Les fichiers de tests **technique et fonctionnel** correspondent au regroupement des catégories par classe de tests 
> (cf. [Difficulté 15](_Frontend-main-courante.md#915-difficulté-15--regroupement-des-tests-techniques-et-fonctionnels-dans-un-même-groupe-de-tests)).

---

## 🔹 7. Évolutivité du plan

Ce plan est conçu pour être enrichi au fil du développement :

- Ajout de tests pour les vues `CreateView`, `UpdateView`, `DeleteView`
- Ajout de tests pour les entités `Emprunt`, `Membre`, `JeuDePlateau`
- Ajout de tests de permissions, formulaires, erreurs, filtrage
- Ajout de tests pour les transitions métier définies dans `Analyse_LifeCycle_Medias.md`
- Ajout de tests pour les vues `MediaTypage<Type>View` et `MediaCancelTypingView`
- Ajout de tests de rollback et de redirection conditionnelle
- Préparation des tests pour UC-DELETE (masquage) et UC-ADMIN (suppression définitive)
- Organisation des fichiers de tests (à partir du Bloc3) regroupant les tests techniques et fonctionnels (cf. [Difficulté 15](_Frontend-main-courante.md#915-difficulté-15--regroupement-des-tests-techniques-et-fonctionnels-dans-un-même-groupe-de-tests)).

---

## 🔹 8. Références

- [Main courante – Étape 5](_Frontend-main-courante.md)
- [Issue #3 – Développement de l’application bibliothécaire](https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version/issues/3)
- [Django Testing Best Practices – CodezUp](https://codezup.com/django-testing-best-practices-unit-tests-integration-tests/)
- [Writing Scalable Unit Tests in Django – Dev.to](https://dev.to/shreyash_jhon_doe/writing-scalable-maintainable-unit-tests-in-django-a-practical-guide-with-real-examples-47a4)

---
