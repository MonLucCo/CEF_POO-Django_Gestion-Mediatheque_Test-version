# 📘 Analyse du Modèle – Issue #3 – Application Fonctionnelle Bibliothécaire

Ce document retrace l’analyse complète menée pour définir le modèle de données de l’application `bibliothecaire`. Il servira de base pour la mise à jour du rapport dans la branche `MonLucCo/issue3/update-rapport`.

---

## 1. Analyse du code existant

Le fichier *Code à reprendre_Sujet.pdf* propose un ensemble de classes Python rudimentaires :

```python
class livre():
    name = ""
    auteur = ""
    dateEmprunt = ""
    disponible = ""
    emprunteur = ""

class dvd():
    name = ""
    realisateur = ""

class cd():
    name = ""
    artiste = ""

class jeuDePlateau():
    name = ""
    createur = ""

class Emprunteur():
    name = ""
    bloque = ""
```

### ❌ Limites identifiées :
- Pas de structure Django (`models.Model`)
- Pas d’héritage entre les types de médias
- Champs non typés, non persistants
- Pas d'utilisation des conventions de nommage de classe (majuscule en début de nom)
- Pas de gestion des relations (ForeignKey)
- Pas de logique métier intégrée (blocage, limite d’emprunt, etc.)
- Pas de validation métier ou de contraintes d’intégrité
- Pas de séparation des responsabilités (modèle, vue, logique métier)

---

## 2. Étapes d’analyse vers le modèle final

### 2.1 Lecture des spécifications

D’après *Sujet-Devoir12_POO avec Python.pdf*, les exigences sont :

- Deux applications distinctes :
  - `bibliothecaire` : gestion complète (CRUD, emprunts, retours)
  - `consultation` : accès libre à la liste des supports
- Types d’objets :
  - Livres, CDs, DVDs → empruntables
  - Jeux de plateau → consultables uniquement
- Rôles :
  - Bibliothécaire : accès sécurisé
  - Membre : accès libre, emprunteur potentiel

### 2.2 Clarification des termes ambigus

| Terme              | Interprétation                                       |
|--------------------|------------------------------------------------------|
| **Support**        | Classe mère abstraite de tous les objets             |
| **Media**          | Sous-classe de `Support`, empruntable                |
| **JeuDePlateau**   | Sous-classe de `Support`, non empruntable            |
| **Utilisateur**    | Classe mère abstraite des personnes                  |
| **Membre**         | Utilisateur avec un `compte`, accès à `consultation` |
| **Bibliothecaire** | Utilisateur avec un `pass`, accès à `bibliothecaire` |

### 2.3 Proposition du modèle conceptuel

#### 📦 Objets

```python
class Support(models.Model):
    titre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Media(Support):
    class Meta:
        abstract = True

class Livre(Media):
    auteur = models.CharField(max_length=100)

class Dvd(Media):
    realisateur = models.CharField(max_length=100)

class Cd(Media):
    artiste = models.CharField(max_length=100)

class JeuDePlateau(Support):
    createur = models.CharField(max_length=100)
```

#### 👤 Utilisateurs

```python
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Membre(Utilisateur):
    compte = models.CharField(max_length=50, unique=True)
    bloque = models.BooleanField(default=False)

class Bibliothecaire(Utilisateur):
    pass_id = models.CharField(max_length=50, unique=True)
```

#### 🔧 Services

```python
class Service(models.Model):
    class Meta:
        abstract = True

class Emprunt(Service):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Membre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=20, choices=[('en_cours', 'En cours'), ('rendu', 'Rendu'), ('retard', 'En retard')])
```

### 2.4 Évolutions du modèle final

- La classe abstraite `Service`, initialement prévue pour regrouper les services comme `Emprunt`, a été retirée du code final car aucun autre service n’est demandé dans le périmètre fonctionnel. Elle reste documentée ici pour faciliter une extension future (ex. : Réservation, Prolongation).

- Une entité d’énumération `StatutEmprunt` a été introduite pour remplacer les chaînes de caractères codées en dur dans le champ `statut` de la classe `Emprunt`. Ce choix permet :
  - une centralisation des valeurs autorisées,
  - un emploi de ces valeurs entre plusieurs entités,
  - une meilleure lisibilité du code,
  - une facilité de maintenance si les statuts évoluent.

- Le champ `media_type` défini dans `Media`, utilise une liste de choix (`TYPE_CHOICES`) définie localement. Bien que cette liste soit interne à la classe, elle pourrait être externalisée dans une énumération dédiée si :
  - les types deviennent dynamiques ou configurables,
  - les valeurs sont utilisés dans plusieurs entités,
  - des règles métier spécifiques s’appliquent à chaque type.
  Pour l’instant, le maintien dans l'entité `Media` est jugé suffisant et plus simple à maintenir.

---

## 3. Validation par les critères du sujet

### 3.1 Mise en place de la POO (6 pts)

| Critère                              | Évaluation                      |
|--------------------------------------|---------------------------------|
| Normes du langage                    | ✅ Respectées                    |
| Séparation Django                    | ✅ `models.py`, `views.py`, etc. |
| Connexion BD sécurisée               | ⚠️ À prévoir si BD distante     |
| Héritage Livre/DVD/CD                | ✅ Via `Media`                   |
| Modèle Media + JeuDePlateau + Membre | ✅ Conforme                      |

### 3.2 Fonctionnalités (9 pts)

| Fonction                   | Couverture |
|----------------------------|------------|
| CRUD Membre                | ✅          |
| CRUD Média                 | ✅          |
| Emprunt / Retour           | ✅          |
| Liste des supports         | ✅          |
| Accès libre à consultation | ✅          |

### 3.3 Projet (5 pts)

| Élément         | Évaluation   |
|-----------------|--------------|
| Log             | ⚠️ À prévoir |
| Tests unitaires | ✅ Prévus     |
| Rapport         | ✅ Structuré  |

### ✅ Tableau de conformité

| Section         | Points visés   | Couverture |
|-----------------|----------------|------------|
| POO             | 6              | ✅ 5.5 à 6  |
| Fonctionnalités | 9              | ✅ 9        |
| Projet          | 5              | ✅ 4.5 à 5  |

---

## 4. Conclusion : adaptabilité du modèle

Le modèle proposé est :

- **Extensible** : ajout de nouveaux services ou types de supports sans modifier la base
- **Modulaire** : séparation claire entre objets, utilisateurs et services
- **Conforme** : respecte les spécifications et les critères d’évaluation
- **Évolutif** : permet d’ajouter des rôles, des règles métier, des interfaces spécifiques

Ce modèle constitue une base solide pour le développement des applications `bibliothecaire` et `consultation`.

---
