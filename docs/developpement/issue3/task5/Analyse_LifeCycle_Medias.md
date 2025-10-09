# 🔄 Analyse du cycle de vie des médias

📁 `/docs/fonctionnel/Analyse_CycleLife_Medias.md`  
📌 Version : index I-1  
🧩 Sujet : formalisation des états métier et transitions du modèle `Media` (tout type)

---

🧭 **Note d’intention**

Ce document ne constitue pas un plan de test opérationnel, mais une analyse fonctionnelle du cycle de vie métier des 
objets `Media`. Il formalise les **états**, **transitions**, **rôles** et **contraintes**, et propose une segmentation 
logique des tests à prévoir.

Il est conçu comme un cadre réutilisable, indépendant du périmètre exact du projet en cours.
Il me sert de guide pour le **développement**, la **documentation**, ou l’**audit fonctionnel** pour mes applications 
Django en _programmation orientée métier_.

📌 Les tests effectivement développés sont référencés dans le fichier [`tests-plan.md`](tests-plan.md).

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

```text
Début (création)
   |=(0)=> État 1 : en attente
       <=(1)=> État 3 : empruntable
           <=(2)=> État 4 : emprunté
État 1
   <=(3)=> État 2 : hors gestion
       |=(4)=> Fin : suppression/masquage
```

### 🔹 Transitions métier

| ID  | Transition                        | Action métier                   | Acteur          | Situation initiale | Situation finale |
|:---:|-----------------------------------|---------------------------------|-----------------|:------------------:|:----------------:|
| (0) | Création                          | Création d’un média             | Bibliothécaire  |     (à créer)      |      État 1      |
| (1) | Validation / mise en consultation | Rendre le média consultable     | Bibliothécaire  |       État 1       |      État 3      |
| (1) | Gestion / mise en attente         | Rendre le média non consultable | Bibliothécaire  |       État 3       |      État 1      |
| (2) | Emprunt                           | Enregistrement d’un emprunt     | Bibliothécaire  |       État 3       |      État 4      |
| (2) | Retour                            | Fin d’un emprunt                | Membre / Biblio |       État 4       |      État 3      |
| (3) | Masquage / hors gestion           | Retirer le média de la gestion  | Bibliothécaire  |       État 1       |      État 2      |
| (3) | Masquage / hors gestion           | Remettre le média en gestion    | Bibliothécaire  |       État 2       |      État 1      |
| (4) | Suppression définitive            | Destruction du média            | Administrateur  |       État 2       |      (Fin)       |

---

## 4. Visibilité selon le profil

| Profil         | États visibles               | Accès aux transitions |
|----------------|------------------------------|-----------------------|
| Bibliothécaire | Tous les états (1 à 4 + fin) | ✅ Toutes              |
| Membre         | États 3 et 4 uniquement      | ❌ Lecture seule       |

> 🔹 Les vues et templates doivent filtrer les médias selon le profil connecté.  
> 🔹 Les membres ne doivent jamais voir les médias en attente (État 1) ni hors gestion (État 2).  
> 🔹 Les bibliothécaires peuvent visualiser tous les états, y compris les médias masqués ou en attente.

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
- Vérifier que les états métier (`Attente`, `Empruntable`, `Emprunté`, `Hors gestion`) sont correctement représentés par les combinaisons de ces deux champs
- Vérifier que les vues ne contiennent pas de médias dans un état incohérent

### 6.3 🔄 Transitions Métier

Tests simulant les changements d’état du média dans son cycle de vie :

- Passage de l’état initial (création) vers l’état "Attente"
- Validation d’un média pour le rendre "Empruntable"
- Enregistrement d’un emprunt pour passer à "Emprunté"
- Retour d’un emprunt pour revenir à "Empruntable"
- Masquage d’un média pour le passer en "Hors gestion"
- Suppression définitive depuis l’état "Hors gestion"
- Vérification des transitions interdites (ex. : emprunter un média en attente, masquer un média emprunté)

> Ces tests ne visent pas à valider uniquement les changements de champs, mais à simuler les actions métiers qui 
déclenchent ces transitions (validation, emprunt, retour, masquage, suppression).

### 6.4 🔐 Permissions

Tests vérifiant que les actions métier sont correctement restreintes :

- Seul un bibliothécaire peut modifier les états (`consultable`, `disponible`)
- Seul un administrateur peut supprimer définitivement un média
- Les actions de transition (validation, emprunt, retour, masquage) doivent être protégées par des permissions explicites
- Les formulaires et boutons d’action doivent être visibles uniquement pour les rôles autorisés

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

- [`Analyse_Fonctionnalites_Bibliothecaire.md`](Analyse_Fonctionnalites_Bibliothecaire.md)
- [`tests-plan.md`](tests-plan.md)
- [`README-dev.md`](../../README-dev.md)
- [`Modelisation_correction-erreurs-suite-tests-unitaires.md`](Modelisation_correction-erreurs-suite-tests-unitaires.md)

---
