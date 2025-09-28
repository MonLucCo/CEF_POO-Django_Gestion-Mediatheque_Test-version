# ✅ Plan de test – Bibliothécaire

Ce document constitue le plan de test unitaire et fonctionnel de l’application dédiée au profil bibliothécaire. 
Il accompagne le développement progressif des fonctionnalités définies dans l’issue #3, en particulier l’étape 5, et sert de base extensible pour les étapes suivantes et les autres issues du projet.

Il est conçu pour :
- Structurer les tests par catégorie (navigation, entités, fonctionnalités)
- Garantir une couverture minimale par vue, extensible selon les besoins
- Faciliter la lecture, la maintenance et l’enrichissement du projet
- Documenter les cas de test, les méthodes de validation et les liens techniques

📌 Version du document :  
- **Indexage** : index D-3 
- **Périmètre couvert** : entité `Media` – vues `liste` et `détail`  
- **Niveau de couverture** : tests de niveau _minimum_ à _intermédiaire_  
- **Évolutivité prévue** :
  - entité `Media` - vues `mise à jour` et `supprime` (masque pour le bibliothécaire)
  - entités `Emprunt`, `Membre`, `JeuDePlateau` et vues CRUD

📌 Ce plan de test est spécifique à l’étape 5 de l’issue #3.
Il pourra être déplacé ou indexé dans `/docs/tests/` (à créer) si une documentation globale est mise en place.

---

## 📑 Sommaire

1. [🔹 Objectifs du plan de test](#-1-objectifs-du-plan-de-test)
2. [🔹 Organisation des tests](#-2-organisation-des-tests)
3. [🔹 Cas de test (Étape 5)](#-3-cas-de-test-étape-5)
   - [🧭 Navigation (`T-NAV-xxx`)](#-navigation-t-nav-xxx)
   - [📚 Entités (`T-ENT-xxx`)](#-entités-t-ent-xxx)
   - [🧪 Vues (`T-VUE-xxx`)](#-vues-t-vue-xxx)
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

Les tests sont répartis en trois catégories :

| Catégorie  | Dossier / Fichier                           | Préfixe ID | Objectif principal                                 |
|------------|---------------------------------------------|------------|----------------------------------------------------|
| Navigation | `tests_blocs/test_urls.py`                  | `T-NAV-`   | Vérifier les accès, les routes, les redirections   |
| Entités    | `tests_blocs/test_entites_media.py`, etc.   | `T-ENT-`   | Vérifier la cohérence des modèles et des données   |
| Vues       | `tests_blocs/test_vues_media_list.py`, etc. | `T-VUE-`   | Vérifier le comportement des vues et des templates |

> Remarque : les catégories Permissions, Formulaires, Erreurs, Filtrages sont envisagées, mais n'ont pas été mises en œuvre pour cette étape du développement.

---

## 🔹 3. Cas de test (Étape 5)

### 🧭 Navigation (`T-NAV-xxx`)

| ID Test  | Description                         | URL ciblée                   | Résultat attendu            | Statut          |
|----------|-------------------------------------|------------------------------|-----------------------------|-----------------|
| T-NAV-01 | Accès à la page d’accueil           | `/bibliothecaire/`           | Code 200 + template accueil | ✅ Validé        |
| T-NAV-02 | Accès à la liste des médias         | `/bibliothecaire/media/`     | Code 200 + template liste   | ✅ Validé        |
| T-NAV-03 | Accès au détail d’un média existant | `/bibliothecaire/media/1/`   | Code 200 + template détail  | ❌ Correction BD |
| T-NAV-04 | Accès à un média inexistant         | `/bibliothecaire/media/999/` | Code 404                    | ✅ Validé        |

> ❌ Le test T-NAV-03 a révélé une contrainte sur le champ `annee_edition` du modèle `Media`. Il sera à reprendre après correction du modèle de données.  
> 🔧 La correction a été intégrée et documentée dans [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](Modelisation_correction-erreurs-suite-tests-unitaires.md).  
> 📌 Aucun point technique à noter dans la main-courante pour cette série.

---

### 📚 Entités (`T-ENT-xxx`)

| ID Test  | Description                                                   | Modèle testé    | Résultat attendu                                                   | Statut   |
|----------|---------------------------------------------------------------|-----------------|--------------------------------------------------------------------|----------|
| T-ENT-01 | Création d’un `Media` typé `Livre`                            | `Media`         | Attributs cohérents (`titre`, `media_type`, `theme`, etc.)         | ✅ Validé |
| T-ENT-02 | Vérification des attributs par défaut                         | `Media`         | `consultable=True`, `disponible=True`                              | ✅ Validé |
| T-ENT-03 | Vérification des attributs accessibles selon le typage        | `Media`         | Champs spécifiques (`auteur`, `resume`, etc.) absents si non typé  | ✅ Validé |
| T-ENT-04 | Vérification du typage multi-table et de la structure en base | `Media → Livre` | `Media.count() == 2`, `Livre.count() == 1`, `Livre.pk == Media.pk` | ✅ Validé |

> ✅ Les tests T-ENT-xx sont validés.  
> ✅ Les assertions couvrent la structure multi-table, les attributs hérités et typés, et la cohérence des enregistrements.  
> 🔧 Les corrections de modélisation ont été intégrées et documentées dans [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](Modelisation_correction-erreurs-suite-tests-unitaires.md).  
> 📌 Aucun point technique à noter dans la main-courante pour cette série.

---

### 🧪 Vues (`T-VUE-xxx`)

| ID Test   | Vue testée        | Description                                               | Résultat attendu                                      | Statut     |
|-----------|-------------------|-----------------------------------------------------------|-------------------------------------------------------|------------|
| T-VUE-01  | `MediaListView`   | Affichage des titres                                      | Présence dans le HTML                                 | ✅ Validé  |
| T-VUE-02  | `MediaListView`   | Affichage du type et disponibilité                        | Présence dans le HTML                                 | ✅ Validé  |
| T-VUE-03  | `MediaDetailView` | Affichage des champs spécifiques du sous-type             | Présence de `auteur`, `resume`, etc. si typé          | ✅ Validé  |
| T-VUE-04  | `MediaDetailView` | Utilisation de l’objet typé dans le contexte              | Instance héritée (`Livre`, `Dvd`, `Cd`) reçue         | ✅ Validé  |
| T-VUE-05  | `MediaDetailView` | Affichage d’un objet non typé malgré `media_type` défini  | Absence des champs spécifiques dans le HTML           | ✅ Ajouté  |

> ✅ La distinction entre typage réel et simple valeur `media_type` est désormais testée.  
> ✅ La logique de typage dynamique est assurée par la surcharge de `get_object()` dans `MediaDetailView`.  
> 📌 Le test `T-VUE-05` confirme que `media_type="LIVRE"` ne suffit pas sans sous-type instancié.

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

| Fichier                     | Fonctionnalité ciblée           | Catégorie  |
|-----------------------------|---------------------------------|------------|
| `test_urls.py`              | Routage et accès (URLs locales) | Navigation |
| `test_entites_media.py`     | Modèle `Media` et sous-types    | Entités    |
| `test_vues_media_detail.py` | Détail d’un média typé          | Vues       |
| `test_vues_media_list.py`   | Liste des médias                | Vues       |



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
