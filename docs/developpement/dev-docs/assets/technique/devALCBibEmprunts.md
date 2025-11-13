# 🔄 Analyse du cycle de vie métier – Entité Emprunt

📁 `/docs/developpement/dev-docs/devALCBibEmprunts.md`  
📌 Version : index H-3  
🧩 Sujet : formalisation des états métier et transitions de l’entité `Emprunt` dans le cadre du profil Bibliothécaire.

---

## 🧭 Sommaire

1. [Objectif du document](#1-objectif-du-document)  
2. [Vecteur de contexte – Emprunt](#2-vecteur-de-contexte--emprunt)
3. [États métier](#3-états-métier)
4. [Transitions typées](#4-transitions-typées)
5. [Règles DDM spécifiques](#5-règles-ddm-spécifiques)
6. [Références croisées](#6-références-croisées)

---

## 1. Objectif du document

Ce document décrit les états successifs d’un `Emprunt`, les transitions déclenchées par les actions métier, et les 
règles DDM associées. Il complète le document transversal de l'analyse du cycle de vie des entités de Bibliothécaire 
[`devALCBib.md`](../../devALCBib.md).

---

## 2. Vecteur de contexte – Emprunt

| Composante | Signification métier         | Type           | Valeurs typiques |
|------------|------------------------------|----------------|------------------|
| `sE`       | statut d’emprunt             | booléen dérivé | `!sE`, `sE`      |
| `dE`       | date d’emprunt enregistrée   | booléen dérivé | `!dE`, `dE`      |
| `dR`       | date de retour enregistrée   | booléen dérivé | `!dR`, `dR`      |

---

## 3. États métier

| État        | Contexte         | Signification métier             |
|-------------|------------------|----------------------------------|
| Emprunt:1   | `!sE/!dE/!dR`    | Emprunt créé – affectable        |
| Emprunt:2   | `sE/!dE/!dR`     | Emprunt demandé                  |
| Emprunt:3   | `sE/dE/!dR`      | Emprunt validé                   |
| Emprunt:4   | `sE/dE/dR`       | Emprunt rendu                    |
| Emprunt:5   | `!sE/dE/dR`      | Emprunt terminé (archivé)        |

---

## 4. Transitions typées

| Transition        | Déclencheur     | Effet sur le vecteur |
|-------------------|-----------------|----------------------|
| `Bib: +sE`        | Fonction métier | `sE = True`          |
| `DDM: +dE`        | Dérivation      | `dE = True`          |
| `Bib: +dR`        | Fonction métier | `dR = True`          |
| `DDM: -sE`        | Dérivation      | `sE = False`         |

---

## 5. Règles DDM spécifiques

- `DDM_09` : activation de l’emprunt
- `DDM_10` : validation de la date d’emprunt
- `DDM_11` : enregistrement du retour
- `DDM_12` : archivage de l’emprunt

---

## 6. Références croisées

- Analyse cycle de vie entités Bibliothécaire : [`devALCBib.md`](../../devALCBib.md)
- Analyse cycle de vie de l'entité `Media` : [`devALCMedias.md`](devALCBibMedias.md)
- Analyse cycle de vie de l'entité `Membre` : [`devALCMembres.md`](devALCBibMembres.md)
