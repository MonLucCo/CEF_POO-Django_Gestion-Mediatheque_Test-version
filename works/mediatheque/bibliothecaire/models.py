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
from django.apps import apps
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

# ── 0. Commun : Enumérations ────────────────────────────────────────────────────────────

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
      - name         : string, max_length=100
      - annee_edition : integer, >= 0 ou laisser vide
      - consultable   : booléen, True si visible en catalogue
    """
    name         = models.CharField(max_length=100)
    annee_edition = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Année d'édition si connue. Sinon laisser vide."
    )
    consultable   = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Media(Support):
    """
    Support empruntable : héritier de Support.

    Représente un média générique pouvant être typé (Livre, DVD, CD) ou laissé non typé.
    Permet la consultation et l’emprunt via l’interface bibliothécaire.

    Attributs :
      - disponible   : booléen, True si le média est disponible à l’emprunt
      - theme        : string, thème ou catégorie du média
      - media_type   : string, choix parmi ['NON_DEFINI', 'LIVRE', 'DVD', 'CD']
                       Définit le type déclaré du média, sans garantir l’instanciation réelle du sous-type.

    Méthodes :
      - __str__()             : Affiche le nom et le type déclaré du média.
      - is_typed()            : Retourne True si un sous-type réel est instancié (Livre, DVD ou CD).
      - get_real_instance()   : Retourne l’instance réelle du sous-type si elle existe, sinon l’objet Media lui-même.

    Remarques :
      - Le champ media_type est utilisé pour l’affichage et les filtres, mais ne garantit pas la présence d’un sous-type.
      - La méthode get_real_instance() permet d’accéder aux attributs spécifiques du type réel sans dépendre de la vue.
    """
    disponible   = models.BooleanField(default=False)
    theme        = models.CharField(max_length=200)
    TYPE_CHOICES = [
        ('NON_DEFINI', 'Non défini'),
        ('LIVRE', 'Livre'),
        ('DVD',   'DVD'),
        ('CD',    'CD'),
    ]
    media_type   = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        default='NON_DEFINI',
        help_text="Type de média. 'NON_DEFINI' si aucun sous-type n'est instancié."
    )

    def __str__(self):
        return f"{self.name} ({self.media_type})"

    def is_typed(self):
        return hasattr(self, 'livre') or hasattr(self, 'dvd') or hasattr(self, 'cd')

    def is_typage_incomplete(self):
        return self.media_type != 'NON_DEFINI' and not self.is_typed()

    def get_real_instance(self):
        if hasattr(self, 'livre'):
            return self.livre
        elif hasattr(self, 'dvd'):
            return self.dvd
        elif hasattr(self, 'cd'):
            return self.cd
        return self

    def mutate_to_typed(self):
        if self.media_type == 'NON_DEFINI':
            raise ValidationError("Impossible de muter un média sans type défini.")

        model_name = self.media_type.capitalize()  # 'LIVRE' → 'Livre'
        TypedModel = apps.get_model('bibliothecaire', model_name)

        # Vérifie si l'objet typé existe déjà
        if TypedModel.objects.filter(pk=self.pk).exists():
            return TypedModel.objects.get(pk=self.pk)

        return TypedModel.objects.create(
                id=self.pk,
                name=self.name,
                annee_edition=self.annee_edition,
                consultable=self.consultable,       # Issue du média non typé, donc 'non consultable'
                disponible=True,                    # Objet typé, donc 'disponible'
                theme=self.theme,
                media_type=self.media_type,
            )

    def get_update_url_name(self):
        valid_types = [key for key, _ in self.TYPE_CHOICES if key != 'NON_DEFINI']
        if self.media_type in valid_types:
            return f'bibliothecaire:media_update_{self.media_type.lower()}'
        return 'bibliothecaire:media_update'    

    def get_typage_url_name(self):
        valid_types = [key for key, _ in self.TYPE_CHOICES if key != 'NON_DEFINI']
        if self.media_type in valid_types:
            return f'bibliothecaire:media_typage_{self.media_type.lower()}'
        return 'bibliothecaire:media_update'


class Livre(Media):
    """
    Média de type livre.

    Attributs :
      - auteur  : string, max_length=100
      - nb_page : integer, >= 1
      - resume  : string, max_length=200
    """
    auteur   = models.CharField(max_length=100)
    nb_page  = models.PositiveIntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1)],
        help_text="Nombre de pages (au moins une), ou laisser vide."
    )
    resume   = models.CharField(max_length=200)

    @staticmethod
    def get_specific_fields():
        return ['auteur', 'nb_page', 'resume']


class Dvd(Media):
    """
    Média de type DVD.

    Attributs :
      - realisateur : string, max_length=100
      - duree       : integer, >= 1 (minutes)
      - histoire    : string, max_length=200
    """
    realisateur = models.CharField(max_length=100)
    duree       = models.PositiveIntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1)],
        help_text="Durée en minute (au moins une), ou laisser vide."
    )
    histoire    = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'DVD'
        verbose_name_plural = "DVDs"

    @staticmethod
    def get_specific_fields():
        return ['realisateur', 'duree', 'histoire']


class Cd(Media):
    """
    Média de type CD audio.

    Attributs :
      - artiste      : string, max_length=100
      - nb_piste     : integer, >= 1
      - duree_ecoute : integer, >= 0 (minutes)
    """
    artiste      = models.CharField(max_length=100)
    nb_piste     = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Nombre de pistes (au moins une)."
    )
    duree_ecoute = models.PositiveIntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1)],
        help_text="Durée d'écoute en minute (au moins une), ou laisser vide."
    )

    class Meta:
        verbose_name = 'CD'
        verbose_name_plural = "CDs"

    @staticmethod
    def get_specific_fields():
        return ['artiste', 'nb_piste', 'duree_ecoute']


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
        return f"{self.name} (Jeu créé par {self.createur}) - ({self.categorie}, {self.nb_joueur_min}-{self.nb_joueur_max} joueurs)"

    class Meta:
        verbose_name_plural = "jeux de plateau"


# ── 2. Utilisateurs ───────────────────────────────────────────────────────────

class Utilisateur(models.Model):
    """
    Abstraction de toute personne utilisant la médiathèque.

    Attributs :
      - name : string, max_length=100
    """
    name = models.CharField(max_length=100)

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
            f"{self.name} ({self.compte}) "
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