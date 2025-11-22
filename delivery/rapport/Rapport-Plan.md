# Rapport de projet – Application Médiathèque Django

## 1. Introduction
1.1. Contexte et objectifs du devoir
1.2. Enjeux pédagogiques (POO, composants serveurs, tests…)
1.3. Présentation générale du livrable (repo GitHub, rapport MD → PDF)

## 2. Reprise et refactoring du code existant
2.1. Analyse du code fourni
2.2. Erreurs identifiées et correctifs appliqués
2.3. Refactoring POO :
  - Hiérarchie des classes (Media, Livre, CD, DVD, JeuDePlateau)
  - Séparation en modules Django (`models.py`, `views.py`, `urls.py`, `tests.py`)
2.4. Justification des choix de conception

## 3. Architecture du projet et mise en place
3.1. Organisation des dossiers (`works/`, `docs/`, `delivery/`)
3.2. Initialisation du dépôt et gestion des branches/issues
3.3. Environnement de développement (venv, dépendances…)
3.4. Couches de l’application Médiathèque
  – settings.py (DB, langue, timezone)
  – couches de l'application médiathèque (centrale, fonctionnelles, admin)
  – routage global et résolution multi-couche (routage et templates)

## 4. Implémentation des fonctionnalités
4.1. Application bibliothécaire
  - Création, lecture, mise à jour, suppression de membres
  - Gestion des médias (CRU[D])
  - Emprunts et retours (contrainte 3 emprunts max, délais, retards)
  - Gestion des jeux
4.2. Application consultation (consultation des supports)
4.3. Contraintes métier respectées (exclusion jeux de plateau, blocage emprunteur en retard)
4.4. Authentification et gestion des rôles
  - Logique connexion/déconnexion
  - Redirection selon le rôle
  - Protection des vues
  - Principes des tests de permissions

## 5. Qualité du code et stratégie de tests
5.1. Logs et monitorage (configuration du logging)
5.2. Tests unitaires Django :
  - 1 test minimum par fonctionnalité
  - Couverture et exemples de résultats
5.3. Exécution automatisée des tests (CI/CD stub)

## 6. Base de données et données de test
6.1. Schéma des modèles et migration
6.2. Jeu de données via fixtures ou script
6.3. Exemple d’insertion et requêtes de vérification

## 7. Mode d’installation et d’exécution
7.1. Prérequis (Python, pip, venv…)
7.2. Commandes pas à pas pour n’importe quelle machine
7.3. URL d’accès et description des interfaces

## 8. Démarche de travail et traçabilité
8.1. Workflow GitHub (issues #1→#7, branches, PR)
8.2. Table de traçabilité des exigences
8.3. Difficultés rencontrées et leçons apprises

## 9. Conclusion et perspectives
9.1. Bilan des compétences acquises
9.2. Améliorations futures (webservices, asynchrone, UI, internationalisation)

## Annexes
- A. Extraits de code avant/après
- B. Logs d’exécution et de tests
- C. Diagrammes (UML, séquence)
- D. Arborescence du projet
- E. Installation Projet et configuration de l'EDI
