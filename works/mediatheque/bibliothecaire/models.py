"""
models.py – Définitions des entités métier de l’application Médiathèque.

Ce fichier ne contient que la structure des modèles (champs, relations,
énumérations et méthodes simples). Toute logique métier plus complexe
(transactionnalité, blocage automatique, calculs dérivés lourds…) sera
implémentée dans les vues ou services de l’app.

Ce module définit les entités métier de la médiathèque, avec :
- les objets gérés (Support, Media, Livre, Dvd, Cd, JeuDePlateau).
- le modèle utilisateur (Membre, Bibliothécaire).
- le service d’emprunt (Emprunt) et ses statuts.

Les règles métier détaillées (cardinalité des prêts, durées, blocages, etc.)
sont documentées dans le rapport de projet (Annexe A).
"""
import warnings
from datetime import timedelta, date

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


class StatutMembre(models.IntegerChoices):
    """
    Enumération des statuts possibles pour un membre.
    """
    MEMBRE     = 0, 'Non abonné'
    EMPRUNTEUR = 1, 'Abonné'
    ARCHIVE    = 2, 'Supprimé'


# ── 1. Objets ─────────────────────────────────────────────────────────────────

class Support(models.Model):
    """
    Abstraction de tout élément consultable dans la médiathèque.

    Attributs :
      - name         : string, max_length=100
      - annee_edition : integer, >= 0 ou laisser vide
      - consultable   : booléen, True si visible en catalogue

    Propriété :
      - is_consultable : Retourne True si le Support est consultable

    Méthodes :
      - count_total()                   : Méthode de classe, compteur du nombre d'enregistrements.
    """
    name         = models.CharField(max_length=100)
    annee_edition = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Année d'édition si connue. Sinon laisser vide."
    )
    consultable   = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @classmethod
    def count_total(cls):
        return cls.objects.count()

    @property
    def is_consultable(self):
        return self.consultable

class Media(Support):
    """
    Support empruntable : héritier de Support.

    Représente un média générique pouvant être typé (Livre, DVD, CD) ou laissé non typé.
    Permet la consultation et l’emprunt via l’interface bibliothécaire.

    Attributs :
      - disponible   : booléen, True si le média est disponible à l’emprunt
      - theme        : string, thème ou catégorie du média
      - media_type   : string, choix parmi ['NON_DEFINI', 'LIVRE', 'DVD', 'CD']

    Propriétés
      - is_disponible   : Retourne True si le média est disponible.
      - is_consultable  : Retourne True si le média est visible en catalogue.
      - est_empruntable : Retourne True si le média est empruntable.
      - est_archivable  : Retourne True si le média est archivable.
      - est_emprunte    : Retourne True si le média est emprunté.
      - est_archive     : Retourne True si le média est archivé.

    Méthodes :
      - __str__()                       : Affiche le nom et le type déclaré du média.
      - count_total()                   : Méthode de classe (héritée), compteur du nombre d'enregistrements.
      - count_empruntes()               : Méthode de classe, compteur du nombre de médias empruntés.
      - count_retards()                 : Méthode de classe, compteur du nombre de médias empruntés en retard.
      - is_typed()                      : Retourne True si un sous-type réel est instancié (Livre, DVD ou CD).
      - is_typage_incomplete()          : Retourne True si `media_type` est défini, mais aucun sous-type instancié.
      - get_real_instance()             : Retourne l’instance réelle du sous-type si elle existe, sinon l’objet Media lui-même.
      - mutate_to_typed()               : Crée dynamiquement le sous-type à partir du `media_type`.
      - get_update_url_name()           : Retourne le nom de route Django pour la mise à jour selon le type.
      - get_typage_url_name()           : Retourne le nom de route Django pour le typage selon le type.
      - get_emprunt_actif()             : Retourne l'emprunt actif (EN_COURS ou RETARD) associé à ce média. Si aucun emprunt, retourne `None`.
      - rendre_disponible(force=False)  : Rend le média disponible s’il est typé. Si déjà disponible, ne fait rien sauf si `force=True`.

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
        consulte = 'Hors gestion' if not self.is_consultable else 'En gestion'
        disponible = 'Disponible' if self.is_disponible else 'Indisponible'
        return f"{self.name} ({self.media_type}) [{consulte} - {disponible}]"

    @classmethod
    def count_empruntes(cls):
        return Emprunt.objects.filter(
            media__in=cls.objects.all(),
            statut__in=[StatutEmprunt.EN_COURS, StatutEmprunt.RETARD]
        ).count()

    @classmethod
    def count_retards(cls):
        return Emprunt.objects.filter(media__in=cls.objects.all(), statut=StatutEmprunt.RETARD).count()

    @property
    def is_disponible(self):
        return self.disponible

    def is_typed(self):
        return hasattr(self, 'livre') or hasattr(self, 'dvd') or hasattr(self, 'cd')

    def is_typage_incomplete(self):
        return self.media_type != 'NON_DEFINI' and not self.is_typed()

    @property
    def est_empruntable(self):
        return self.is_typed() and self.is_consultable and self.is_disponible

    @property
    def est_archivable(self):
        return self.is_typed() and not self.is_consultable and self.is_disponible

    @property
    def est_emprunte(self):
        return self.is_typed() and self.is_consultable and not self.is_disponible

    @property
    def est_archive(self):
        return self.is_typed() and not self.is_consultable and not self.is_disponible

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

    def rendre_disponible(self, force=False):
        """
        Rend le média disponible s’il est typé.
        - Si déjà disponible, ne fait rien sauf si `force=True`.
        - Retourne True si le média a été modifié.
        """
        if not self.is_typed():
            warnings.warn(f"Le média '{self}' n'est pas typé. Aucun changement de disponibilité effectué.")
            return False
        if self.is_disponible and not force:
            warnings.warn(f"Le média '{self}' est déjà disponible. Aucun changement de disponibilité effectué.")
            return False
        if force:
            warnings.warn(f"Le média '{self}' est forcé à être disponible.")
        self.disponible = True
        self.save()
        return True

    def get_emprunt_actif(self):
        """
        Retourne l’emprunt actif (EN_COURS ou RETARD) associé à ce média.
        Si aucun emprunt actif, retourne None.
        """
        return self.emprunts.filter(statut__in=[StatutEmprunt.EN_COURS, StatutEmprunt.RETARD]).first()


class Livre(Media):
    """
    Média de type livre.

    Attributs :
      - auteur  : string, max_length=100
      - nb_page : integer, >= 1
      - resume  : string, max_length=200

    Méthodes :
      - count_total()   : Méthode de classe (héritée), Compteur du nombre d'enregistrements.
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

    Méthodes :
      - count_total()           : Méthode de classe (héritée), Compteur du nombre d'enregistrements.
      - get_specific_fields()   : Retourne la liste des champs spécifiques.
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

    @classmethod
    def count_total(cls):
        return cls.objects.count()


class Cd(Media):
    """
    Média de type CD audio.

    Attributs :
      - artiste      : string, max_length=100
      - nb_piste     : integer, >= 1
      - duree_ecoute : integer, >= 0 (minutes)

    Méthodes :
      - count_total()           : Méthode de classe (héritée), Compteur du nombre d'enregistrements.
      - get_specific_fields()   : Retourne la liste des champs spécifiques.
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

    Méthodes :
      - count_total()           : Méthode de classe, compteur du nombre total d'enregistrements
      - get_specific_fields()   : Retourne la liste des champs spécifiques.
    """
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    @classmethod
    def count_total(cls):
        return cls.objects.count()


class Membre(Utilisateur):
    """
    Membre habilité à emprunter des médias.

    Attributs :
      - compte : string, identifiant unique, max_length=50
      - statut : entier, défini par l'enum StatutMembre (MEMBRE, EMPRUNTEUR, ARCHIVE)

    Constantes :
      - MAX_EMPRUNTS : nombre maximal d’emprunts simultanés autorisés
      - MIN_EMPRUNTS : borne minimale (toujours 0)
      - MAX_RETARDS  : nombre maximal de retards autorisés (0 = aucun)
      - MIN_RETARDS  : borne minimale (toujours 0)

    Propriétés :
      - nb_emprunts_en_cours    : entier ≥ 0, nombre d’emprunts actifs (EN_COURS ou RETARD)
      - nb_retards              : entier ≥ 0, nombre d’emprunts en retard
      - is_membre               : True si statut == MEMBRE
      - is_emprunteur           : True si statut == EMPRUNTEUR
      - is_supprime             : True si statut == ARCHIVE
      - is_retard               : True si nb_retards > MAX_RETARDS
      - is_max_emprunt          : True si nb_emprunts_en_cours == MAX_EMPRUNTS
      - is_min_emprunt          : True si nb_emprunts_en_cours == MIN_EMPRUNTS
      - nb_emprunts_en_cours    : Nombre d’emprunts actifs (`EN_COURS` ou `RETARD`)
      - nb_retards              : Nombre d’emprunts en retard

    Méthodes :
      - generer_compte(nom_utilisateur) : Méthode de classe, génère un identifiant unique basé sur le nom et l’année
      - count_total()                   : Méthode de classe (héritée), compteur du nombre total d'enregistrements
      - count_emprunteur()              : méthode de classe, compteur du nombre de membres-emprunteurs
      - peut_emprunter()                : Retourne True si le membre est autorisé à emprunter selon les règles métier
      - peut_etre_supprime()            : Retourne True si le membre peut être supprimé logiquement
      - activer_emprunteur()            : Active le statut emprunteur si le membre est standard
      - supprimer_membre_emprunteur()   : Supprime logiquement le membre (statut = ARCHIVE)
      - get_emprunts_actifs()           : Retourne les emprunts actifs (EN_COURS ou RETARD) associés à ce membre. Si aucun emprunt, retourne `None`.


    Remarques :
      - Les propriétés d’état permettent une lecture métier directe dans les vues et les templates.
      - Les compteurs sont toujours des entiers positifs ou nuls, calculés dynamiquement.
    """
    MAX_EMPRUNTS = 3
    MIN_EMPRUNTS = 0
    MAX_RETARDS = 0
    MIN_RETARDS = 0

    compte = models.CharField(max_length=50, unique=True)
    statut = models.IntegerField(
        choices=StatutMembre.choices,
        default=StatutMembre.MEMBRE
    )

    @classmethod
    def generer_compte(cls, nom_utilisateur: str) -> str:
        from datetime import datetime
        annee = datetime.now().year
        nom_tronque = nom_utilisateur.strip().replace(" ", "_")[:30]
        prefixe = f"{annee}_{nom_tronque}_"
        compteur = cls.objects.filter(compte__startswith=prefixe).count() + 1
        return f"{prefixe}{compteur}"

    @classmethod
    def count_emprunteurs(cls):
        return cls.objects.filter(statut=StatutMembre.EMPRUNTEUR).count()

    @classmethod
    def count_supprimes(cls):
        return cls.objects.filter(statut=StatutMembre.ARCHIVE).count()

    @property
    def is_membre(self):
        return self.statut == StatutMembre.MEMBRE

    @property
    def is_emprunteur(self):
        return self.statut == StatutMembre.EMPRUNTEUR

    @property
    def is_supprime(self):
        return self.statut == StatutMembre.ARCHIVE

    @property
    def is_retard(self):
        return self.nb_retards > self.MAX_RETARDS

    @property
    def is_max_emprunt(self):
        return self.nb_emprunts_en_cours == self.MAX_EMPRUNTS

    @property
    def is_min_emprunt(self):
        return self.nb_emprunts_en_cours == self.MIN_EMPRUNTS

    @property
    def nb_emprunts_en_cours(self) -> int:
        """
        Nombre d’emprunts actuellement en cours (statut=EN_COURS).
        """
        return self.emprunts.filter(statut__in=[StatutEmprunt.EN_COURS, StatutEmprunt.RETARD]).count()

    @property
    def nb_retards(self) -> int:
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
          - le membre est abonné
        """
        return (
                self.is_emprunteur
                and not ( self.is_max_emprunt or self.is_retard )
                )

    def peut_etre_supprime(self):
        return self.is_min_emprunt and not self.is_supprime

    def __str__(self):
        statut_label = StatutMembre(self.statut).label
        retour = 'Retard' if self.is_retard else 'À jour'
        quota = f"{self.nb_emprunts_en_cours}/{self.MAX_EMPRUNTS}"
        return f"{self.name} ({self.compte}) [{statut_label}] – Emprunts : {quota} – {retour}"

    def activer_emprunteur(self):
        """
        Active le statut emprunteur si le membre est standard.
        Retourne True si la transition a été effectuée.
        """
        if self.is_membre:
            self.statut = StatutMembre.EMPRUNTEUR
            self.save()
            return self.is_emprunteur
        return False

    def supprimer_membre_emprunteur(self):
        """
        Supprime (suppression logique) le membre (standard ou emprunteur) de la gestion.
        Retourne True si la transition a été effectuée.
        """
        if self.peut_etre_supprime():
            self.statut = StatutMembre.ARCHIVE
            self.save()
            return self.is_supprime
        return False

    def get_emprunts_actifs(self):
        """
        Retourne les emprunts actifs (EN_COURS ou RETARD) associés à ce membre.
        Si aucun emprunt actif, retourne None.
        """
        return self.emprunts.filter(statut__in=[StatutEmprunt.EN_COURS, StatutEmprunt.RETARD])


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

    Attributs :
    - media         : Media, média emprunté
    - emprunteur    : Membre, membre emprunteur
    - date_emprunt  : date, date de début du prêt
    - date_retour   : date, date de retour du média
    - statut        : int, définit par l'enum `StatutEmprunt` (`EN_COURS`, `RETARD`, `RENDU`)

    Constantes :
    - `DELAI_EMPRUNT = 7` → Durée standard d’un emprunt en jours

    Propriétés :
    - date_retour_prevu : Date prévue du retour (calculée dynamiquement avec DELAI_EMPRUNT)
    - est_en_retard     : Retourne True si l’emprunt est en retard par rapport à `date_retour_prevu`
    - est_non_rendu      : Retourne True si l'emprunt est à rendre

    Méthodes :
    - count_total()         : Méthode de classe, compteur du nombre total d'enregistrements
    - count_en_cours()      : Méthode de classe, compteur du nombre d'emprunts non-rendus et dans les délais (en cours)
    - count_en_retard()     : Méthode de classe, compteur du nombre d'emprunts non-rendus et hors délais (en retard)
    - enregistrer_retour()  : Retourne True si : média rendu disponible vérifié, puis met à jour la date, le statut, et la disponibilité
    - marquer_retard()      : Méthode de classe, parcourt les emprunts en cours et marque ceux en retard

    """
    DELAI_EMPRUNT = 7 #jours

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
    # ⚠️ Non modifiable, même en interface admin. Les dates personnalisées sont injectées uniquement via fixtures/tests.
    date_retour  = models.DateField(null=True, blank=True)
    statut       = models.IntegerField(
        choices=StatutEmprunt.choices,
        default=StatutEmprunt.EN_COURS
    )

    def __str__(self):
        return f"{self.emprunteur} → {self.media} [{self.statut}]"

    @classmethod
    def count_total(cls):
        return cls.objects.count()

    @classmethod
    def count_en_cours(cls):
        return cls.objects.filter(statut=StatutEmprunt.EN_COURS).count()

    @classmethod
    def count_en_retard(cls):
        return cls.objects.filter(statut=StatutEmprunt.RETARD).count()

    @property
    def date_retour_prevu(self):
        """
        Calcule la date de retour prévue : date_emprunt + DELAI_EMPRUNT.
        """
        return self.date_emprunt + timedelta(days=self.DELAI_EMPRUNT)

    @property
    def est_en_retard(self):
        """
        Retourne True si l’emprunt est en retard par rapport à la date prévue.
        """
        return self.statut == StatutEmprunt.EN_COURS and self.date_retour_prevu < date.today()

    @property
    def est_a_rendre(self):
        """
        Retourne True si l’emprunt est à rendre.
        """
        return self.statut != StatutEmprunt.RENDU

    def enregistrer_retour(self):
        """
        Enregistre le retour du média :
        - vérifie que le média est bien à rendre
        - met à jour la date de retour
        - change le statut en RENDU
        - rend le média disponible
        """
        if not self.media.rendre_disponible():
            warnings.warn(f"Le média '{self.media}' ne peut pas être rendu disponible.")
            return False
        self.date_retour = date.today()
        self.statut = StatutEmprunt.RENDU
        self.save()
        return True

    @classmethod
    def marquer_retard(cls):
        """
        Parcourt les emprunts en cours et marque ceux en retard.
        Retourne un dictionnaire structuré pour exploitation métier.
        """
        aujourd_hui = date.today()
        date_seuil_retard = aujourd_hui - timedelta(days=cls.DELAI_EMPRUNT)

        emprunts_en_cours = list(cls.objects.filter(statut=StatutEmprunt.EN_COURS))
        emprunts_marques = []

        for emprunt in emprunts_en_cours:
            if emprunt.est_en_retard:
                emprunt.statut = StatutEmprunt.RETARD
                emprunt.save()
                emprunts_marques.append(emprunt)

        nb = len(emprunts_marques)
        if nb > 0:
            date_premier_retard = emprunts_marques[0].date_retour_prevu
            date_dernier_retard = emprunts_marques[-1].date_retour_prevu
        else:
            date_premier_retard = None
            date_dernier_retard = None

        message = {
            "tag": "success" if nb > 0 else "warning",
            "text": (f"{nb} emprunt{'s' if nb != 1 else ''} marqué{'s' if nb != 1 else ''} comme en retard."
                     if nb > 0 else "Aucun emprunt marqué comme en retard")
        }

        return {
            "date_du_jour": aujourd_hui,
            "date_seuil_retard": date_seuil_retard,
            "date_premier_retard": date_premier_retard,
            "date_dernier_retard": date_dernier_retard,
            "emprunts_en_cours": emprunts_en_cours,
            "emprunts_marques": emprunts_marques,
            "message": message
        }

# ──────────────────────────────────────────────────────────────────────────────