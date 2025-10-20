# 📋 Spécifications fonctionnelles – Projet Médiathèque Django

Ce document décrit les **fonctionnalités attendues**, les **cas d’usage**, et les **règles métier** du projet de gestion de médiathèque développé avec Django.

Les documents suivants le complète :
- [`README-fonct.md`](README-fonct.md) en détaillant les fonctionnalités indépendamment des étapes de développement.
- [`Analyse_Fonctionnalites_Bibliothecaire.md` (version courante)](../developpement/issue3/task6/Analyse_Fonctionnalites_Bibliothecaire.md) 
en précisant les cas d'usage fonctionnels relatifs aux Bibliothécaires :
  - version figée pour les Médias seuls en version **index G-10** [`Analyse_Fonctionnalites_Bibliothecaire.md` (version Medias seuls)](../developpement/issue3/task5/Analyse_Fonctionnalites_Bibliothecaire_indexG-10.md).

---

## 🧭 Sommaire

1. [🎯 Objectif](#-1-objectif)
2. [🧩 Fonctionnalités prévues](#-2-fonctionnalités-prévues)
3. [👥 Cas d’usage](#-3-cas-dusage)
4. [📌 Contraintes](#-4-contraintes)
5. [📎 Liens utiles](#-5-liens-utiles)

---

## 🎯 1. Objectif

Développer une application web permettant la gestion des ressources d’une médiathèque :
- Livres, CD, DVD
- Usagers
- Emprunts et retours

L’application doit être simple, intuitive et adaptée à un usage pédagogique.

---

## 🧩 2. Fonctionnalités prévues

### 🔹 2.1 Gestion des ressources
- Ajout, modification, suppression de livres, CD, DVD
- Classification par type, thème, auteur
- Gestion de la disponibilité
- Gestion de l'emprunt
- Gestion du blocage d'emprunt
- Gestion du retour d'emprunt
- Gestion de la consultabilité

### 🔹 2.2 Gestion des usagers
- Création de comptes usagers (membres)
- Suivi des emprunts et retours
- Historique des interactions

### 🔹 2.3 Emprunts
- Enregistrement d’un emprunt
- Détection des retards
- Retour de ressource

### 🔹 2.4 Interfaces
- Interface d’administration Django
- Interface utilisateur simplifiée (HTML/CSS)

---

## 👥 3. Cas d’usage

- Un usager emprunte un livre et le retourne
- Un gestionnaire affiche la liste des membres
- Un gestionnaire crée un membre-emprunteur
- Un gestionnaire met à jour la fiche d'un membre
- Un gestionnaire supprime un membre
- Un gestionnaire affiche la liste des médias
- Un gestionnaire crée un emprunt pour un média disponible
- Un gestionnaire ajoute un média
- Un gestionnaire rentre un emprunt
- Un usager consulte la liste des médias (les supports consultables)
- Un administrateur consulte l'historique des Logs

Souhaité :
- Un administrateur ajoute une nouvelle ressource
- Un usager consulte un historique d'emprunt
- Un gestionnaire vérifie les ressources disponibles

---

## 📌 4. Contraintes

- Base de données locale (SQLite)
- Un test (au moins et sans erreurs) par fonctionnalité
- Authentification simple
- Application mono-utilisateur en local
- Respect des bonnes pratiques Django/POO

---

## 📎 5. Liens utiles

- [README principal du projet](../../README.md)
- [README général de la documentation](../README.md)
- [Spécifications techniques](../technique/README-tech.md)
- [Suivi du développement](../developpement/README-dev.md)
- [Architecture du projet](../architecture/README-archi.md)

---
