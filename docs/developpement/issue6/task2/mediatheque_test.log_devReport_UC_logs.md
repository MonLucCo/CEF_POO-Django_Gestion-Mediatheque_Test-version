[03/Dec/2025 20:47:01] [INFO] <accounts.views> "POST /logout/ HTTP/1.1" 302 0 : [LOGOUT] utilisateur=testbib_gestion
[03/Dec/2025 20:47:02] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=staff
[03/Dec/2025 20:47:03] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=superadmin
[03/Dec/2025 20:47:03] [INFO] <accounts.views> "POST /logout/ HTTP/1.1" 302 0 : [LOGOUT] utilisateur=superadmin
[03/Dec/2025 20:47:03] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=anonyme
[03/Dec/2025 20:47:04] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:04] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:04] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:04] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:04] [INFO] <bibliothecaire.views_debug> "POST /bibliothecaire/rejeu-ux/retard/reset-session/ HTTP/1.1" 302 0 : [ResetRetardSession] utilisateur=testbib_admin décalage=1 jour(s), nouvelle_date=2025-12-02
[03/Dec/2025 20:47:04] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/rejeu-ux/retard/reset-session/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:05] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:05] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:05] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=NON_DEFINI, nom=TestMedia
[03/Dec/2025 20:47:05] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:05] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:05] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:05] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [MediaUpdate] utilisateur=testbib_admin a mis à jour le média id=1, type=LIVRE, nom=Le Petit Prince
[03/Dec/2025 20:47:05] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:06] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:06] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:06] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=LIVRE, nom=TestLivre
[03/Dec/2025 20:47:06] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [LivreCreate] utilisateur=testbib_admin a créé un Livre id=16, nom=TestLivre, année=None
[03/Dec/2025 20:47:06] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:07] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:07] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:07] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=NON_DEFINI, nom=MediaNonType
[03/Dec/2025 20:47:07] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:07] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/16/modifier/livre/ HTTP/1.1" 302 0 : [MediaTypageLivre] utilisateur=testbib_admin a typé le média id=16 en Livre, nom=MediaNonType, année=None
[03/Dec/2025 20:47:07] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/16/modifier/livre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:07] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:07] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:07] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/livre/modifier/ HTTP/1.1" 302 0 : [LivreUpdate] utilisateur=testbib_admin a modifié le Livre id=1, nom=Le Petit Prince, année=1943
[03/Dec/2025 20:47:07] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/livre/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:08] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:08] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:08] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=DVD, nom=TestDVD
[03/Dec/2025 20:47:08] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [DvdCreate] utilisateur=testbib_admin a créé un DVD id=16, nom=TestDVD, année=None
[03/Dec/2025 20:47:08] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:09] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:09] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:09] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=CD, nom=TestCD
[03/Dec/2025 20:47:09] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [CdCreate] utilisateur=testbib_admin a créé un CD id=16, nom=TestCD, année=None
[03/Dec/2025 20:47:09] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:09] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:09] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:09] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_admin a créé un Membre id=6, nom=Jean Dupont, compte=2025_Jean_Dupont_1
[03/Dec/2025 20:47:09] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:09] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=anonyme
[03/Dec/2025 20:47:10] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:10] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_admin a créé un Membre Emprunteur id=6, nom=Marie Durand, compte=2025_Marie_Durand_1
[03/Dec/2025 20:47:10] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:10] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:10] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:10] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [MembreUpdate] utilisateur=testbib_admin a modifié le Membre id=1, nom=Jean Modif, compte=2023_Dupont_1, statut=1
[03/Dec/2025 20:47:10] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:11] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:11] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:11] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/6/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_admin a activé le statut emprunteur pour Membre id=6, nom=TestMembre, compte=2025_TestMembre_1
[03/Dec/2025 20:47:11] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/6/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:12] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:47:12] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:12] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=6, emprunteur=Dupont, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:47:12] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:12] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:47:12] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:12] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:47:12] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:13] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:47:13] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:13] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=6, emprunteur=EmprunteurTest, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:47:13] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:14] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:47:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/7/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:14] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=4, emprunteur=Thomas, media=Matrix (DVD)
[03/Dec/2025 20:47:14] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:14] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:47:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:14] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=6, emprunteur=Dupont, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:47:14] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:15] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:47:15] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:15] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/4/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:15] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=4, emprunteur=Thomas, media=Matrix (DVD)
[03/Dec/2025 20:47:15] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:47:15] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:47:15] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:47:15] [INFO] <bibliothecaire.views> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [JeuCreate] utilisateur=testbib_admin a créé un Jeu id=21, nom=TestJeu, année=None
[03/Dec/2025 20:47:15] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
