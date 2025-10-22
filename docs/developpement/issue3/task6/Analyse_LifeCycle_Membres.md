# 🔄 Analyse du cycle de vie métier – Entité Membre

📁 `/docs/fonctionnel/Analyse_LifeCycle_Membres.md`  
📌 Version : index H-3  
🧩 Sujet : formalisation des états métier et transitions de l’entité `Membre` dans le cadre du profil Bibliothécaire.

---

## 🧭 Sommaire

1. [Objectif du document](#1-objectif-du-document)  
2. [Vecteur de contexte – Membre](#2-vecteur-de-contexte--membre)
3. [États métier](#3-états-métier)
4. [Transitions typées](#4-transitions-typées)
5. [Règles DDM spécifiques](#5-règles-ddm-spécifiques)
6. [Références croisées](#6-références-croisées)

---

## 1. Objectif du document

Ce document détaille les états successifs d’un `Membre`, les transitions déclenchées par les actions métier, et les 
règles DDM associées. Il complète le document transversal [`Analyse_LifeCycle_Bibliothecaire.md`](Analyse_LifeCycle_Bibliothecaire.md).

---

## 2. Vecteur de contexte – Membre

| Composante | Signification métier       | Type    | Valeurs typiques         |
|------------|----------------------------|---------|--------------------------|
| `S`        | supprimé (archivé)         | booléen | `!S`, `S`                |
| `A`        | abonné                     | booléen | `!A`, `A`                |
| `Q`        | quota d’emprunt disponible | entier  | `!Q`, `nQ`, `mQ`         |
| `R`        | retard constaté            | booléen | `!R`, `R`                |

> 🔸 Chaque état métier est défini par une combinaison unique de ces quatre composantes.

---

## 3. États métier

| État     | Contexte      | Signification métier                          |
|----------|---------------|-----------------------------------------------|
| Membre:1 | `!S/!A/!Q/!R` | Membre créé – non activé                      |
| Membre:2 | `!S/A/!Q/!R`  | Membre abonné – aucun emprunt                 |
| Membre:3 | `!S/A/nQ/!R`  | Membre abonné – emprunts en cours sans retard |
| Membre:4 | `!S/A/mQ/!R`  | Membre abonné – quota maximal atteint         |
| Membre:5 | `!S/A/nQ/R`   | Membre abonné – emprunts en cours avec retard |
| Membre:6 | `!S/A/mQ/R`   | Membre abonné – quota max avec retard         |
| Membre:7 | `S/!A/!Q/!R`  | Membre supprimé – aucun emprunt               |

---

## 4. Transitions typées

| Transition  | Déclencheur     | Effet sur le vecteur    |
|-------------|-----------------|-------------------------|
| `Bib: +A`   | Fonction métier | `A = True`              |
| `DDM: ±Q`   | Dérivation      | `Q = nQ` ou `mQ`        |
| `DDM: ±R`   | Dérivation      | `R = True` ou `False`   |
| `Bib: +S-A` | Fonction métier | `S = True`, `A = False` |

---

## 5. Règles DDM spécifiques

- `DDM_04` : augmentation du quota après emprunt
- `DDM_05` : diminution du quota après retour
- `DDM_06` : activation du retard (système)
- `DDM_07` : levée du retard
- `DDM_08` : suppression du membre

---

## 6. Références croisées

- [`Analyse_LifeCycle_Bibliothecaire.md`](Analyse_LifeCycle_Bibliothecaire.md)
- [`Analyse_LifeCycle_Emprunts.md`](Analyse_LifeCycle_Emprunts.md)
