# 🛠️ Suivi du développement – Projet Médiathèque Django

Ce document centralise le suivi des **issues**, des **branches**, et des **étapes de développement** du projet Django de gestion de médiathèque.

---

## 🧭 Sommaire

- [📌 Objectifs](#-objectifs)
- [📋 Issues traitées](#-issues-traitées)
- [🧪 Branches](#-branches)
- [📂 Historique des commits](#-historique-des-commits)
- [📎 Liens vers la documentation](#-liens-vers-la-documentation)

---

## 📌 Objectifs

- Documenter les tâches réalisées et à venir  
- Suivre l’évolution du projet par branche et par issue  
- Faciliter la relecture pédagogique ou technique  

---

## 📋 Issues traitées

### Version initiale du Plan de développement

| Numéro | Branche associée | Description                              | Statut         |
|--------|------------------|------------------------------------------|----------------|
| #1     | MonLucCo/issue1  | Préparation de l’environnement           | ✅ Clôturée     |
| #2     | MonLucCo/issue2  | Initialisation du projet Django          | 🚧 À engager   |
| #3     | À définir        | Modélisation des entités                 | ⏳ À venir      |
| #4     | À définir        | Développement des vues et logique métier | ⏳ À venir      |
| #5     | À définir        | Interfaces utilisateur et templates      | ⏳ À venir      |
| #6     | À définir        | Tests et validation                      | ⏳ À venir      |
| #7     | À définir        | Rapport final et livraison               | ⏳ À venir      |

### Version en cours du plan de développement

| Issue | Parent) | Branche associée | Titre de l’issue                                               | Objectif              | Statut          |
|-------|---------|------------------|----------------------------------------------------------------|-----------------------|-----------------|
| #1    |         | MonLucCo/issue1  | Préparation de l’environnement                                 | Projet                | ✅ Clôturée      |
| #2    |         | MonLucCo/issue2  | Initialisation du projet et configuration centrale             | Django, `mediatheque` | 🚧 À engager    |
| #3    |         | MonLucCo/issue3  | Développement de l’application fonctionnelle bibliothécaire    | Métier `bibliotheque` | ⏳ À venir       |
| #4    |         | MonLucCo/issue4  | Développement de l’application fonctionnelle membre            | Métier `membre`       | ⏳ À venir       |
| #5    |         | MonLucCo/issue5  | Authentification, autorisation et sécurité                     | Couche `mediatheque`  | ⏳ À venir       |
| #6    |         | MonLucCo/issue6  | Tests et validation                                            | Application           | ⏳ À venir       |
| #7    |         | MonLucCo/issue7  | Rapport final et livraison                                     | Projet                | ⏳ À venir       |
| #12   | #1      | MonLucCo/issue12 | Actualisation de la documentation et réorganisation des issues | Projet                | ✅ Clôturée      |


> 🔗 [Voir les issues sur GitHub](https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version/issues)

---

## 🧪 Branches

- `main` : branche stable  
- `MonLucCo/issueX` : branches de développement liées aux issues  

---

## 📂 Historique des commits

Utiliser la commande suivante pour afficher un historique condensé :

```bash
git log --oneline
```

Ou bien consulter directement l’interface GitHub pour une vue détaillée des commits.

---

## 📎 Liens vers la documentation

- [README principal du projet](../../README.md)
- [README général de la documentation](../README.md)
- [Suivi du développement](../developpement/README-dev.md)
- [Architecture du projet](../architecture/README-archi.md)
- [Spécifications fonctionnelles](../fonctionnel/README-fonct.md)  
- [Documentation technique](../technique/README-tech.md)
- [Rapport de projet](../../delivery/rapport/rapport-projet.md)

---
