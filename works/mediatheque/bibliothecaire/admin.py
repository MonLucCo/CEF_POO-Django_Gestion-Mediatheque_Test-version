from django.contrib import admin
from .models import (
#    Media,
    Livre,
    Dvd,
    Cd,
    JeuDePlateau,
    Membre,
    Bibliothecaire,
    Emprunt
)

# Enregistrement avec personnalisation de l'interface d'administration
@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ['disponible', 'titre', 'auteur', 'nb_page', 'theme']
    search_fields = ['titre', 'auteur', 'theme']
    list_filter = ['disponible', 'theme']
    ordering = ['-disponible', 'titre', 'auteur', 'theme']
    readonly_fields = ['media_type']
    fieldsets = (
        ('Informations générales', {
            'fields': ('titre', 'auteur', 'nb_page', 'resume')
        }),
        ('Disponibilité et classification', {
            'fields': ('disponible', 'consultable', 'media_type', 'theme', 'annee_edition')
        }),
    )

@admin.register(Dvd)
class DvdAdmin(admin.ModelAdmin):
    list_display = ['disponible', 'titre', 'realisateur', 'duree', 'theme']
    search_fields = ['titre', 'realisateur', 'theme']
    list_filter = ['disponible', 'theme', 'realisateur']
    ordering = ['-disponible', 'titre', 'realisateur', 'duree']
    readonly_fields = ['media_type']
    fieldsets = (
        ('Informations générales', {
            'fields': ('titre', 'realisateur', 'duree', 'histoire')
        }),
        ('Disponibilité et classification', {
            'fields': ('disponible', 'consultable', 'media_type', 'theme', 'annee_edition')
        }),
    )

@admin.register(Cd)
class CdAdmin(admin.ModelAdmin):
    list_display = ['disponible', 'titre', 'artiste', 'nb_piste', 'duree_ecoute', 'theme']
    search_fields = ['titre', 'artiste', 'theme']
    list_filter = ['disponible', 'theme', 'artiste']
    ordering = ['-disponible', 'titre', 'artiste', 'theme']
    readonly_fields = ['media_type']
    fieldsets = (
        ('Informations générales', {
            'fields': ('titre', 'artiste', 'nb_piste', 'duree_ecoute')
        }),
        ('Disponibilité et classification', {
            'fields': ('disponible', 'consultable', 'media_type', 'theme', 'annee_edition')
        }),
    )

@admin.register(JeuDePlateau)
class JeuDePlateauAdmin(admin.ModelAdmin):
    list_display = [
        'consultable', 'titre', 'createur', 'categorie',
        'nb_joueur_min', 'nb_joueur_max', 'age_min', 'duree_partie'
    ]
    search_fields = ['titre', 'createur', 'categorie']
    list_filter = ['consultable', 'createur', 'categorie']
    ordering = ['-consultable', 'titre', 'categorie', 'nb_joueur_min']
    fieldsets = (
        ('Informations générales', {
            'fields': ('titre', 'createur', 'annee_edition', 'categorie')
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
    list_display = ['bloque', 'nom', 'compte', 'nb_emprunts_en_cours', 'nb_retards']
    search_fields = ['nom', 'compte']
    list_filter = ['bloque']
    ordering = ['-bloque', 'nom', 'compte']
    readonly_fields = ['nb_emprunts_en_cours', 'nb_retards']
    fieldsets = (
        ('Identité du membre', {
            'fields': ('nom', 'compte')
        }),
        ('Statut et suivi', {
            'fields': ('bloque', 'nb_emprunts_en_cours', 'nb_retards')
        }),
    )

@admin.register(Bibliothecaire)
class BibliothecaireAdmin(admin.ModelAdmin):
    list_display = ['nom']
    ordering = ['nom']
    search_fields = ['nom']
    fieldsets = (
        ('Identité du bibliothécaire', {
            'fields': ('nom',)
        }),
    )

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ['statut', 'date_emprunt', 'date_retour', 'emprunteur', 'media']
    search_fields = ['emprunteur__nom', 'media__titre']
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

# Enregistrement simple sans personnalisation
# admin.site.register(Media)  # non exposé, car pas d'enregistrement spécifique
# admin.site.register(Livre)
# admin.site.register(Dvd)
# admin.site.register(Cd)
# admin.site.register(JeuDePlateau)
# admin.site.register(Membre)
# admin.site.register(Bibliothecaire)
# admin.site.register(Emprunt)
