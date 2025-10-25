from django.contrib import admin
from .models import (
    #    Media,
    Livre,
    Dvd,
    Cd,
    JeuDePlateau,
    Membre,
    Bibliothecaire,
    Emprunt, Media
)

# Enregistrement avec personnalisation de l'interface d'administration
@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ['disponible', 'name', 'auteur', 'nb_page', 'theme']
    search_fields = ['name', 'auteur', 'theme']
    list_filter = ['disponible', 'theme']
    ordering = ['-disponible', 'name', 'auteur', 'theme']
    readonly_fields = ['media_type']
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'auteur', 'nb_page', 'resume')
        }),
        ('Disponibilité et classification', {
            'fields': ('disponible', 'consultable', 'media_type', 'theme', 'annee_edition')
        }),
    )

@admin.register(Dvd)
class DvdAdmin(admin.ModelAdmin):
    list_display = ['disponible', 'name', 'realisateur', 'duree', 'theme']
    search_fields = ['name', 'realisateur', 'theme']
    list_filter = ['disponible', 'theme', 'realisateur']
    ordering = ['-disponible', 'name', 'realisateur', 'duree']
    readonly_fields = ['media_type']
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'realisateur', 'duree', 'histoire')
        }),
        ('Disponibilité et classification', {
            'fields': ('disponible', 'consultable', 'media_type', 'theme', 'annee_edition')
        }),
    )

@admin.register(Cd)
class CdAdmin(admin.ModelAdmin):
    list_display = ['disponible', 'name', 'artiste', 'nb_piste', 'duree_ecoute', 'theme']
    search_fields = ['name', 'artiste', 'theme']
    list_filter = ['disponible', 'theme', 'artiste']
    ordering = ['-disponible', 'name', 'artiste', 'theme']
    readonly_fields = ['media_type']
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'artiste', 'nb_piste', 'duree_ecoute')
        }),
        ('Disponibilité et classification', {
            'fields': ('disponible', 'consultable', 'media_type', 'theme', 'annee_edition')
        }),
    )

@admin.register(JeuDePlateau)
class JeuDePlateauAdmin(admin.ModelAdmin):
    list_display = [
        'consultable', 'name', 'createur', 'categorie',
        'nb_joueur_min', 'nb_joueur_max', 'age_min', 'duree_partie'
    ]
    search_fields = ['name', 'createur', 'categorie']
    list_filter = ['consultable', 'createur', 'categorie']
    ordering = ['-consultable', 'name', 'categorie', 'nb_joueur_min']
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'createur', 'annee_edition', 'categorie')
        }),
        ('Consultabilité et règles', {
            'fields': ('consultable', 'regle_consultable')
        }),
        ('Paramètres de jeu', {
            'fields': ('nb_joueur_min', 'nb_joueur_max', 'age_min', 'duree_partie')
        }),
    )

@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ['statut', 'name', 'compte', 'nb_emprunts_en_cours', 'nb_retards']
    search_fields = ['name', 'compte']
    list_filter = ['statut']
    ordering = ['statut', 'name', 'compte']
    readonly_fields = ['nb_emprunts_en_cours', 'nb_retards']
    fieldsets = (
        ('Identité du membre', {
            'fields': ('name', 'compte')
        }),
        ('Statut et suivi', {
            'fields': ('statut', 'nb_emprunts_en_cours', 'nb_retards')
        }),
    )

@admin.register(Bibliothecaire)
class BibliothecaireAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    fieldsets = (
        ('Identité du bibliothécaire', {
            'fields': ('name',)
        }),
    )

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ['statut', 'date_emprunt', 'date_retour', 'emprunteur', 'media']
    search_fields = ['emprunteur__name', 'media__name']
    list_filter = ['statut', 'emprunteur', 'media']
    ordering = ['statut', '-date_emprunt']
    readonly_fields = ['date_emprunt']
    fieldsets = (
        ('Informations sur le prêt', {
            'fields': ('media', 'emprunteur', 'statut')
        }),
        ('Dates', {
            'fields': ('date_emprunt', 'date_retour')
        }),
    )

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True # False
    def has_change_permission(self, request, obj=None):
        return True # False
    def has_delete_permission(self, request, obj=None):
        return True # False
    def has_view_permission(self, request, obj=None):
        return True

# Enregistrement simple sans personnalisation

# non exposé, car pas d'enregistrement spécifique
# admin.site.register(Media)

# admin.site.register(Livre)
# admin.site.register(Dvd)
# admin.site.register(Cd)
# admin.site.register(JeuDePlateau)
# admin.site.register(Membre)
# admin.site.register(Bibliothecaire)
# admin.site.register(Emprunt)
