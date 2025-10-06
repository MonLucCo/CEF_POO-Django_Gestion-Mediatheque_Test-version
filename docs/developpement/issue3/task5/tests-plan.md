# ✅ Plan de test – Bibliothécaire

📁 `/docs/developpement/issue3/task5/tests-plan.md`  

📌 Version : index F-1 (issue #3 – étape 5)
___

Ce document constitue le plan de test unitaire et fonctionnel de l’application dédiée au profil bibliothécaire. 
Il accompagne le développement progressif des fonctionnalités définies dans l’issue #3, en particulier l’étape 5, 
et sert de base extensible pour les étapes suivantes et les autres issues du projet.

Les tests ont été regroupé en **Bloc de tests** qui correspondent à des phases de développement de l'issue #3 :
- **Bloc 1** : Première correction majeure de la modélisation
- **Bloc 2** : développement fonctionnel de l'application bibliothécaire.

Il est conçu pour :
- Structurer les tests par catégorie (navigation, entités, fonctionnalités)
- Garantir une couverture minimale par vue, extensible selon les besoins
- Faciliter la lecture, la maintenance et l’enrichissement du projet
- Documenter les cas de test, les méthodes de validation et les liens techniques

📌 Version du document :  
- **Indexage** : 
  - index E-7 (index D-3, avec correction de la modélisation) pour le **Bloc 1** de correction
  - index F-1 pour le **Bloc 2** de correction
- **Périmètre couvert** : site administration, entité `Media` – vues `liste` et `détail`  
- **Niveau de couverture** : tests de niveau _minimum_ à _intermédiaire_  
- **Évolutivité prévue** :
  - entité `Media` - vues `mise à jour` et `supprime` (masque pour le bibliothécaire)
  - entités `Emprunt`, `Membre`, `JeuDePlateau` et vues CRUD

📌 Ce plan de test est spécifique à l’étape 5 de l’issue #3.
Il pourra être déplacé ou indexé dans `/docs/tests/` (à créer) si une documentation globale est mise en place.
Chaque index de ce plan possède un rapport de tests nommé `tests_report_index[version].md`.

---

## 📑 Sommaire

1. [🔹 Objectifs du plan de test](#-1-objectifs-du-plan-de-test)
2. [🔹 Organisation des tests](#-2-organisation-des-tests)
3. [🔹 Cas de test (Étape 5)](#-3-cas-de-test-étape-5)
   - [🧭 Navigation (`T-NAV-xxx`)](#-navigation-t-nav-xxx)
   - [📚 Entités (`T-ENT-xxx`)](#-entités-t-ent-xxx)
   - [🧪 Vues (`T-VUE-xxx`)](#-vues-t-vue-xxx)
   - [🧪 Administration (`T-ADM-xxx`)](#-administration-t-adm-xxx)
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

> Remarque : les catégories Permissions, Formulaires, Erreurs, Filtrages sont envisagées, mais n'ont pas été mises en œuvre pour cette étape du développement.

---

## 🔹 3. Cas de test (Étape 5)

Chaque catégorie de tests est regroupée dans une sous-section spécifique avec une indication de son status :
- 🔄 À tester
- ❌ Echec
- ✅ Validé

### 🧭 Navigation (`T-NAV-xxx`)

| Série  | ID Test  | Description                              | URL ciblée                             | Résultat attendu            | Statut      |
|--------|----------|------------------------------------------|----------------------------------------|-----------------------------|-------------|
| Bloc 1 | T-NAV-01 | Accès à la page d’accueil                | `/bibliothecaire/`                     | Code 200 + template accueil | ✅ Validé    |
| Bloc 1 | T-NAV-02 | Accès à la liste des médias              | `/bibliothecaire/media/`               | Code 200 + template liste   | ✅ Validé    |
| Bloc 1 | T-NAV-03 | Accès au détail d’un média existant      | `/bibliothecaire/media/1/`             | Code 200 + template détail  | ✅ Validé    |
| Bloc 1 | T-NAV-04 | Accès à un média inexistant              | `/bibliothecaire/media/999/`           | Code 404                    | ✅ Validé    |
| Bloc 2 | T-NAV-05 | Accès à la liste des médias consultables | `/bibliothecaire/medias/consultables/` | Code 200 + template liste   | ✅ Validé    |
| Bloc 2 | T-NAV-06 | Accès à la liste des médias disponibles  | `/bibliothecaire/medias/disponibles/`  | Code 200 + template liste   | 🔄 À tester |


> ❌ Le test T-NAV-03 a révélé une contrainte sur le champ `annee_edition` du modèle `Media`. ✅ Il a été repris après correction du modèle de données.  
> 🔧 La correction a été intégrée et documentée dans [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](Modelisation_correction-erreurs-suite-tests-unitaires.md).  
> 📌 Aucun point technique à noter dans la main-courante pour la série du **Bloc 1**.

---

### 📚 Entités (`T-ENT-xxx`)

| Série  | ID Test  | Description                                                     | Modèle testé    | Résultat attendu                                                        | Statut      |
|--------|----------|-----------------------------------------------------------------|-----------------|-------------------------------------------------------------------------|-------------|
| Bloc 1 | T-ENT-01 | Création d’un `Media` non typé (création minimaliste)           | `Media`         | Attributs cohérents (`titre`, `media_type`, `theme`, etc.)              | ✅ Validé    |
| Bloc 1 | T-ENT-02 | Vérification des attributs par défaut                           | `Media`         | `consultable=True`, `disponible=True`                                   | ✅ Validé    |
| Bloc 1 | T-ENT-03 | Vérification des attributs accessibles selon le typage          | `Media`         | Champs spécifiques (`auteur`, `resume`, etc.) absents si non typé       | ✅ Validé    |
| Bloc 1 | T-ENT-04 | Vérification du typage multi-table et de la structure en base   | `Media → Livre` | `Media.count() == 2`, `Livre.count() == 1`, `Livre.pk == Media.pk`      | ✅ Validé    |
| Bloc 2 | T-ENT-05 | Vérification de tous les objets affichés ont `consultable=True` | `Media`         | `consultable=True` pour une sélection de `Media`                        | ✅ Validé    |
| Bloc 2 | T-ENT-06 | Vérifie que tous les objets affichés ont `disponible=True`      | `Media`         | `disponible=True` (et `consultable=True`) pour une sélection de `Media` | 🔄 À tester |

> ✅ Les tests T-ENT-xx sont validés.  
> ✅ Les assertions couvrent la structure multi-table, les attributs hérités et typés, et la cohérence des enregistrements.  
> 🔧 Les corrections de modélisation ont été intégrées et documentées dans [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](Modelisation_correction-erreurs-suite-tests-unitaires.md).  
> 📌 Aucun point technique à noter dans la main-courante pour la série du **Bloc 1**.

---

### 🧪 Vues (`T-VUE-xxx`)

| Série  | ID Test  | Vue testée                 | Description                                                 | Résultat attendu                              | Statut      |
|--------|----------|----------------------------|-------------------------------------------------------------|-----------------------------------------------|-------------|
| Bloc 1 | T-VUE-01 | `MediaListView`            | Affichage des titres                                        | Présence dans le HTML                         | ✅ Validé    |
| Bloc 1 | T-VUE-02 | `MediaListView`            | Affichage du type et disponibilité                          | Présence dans le HTML                         | ✅ Validé    |
| Bloc 1 | T-VUE-03 | `MediaDetailView`          | Affichage des champs spécifiques du sous-type               | Présence de `auteur`, `resume`, etc. si typé  | ✅ Validé    |
| Bloc 1 | T-VUE-04 | `MediaDetailView`          | Utilisation de l’objet typé dans le contexte                | Instance héritée (`Livre`, `Dvd`, `Cd`) reçue | ✅ Validé    |
| Bloc 1 | T-VUE-05 | `MediaDetailView`          | Affichage d’un objet non typé malgré `media_type` défini    | Absence des champs spécifiques dans le HTML   | ✅ Ajouté    |
| Bloc 2 | T-VUE-06 | `MediaListConsultableView` | Le titre <`h2`> du template correspond à la vue consultable | Présence dans le HTML                         | ✅ Validé    |
| Bloc 2 | T-VUE-07 | `MediaDisponibleListView`  | Le titre <`h2`> du template correspond à la vue disponibles | Présence dans le HTML                         | 🔄 À tester |

> ✅ La distinction entre typage réel et simple valeur `media_type` est désormais testée.  
> ✅ La logique de typage dynamique est assurée par la surcharge de `get_object()` dans `MediaDetailView`.  
> 📌 Le test `T-VUE-05` confirme que `media_type="LIVRE"` ne suffit pas sans sous-type instancié.

---

### 🧪 Administration (`T-ADM-xxx`)

| Série  | ID Test  | Description                                                                 | Cible                         | Résultat attendu                                           | Statut   |
|--------|----------|-----------------------------------------------------------------------------|-------------------------------|------------------------------------------------------------|----------|
| Bloc 1 | T-ADM-01 | Accès à l’interface admin et aux apps exposées (`/admin/{app_label}/`)      | `admin:index` + apps exposées | Code 200 pour chaque URL                                   | ✅ Validé |
| Bloc 1 | T-ADM-02 | Vérification des URLs admin selon les permissions déclarées dans ModelAdmin | `ModelAdmin` exposés          | Code 200 pour chaque vue autorisée (`add`, `change`, etc.) | ✅ Validé |

> 🔧 Les tests utilisent `RequestFactory` pour simuler une requête authentifiée (`mock_request`) et éviter les erreurs liées à `self.client.request()`.  
> ✅ Le test T-ADM-02 est dynamique : il s’adapte aux permissions et à la présence d’objets pour chaque modèle.  
> 📌 Le modèle `Media` est exposé en lecture seule, ce qui est pris en compte dans le test.

---

### 🧪 Fonctionnel (`T-FUN-xxx`)

| Série  | ID Test  | Description                                                                     | Résultat attendu                                                                 | Statut      |
|--------|----------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-------------|
| Bloc 2 | T-FUN-01 | Vérifie que la vue consultable respecte les règles métier définies (UC-LIST-01) | Code 200 + template (T-NAV-05), Booléen vrai (T-ENT-05), Contenu HTML (T-VUE-06) | ✅ Validé    |
| Bloc 2 | T-FUN-02 | Vérifie que la vue disponibles respecte les règles métier définies (UC-LIST-02) | Code 200 + template (T-NAV-06), Booléen vrai (T-ENT-06), Contenu HTML (T-VUE-07) | 🔄 À tester |

> 🔧 Les tests unitaires _fonctionnels_ sont définis pour être autonome. Ils peuvent se rapprocher de tests unitaires _techniques_ qui sont indiqués dans le _résultat attendu_. 
> Pour une facilité de développement et de maintenance, ils sont regroupés dans une classe de tests fonctionnels et techniques.  
> 🔹 Cette organisation permet de valider chaque UC dans une classe dédiée, tout en conservant la granularité des tests techniques pour le diagnostic.

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

> ℹ️ Note : pour obtenir les résultats en redirigeant la sortie vers un fichier `test_report.txt`, il faut aussi rediger le canal de sortie d'erreur (canal 2) vers le canal standard (canal 1).
> 
> Cette redirection permet de capturer les messages de test affichés dans le terminal, qui sont parfois envoyés sur le canal d’erreur (stderr) par Django ou les frameworks de test. 
> Pour une analyse structurée, il faut utiliser `--verbosity=2` ou `--verbosity=3` selon le niveau de détail souhaité.

> La commande dans le terminal est :
> 
> ```bash
> python manage.py test bibliothecaire --verbosity=2 > test_report.txt 2>&1
> ```

---

## 🔹 5. Couverture attendue

| Niveau de couverture | Description                                            |
|----------------------|--------------------------------------------------------|
| Minimum              | 1 test par vue (liste, détail, accueil)                |
| Étendu               | Tests de contenu, modèle, navigation                   |
| Futur                | Tests de création, modification, suppression, filtrage |

---

## 🔹 6. Liens vers les fichiers de test

| Fichier                     | Fonctionnalité ciblée                                            | Catégorie      |
|-----------------------------|------------------------------------------------------------------|----------------|
| `test_urls.py`              | Routage et accès (URLs locales)                                  | Navigation     |
| `test_entites_media.py`     | Modèle `Media` et sous-types                                     | Entités        |
| `test_vues_media_detail.py` | Détail d’un média typé                                           | Vues           |
| `test_vues_media_list.py`   | Liste des médias                                                 | Vues           |
| `test_admin.py`             | Interface d’administration                                       | Administration |
| `test_uc_list_media.py`     | Cas d’usage UC-LIST-01 et UC-LIST-02 (consultables, disponibles) | Fonctionnel    |

---

## 🔹 7. Évolutivité du plan

Ce plan est conçu pour être enrichi au fil du développement :

- Ajout de tests pour les vues `CreateView`, `UpdateView`, `DeleteView`
- Ajout de tests pour les entités `Emprunt`, `Membre`, `JeuDePlateau`
- Ajout de tests de permissions, formulaires, erreurs, filtrage

---

## 🔹 8. Références

- [Main courante – Étape 5](_Frontend-main-courante.md)
- [Issue #3 – Développement de l’application bibliothécaire](https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version/issues/3)
- [Django Testing Best Practices – CodezUp](https://codezup.com/django-testing-best-practices-unit-tests-integration-tests/)
- [Writing Scalable Unit Tests in Django – Dev.to](https://dev.to/shreyash_jhon_doe/writing-scalable-maintainable-unit-tests-in-django-a-practical-guide-with-real-examples-47a4)

---
