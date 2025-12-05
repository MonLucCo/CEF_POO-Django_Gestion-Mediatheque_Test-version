### Annexe B - Logs d’exécution et de tests


La première section contient les logs de l'application durant les tests `mediatheque_test.log`.

La seconde section contient les traces des Logs obtenus lors des 198 tests de l'application avec la commande :

```bash
python manage.py test > mediatheque_test.log_devReport.md 2>&1 -v 2
```

---

#### Sommaire

- [Logs des tests de l'application médiathèque](#logs-des-tests-de-lapplication-médiathèque)
- [Traces des tests de l'application incluant les log](#traces-des-tests-de-lapplication-incluant-les-logs)

---

#### Logs des tests de l'application médiathèque

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

---

#### Traces des tests de l'application incluant les logs

python : Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Au caractère Ligne:1 : 1
+ python manage.py test > devReport.md 2>&1 -v 2
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (Creating test d...che=shared')...:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 

Found 198 test(s).
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, bibliothecaire, contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying bibliothecaire.0001_initial... OK
  Applying bibliothecaire.0002_alter_cd_options_alter_dvd_options_and_more... OK
  Applying bibliothecaire.0003_alter_emprunt_statut... OK
  Applying bibliothecaire.0004_rename_nom_bibliothecaire_name_and_more... OK
  Applying bibliothecaire.0005_alter_jeudeplateau_annee_edition_and_more... OK
  Applying bibliothecaire.0006_alter_jeudeplateau_annee_edition_and_more... OK
  Applying bibliothecaire.0007_alter_jeudeplateau_annee_edition_and_more... OK
  Applying bibliothecaire.0008_alter_cd_duree_ecoute_alter_cd_nb_piste_and_more... OK
  Applying bibliothecaire.0009_alter_cd_nb_piste_alter_media_media_type... OK
  Applying bibliothecaire.0010_alter_jeudeplateau_consultable_and_more... OK
  Applying bibliothecaire.0011_remove_membre_bloque_membre_statut... OK
  Applying bibliothecaire.0012_bibliothecaire_role_bibliothecaire_user_and_more... OK
  Applying bibliothecaire.0013_alter_bibliothecaire_user... OK
test_fun_52_connexion_valide_redirige_accueil (accounts.tests_blocs.test_uc_accounts_compte.TestFonctionnelAccounts.test_fun_52_connexion_valide_redirige_accueil) ... ok
test_fun_53_connexion_invalide_affiche_erreur (accounts.tests_blocs.test_uc_accounts_compte.TestFonctionnelAccounts.test_fun_53_connexion_invalide_affiche_erreur) ... [03/Dec/2025 
20:50:36] [WARNING] <accounts.views> "POST /login/ HTTP/1.1" 200 0 : [LOGIN_INVALID] tentative de connexion
ok
test_fun_54_deconnexion_redirige_accueil_bibliothecaire (accounts.tests_blocs.test_uc_accounts_compte.TestFonctionnelAccounts.test_fun_54_deconnexion_redirige_accueil_bibliothecaire) ... 
[03/Dec/2025 20:50:36] [INFO] <accounts.views> "POST /logout/ HTTP/1.1" 302 0 : [LOGOUT] utilisateur=testbib_gestion
ok
test_fun_55_menu_affiche_connexion_ou_deconnexion_selon_etat 
(accounts.tests_blocs.test_uc_accounts_compte.TestFonctionnelAccounts.test_fun_55_menu_affiche_connexion_ou_deconnexion_selon_etat) ... ok
test_fun_56_affichage_nom_utilisateur_connecte (accounts.tests_blocs.test_uc_accounts_compte.TestFonctionnelAccounts.test_fun_56_affichage_nom_utilisateur_connecte) ... ok
test_nav_38_acces_accueil_mediatheque (accounts.tests_blocs.test_uc_accounts_compte.TestNavigationAccueil.test_nav_38_acces_accueil_mediatheque) ... ok
test_nav_39_lien_bibliothecaire (accounts.tests_blocs.test_uc_accounts_compte.TestNavigationAccueil.test_nav_39_lien_bibliothecaire) ... [03/Dec/2025 20:50:40] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_40_lien_consultation (accounts.tests_blocs.test_uc_accounts_compte.TestNavigationAccueil.test_nav_40_lien_consultation) ... ok
test_nav_41_lien_connexion_affiche_si_non_connecte (accounts.tests_blocs.test_uc_accounts_compte.TestNavigationAccueil.test_nav_41_lien_connexion_affiche_si_non_connecte) ... ok
test_nav_42_lien_deconnexion_affiche_si_connecte (accounts.tests_blocs.test_uc_accounts_compte.TestNavigationAccueil.test_nav_42_lien_deconnexion_affiche_si_connecte) ... ok
test_log_01_fichier_log_cree_et_alimente (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_01_fichier_log_cree_et_alimente)
T-LOG-01 : VÚrifie la crÚation et lÆalimentation du fichier mediatheque.log. ... [03/Dec/2025 20:50:43] [INFO] <accounts.views> "POST /logout/ HTTP/1.1" 302 0 : [LOGOUT] 
utilisateur=testbib_gestion
ok
test_log_02_connexion_genere_un_log_LOGIN (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_02_connexion_genere_un_log_LOGIN)
T-LOG-02 : VÚrifie quÆune connexion gÚnÞre un message [LOGIN]. ... [03/Dec/2025 20:50:43] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=staff
ok
test_log_03_deconnexion_genere_un_log_LOGOUT (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_03_deconnexion_genere_un_log_LOGOUT)
T-LOG-03 : VÚrifie quÆune dÚconnexion gÚnÞre [LOGOUT] ou [LOGOUT_INVALID]. ... [03/Dec/2025 20:50:44] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=superadmin
[03/Dec/2025 20:50:44] [INFO] <accounts.views> "POST /logout/ HTTP/1.1" 302 0 : [LOGOUT] utilisateur=superadmin
ok
test_log_04_acces_refuse_genere_un_log_ACCESS_DENIED (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_04_acces_refuse_genere_un_log_ACCESS_DENIED)
T-LOG-04 : VÚrifie quÆun accÞs refusÚ gÚnÞre [ACCESS_DENIED]. ... [03/Dec/2025 20:50:44] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : 
[ACCESS_DENIED] utilisateur=anonyme
ok
test_log_05_acces_accepte_genere_un_log_ACCESS_GRANTED (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_05_acces_accepte_genere_un_log_ACCESS_GRANTED)
T-LOG-05 : VÚrifie quÆun accÞs accordÚ gÚnÞre [ACCESS_GRANTED]. ... [03/Dec/2025 20:50:45] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_10_reset_retard_session (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_10_reset_retard_session)
T-LOG-10 : VÚrifie que le changement de date de marquage gÚnÞre [ResetRetardSession]. ... [03/Dec/2025 20:50:45] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_admin
[03/Dec/2025 20:50:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:45] [INFO] <bibliothecaire.views_debug> "POST /bibliothecaire/rejeu-ux/retard/reset-session/ HTTP/1.1" 302 0 : [ResetRetardSession] utilisateur=testbib_admin dÚcalage=1 
jour(s), nouvelle_date=2025-12-02
[03/Dec/2025 20:50:45] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/rejeu-ux/retard/reset-session/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_11_media_create (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_11_media_create)
T-LOG-11 : VÚrifie que la crÚation dÆun mÚdia gÚnÞre [MediaCreate]. ... [03/Dec/2025 20:50:46] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:46] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:46] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a crÚÚ un mÚdia id=16, 
type=NON_DEFINI, nom=TestMedia
[03/Dec/2025 20:50:46] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_16_media_update (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_16_media_update)
T-LOG-16 : VÚrifie que la modification dÆun mÚdia gÚnÞre [MediaUpdate]. ... [03/Dec/2025 20:50:47] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [MediaUpdate] utilisateur=testbib_admin a mis Ó jour le mÚdia id=1, 
type=LIVRE, nom=Le Petit Prince
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_18_livre_create (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_18_livre_create)
T-LOG-18 : VÚrifie que la crÚation dÆun Livre gÚnÞre [LivreCreate]. ... [03/Dec/2025 20:50:47] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a crÚÚ un mÚdia id=16, 
type=LIVRE, nom=TestLivre
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [LivreCreate] utilisateur=testbib_admin a crÚÚ un Livre id=16, 
nom=TestLivre, annÚe=None
[03/Dec/2025 20:50:47] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_20_media_typage_livre (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_20_media_typage_livre)
T-LOG-20 : VÚrifie que le typage dÆun mÚdia en Livre gÚnÞre [MediaTypageLivre]. ... [03/Dec/2025 20:50:48] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a crÚÚ un mÚdia id=16, 
type=NON_DEFINI, nom=MediaNonType
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/16/modifier/livre/ HTTP/1.1" 302 0 : [MediaTypageLivre] utilisateur=testbib_admin a typÚ le mÚdia id=16 
en Livre, nom=MediaNonType, annÚe=None
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/16/modifier/livre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_21_livre_update (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_21_livre_update)
T-LOG-21 : VÚrifie que la modification dÆun Livre gÚnÞre [LivreUpdate]. ... [03/Dec/2025 20:50:48] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/livre/modifier/ HTTP/1.1" 302 0 : [LivreUpdate] utilisateur=testbib_admin a modifiÚ le Livre id=1, 
nom=Le Petit Prince, annÚe=1943
[03/Dec/2025 20:50:48] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/livre/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_23_dvd_create (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_23_dvd_create)
T-LOG-23 : VÚrifie que la crÚation dÆun DVD gÚnÞre [DvdCreate]. ... [03/Dec/2025 20:50:49] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:49] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:49] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a crÚÚ un mÚdia id=16, type=DVD, 
nom=TestDVD
[03/Dec/2025 20:50:49] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [DvdCreate] utilisateur=testbib_admin a crÚÚ un DVD id=16, nom=TestDVD, 
annÚe=None
[03/Dec/2025 20:50:49] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_27_cd_create (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_27_cd_create)
T-LOG-27 : VÚrifie que la crÚation dÆun CD gÚnÞre [CdCreate]. ... [03/Dec/2025 20:50:50] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_admin a crÚÚ un mÚdia id=16, type=CD, 
nom=TestCD
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [CdCreate] utilisateur=testbib_admin a crÚÚ un CD id=16, nom=TestCD, 
annÚe=None
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_31_membre_create (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_31_membre_create)
T-LOG-31 : VÚrifie que la crÚation dÆun Membre gÚnÞre [MembreCreate]. ... [03/Dec/2025 20:50:50] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_admin a crÚÚ un Membre id=6, nom=Jean 
Dupont, compte=2025_Jean_Dupont_1
[03/Dec/2025 20:50:50] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_32_membre_create_emprunteur (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_32_membre_create_emprunteur)
T-LOG-32 : VÚrifie que la crÚation dÆun Membre emprunteur gÚnÞre [MembreCreateEmprunteur]. ... [03/Dec/2025 20:50:51] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ 
HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=anonyme
[03/Dec/2025 20:50:51] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:51] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_admin a crÚÚ un Membre 
Emprunteur id=6, nom=Marie Durand, compte=2025_Marie_Durand_1
[03/Dec/2025 20:50:51] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_37_membre_update (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_37_membre_update)
T-LOG-37 : VÚrifie que la modification dÆun Membre gÚnÞre [MembreUpdate]. ... [03/Dec/2025 20:50:52] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [MembreUpdate] utilisateur=testbib_admin a modifiÚ le Membre id=1, 
nom=Jean Modif, compte=2023_Dupont_1, statut=1
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_38_membre_activate_emprunteur (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_38_membre_activate_emprunteur)
T-LOG-38 : VÚrifie que lÆactivation dÆun emprunteur gÚnÞre [MembreActivateEmprunteur]. ... [03/Dec/2025 20:50:52] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/6/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_admin a activÚ le 
statut emprunteur pour Membre id=6, nom=TestMembre, compte=2025_TestMembre_1
[03/Dec/2025 20:50:52] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/6/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_log_41_emprunt_create (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_41_emprunt_create)
T-LOG-41 : VÚrifie que la crÚation dÆun Emprunt gÚnÞre [EmpruntCreate]. ... [03/Dec/2025 20:50:53] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a crÚÚ un Emprunt id=6, 
emprunteur=Dupont, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_log_42_emprunt_retour_confirm (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_42_emprunt_retour_confirm)
T-LOG-42 : VÚrifie que la confirmation du retour gÚnÞre [EmpruntRetourConfirm]. ... [03/Dec/2025 20:50:53] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmÚ 
le retour de lÆEmprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:50:53] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_log_43_media_emprunter (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_43_media_emprunter)
T-LOG-43 : VÚrifie que lÆemprunt depuis un mÚdia gÚnÞre [EmpruntCreateFromMedia] ou [EmpruntCreate]. ... [03/Dec/2025 20:50:54] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : 
[LOGIN] utilisateur=testbib_gestion
[03/Dec/2025 20:50:54] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:54] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/1/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a crÚÚ un Emprunt id=6, 
emprunteur=EmprunteurTest, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:50:54] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_log_44_media_rendre (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_44_media_rendre)
T-LOG-44 : VÚrifie que le rendu depuis un mÚdia gÚnÞre [EmpruntRetourConfirm]. ... [03/Dec/2025 20:50:55] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/7/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmÚ 
le retour de lÆEmprunt id=4, emprunteur=Thomas, media=Matrix (DVD)
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_log_45_membre_emprunter (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_45_membre_emprunter)
T-LOG-45 : VÚrifie que la crÚation dÆun emprunt depuis un membre gÚnÞre [EmpruntCreate]. ... [03/Dec/2025 20:50:55] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a crÚÚ un Emprunt id=6, 
emprunteur=Dupont, media=Le Petit Prince (LIVRE)
[03/Dec/2025 20:50:55] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_log_46_membre_rendre (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_46_membre_rendre)
T-LOG-46 : VÚrifie que le rendu dÆun emprunt depuis un membre gÚnÞre [EmpruntRetourConfirm]. ... [03/Dec/2025 20:50:56] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] 
utilisateur=testbib_gestion
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/4/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmÚ 
le retour de lÆEmprunt id=4, emprunteur=Thomas, media=Matrix (DVD)
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/4/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_log_48_jeu_create (accounts.tests_blocs.test_uc_logs.TestLogs.test_log_48_jeu_create)
T-LOG-48 : VÚrifie que la crÚation dÆun Jeu gÚnÞre [JeuCreate]. ... [03/Dec/2025 20:50:56] [INFO] <accounts.views> "POST /login/ HTTP/1.1" 302 0 : [LOGIN] utilisateur=testbib_admin
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.views> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [JeuCreate] utilisateur=testbib_admin a crÚÚ un Jeu id=21, nom=TestJeu, 
annÚe=None
[03/Dec/2025 20:50:56] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_sec_03_bibadmin_acces_complet_bibliothecaire (accounts.tests_blocs.test_uc_securite.TestFonctionnelSecurite.test_sec_03_bibadmin_acces_complet_bibliothecaire) ... [03/Dec/2025 
20:50:58] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_admin
ok
test_sec_04_membre_ou_anonyme_refus_bibliothecaire (accounts.tests_blocs.test_uc_securite.TestFonctionnelSecurite.test_sec_04_membre_ou_anonyme_refus_bibliothecaire) ... [03/Dec/2025 
20:50:59] [WARNING] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=anonyme
ok
test_sec_05_membre_acces_consultation (accounts.tests_blocs.test_uc_securite.TestFonctionnelSecurite.test_sec_05_membre_acces_consultation) ... ok
test_sec_06_superuser_refus_bibliothecaire (accounts.tests_blocs.test_uc_securite.TestFonctionnelSecurite.test_sec_06_superuser_refus_bibliothecaire) ... [03/Dec/2025 20:51:00] [WARNING] 
<bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=superadmin (non bibliothÚcaire)
ok
test_sec_07_staff_refus_bibliothecaire (accounts.tests_blocs.test_uc_securite.TestFonctionnelSecurite.test_sec_07_staff_refus_bibliothecaire) ... [03/Dec/2025 20:51:00] [WARNING] 
<bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_DENIED] utilisateur=staff (non bibliothÚcaire)
ok
test_sec_01_superuser_acces_admin (accounts.tests_blocs.test_uc_securite.TestNavigationSecurite.test_sec_01_superuser_acces_admin) ... ok
test_sec_02_staff_acces_admin_limite (accounts.tests_blocs.test_uc_securite.TestNavigationSecurite.test_sec_02_staff_acces_admin_limite) ... ok
test_access_with_login (bibliothecaire.tests.BibliothecaireAccessTest.test_access_with_login) ... [03/Dec/2025 20:51:04] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ 
HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_admin_base_access (bibliothecaire.tests_blocs.test_admin.AdminAccessTest.test_admin_base_access)
VÚrifie que l'accÞs Ó la page d'accueil de l'admin est autorisÚ ... ok
test_admin_urls_by_permissions (bibliothecaire.tests_blocs.test_admin.AdminAccessTest.test_admin_urls_by_permissions)
VÚrifie que l'accÞs aux URLs de l'admin est restreint ... ok
test_ent_01_media_creation (bibliothecaire.tests_blocs.test_entites_media.MediaEntityTests.test_ent_01_media_creation) ... ok
test_ent_02_media_default_values (bibliothecaire.tests_blocs.test_entites_media.MediaEntityTests.test_ent_02_media_default_values) ... ok
test_ent_03_media_sans_sous_type (bibliothecaire.tests_blocs.test_entites_media.MediaEntityTests.test_ent_03_media_sans_sous_type) ... ok
test_ent_04a_media_avec_sous_type_livre (bibliothecaire.tests_blocs.test_entites_media.MediaEntityTests.test_ent_04a_media_avec_sous_type_livre) ... ok
test_ent_04b_media_avec_sous_type_dvd (bibliothecaire.tests_blocs.test_entites_media.MediaEntityTests.test_ent_04b_media_avec_sous_type_dvd) ... ok
test_ent_04c_media_avec_sous_type_cd (bibliothecaire.tests_blocs.test_entites_media.MediaEntityTests.test_ent_04c_media_avec_sous_type_cd) ... ok
test_ent_20_creation_emprunt_valide (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestEntitesEmpruntUcCreate.test_ent_20_creation_emprunt_valide) ... [03/Dec/2025 20:51:07] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a crÚÚ un Emprunt id=1, emprunteur=Dupont, media=Thriller (CD)
[03/Dec/2025 20:51:07] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_26_creation_emprunt_valide (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreate.test_fun_26_creation_emprunt_valide) ... [03/Dec/2025 20:51:08] 
[INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a crÚÚ un Emprunt id=1, emprunteur=Dupont, 
media=Thriller (CD)
[03/Dec/2025 20:51:08] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_27_refus_membre_non_abonne (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreate.test_fun_27_refus_membre_non_abonne) ... [03/Dec/2025 20:51:08] 
[INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_28_refus_membre_retard (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreate.test_fun_28_refus_membre_retard) ... [03/Dec/2025 20:51:09] [INFO] 
<bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_29_refus_membre_au_quota (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreate.test_fun_29_refus_membre_au_quota) ... [03/Dec/2025 20:51:09] [INFO] 
<bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_30_refus_media_non_typÚ (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreate.test_fun_30_refus_media_non_typÚ) ... [03/Dec/2025 20:51:09] [INFO] 
<bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_31_refus_media_non_consultable (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreate.test_fun_31_refus_media_non_consultable) ... [03/Dec/2025 
20:51:10] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_32_refus_media_indisponible (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreate.test_fun_32_refus_media_indisponible) ... [03/Dec/2025 20:51:10] 
[INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_35_creation_emprunt_depuis_media_valide 
(bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreateFromMedia.test_fun_35_creation_emprunt_depuis_media_valide) ... [03/Dec/2025 20:51:12] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/medias/11/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a crÚÚ un Emprunt id=1, emprunteur=Dupont, media=Thriller 
(CD)
[03/Dec/2025 20:51:12] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/11/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:12] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_36_refus_membre_non_emprunteur_depuis_media 
(bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreateFromMedia.test_fun_36_refus_membre_non_emprunteur_depuis_media) ... [03/Dec/2025 20:51:12] [INFO] 
<bibliothecaire.decorator> "POST /bibliothecaire/medias/11/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_33_creation_emprunt_depuis_membre_valide 
(bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreateFromMembre.test_fun_33_creation_emprunt_depuis_membre_valide) ... [03/Dec/2025 20:51:14] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a crÚÚ un Emprunt id=1, emprunteur=Dupont, media=Thriller 
(CD)
[03/Dec/2025 20:51:14] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_34_refus_media_non_empruntable_depuis_membre 
(bibliothecaire.tests_blocs.test_uc_create_emprunt.TestFonctionnelEmpruntUcCreateFromMembre.test_fun_34_refus_media_non_empruntable_depuis_membre) ... [03/Dec/2025 20:51:14] [INFO] 
<bibliothecaire.decorator> "POST /bibliothecaire/membres/1/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_21_acces_vue_creation_emprunt (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestNavigationEmpruntUcCreate.test_nav_21_acces_vue_creation_emprunt) ... [03/Dec/2025 20:51:15] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_23_acces_vue_creation_emprunt_depuis_media 
(bibliothecaire.tests_blocs.test_uc_create_emprunt.TestNavigationEmpruntUcCreateFromMedia.test_nav_23_acces_vue_creation_emprunt_depuis_media) ... [03/Dec/2025 20:51:17] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/11/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_22_acces_vue_creation_emprunt_depuis_membre 
(bibliothecaire.tests_blocs.test_uc_create_emprunt.TestNavigationEmpruntUcCreateFromMembre.test_nav_22_acces_vue_creation_emprunt_depuis_membre) ... [03/Dec/2025 20:51:19] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/1/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_25_persistance_selection_si_erreur (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestVuesEmpruntUcCreate.test_vue_25_persistance_selection_si_erreur) ... [03/Dec/2025 
20:51:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_26_accumulation_messages_erreur (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestVuesEmpruntUcCreate.test_vue_26_accumulation_messages_erreur) ... [03/Dec/2025 20:51:20] 
[INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_27_redirection_apres_creation (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestVuesEmpruntUcCreate.test_vue_27_redirection_apres_creation) ... [03/Dec/2025 20:51:21] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [EmpruntCreate] utilisateur=testbib_gestion a crÚÚ un Emprunt id=1, emprunteur=Dupont, media=Thriller (CD)
[03/Dec/2025 20:51:21] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_30_champ_media_fige (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestVuesEmpruntUcCreateFromMedia.test_vue_30_champ_media_fige) ... [03/Dec/2025 20:51:22] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/11/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_31_bloc_info_present (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestVuesEmpruntUcCreateFromMedia.test_vue_31_bloc_info_present) ... [03/Dec/2025 20:51:23] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/11/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_28_champ_emprunteur_fige (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestVuesEmpruntUcCreateFromMembre.test_vue_28_champ_emprunteur_fige) ... [03/Dec/2025 20:51:24] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/1/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_29_bloc_info_present (bibliothecaire.tests_blocs.test_uc_create_emprunt.TestVuesEmpruntUcCreateFromMembre.test_vue_29_bloc_info_present) ... [03/Dec/2025 20:51:24] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/1/emprunter HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_08_created_media_has_expected_values (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_ent_08_created_media_has_expected_values) ... [03/Dec/2025 20:51:26] 
[INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a crÚÚ un mÚdia id=1, type=NON_DEFINI, nom=MÚdia temporaire
[03/Dec/2025 20:51:26] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_form_01_fields_present (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_form_01_fields_present) ... [03/Dec/2025 20:51:26] [INFO] <bibliothecaire.decorator> 
"GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_form_02_labels_customized (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_form_02_labels_customized) ... [03/Dec/2025 20:51:27] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_form_03_required_and_optional_fields (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_form_03_required_and_optional_fields) ... [03/Dec/2025 20:51:27] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_04_valid_creation_redirects (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_fun_04_valid_creation_redirects) ... [03/Dec/2025 20:51:27] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a crÚÚ un mÚdia id=1, type=NON_DEFINI, nom=ValidÚ
[03/Dec/2025 20:51:27] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:27] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_05_missing_required_field_name (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_fun_05_missing_required_field_name) ... [03/Dec/2025 20:51:27] [INFO] 
<bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_07_creation_typage_etat_metier (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_fun_07_creation_typage_etat_metier)
T-FUN-07 : VÚrifie la transition mÚtier (0) et (0+1) pour chaque mÚdia typÚ (Livre, Dvd, Cd) ... [03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST 
/bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a crÚÚ un mÚdia id=1, type=LIVRE, nom=MÚdia livre attente
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [LivreCreate] utilisateur=testbib_gestion a crÚÚ un Livre id=1, nom=MÚdia 
livre attente, annÚe=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a crÚÚ un mÚdia id=2, 
type=LIVRE, nom=MÚdia livre prÛt
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [LivreCreate] utilisateur=testbib_gestion a crÚÚ un Livre id=2, nom=MÚdia 
livre prÛt, annÚe=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/livre HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a crÚÚ un mÚdia id=3, type=DVD, 
nom=MÚdia dvd attente
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [DvdCreate] utilisateur=testbib_gestion a crÚÚ un DVD id=3, nom=MÚdia dvd 
attente, annÚe=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a crÚÚ un mÚdia id=4, type=DVD, 
nom=MÚdia dvd prÛt
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [DvdCreate] utilisateur=testbib_gestion a crÚÚ un DVD id=4, nom=MÚdia dvd 
prÛt, annÚe=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/dvd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a crÚÚ un mÚdia id=5, type=CD, 
nom=MÚdia cd attente
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [CdCreate] utilisateur=testbib_gestion a crÚÚ un CD id=5, nom=MÚdia cd 
attente, annÚe=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [MediaCreate] utilisateur=testbib_gestion a crÚÚ un mÚdia id=6, type=CD, 
nom=MÚdia cd prÛt
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.views> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [CdCreate] utilisateur=testbib_gestion a crÚÚ un CD id=6, nom=MÚdia cd prÛt, 
annÚe=None
[03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/ajouter/cd HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_08_access_create_view (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_nav_08_access_create_view) ... [03/Dec/2025 20:51:28] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_09_template_used (bibliothecaire.tests_blocs.test_uc_create_media.MediaCreateTests.test_vue_09_template_used) ... [03/Dec/2025 20:51:28] [INFO] <bibliothecaire.decorator> "GET 
/bibliothecaire/medias/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_13_creation_membre_standard_compte_exact (bibliothecaire.tests_blocs.test_uc_create_membre.TestEntitesMembreUcCreate.test_ent_13_creation_membre_standard_compte_exact) ... 
[03/Dec/2025 20:51:30] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_gestion a crÚÚ un Membre id=1, nom=Alice 
Dupont, compte=2025_Alice_Dupont_1
[03/Dec/2025 20:51:30] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_14_creation_membre_emprunteur_compte_exact (bibliothecaire.tests_blocs.test_uc_create_membre.TestEntitesMembreUcCreate.test_ent_14_creation_membre_emprunteur_compte_exact) ... 
[03/Dec/2025 20:51:30] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_gestion a crÚÚ un 
Membre Emprunteur id=1, nom=Bob Martin, compte=2025_Bob_Martin_1
[03/Dec/2025 20:51:30] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_14_uc_create_01_incrementation_membre_standard 
(bibliothecaire.tests_blocs.test_uc_create_membre.TestFonctionnelMembreUcCreate.test_fun_14_uc_create_01_incrementation_membre_standard) ... [03/Dec/2025 20:51:32] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_gestion a crÚÚ un Membre id=1, nom=Claire Lemoine, 
compte=2025_Claire_Lemoine_1
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_gestion a crÚÚ un Membre id=2, nom=Claire 
Lemoine, compte=2025_Claire_Lemoine_2
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [MembreCreate] utilisateur=testbib_gestion a crÚÚ un Membre id=3, nom=Claire 
Lemoine, compte=2025_Claire_Lemoine_3
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_15_uc_create_02_incrementation_membre_emprunteur 
(bibliothecaire.tests_blocs.test_uc_create_membre.TestFonctionnelMembreUcCreate.test_fun_15_uc_create_02_incrementation_membre_emprunteur) ... [03/Dec/2025 20:51:32] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_gestion a crÚÚ un Membre Emprunteur id=1, nom=David 
Morel, compte=2025_David_Morel_1
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_gestion a crÚÚ un 
Membre Emprunteur id=2, nom=David Morel, compte=2025_David_Morel_2
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [MembreCreateEmprunteur] utilisateur=testbib_gestion a crÚÚ un 
Membre Emprunteur id=3, nom=David Morel, compte=2025_David_Morel_3
[03/Dec/2025 20:51:32] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_form_04_champ_name_visible_et_label (bibliothecaire.tests_blocs.test_uc_create_membre.TestFormulairesMembreUcCreate.test_form_04_champ_name_visible_et_label) ... [03/Dec/2025 
20:51:34] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_14_acces_vue_creation_membre (bibliothecaire.tests_blocs.test_uc_create_membre.TestNavigationMembreUcCreate.test_nav_14_acces_vue_creation_membre) ... [03/Dec/2025 20:51:35] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_15_acces_vue_creation_emprunteur (bibliothecaire.tests_blocs.test_uc_create_membre.TestNavigationMembreUcCreate.test_nav_15_acces_vue_creation_emprunteur) ... [03/Dec/2025 
20:51:36] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_16_titre_dynamique_selon_contexte (bibliothecaire.tests_blocs.test_uc_create_membre.TestVuesMembreUcCreate.test_vue_16_titre_dynamique_selon_contexte) ... [03/Dec/2025 20:51:37] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:37] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ajouter/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_17_suppression_logique_membre_sans_emprunt (bibliothecaire.tests_blocs.test_uc_delete_membre.TestEntitesMembreUcDelete.test_ent_17_suppression_logique_membre_sans_emprunt) ... 
[03/Dec/2025 20:51:39] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/supprimer/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_18_refus_suppression_membre_avec_emprunt (bibliothecaire.tests_blocs.test_uc_delete_membre.TestEntitesMembreUcDelete.test_ent_18_refus_suppression_membre_avec_emprunt) ... 
[03/Dec/2025 20:51:39] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/2/supprimer/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_19_suppression_reussie_membre_sans_emprunt (bibliothecaire.tests_blocs.test_uc_delete_membre.TestFonctionnelMembreUcDelete.test_fun_19_suppression_reussie_membre_sans_emprunt) 
... [03/Dec/2025 20:51:40] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/supprimer/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_20_suppression_refusee_membre_avec_emprunt (bibliothecaire.tests_blocs.test_uc_delete_membre.TestFonctionnelMembreUcDelete.test_fun_20_suppression_refusee_membre_avec_emprunt) 
... [03/Dec/2025 20:51:41] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/2/supprimer/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_form_07_confirmation_suppression_affiche_donnees 
(bibliothecaire.tests_blocs.test_uc_delete_membre.TestFormulairesMembreUcDelete.test_form_07_confirmation_suppression_affiche_donnees) ... [03/Dec/2025 20:51:42] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/1/supprimer/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_18_acces_vue_confirmation_suppression (bibliothecaire.tests_blocs.test_uc_delete_membre.TestNavigationMembreUcDelete.test_nav_18_acces_vue_confirmation_suppression) ... 
[03/Dec/2025 20:51:44] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/supprimer/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_19_lien_suppression_visible_si_autorisÚ (bibliothecaire.tests_blocs.test_uc_delete_membre.TestVuesMembreUcDelete.test_vue_19_lien_suppression_visible_si_autorisÚ) ... 
[03/Dec/2025 20:51:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_20_lien_suppression_non_visible_si_emprunt (bibliothecaire.tests_blocs.test_uc_delete_membre.TestVuesMembreUcDelete.test_vue_20_lien_suppression_non_visible_si_emprunt) ... 
[03/Dec/2025 20:51:46] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_42_creation_jeu_valide (bibliothecaire.tests_blocs.test_uc_gestion_jeu.TestFonctionnelJeu.test_fun_42_creation_jeu_valide) ... [03/Dec/2025 20:51:47] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [JeuCreate] utilisateur=testbib_gestion a crÚÚ un Jeu id=21, nom=Nouveau Jeu, annÚe=2020
[03/Dec/2025 20:51:47] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/jeux/ajouter/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_43_modification_jeu (bibliothecaire.tests_blocs.test_uc_gestion_jeu.TestFonctionnelJeu.test_fun_43_modification_jeu) ... [03/Dec/2025 20:51:47] [INFO] <bibliothecaire.decorator> 
"POST /bibliothecaire/jeux/16/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:47] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/jeux/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_44_liste_cliquable (bibliothecaire.tests_blocs.test_uc_gestion_jeu.TestFonctionnelJeu.test_fun_44_liste_cliquable) ... [03/Dec/2025 20:51:48] [INFO] <bibliothecaire.decorator> 
"GET /bibliothecaire/jeux/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_45_indicateurs_accueil (bibliothecaire.tests_blocs.test_uc_gestion_jeu.TestFonctionnelJeu.test_fun_45_indicateurs_accueil) ... [03/Dec/2025 20:51:48] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_28_acces_liste_jeux (bibliothecaire.tests_blocs.test_uc_gestion_jeu.TestNavigationJeu.test_nav_28_acces_liste_jeux) ... [03/Dec/2025 20:51:49] [INFO] <bibliothecaire.decorator> 
"GET /bibliothecaire/jeux/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_29_acces_detail_jeu (bibliothecaire.tests_blocs.test_uc_gestion_jeu.TestNavigationJeu.test_nav_29_acces_detail_jeu) ... [03/Dec/2025 20:51:50] [INFO] <bibliothecaire.decorator> 
"GET /bibliothecaire/jeux/16/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_30_acces_creation_jeu (bibliothecaire.tests_blocs.test_uc_gestion_jeu.TestNavigationJeu.test_nav_30_acces_creation_jeu) ... [03/Dec/2025 20:51:50] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/jeux/ajouter/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_31_acces_modification_jeu (bibliothecaire.tests_blocs.test_uc_gestion_jeu.TestNavigationJeu.test_nav_31_acces_modification_jeu) ... [03/Dec/2025 20:51:50] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/jeux/16/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_05_consultable_objects_only (bibliothecaire.tests_blocs.test_uc_list_media.MediaConsultableViewTests.test_ent_05_consultable_objects_only)
T-ENT-05 : VÚrifie que tous les objets affichÚs ont consultable=True ... [03/Dec/2025 20:51:52] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/consultables/ HTTP/1.1" 200 0 
: [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_01_uc_list_01_verification (bibliothecaire.tests_blocs.test_uc_list_media.MediaConsultableViewTests.test_fun_01_uc_list_01_verification)
T-FUN-01 : VÚrification fonctionnelle du cas dÆusage UC-LIST-01 ... [03/Dec/2025 20:51:52] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/consultables/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_05_url_and_template (bibliothecaire.tests_blocs.test_uc_list_media.MediaConsultableViewTests.test_nav_05_url_and_template)
T-NAV-05 : AccÞs Ó la vue consultable et vÚrification du template ... [03/Dec/2025 20:51:53] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/consultables/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_06_title_displayed (bibliothecaire.tests_blocs.test_uc_list_media.MediaConsultableViewTests.test_vue_06_title_displayed)
T-VUE-06 : VÚrifie que le titre <h2> correspond Ó la vue consultable ... [03/Dec/2025 20:51:53] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/consultables/ HTTP/1.1" 200 0 
: [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_06_disponible_objects_only (bibliothecaire.tests_blocs.test_uc_list_media.MediaDisponibleViewTests.test_ent_06_disponible_objects_only)
T-ENT-06 : VÚrifie que tous les objets affichÚs ont disponible=True ... [03/Dec/2025 20:51:54] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/disponibles/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_02_uc_list_02_verification (bibliothecaire.tests_blocs.test_uc_list_media.MediaDisponibleViewTests.test_fun_02_uc_list_02_verification)
T-FUN-02 : VÚrification fonctionnelle du cas dÆusage UC-LIST-02 ... [03/Dec/2025 20:51:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/disponibles/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_06_url_and_template (bibliothecaire.tests_blocs.test_uc_list_media.MediaDisponibleViewTests.test_nav_06_url_and_template)
T-NAV-06 : AccÞs Ó la vue disponible et vÚrification du template ... [03/Dec/2025 20:51:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/disponibles/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_07_title_displayed (bibliothecaire.tests_blocs.test_uc_list_media.MediaDisponibleViewTests.test_vue_07_title_displayed)
T-VUE-07 : VÚrifie que le titre <h2> correspond Ó la vue disponibles ... [03/Dec/2025 20:51:55] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/disponibles/ HTTP/1.1" 200 0 
: [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_09_type_objects_only (bibliothecaire.tests_blocs.test_uc_list_media.MediaNonTypeViewTests.test_ent_09_type_objects_only)
T-ENT-09 : VÚrifie que tous les objets affichÚs ont le bon media_type ... [03/Dec/2025 20:51:57] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/non-types/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_06_uc_list_06_verification (bibliothecaire.tests_blocs.test_uc_list_media.MediaNonTypeViewTests.test_fun_06_uc_list_06_verification)
T-FUN-06 : VÚrifie la cohÚrence fonctionnelle de UC-LIST-04 ... [03/Dec/2025 20:51:57] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/non-types/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_09_url_and_template (bibliothecaire.tests_blocs.test_uc_list_media.MediaNonTypeViewTests.test_nav_09_url_and_template)
T-NAV-09 : VÚrifie lÆaccÞs et le template pour chaque type ... [03/Dec/2025 20:51:57] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/non-types/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_10_title_displayed (bibliothecaire.tests_blocs.test_uc_list_media.MediaNonTypeViewTests.test_vue_10_title_displayed)
T-VUE-10 : VÚrifie que le titre <h2> correspond au type demandÚ ... [03/Dec/2025 20:51:58] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/non-types/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_07_type_objects_only (bibliothecaire.tests_blocs.test_uc_list_media.MediaTypeViewTests.test_ent_07_type_objects_only)
T-ENT-07 : VÚrifie que tous les objets affichÚs ont le bon media_type ... [03/Dec/2025 20:51:59] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:59] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:51:59] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_03_uc_list_03_verification (bibliothecaire.tests_blocs.test_uc_list_media.MediaTypeViewTests.test_fun_03_uc_list_03_verification)
T-FUN-03 : VÚrifie la cohÚrence fonctionnelle de UC-LIST-03 ... [03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_07_url_and_template (bibliothecaire.tests_blocs.test_uc_list_media.MediaTypeViewTests.test_nav_07_url_and_template)
T-NAV-07 : VÚrifie lÆaccÞs et le template pour chaque type ... [03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_08_title_displayed (bibliothecaire.tests_blocs.test_uc_list_media.MediaTypeViewTests.test_vue_08_title_displayed)
T-VUE-08 : VÚrifie que le titre <h2> correspond au type demandÚ ... [03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : 
[ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:00] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/types/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_10_filtrage_statut_non_archive (bibliothecaire.tests_blocs.test_uc_list_membre.TestEntitesMembreUcList.test_ent_10_filtrage_statut_non_archive) ... [03/Dec/2025 20:52:02] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/liste HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_11_filtrage_statut_emprunteur (bibliothecaire.tests_blocs.test_uc_list_membre.TestEntitesMembreUcList.test_ent_11_filtrage_statut_emprunteur) ... [03/Dec/2025 20:52:02] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/emprunteurs HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_12_filtrage_statut_archive (bibliothecaire.tests_blocs.test_uc_list_membre.TestEntitesMembreUcList.test_ent_12_filtrage_statut_archive) ... [03/Dec/2025 20:52:02] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/supprimes HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_11_uc_list_02_membres_non_archives (bibliothecaire.tests_blocs.test_uc_list_membre.TestFonctionnelMembreUcList.test_fun_11_uc_list_02_membres_non_archives) ... [03/Dec/2025 
20:52:04] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_12_uc_list_03_membres_emprunteurs (bibliothecaire.tests_blocs.test_uc_list_membre.TestFonctionnelMembreUcList.test_fun_12_uc_list_03_membres_emprunteurs) ... [03/Dec/2025 
20:52:04] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/emprunteurs HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_13_uc_list_04_membres_archives (bibliothecaire.tests_blocs.test_uc_list_membre.TestFonctionnelMembreUcList.test_fun_13_uc_list_04_membres_archives) ... [03/Dec/2025 20:52:05] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/supprimes HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_10_acces_vue_tous_les_membres (bibliothecaire.tests_blocs.test_uc_list_membre.TestNavigationMembreUcList.test_nav_10_acces_vue_tous_les_membres) ... [03/Dec/2025 20:52:06] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_11_acces_vue_membres_en_gestion (bibliothecaire.tests_blocs.test_uc_list_membre.TestNavigationMembreUcList.test_nav_11_acces_vue_membres_en_gestion) ... [03/Dec/2025 20:52:06] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_12_acces_vue_membres_emprunteurs (bibliothecaire.tests_blocs.test_uc_list_membre.TestNavigationMembreUcList.test_nav_12_acces_vue_membres_emprunteurs) ... [03/Dec/2025 20:52:07] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/emprunteurs HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_13_acces_vue_membres_supprimes (bibliothecaire.tests_blocs.test_uc_list_membre.TestNavigationMembreUcList.test_nav_13_acces_vue_membres_supprimes) ... [03/Dec/2025 20:52:07] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/supprimes HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_11_tableau_colonnes_presentes (bibliothecaire.tests_blocs.test_uc_list_membre.TestVuesMembreUcList.test_vue_11_tableau_colonnes_presentes) ... [03/Dec/2025 20:52:09] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_12_affichage_membres_non_archives (bibliothecaire.tests_blocs.test_uc_list_membre.TestVuesMembreUcList.test_vue_12_affichage_membres_non_archives) ... [03/Dec/2025 20:52:09] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/liste HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_13_affichage_membres_emprunteurs (bibliothecaire.tests_blocs.test_uc_list_membre.TestVuesMembreUcList.test_vue_13_affichage_membres_emprunteurs) ... [03/Dec/2025 20:52:09] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/emprunteurs HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_14_affichage_membres_archives (bibliothecaire.tests_blocs.test_uc_list_membre.TestVuesMembreUcList.test_vue_14_affichage_membres_archives) ... [03/Dec/2025 20:52:09] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/liste/supprimes HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_15_tableau_conditionnel_si_liste_vide (bibliothecaire.tests_blocs.test_uc_list_membre.TestVuesMembreUcList.test_vue_15_tableau_conditionnel_si_liste_vide) ... [03/Dec/2025 
20:52:10] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_19_transition_statut_retard (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestEntitesEmpruntUcRetard.test_ent_19_transition_statut_retard) ... ok
test_fun_21_marquage_manuel (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestFonctionnelEmpruntUcRetard.test_fun_21_marquage_manuel) ... [03/Dec/2025 20:52:13] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/emprunts/retards/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_22_marquage_automatique (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestFonctionnelEmpruntUcRetard.test_fun_22_marquage_automatique) ... [03/Dec/2025 20:52:13] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_23_toggle_affichage_tableau (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestFonctionnelEmpruntUcRetard.test_fun_23_toggle_affichage_tableau) ... [03/Dec/2025 20:52:14] 
[INFO] <bibliothecaire.decorator> "POST /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_24_toggle_affichage_masque_tableau (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestFonctionnelEmpruntUcRetard.test_fun_24_toggle_affichage_masque_tableau) ... [03/Dec/2025 
20:52:14] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/accueil/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:14] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_19_acces_vue_retard_manuel (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestNavigationEmpruntUcRetard.test_nav_19_acces_vue_retard_manuel) ... [03/Dec/2025 20:52:15] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/emprunts/retards/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_20_acces_vue_liste_emprunts (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestNavigationEmpruntUcRetard.test_nav_20_acces_vue_liste_emprunts) ... [03/Dec/2025 20:52:16] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_21_message_retard_affiche_accueil (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestVuesEmpruntUcRetard.test_vue_21_message_retard_affiche_accueil) ... [03/Dec/2025 
20:52:17] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_22_tableau_retard_affiche_si_toggle_true (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestVuesEmpruntUcRetard.test_vue_22_tableau_retard_affiche_si_toggle_true) ... 
[03/Dec/2025 20:52:18] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_23_tableau_retard_affiche_vue_manuel (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestVuesEmpruntUcRetard.test_vue_23_tableau_retard_affiche_vue_manuel) ... [03/Dec/2025 
20:52:18] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/retards/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_24_tableau_retard_colonnes_correctes (bibliothecaire.tests_blocs.test_uc_retard_emprunt.TestVuesEmpruntUcRetard.test_vue_24_tableau_retard_colonnes_correctes) ... [03/Dec/2025 
20:52:18] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/retards/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_37_selection_emprunt_redirige_confirmation (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestFonctionnelEmpruntRetour.test_fun_37_selection_emprunt_redirige_confirmation) 
... [03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_38_confirmation_retour_met_a_jour_emprunt (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestFonctionnelEmpruntRetour.test_fun_38_confirmation_retour_met_a_jour_emprunt) ... 
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmÚ 
le retour de lÆEmprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_39_retour_depuis_media_met_a_jour_emprunt (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestFonctionnelEmpruntRetour.test_fun_39_retour_depuis_media_met_a_jour_emprunt) ... 
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmÚ 
le retour de lÆEmprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:20] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_40_retour_depuis_membre_si_un_seul_emprunt (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestFonctionnelEmpruntRetour.test_fun_40_retour_depuis_membre_si_un_seul_emprunt) 
... [03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_41_retour_depuis_membre_avec_selection (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestFonctionnelEmpruntRetour.test_fun_41_retour_depuis_membre_avec_selection) ... 
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.views> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [EmpruntRetourConfirm] utilisateur=testbib_gestion a confirmÚ 
le retour de lÆEmprunt id=2, emprunteur=Martin, media=1984 (LIVRE)
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:21] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_24_acces_vue_selection_retour (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestNavigationEmpruntRetour.test_nav_24_acces_vue_selection_retour) ... [03/Dec/2025 20:52:23] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/rendre/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_25_acces_vue_confirmation_retour (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestNavigationEmpruntRetour.test_nav_25_acces_vue_confirmation_retour) ... [03/Dec/2025 
20:52:23] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_26_acces_vue_retour_depuis_media (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestNavigationEmpruntRetour.test_nav_26_acces_vue_retour_depuis_media) ... [03/Dec/2025 
20:52:23] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:23] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_27_acces_vue_retour_depuis_membre (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestNavigationEmpruntRetour.test_nav_27_acces_vue_retour_depuis_membre) ... [03/Dec/2025 
20:52:24] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_32_formulaire_retour_affiche_champs (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestVuesEmpruntRetour.test_vue_32_formulaire_retour_affiche_champs) ... [03/Dec/2025 
20:52:25] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/rendre/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_33_script_js_synchronise_champs (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestVuesEmpruntRetour.test_vue_33_script_js_synchronise_champs) ... [03/Dec/2025 20:52:26] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/rendre/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_34_affichage_confirmation_retour (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestVuesEmpruntRetour.test_vue_34_affichage_confirmation_retour) ... [03/Dec/2025 20:52:26] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_35_redirection_retour_depuis_media (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestVuesEmpruntRetour.test_vue_35_redirection_retour_depuis_media) ... [03/Dec/2025 
20:52:26] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/rendre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:26] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/emprunts/2/retour/confirmation/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_36_formulaire_retour_depuis_membre (bibliothecaire.tests_blocs.test_uc_retour_emprunt.TestVuesEmpruntRetour.test_vue_36_formulaire_retour_depuis_membre) ... [03/Dec/2025 
20:52:27] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/2/rendre/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_redirection_vers_typage_cd (bibliothecaire.tests_blocs.test_uc_typage_media.RedirectionTypageDepuisUpdateTest.test_redirection_vers_typage_cd) ... [03/Dec/2025 20:52:28] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [MediaUpdate] utilisateur=testbib_gestion a modifiÚ le mÚdia id=1, transition de type NON_DEFINI \u2192 CD
[03/Dec/2025 20:52:28] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:28] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/1/modifier/cd/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_annulation_typage (bibliothecaire.tests_blocs.test_uc_typage_media.RollbackTypageTest.test_annulation_typage) ... [03/Dec/2025 20:52:30] [INFO] <bibliothecaire.decorator> "POST 
/bibliothecaire/medias/1/annuler_typage/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:30] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_typage_en_livre (bibliothecaire.tests_blocs.test_uc_typage_media.TypageMediaTest.test_typage_en_livre) ... [03/Dec/2025 20:52:31] [INFO] <bibliothecaire.views> "POST 
/bibliothecaire/medias/1/modifier/livre/ HTTP/1.1" 302 0 : [MediaTypageLivre] utilisateur=testbib_gestion a typÚ le mÚdia id=1 en Livre, nom=└ typer, annÚe=None
[03/Dec/2025 20:52:31] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/medias/1/modifier/livre/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:31] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_15_modification_nom_membre (bibliothecaire.tests_blocs.test_uc_update_membre.TestEntitesMembreUcUpdate.test_ent_15_modification_nom_membre) ... [03/Dec/2025 20:52:33] [INFO] 
<bibliothecaire.views> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [MembreUpdate] utilisateur=testbib_gestion a modifiÚ le Membre id=1, nom=╔lodie M., 
compte=2025_╔lodie_Martin_1, statut=0
[03/Dec/2025 20:52:33] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_ent_16_activation_statut_emprunteur (bibliothecaire.tests_blocs.test_uc_update_membre.TestEntitesMembreUcUpdate.test_ent_16_activation_statut_emprunteur) ... [03/Dec/2025 20:52:33] 
[INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_gestion a activÚ le statut emprunteur 
pour Membre id=1, nom=╔lodie Martin, compte=2025_╔lodie_Martin_1
[03/Dec/2025 20:52:33] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_16_uc_update_01_modifie_nom (bibliothecaire.tests_blocs.test_uc_update_membre.TestFonctionnelMembreUcUpdate.test_fun_16_uc_update_01_modifie_nom) ... [03/Dec/2025 20:52:35] 
[INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [MembreUpdate] utilisateur=testbib_gestion a modifiÚ le Membre id=1, nom=╔lodie M., 
compte=2025_╔lodie_Martin_1, statut=0
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/modifier/ HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_17_uc_update_02_active_emprunteur (bibliothecaire.tests_blocs.test_uc_update_membre.TestFonctionnelMembreUcUpdate.test_fun_17_uc_update_02_active_emprunteur) ... [03/Dec/2025 
20:52:35] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_gestion a activÚ le statut 
emprunteur pour Membre id=1, nom=╔lodie Martin, compte=2025_╔lodie_Martin_1
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_18_uc_update_02_enchainement_activation_emprunteur 
(bibliothecaire.tests_blocs.test_uc_update_membre.TestFonctionnelMembreUcUpdate.test_fun_18_uc_update_02_enchainement_activation_emprunteur) ... [03/Dec/2025 20:52:35] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.views> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [MembreActivateEmprunteur] utilisateur=testbib_gestion a activÚ 
le statut emprunteur pour Membre id=1, nom=╔lodie Martin, compte=2025_╔lodie_Martin_1
[03/Dec/2025 20:52:35] [INFO] <bibliothecaire.decorator> "POST /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 302 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_form_05_champ_name_visible_et_modifiable (bibliothecaire.tests_blocs.test_uc_update_membre.TestFormulairesMembreUcUpdate.test_form_05_champ_name_visible_et_modifiable) ... 
[03/Dec/2025 20:52:37] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_form_06_champ_statut_non_expose (bibliothecaire.tests_blocs.test_uc_update_membre.TestFormulairesMembreUcUpdate.test_form_06_champ_statut_non_expose) ... [03/Dec/2025 20:52:37] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_16_acces_vue_update_membre (bibliothecaire.tests_blocs.test_uc_update_membre.TestNavigationMembreUcUpdate.test_nav_16_acces_vue_update_membre) ... [03/Dec/2025 20:52:39] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/1/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_17_acces_vue_activation_emprunteur (bibliothecaire.tests_blocs.test_uc_update_membre.TestNavigationMembreUcUpdate.test_nav_17_acces_vue_activation_emprunteur) ... [03/Dec/2025 
20:52:39] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_17_formulaire_update_affiche_nom (bibliothecaire.tests_blocs.test_uc_update_membre.TestVuesMembreUcUpdate.test_vue_17_formulaire_update_affiche_nom) ... [03/Dec/2025 20:52:40] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/membres/1/modifier/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_18_page_activation_emprunteur (bibliothecaire.tests_blocs.test_uc_update_membre.TestVuesMembreUcUpdate.test_vue_18_page_activation_emprunteur) ... [03/Dec/2025 20:52:41] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/membres/1/activer/emprunteur HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_01_accueil_accessible (bibliothecaire.tests_blocs.test_urls.NavigationTests.test_nav_01_accueil_accessible) ... [03/Dec/2025 20:52:42] [INFO] <bibliothecaire.decorator> "GET 
/bibliothecaire/accueil/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_02_media_list_accessible (bibliothecaire.tests_blocs.test_urls.NavigationTests.test_nav_02_media_list_accessible) ... [03/Dec/2025 20:52:43] [INFO] <bibliothecaire.decorator> 
"GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_03_media_detail_accessible (bibliothecaire.tests_blocs.test_urls.NavigationTests.test_nav_03_media_detail_accessible) ... [03/Dec/2025 20:52:43] [INFO] <bibliothecaire.decorator> 
"GET /bibliothecaire/medias/1/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_nav_04_media_detail_404 (bibliothecaire.tests_blocs.test_urls.NavigationTests.test_nav_04_media_detail_404) ... [03/Dec/2025 20:52:43] [WARNING] <django.request> Not Found: 
/bibliothecaire/medias/999/
ok
test_vue_03_media_detail_vue_type (bibliothecaire.tests_blocs.test_vues_media_detail.MediaDetailViewTests.test_vue_03_media_detail_vue_type) ... [03/Dec/2025 20:52:45] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/3/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
[03/Dec/2025 20:52:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/4/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_04a_media_detail_instance_type_livre (bibliothecaire.tests_blocs.test_vues_media_detail.MediaDetailViewTests.test_vue_04a_media_detail_instance_type_livre) ... [03/Dec/2025 
20:52:45] [INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/2/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_04b_media_detail_instance_type_dvd (bibliothecaire.tests_blocs.test_vues_media_detail.MediaDetailViewTests.test_vue_04b_media_detail_instance_type_dvd) ... [03/Dec/2025 20:52:45] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/3/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_04c_media_detail_instance_type_cd (bibliothecaire.tests_blocs.test_vues_media_detail.MediaDetailViewTests.test_vue_04c_media_detail_instance_type_cd) ... [03/Dec/2025 20:52:46] 
[INFO] <bibliothecaire.decorator> "GET /bibliothecaire/medias/4/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_05_media_detail_vue_sans_type (bibliothecaire.tests_blocs.test_vues_media_detail.MediaDetailViewTests.test_vue_05_media_detail_vue_sans_type) ... [03/Dec/2025 20:52:46] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/1/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_01_media_list_affichage (bibliothecaire.tests_blocs.test_vues_media_list.MediaListViewTests.test_vue_01_media_list_affichage) ... [03/Dec/2025 20:52:47] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_vue_02_media_list_champs_generiques (bibliothecaire.tests_blocs.test_vues_media_list.MediaListViewTests.test_vue_02_media_list_champs_generiques) ... [03/Dec/2025 20:52:48] [INFO] 
<bibliothecaire.decorator> "GET /bibliothecaire/medias/ HTTP/1.1" 200 0 : [ACCESS_GRANTED] utilisateur=testbib_gestion
ok
test_fun_46_filtrage_medias_consultables (consultation.tests_blocs.test_uc_consult_support.TestFonctionnelConsultation.test_fun_46_filtrage_medias_consultables) ... ok
test_fun_47_filtrage_jeux_consultables (consultation.tests_blocs.test_uc_consult_support.TestFonctionnelConsultation.test_fun_47_filtrage_jeux_consultables) ... ok
test_fun_48_filtrage_medias_disponibles (consultation.tests_blocs.test_uc_consult_support.TestFonctionnelConsultation.test_fun_48_filtrage_medias_disponibles) ... ok
test_fun_49_cas_liste_vide (consultation.tests_blocs.test_uc_consult_support.TestFonctionnelConsultation.test_fun_49_cas_liste_vide) ... ok
test_fun_50_persistance_filtre (consultation.tests_blocs.test_uc_consult_support.TestFonctionnelConsultation.test_fun_50_persistance_filtre) ... ok
test_fun_51_cta_accueil_consultation (consultation.tests_blocs.test_uc_consult_support.TestFonctionnelConsultation.test_fun_51_cta_accueil_consultation) ... ok
test_nav_32_acces_accueil_consultation (consultation.tests_blocs.test_uc_consult_support.TestNavigationConsultation.test_nav_32_acces_accueil_consultation) ... ok
test_nav_33_acces_liste_supports (consultation.tests_blocs.test_uc_consult_support.TestNavigationConsultation.test_nav_33_acces_liste_supports) ... ok
test_nav_34_acces_liste_medias (consultation.tests_blocs.test_uc_consult_support.TestNavigationConsultation.test_nav_34_acces_liste_medias) ... ok
test_nav_35_acces_liste_jeux (consultation.tests_blocs.test_uc_consult_support.TestNavigationConsultation.test_nav_35_acces_liste_jeux) ... ok
test_nav_36_acces_liste_medias_disponibles (consultation.tests_blocs.test_uc_consult_support.TestNavigationConsultation.test_nav_36_acces_liste_medias_disponibles) ... ok
test_nav_37_acces_liste_vide (consultation.tests_blocs.test_uc_consult_support.TestNavigationConsultation.test_nav_37_acces_liste_vide) ... ok

----------------------------------------------------------------------
Ran 198 tests in 133.940s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...

  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).

---
