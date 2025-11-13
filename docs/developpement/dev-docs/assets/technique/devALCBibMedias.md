# 🔄 Analyse du cycle de vie des médias

📁 `/docs/developpement/dev-docs/devALVBibMedias.md`  
📌 Version : index G-10  
🧩 Sujet : formalisation des états métier et transitions du modèle `Media` (tout type)

---

🧭 **Note d’intention**

Ce document ne constitue pas un plan de test opérationnel, mais une analyse fonctionnelle du cycle de vie métier des 
objets `Media`. Il formalise les **états**, **transitions**, **rôles** et **contraintes**, et propose une segmentation 
logique des tests à prévoir.

Il est conçu comme un cadre réutilisable, indépendant du périmètre exact du projet en cours.
Il me sert de guide pour le **développement**, la **documentation**, ou l’**audit fonctionnel** pour mes applications 
Django en _programmation orientée métier_.

📌 Les tests effectivement développés sont référencés dans le fichier [`devTests.md`](../../devTests.md).

📌 Ce document est conservé dans le dépôt GitHub comme référence métier durable, même si tous les tests ne sont pas 
implémentés.

---

## Sommaire

- [1. Objectif du document](#1-objectif-du-document)
- [2. États métier du média](#2-états-métier-du-média)
- [3. Cycle de vie métier](#3-cycle-de-vie-métier)
- [4. Visibilité selon le profil](#4-visibilité-selon-le-profil)
- [5. Impacts techniques](#5-impacts-techniques)
  - [5.1 🔧 Modèle](#51--modèle)
  - [5.2 🔧 Vues](#52--vues)
  - [5.3 🔧 Recommandations](#53--recommandations)
- [6. Tests à prévoir (segmentation fonctionnelle)](#6-tests-à-prévoir-segmentation-fonctionnelle)
  - [6.1 🧩 Usage Métier](#61--usage-métier)
  - [6.2 🧠 Cohérence des états](#62--cohérence-des-états)
  - [6.3 🔄 Transitions Métier](#63--transitions-métier)
  - [6.4 🔐 Permissions](#64--permissions)
  - [6.5 👥 Profils](#65--profils)
  - [6.6 🛡️ Sécurité](#66--sécurité)
- [7. Références](#7-références)

---

## 1. Objectif du document

Ce document décrit les états possibles d’un média dans la médiathèque, les transitions entre ces états, et les rôles 
des acteurs impliqués. Il formalise la logique métier implicite liée aux champs `consultable` et `disponible`, et sert 
de référence pour le développement des vues, formulaires et tests fonctionnels.

---

## 2. États métier du média

| État | `consultable` | `disponible` | Désignation métier | Description métier                                    |
|------|---------------|--------------|--------------------|-------------------------------------------------------|
| 1    | ❌             | ✅            | Attente            | Média créé, non empruntable, en attente de validation |
| 2    | ❌             | ❌            | Hors gestion       | Média masqué ou supprimé, non visible ni empruntable  |
| 3    | ✅             | ✅            | Empruntable        | Média prêt à être emprunté par les membres            |
| 4    | ✅             | ❌            | Emprunté           | Média visible mais temporairement indisponible        |

> 🔹 Ces états sont valides pour tous les types de médias (`Livre`, `Dvd`, `Cd`, etc.).  
> 🔹 Le champ `disponible` est dérivé du champ `consultable` et des actions métier.

---

## 3. Cycle de vie métier

Le _cycle de vie métier_ des médias se caractérise par un schéma d'états-transitions. Le schéma ci-dessous présente les 
états et les transitions de l'objet `Media`. La description des états et des transitions est fournies dans les 
sections suivantes.

![img.png](../images/img_LifeCycle_Medias.png)

### 🔹 États métier formalisés
Chaque état est défini par la combinaison des trois attributs : `consultable`, `disponible`, `media_type`.

| État | Notation       | Attributs                  | Description métier                             |
|------|----------------|----------------------------|------------------------------------------------|
| E:BD | `[]`           | Aucun objet en base        | État initial ou final de la base de données    |
| E:0  | `[0/0/-]`      | Media non typé             | Création initiale sans typage                  |
| E:1  | `[0/1/<type>]` | Media typé non consultable | Média typé mais non visible en catalogue       |
| E:2  | `[0/0/<type>]` | Media typé masqué          | Média retiré de la gestion                     |
| E:3  | `[1/1/<type>]` | Media typé empruntable     | Média visible et disponible                    |
| E:4  | `[1/0/<type>]` | Media typé emprunté        | Média visible mais temporairement indisponible |

> 🔹 Le champ `media_type` est obligatoire sauf en `E:0`.  
> 🔹 Les transitions sont orientées et notées `(T:x-y)` pour indiquer le passage de l’état `x` vers l’état `y`.

### 🔹 Transitions métier autorisées

| ID     | Transition                    | Description métier                             | Vue / Action technique                           |
|--------|-------------------------------|------------------------------------------------|--------------------------------------------------|
| T:BD-0 | Base → Non typé               | Création d’un média non typé                   | `MediaCreateView`                                |
| T:BD-1 | Base → Typé (non consultable) | Création d’un média typé non visible           | `Media<Type>CreateView` avec `consultable=False` |
| T:BD-3 | Base → Empruntable            | Création d’un média typé visible et disponible | `Media<Type>CreateView` avec `consultable=True`  |
| T:0-1  | Typage simple                 | Transformation d’un média non typé en typé     | `MediaTypage<Type>View`                          |
| T:0-3  | Typage complet                | Transformation directe en média empruntable    | `MediaTypage<Type>View` avec `consultable=True`  |
| T:1-2  | Masquage                      | Retrait de la gestion d’un média typé          | `MediaUpdateView` ou vue dédiée                  |
| T:1-3  | Validation                    | Mise en consultation d’un média typé           | `MediaUpdateView`                                |
| T:3-1  | Retrait temporaire            | Retrait temporaire d’un média empruntable      | `MediaUpdateView`                                |
| T:3-4  | Emprunt                       | Enregistrement d’un emprunt                    | `EmpruntCreateView`                              |
| T:4-3  | Retour                        | Fin d’un emprunt, remise en disponibilité      | `RetourUpdateView`                               |
| T:R-0  | Rollback typage               | Annulation du typage, retour à média non typé  | `MediaCancelTypingView`                          |

> 🔹 La transition `(T:R-0)` est une **transition conditionnelle**, déclenchée en parallèle d’une transition de typage 
> `(T:0-1)` ou `(T:0-3)` lors d'une demande d'annulation du **bibliothécaire**.

---

## 4. Visibilité selon le profil

| Profil         | États visibles        | Accès aux transitions autorisées    |
|----------------|-----------------------|-------------------------------------|
| Bibliothécaire | E:0 à E:4             | ✅ Toutes sauf T:2-1 (à restreindre) |
| Membre         | E:3 et E:4 uniquement | ❌ Lecture seule                     |

> 🔹 Les membres ne doivent jamais voir les médias en E:0 (non typés), E:1 (non consultables), ou E:2 (masqués - hors gestion).  
> 🔹 Les transitions de typage, rollback et masquage sont réservées au profil bibliothécaire.  
> 🔹 Les vues et templates doivent filtrer dynamiquement les médias selon le profil connecté.

---

## 5. Impacts techniques

### 5.1 🔧 Modèle
- `consultable`: booléen métier
- `disponible`: booléen dérivé ou contrôlé par les transitions

### 5.2 🔧 Vues
- `MediaListView` → filtrage selon profil
- `MediaUpdateView` → gestion des transitions métier
- `MediaDeleteView` → passage à l’état 2 ou suppression
- `MediaListHorsGestionView` → vue dédiée pour les médias en État 2 (optionnelle)

### 5.3 🔧 Recommandations

- Ne pas exposer le champ `disponible` dans les formulaires
- Gérer `disponible` automatiquement selon les transitions métier
- Documenter les transitions dans les vues et les tests
- Prévoir une interface d’administration pour les suppressions définitives
- Prévoir une vue dédiée pour les médias en État 2 (hors gestion), accessible uniquement aux bibliothécaires
- Prévoir de vérifier que les membres ne peuvent jamais accéder aux médias en État 1 ou 2.

---

## 6. Tests à prévoir (segmentation fonctionnelle)

Pour garantir la robustesse du cycle de vie des médias, les tests doivent être organisés selon six axes complémentaires :

### 6.1 🧩 Usage Métier

Tests centrés sur les cas d’usage attendus par le bibliothécaire :

- Vérifier que les vues de liste affichent les bons médias selon leur état (`consultable`, `disponible`, `media_type`)
- Vérifier que la création d’un média initialise correctement les champs (`name`, `theme`, `media_type`, etc.)
- Vérifier que les formulaires permettent la saisie des données métier sans incohérence
- Vérifier que les vues de détail affichent les champs spécifiques selon le type réel (`Livre`, `Dvd`, `Cd`)

### 6.2 🧠 Cohérence des états

Tests garantissant l’intégrité logique des champs `consultable` et `disponible` :

- Si un média est `consultable=True`, il doit être `disponible=True`
- Si un média est `consultable=False`, il doit être `disponible=False`
- Vérifier que les états métier (`Attente`, `Empruntable`, `Emprunté`, `Hors gestion`) sont correctement représentés par 
les combinaisons de ces deux champs avec le type du média (soit un contexte donné par le triplé `consultable`, `disponible`, `type`. 
- Vérifier que les vues ne contiennent pas de médias dans un état incohérent

### 6.3 🔄 Transitions Métier

Tests simulant les changements d’état du média dans son cycle de vie :

- Création d'un média non typé
- Création d'un média typé non consultable
- Création d'un média typé empruntable
- Typage simple d'un média non typé
- Typage complet d'un média non typé
- Masquage d'un média typé
- Validation d’un média (typé) pour le rendre "Empruntable"
- Emprunt d'un média typé
- Retour d’un emprunt pour revenir à "Empruntable"
- Masquage d’un média pour le passer en "Hors gestion"
- Annulation du typage en cours (rollback) 
- Suppression définitive depuis l’état "Hors gestion" (action par l'utilisateur Administrateur)
- Vérification des transitions interdites (ex. : emprunter un média en attente, masquer un média emprunté)

> Ces tests ne visent pas à valider uniquement les changements de champs, mais à simuler les actions métiers qui 
déclenchent ces transitions (validation, emprunt, retour, masquage, suppression).

### 6.4 🔐 Permissions

Tests vérifiant que les actions métier sont correctement restreintes :

- Seul un bibliothécaire peut modifier les états (`consultable`, `disponible`).
- Seul un administrateur peut supprimer définitivement un média.
- Les actions de transition (validation, emprunt, retour, masquage) doivent être protégées par des permissions explicites.
- Les formulaires et boutons d’action doivent être visibles uniquement pour les rôles autorisés.

### 6.5 👥 Profils

Tests de visibilité et d’accès selon le profil utilisateur :

- Un membre ne doit jamais voir les médias en attente ou hors gestion
- Un bibliothécaire doit pouvoir accéder à tous les états
- Les vues doivent filtrer dynamiquement les médias selon le profil connecté
- Les transitions doivent être simulées avec des utilisateurs de rôles différents

### 6.6 🛡️ Sécurité

Tests garantissant la protection contre les usages non prévus ou malveillants :

- Empêcher la modification directe des champs `disponible` via formulaire
- Vérifier que les URLs de transition ne sont pas accessibles sans authentification
- Vérifier que les transitions interdites lèvent une exception ou redirigent proprement
- Vérifier que les objets supprimés ne sont plus accessibles via leur URL

---

## 7. Références

- analyse des fonctionnalités de Bibliothécaire : [`devAFBib.md`](../../devAFBib.md)
- plan de tests du projet : [`devTests.md`](../../devTests.md)
- organisation du développement [`README-dev.md`](../../../README-dev.md)
- correction des erreurs de modélisation : [`Modelisation_correction-erreurs-suite-tests-unitaires.md` (issue3/étape 5)](Modelisation_correction-erreurs-suite-tests-unitaires.md)

- Analyse cycle de vie entités Bibliothécaire : [`devALCBib.md`](../../devALCBib.md)
- Analyse cycle de vie de l'entité `Membre` : [`devALCMembres.md`](devALCBibMembres.md)
- Analyse cycle de vie de l'entité `Emprunt` : [`devALCEmprunts.md`](devALCBibEmprunts.md)

---
