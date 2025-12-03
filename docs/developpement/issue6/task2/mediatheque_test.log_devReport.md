[03/Dec/2025 20:50:43] [INFO] <accounts.views> "POST /logout/ HTTP/1.1" 302 0 : [LOGOUT] utilisateur=testbib_gestion
[03/Dec/2025 20:50:43] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=staff
[03/Dec/2025 20:50:44] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=superadmin
[03/Dec/2025 20:50:44] [INFO] <accounts.views> "POST /logout/ HTTP/1.1" 302 0 : [LOGOUT] utilisateur=superadmin
[03/Dec/2025 20:50:44] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=anonyme
[03/Dec/2025 20:50:45] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:45] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:45] [INFO] <bibliothecaire.views_debug> "POST /bibliothecaire/rejeu-ux/retard/reset-session/ HTTP/1.1" 302 0 : [ResetRetardSession] utilisateur=testbib_admin décalage=1 jour(s), nouvelle_date=2025-12-02
[03/Dec/2025 20:50:45] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/rejeu-ux/retard/reset-session/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:46] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:46] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:46] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=NON_DEFINI, nom=TestMedia
[03/Dec/2025 20:50:46] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [MediaUpdate] utilisateur=testbib_admin a mis à jour le média id=1, type=LIVRE, nom=Le Petit Prince
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=LIVRE, nom=TestLivre
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [LivreCreate] utilisateur=testbib_admin a créé un Livre id=16, nom=TestLivre, année=None
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=NON_DEFINI, nom=MediaNonType
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/16/modifier/livre/ HTTP/1.1" 302 0 : [MediaTypageLivre] utilisateur=testbib_admin a typé le média id=16 en Livre, nom=MediaNonType, année=None
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/16/modifier/livre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/livre/modifier/ HTTP/1.1" 302 0 : [LivreUpdate] utilisateur=testbib_admin a modifié le Livre id=1, nom=Le Petit Prince, année=1943
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/livre/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:49] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:49] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:49] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=DVD, nom=TestDVD
[03/Dec/2025 20:50:49] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [DvdCreate] utilisateur=testbib_admin a créé un DVD id=16, nom=TestDVD, année=None
[03/Dec/2025 20:50:49] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a créé un média id=16, type=CD, nom=TestCD
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [CdCreate] utilisateur=testbib_admin a créé un CD id=16, nom=TestCD, année=None
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_admin a créé un Membre id=6, nom=Jean Dupont, compte=2025_Jean_Dupont_1
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:51] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=anonyme
[03/Dec/2025 20:50:51] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:51] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_admin a créé un Membre Emprunteur id=6, nom=Marie Durand, compte=2025_Marie_Durand_1
[03/Dec/2025 20:50:51] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [MembreUpdate] utilisateur=testbib_admin a modifié le Membre id=1, nom=Jean Modif, compte=2023_Dupont_1, statut=1
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/6/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_admin a activé le statut emprunteur pour Membre id=6, nom=TestMembre, compte=2025_TestMembre_1
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/6/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:53] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=6, emprunteur=Dupont, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:54] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:50:54] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:54] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=6, emprunteur=EmprunteurTest, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:50:54] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/7/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=4, emprunteur=Thomas, media=Matrix (DVD)
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=6, emprunteur=Dupont, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:56] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/4/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=4, emprunteur=Thomas, media=Matrix (DVD)
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:56] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.views> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [JeuCreate] utilisateur=testbib_admin a créé un Jeu id=21, nom=TestJeu, année=None
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:58] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:59] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=anonyme
[03/Dec/2025 20:51:00] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=superadmin (non bibliothécaire)
[03/Dec/2025 20:51:00] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=staff (non bibliothécaire)
[03/Dec/2025 20:51:04] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:07] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=1, emprunteur=Dupont, media=Thriller (CD)
[03/Dec/2025 20:51:07] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:08] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=1, emprunteur=Dupont, media=Thriller (CD)
[03/Dec/2025 20:51:08] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:08] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:09] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:09] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:09] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:10] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:10] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:12] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/11/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=1, emprunteur=Dupont, media=Thriller (CD)
[03/Dec/2025 20:51:12] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/11/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:12] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:12] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/11/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:14] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=1, emprunteur=Dupont, media=Thriller (CD)
[03/Dec/2025 20:51:14] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:14] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:15] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:17] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/11/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:19] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:21] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a créé un Emprunt id=1, emprunteur=Dupont, media=Thriller (CD)
[03/Dec/2025 20:51:21] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:22] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/11/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:23] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/11/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:24] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:24] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:26] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a créé un média id=1, type=NON_DEFINI, nom=Média temporaire
[03/Dec/2025 20:51:26] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:26] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:27] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:27] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:27] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a créé un média id=1, type=NON_DEFINI, nom=Validé
[03/Dec/2025 20:51:27] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:27] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:27] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a créé un média id=1, type=LIVRE, nom=Média livre attente
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [LivreCreate] utilisateur=testbib_gestion a créé un Livre id=1, nom=Média livre attente, année=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a créé un média id=2, type=LIVRE, nom=Média livre prêt
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [LivreCreate] utilisateur=testbib_gestion a créé un Livre id=2, nom=Média livre prêt, année=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a créé un média id=3, type=DVD, nom=Média dvd attente
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [DvdCreate] utilisateur=testbib_gestion a créé un DVD id=3, nom=Média dvd attente, année=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a créé un média id=4, type=DVD, nom=Média dvd prêt
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [DvdCreate] utilisateur=testbib_gestion a créé un DVD id=4, nom=Média dvd prêt, année=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a créé un média id=5, type=CD, nom=Média cd attente
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [CdCreate] utilisateur=testbib_gestion a créé un CD id=5, nom=Média cd attente, année=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a créé un média id=6, type=CD, nom=Média cd prêt
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [CdCreate] utilisateur=testbib_gestion a créé un CD id=6, nom=Média cd prêt, année=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:30] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_gestion a créé un Membre id=1, nom=Alice Dupont, compte=2025_Alice_Dupont_1
[03/Dec/2025 20:51:30] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:30] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_gestion a créé un Membre Emprunteur id=1, nom=Bob Martin, compte=2025_Bob_Martin_1
[03/Dec/2025 20:51:30] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_gestion a créé un Membre id=1, nom=Claire Lemoine, compte=2025_Claire_Lemoine_1
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_gestion a créé un Membre id=2, nom=Claire Lemoine, compte=2025_Claire_Lemoine_2
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_gestion a créé un Membre id=3, nom=Claire Lemoine, compte=2025_Claire_Lemoine_3
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_gestion a créé un Membre Emprunteur id=1, nom=David Morel, compte=2025_David_Morel_1
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_gestion a créé un Membre Emprunteur id=2, nom=David Morel, compte=2025_David_Morel_2
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_gestion a créé un Membre Emprunteur id=3, nom=David Morel, compte=2025_David_Morel_3
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:34] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:35] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:36] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:37] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:37] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:39] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/supprimer/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:39] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/2/supprimer/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:40] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/supprimer/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:41] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/2/supprimer/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:42] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/supprimer/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:44] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/supprimer/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:46] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:47] [INFO] <bibliothecaire.views> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [JeuCreate] utilisateur=testbib_gestion a créé un Jeu id=21, nom=Nouveau Jeu, année=2020
[03/Dec/2025 20:51:47] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:47] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/jeux/16/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:48] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:48] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:49] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:50] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/16/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:50] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:50] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/16/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:52] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/consultables/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:52] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/consultables/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:53] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/consultables/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:53] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/consultables/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:54] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/disponibles/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/disponibles/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/disponibles/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/disponibles/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:57] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/non-types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:57] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/non-types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:57] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/non-types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:58] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/non-types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:59] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:59] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:59] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:02] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:02] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/emprunteurs HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:02] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/supprimes HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:04] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:04] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/emprunteurs HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:05] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/supprimes HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:06] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:06] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:07] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/emprunteurs HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:07] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/supprimes HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:09] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:09] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:09] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/emprunteurs HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:09] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/supprimes HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:10] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:13] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/retards/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:13] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:14] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:14] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:15] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/retards/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:16] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:17] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:18] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:18] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/retards/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:18] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/retards/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmé le retour de l’Emprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:23] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/rendre/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:23] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:23] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:23] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:24] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:25] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/rendre/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:26] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/rendre/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:26] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:26] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:26] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:27] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/rendre/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [MediaUpdate] utilisateur=testbib_gestion a modifié le média id=1, transition de type NON_DEFINI → CD
[03/Dec/2025 20:52:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:28] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/1/modifier/cd/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:30] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/annuler_typage/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:30] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:31] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/modifier/livre/ HTTP/1.1" 302 0 : [MediaTypageLivre] utilisateur=testbib_gestion a typé le média id=1 en Livre, nom=À typer, année=None
[03/Dec/2025 20:52:31] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/modifier/livre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:31] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:33] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [MembreUpdate] utilisateur=testbib_gestion a modifié le Membre id=1, nom=Élodie M., compte=2025_Élodie_Martin_1, statut=0
[03/Dec/2025 20:52:33] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:33] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_gestion a activé le statut emprunteur pour Membre id=1, nom=Élodie Martin, compte=2025_Élodie_Martin_1
[03/Dec/2025 20:52:33] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [MembreUpdate] utilisateur=testbib_gestion a modifié le Membre id=1, nom=Élodie M., compte=2025_Élodie_Martin_1, statut=0
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_gestion a activé le statut emprunteur pour Membre id=1, nom=Élodie Martin, compte=2025_Élodie_Martin_1
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_gestion a activé le statut emprunteur pour Membre id=1, nom=Élodie Martin, compte=2025_Élodie_Martin_1
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:37] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:37] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:39] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:39] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:40] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:41] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:42] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:43] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:43] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/1/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:43] [WARNING] <django.request> Not Found: /bibliothecaire/medias/999/
[03/Dec/2025 20:52:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/3/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/4/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/3/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:46] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/4/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:46] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/1/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:48] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
