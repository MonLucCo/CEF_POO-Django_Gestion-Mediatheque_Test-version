"""
models.py – Définitions des entités métier de l’application Médiathèque.

Ce fichier ne contient que la structure des modèles (champs, relations,
énumérations et méthodes simples). Toute logique métier plus complexe
(transactionnalité, blocage automatique, calculs dérivés lourds…) sera
implémentée dans les vues ou services de l’app.

Ce module définit les entités métier de la médiathèque, avec :
- les objets consultables et empruntables (Support, Media, Livre, Dvd, Cd, JeuDePlateau).
- le modèle utilisateur (Membre, Bibliothécaire).
- le service d’emprunt (Emprunt) et ses statuts.

Les règles métier détaillées (cardinalité des prêts, durées, blocages, etc.)
sont documentées dans le rapport de projet (Annexe A).
"""

from django.db import models

# ── 0. Enumérations ────────────────────────────────────────────────────────────

class StatutEmprunt(models.IntegerChoices):
    """
    Enumération des statuts possibles pour un emprunt.
    """
    RETARD   = 0, 'En retard'
    EN_COURS = 1, 'En cours'
    RENDU    = 2, 'Rendu'


# ── 1. Objets ─────────────────────────────────────────────────────────────────

class Support(models.Model):
    """
    Abstraction de tout élément consultable dans la médiathèque.

    Attributs :
      - titre         : string, max_length=100
      - annee_edition : integer, >= 0
      - consultable   : booléen, True si visible en catalogue
    """
    titre         = models.CharField(max_length=100)
    annee_edition = models.PositiveIntegerField()
    consultable   = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Media(Support):
    """
    Support empruntable : héritier de Support.

    Attributs :
      - disponible  : booléen, True si non prêté
      - theme       : string, max_length=200
      - media_type  : choix parmi ['LIVRE','DVD','CD']
    """
    disponible   = models.BooleanField(default=True)
    theme        = models.CharField(max_length=200)
    TYPE_CHOICES = [
        ('LIVRE', 'Livre'),
        ('DVD',   'DVD'),
        ('CD',    'CD'),
    ]
    media_type   = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.titre} ({self.media_type})"


class Livre(Media):
    """
    Média de type livre.

    Attributs :
      - auteur  : string, max_length=100
      - nb_page : integer, >= 0
      - resume  : string, max_length=200
    """
    auteur   = models.CharField(max_length=100)
    nb_page  = models.PositiveIntegerField()
    resume   = models.CharField(max_length=200)


class Dvd(Media):
    """
    Média de type DVD.

    Attributs :
      - realisateur : string, max_length=100
      - duree       : integer, >= 0 (minutes)
      - histoire    : string, max_length=200
    """
    realisateur = models.CharField(max_length=100)
    duree       = models.PositiveIntegerField()
    histoire    = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'DVD'
        verbose_name_plural = "DVDs"

class Cd(Media):
    """
    Média de type CD audio.

    Attributs :
      - artiste      : string, max_length=100
      - nb_piste     : integer, >= 1
      - duree_ecoute : integer, >= 0 (minutes)
    """
    artiste      = models.CharField(max_length=100)
    nb_piste     = models.PositiveIntegerField(default=1)
    duree_ecoute = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'CD'
        verbose_name_plural = "CDs"


class JeuDePlateau(Support):
    """
    Jeu de plateau uniquement consultable, non empruntable.

    Attributs :
      - createur           : string, max_length=100
      - regle_consultable  : booléen, True si la règle est disponible
      - categorie          : string, max_length=100
      - duree_partie       : integer, durée moyenne en minutes
      - nb_joueur_min      : integer, nombre minimal de joueurs
      - nb_joueur_max      : integer, nombre maximal de joueurs
      - age_min            : integer, âge minimal recommandé
    """
    createur          = models.CharField(max_length=100)
    regle_consultable = models.BooleanField(default=False)
    categorie         = models.CharField(max_length=100, default="Non classé")
    duree_partie      = models.PositiveIntegerField(default=30)
    nb_joueur_min     = models.PositiveIntegerField(default=2)
    nb_joueur_max     = models.PositiveIntegerField(default=4)
    age_min           = models.PositiveIntegerField(default=8)

    def __str__(self):
        return f"{self.titre} (Jeu créé par {self.createur}) - ({self.categorie}, {self.nb_joueur_min}-{self.nb_joueur_max} joueurs)"

    class Meta:
        verbose_name_plural = "jeux de plateau"

# ── 2. Utilisateurs ───────────────────────────────────────────────────────────

class Utilisateur(models.Model):
    """
    Abstraction de toute personne utilisant la médiathèque.

    Attributs :
      - nom : string, max_length=100
    """
    nom = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Membre(Utilisateur):
    """
    Membre habilité à emprunter des médias.

    Attributs :
      - compte : string, identifiant unique, max_length=50
      - bloque : booléen, True si compte temporairement suspendu
    Constantes :
      - MAX_EMPRUNTS : nombre maximal d’emprunts simultanés
      - MAX_RETARDS : nombre maximal de retards autorisés (0 = aucun)
    Propriétés :
      - nb_emprunts_en_cours
      - nb_retards
    Méthodes :
      - peut_emprunter()
    """
    MAX_EMPRUNTS = 3
    MAX_RETARDS = 0

    compte = models.CharField(max_length=50, unique=True)
    bloque = models.BooleanField(default=False)

    @property
    def nb_emprunts_en_cours(self):
        """
        Nombre d’emprunts actuellement en cours (statut=EN_COURS).
        """
        return self.emprunts.filter(statut=StatutEmprunt.EN_COURS).count()

    @property
    def nb_retards(self):
        """
        Nombre d’emprunts actuellement en retard (statut=RETARD).
        """
        return self.emprunts.filter(statut=StatutEmprunt.RETARD).count()

    def peut_emprunter(self):
        """
        Indique si le membre peut initier un nouveau prêt.
        Conditions :
          - moins de MAX_EMPRUNTS emprunts actifs
          - correspond au retard autorisé
        """
        return (
                (self.nb_emprunts_en_cours < self.MAX_EMPRUNTS)
                and (self.nb_retards == self.MAX_RETARDS)
                )

    def __str__(self):
        etat = 'Bloqué' if self.bloque else 'Actif'
        return (
            f"{self.nom} ({self.compte}) "
            f"[{etat}] Emprunts : {self.nb_emprunts_en_cours}/{self.MAX_EMPRUNTS}"
        )


class Bibliothecaire(Utilisateur):
    """
    Profil métier du bibliothécaire.

    **Placeholder** : Authentification et autorisations gérées via Django Auth (issue #5).
    """
    pass


# ── 3. Services d'emprunt──────────────────────────────────────────────────────

class Emprunt(models.Model):
    """
    Enregistrement d’un prêt de média.

    **Statut** géré par `StatutEmprunt`.
    Les changements de statut impactent la disponibilité du média.
    """
    media      = models.ForeignKey(
        Media,
        on_delete=models.CASCADE,
        related_name='emprunts'
    )
    emprunteur = models.ForeignKey(
        Membre,
        on_delete=models.CASCADE,
        related_name='emprunts'
    )
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour  = models.DateField(null=True, blank=True)
    statut       = models.IntegerField(
        choices=StatutEmprunt.choices,
        default=StatutEmprunt.EN_COURS
    )

    def __str__(self):
        return f"{self.emprunteur} → {self.media} [{self.statut}]"

# ──────────────────────────────────────────────────────────────────────────────