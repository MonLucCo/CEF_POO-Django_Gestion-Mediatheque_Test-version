# 📋 Spécifications fonctionnelles – Projet Médiathèque Django

Ce document décrit les **fonctionnalités attendues**, les **cas d’usage**, et les **règles métier** du projet de gestion de médiathèque développé avec Django.

---

## 🧭 Sommaire

- [🎯 Objectif](#-objectif)
- [🧩 Fonctionnalités prévues](#-fonctionnalités-prévues)
- [👥 Cas d’usage](#-cas-dusage)
- [📌 Contraintes](#-contraintes)
- [📎 Liens utiles](#-liens-utiles)

---

## 🎯 Objectif

Développer une application web permettant la gestion des ressources d’une médiathèque :
- Livres, CD, DVD
- Usagers
- Emprunts et retours

L’application doit être simple, intuitive et adaptée à un usage pédagogique.

---

## 🧩 Fonctionnalités prévues

### 🔹 Gestion des ressources
- Ajout, modification, suppression de livres, CD, DVD
- Classification par type, genre, auteur

### 🔹 Gestion des usagers
- Création de comptes usagers
- Suivi des emprunts et retours
- Historique des interactions

### 🔹 Emprunts
- Enregistrement d’un emprunt
- Détection des retards
- Retour de ressource

### 🔹 Interfaces
- Interface d’administration Django
- Interface utilisateur simplifiée (HTML/CSS)

---

## 👥 Cas d’usage

- Un usager emprunte un livre et le retourne
- Un administrateur ajoute une nouvelle ressource
- Un usager consulte son historique d’emprunts
- Un gestionnaire vérifie les ressources disponibles

---

## 📌 Contraintes

- Base de données locale (SQLite)
- Authentification simple
- Application mono-utilisateur en local
- Respect des bonnes pratiques Django/POO

---

## 📎 Liens utiles

- [README principal du projet](../../README.md)
- [README général de la documentation](../README.md)
- [Spécifications techniques](../technique/README-tech.md)
- [Suivi du développement](../developpement/README-dev.md)
- [Architecture du projet](../architecture/README-archi.md)

---
