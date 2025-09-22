# 📋 Spécifications fonctionnelles – Médiathèque Django

Ce document présente une vue synthétique des fonctionnalités attendues et implémentées (ou à venir) dans le projet Django de gestion de médiathèque. Il s’appuie sur les spécifications pédagogiques du CEF et sur les choix d’architecture du projet.
Pour une analyse métier complète, se référer à [`Analyse_Fonctionnalites.md`](Analyse_Fonctionnalites.md).

Les fonctionnalités sont organisées selon trois pôles :
- `membre` : consultation et accès public au catalogue
- `bibliothecaire` : gestion des emprunts, retours, membres
- `accueil` : redirection et gestion des comptes

Chaque fonctionnalité est associée à un rôle utilisateur (`visiteur`, `membre`, `bibliothécaire`) et à une logique métier définie dans les modèles (`Media`, `Emprunt`, `Membre`, etc.).

---

## 🧭 Sommaire

1. [Objectifs fonctionnels](#1-objectifs-fonctionnels)  
2. [Segmentation des rôles et des pôles](#2-segmentation-des-rôles-et-des-pôles)
3. [Fonctionnalités validées](#3-fonctionnalités-validées-étape-4)  
4. [Fonctionnalités à implémenter](#4-fonctionnalités-à-implémenter-étape-5)  
5. [Couverture par les issues](#5-couverture-par-les-issues)
6. [Liens vers les documents associés](#6-liens-vers-les-documents-associés)

---

## 1. Objectifs fonctionnels

L’application doit permettre :

- La **consultation du catalogue** par tout utilisateur
- L’**emprunt et le retour de médias** par les membres
- La **gestion des membres et des emprunts** par les bibliothécaires
- Le **blocage automatique** des membres en cas de retard ou dépassement de quota
- La **navigation sécurisée** selon les rôles

> 📎 Voir aussi : [`Analyse_Fonctionnalites.md`](Analyse_Fonctionnalites.md) pour le détail des cas d’usage et des règles métier.

---

## 2. Segmentation des rôles et des pôles

| Pôle             | Rôle utilisateur  | Accès / Fonction                       |
|------------------|-------------------|----------------------------------------|
| `consultation`   | Visiteur / Membre | Consultation du catalogue              |
| `bibliothecaire` | Bibliothécaire    | Gestion des emprunts, retours, membres |
| `accueil`        | Tous              | Redirection, login, accueil            |
| `mediatheque`    | Technique         | Routage, configuration, modèles        |

---

## 3. Fonctionnalités validées (étape 4)

| Fonctionnalité               | Statut | Étape   | Document associé             |
|------------------------------|--------|---------|------------------------------|
| Consultation du catalogue    | ✅      | Étape 4 | `_Admin-main-courante.md`    |
| Visualisation des emprunts   | ✅      | Étape 4 | idem                         |
| Affichage des membres        | ✅      | Étape 4 | idem                         |
| Blocage manuel d’un membre   | ✅      | Étape 4 | `models.py_indexH-final.txt` |
| Typage des statuts d’emprunt | ✅      | Étape 4 | idem                         |

---

## 4. Fonctionnalités à implémenter (étape 5+)

| Fonctionnalité                | Statut | Étape prévue | Document associé             |
|-------------------------------|--------|--------------|------------------------------|
| Emprunt d’un média            | 🕒     | Étape 5      | `_Frontend-main-courante.md` |
| Retour d’un média             | 🕒     | Étape 5      | idem                         |
| Blocage automatique           | ⏳      | Étape 6      | `tests.py` (à venir)         |
| Calcul du statut d’un emprunt | ⏳      | Étape 6      | idem                         |
| Consultation publique         | ⏳      | Étape 7      | à créer                      |
| Accès restreint selon rôle    | ⏳      | Étape 7      | à créer                      |

---

## 5. Couverture par les issues

| Issue | Description                   | Fonctionnalités couvertes              |
|-------|-------------------------------|----------------------------------------|
| #1    | Initialisation du projet      | —                                      |
| #2    | Installation et configuration | —                                      |
| #3    | Développement fonctionnel     | Toutes les fonctionnalités métier      |
| #12   | Réorganisation documentaire   | Mise à jour des documents fonctionnels |

---

## 6. Liens vers les documents associés

- [`_Admin-main-courante.md`](../developpement/issue3/task4/_Admin-main-courante.md)
- [`_Frontend-main-courante.md`](../developpement/issue3/task5/_Frontend-main-courante.md)
- [`models.py_indexH.txt`](../developpement/issue3/task1/models.py_indexH.txt)
- [`Analyse-initial_data.md`](../developpement/issue3/task2/Analyse-initial_data.md)
- [`Analyse_Fonctionnalites.md`](Analyse_Fonctionnalites.md)

