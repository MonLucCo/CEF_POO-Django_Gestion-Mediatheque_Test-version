# 🔄 Analyse du cycle de vie métier – Profil Bibliothécaire

📁 `/docs/fonctionnel/Analyse_LifeCycle_Bibliothecaire.md`  
📌 Version : index H-1  
🧩 Sujet : synthèse des états métier et des interactions entre les entités `Media`, `Membre`, et `Emprunt` dans le 
cadre du profil Bibliothécaire.

---

## 🧭 Sommaire

1. [Objectif du document](#1-objectif-du-document)  
2. [Schémas de référence](#2-schémas-de-référence)  
3. [Vecteurs de contexte](#3-vecteurs-de-contexte)  
   - [3.1 Media](#31-media)  
   - [3.2 Membre](#32-membre)  
   - [3.3 Emprunt](#33-emprunt)  
4. [Typologie des transitions](#4-typologie-des-transitions)  
5. [Interactions entre entités](#5-interactions-entre-entités)  
6. [Règles DDM (Modèle Dérivé des Données)](#6-règles-ddm-modèle-dérivé-des-données)  
7. [Références croisées](#7-références-croisées)  

---

## 1. Objectif du document

Ce document formalise les **états métier**, **vecteurs de contexte**, et **transitions** des principales entités 
manipulées par le profil Bibliothécaire.  
Il constitue une synthèse transversale des documents spécialisés :
- [`Analyse_LifeCycle_Medias.md`](Analyse_LifeCycle_Medias.md)
- [`Analyse_LifeCycle_Membres.md`](Analyse_LifeCycle_Membres.md)
- [`Analyse_LifeCycle_Emprunts.md`](Analyse_LifeCycle_Emprunts.md)

---

## 2. Schémas de référence

Le cycle de vie métier du profil Bibliothécaire pour les entités `Media`, `Membre` et `Emprunt` a été développée avec 
les notions métier clés indiquées dans le tableau suivant avec leurs définitions opérationnelles et des mots-clés utiles 
pour approfondir les recherches.

| Notion métier                       | Définition opérationnelle                                                                 | Mots-clés de recherche recommandés                   |
|-------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------|
| **État**                            | Situation stable ou transitoire d’une entité métier (`Media`, `Membre`, `Emprunt`)        | `django model state`, `état métier`, `FSM`           |
| **Transition**                      | Passage d’un état à un autre, déclenché par une action ou une condition                   | `django transition`, `state change`, `FSM`           |
| **Vecteur de contexte**             | Ensemble structuré de composantes métier décrivant l’état d’une entité à un instant donné | `domain model`, `context vector`, `DDD entity`       |
| **Machine d’état (FSM)**            | Abstraction permettant de modéliser les états et transitions d’un système                 | `finite state machine`, `statechart`, `FSM`          |
| **DDM (Modèle Dérivé des Données)** | Ensemble de règles qui évaluent automatiquement des états ou transitions                  | `computed field`, `derived state`, `django property` |

La figure suivante constitue le socle visuel du cycle de vie du profil Bibliothécaire.

![img.png](img_LifeCycle_Bibliothecaire.png)

Elles présentent :
- Les états stables et initiaux des entités
- Les transitions typées (saisie, fonction métier, DDM)
- Les vecteurs de contexte codés
- Les interactions croisées entre `Media`, `Membre`, et `Emprunt`

> 🔸 Les couleurs des transitions :  
> 🟩 Verte = saisie utilisateur  
> 🟧 Orange = fonction métier  
> ⬜ Grise = calcul automatisé (DDM)

> 🔸 Les formes des états :  
> ◼ Rectangle = état stable  
> ◿ Rectangle arrondi = état initial  
> ⬭ Ovoïde bordé = état final ou masqué

La recherche de la cohérence du cycle de vie de chaque entité s'est traduite par l'identification d'une représentation 
simplifiée dans un tableau spécifique à chaque entité avec sa situation amont et aval de chaque état.

Pour l'entité Media :
![img.png](img_LifeCycle_TableauMedia.png)

Pour l'entité Membre
![img.png](img_LifeCycle_tableauMembre.png)

Pour l'entité Emprunt
![img.png](img_LifeCycle_TableauEmprunt.png)

---

## 3. Vecteurs de contexte

### 3.1 Media

| Composante | Signification métier                     | Type       |
|------------|------------------------------------------|------------|
| `C`        | consultable (`True` / `False`)           | booléen    |
| `D`        | disponible (`True` / `False`)            | booléen    |
| `T`        | typage réel (`Livre`, `Dvd`, `Cd`, etc.) | catégoriel |

---

### 3.2 Membre

| Composante | Signification métier                          | Type       |
|------------|-----------------------------------------------|------------|
| `S`        | suspendu (`True` / `False`)                   | booléen    |
| `A`        | abonné (`True` / `False`)                     | booléen    |
| `I`        | inscrit à un emprunt en cours                 | booléen    |
| `Q`        | quota d’emprunt disponible                    | entier     |
| `R`        | retour enregistré (`True` / `False`)          | booléen    |

---

### 3.3 Emprunt

| Composante | Signification métier                       | Type           | Source |
|------------|--------------------------------------------|----------------|--------|
| `sE`       | statut d’emprunt valide (`True` / `False`) | booléen dérivé | DDM    |
| `dE`       | date d’emprunt valide (`True` / `False`)   | booléen dérivé | DDM    |
| `dR`       | date de retour valide (`True` / `False`)   | booléen dérivé | DDM    |

---

## 4. Typologie des transitions

| Couleur   | Type de transition      | Déclencheur                     |
|-----------|-------------------------|---------------------------------|
| 🟩 Verte  | Saisie utilisateur      | Formulaire ou action directe    |
| 🟧 Orange | Fonction métier         | Vue métier ou logique métier    |
| ⬜ Grise   | Calcul automatisé (DDM) | Condition métier ou état croisé |

---

## 5. Interactions entre entités

### 5.1 Media → Emprunt

- Un média doit être `consultable=True` et `disponible=True` pour être emprunté.
- La transition `EmpruntCreateView` vérifie ces conditions via `sE`.

### 5.2 Emprunt → Membre

- La création d’un emprunt modifie le vecteur `[I/Q]` du membre.
- Le retour d’un emprunt modifie `R`, et peut lever une suspension (`S=False`).

### 5.3 Membre → Media

- Un membre suspendu ne peut pas emprunter → bloque la transition `T:3-4` (emprunt).
- Le retour d’un emprunt peut rendre le média `disponible=True` via `T:4-3`.

---

## 6. Règles DDM (Modèle Dérivé des Données)

| Règle ID | Condition déclencheuse                         | Action métier déclenchée   |
|----------|------------------------------------------------|----------------------------|
| DDM-01   | `dR > date_retour_prevue`                      | `statut_emprunt = RETARD`  |
| DDM-02   | `statut_emprunt = RETARD`                      | `membre.suspendu = True`   |
| DDM-03   | `membre.retard_en_cours = False`               | `membre.suspendu = False`  |
| DDM-04   | `media.consultable = False`                    | `media.disponible = False` |
| DDM-05   | `media.disponible = False` and `emprunt.rendu` | `media.disponible = True`  |

---

## 7. Références croisées

- [`Analyse_LifeCycle_Medias.md`](Analyse_LifeCycle_Medias.md)
- [`Analyse_LifeCycle_Membres.md`](Analyse_LifeCycle_Membres.md)
- [`Analyse_LifeCycle_Emprunts.md`](Analyse_LifeCycle_Emprunts.md)
- [`Analyse_Fonctionnalites_Bibliothecaire.md`](Analyse_Fonctionnalites_Bibliothecaire.md)
- [`tests-plan.md`](tests-plan.md)

---

