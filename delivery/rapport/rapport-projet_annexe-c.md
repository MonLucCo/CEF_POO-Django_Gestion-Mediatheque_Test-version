### Annexe C - Diagrammes (UML, séquence)

---

#### C.1 Diagramme de classes (simplifié)

Le diagramme ci‑dessous présente la hiérarchie des principales entités du projet Médiathèque.  
Il met en évidence l’héritage entre les médias et les relations avec les membres et les emprunts.

```plaintext
                Media
        ┌─────────┼─────────┐
        │         │         │
      Livre      DVD        CD
       
JeuDePlateau (indépendant)

Membre ────────┐
               │
               └── Emprunt ─── Media
```

- **Media** : classe abstraite regroupant les attributs communs (titre, auteur, disponibilité).  
- **Livre, DVD, CD** : spécialisations de Media.  
- **JeuDePlateau** : entité indépendante, non empruntable, uniquement consultable.  
- **Membre** : utilisateur de la médiathèque, peut être simple ou emprunteur.  
- **Emprunt** : relie un Membre à un Media, avec contraintes (3 emprunts max, délais, retards).

---

#### C.2 Diagramme de séquence (scénario : emprunt d’un média)

Ce diagramme illustre le déroulement d’un emprunt par un membre, depuis l’authentification jusqu’à la traçabilité par 
log.

```plaintext
Membre        Accounts        Bibliothecaire        Emprunt        Logger
  │              │                  │                 │              │
  │── Login ────>│                  │                 │              │
  │              │── Redirection ──>│                 │              │
  │              │                  │── Créer emprunt ─>│            │
  │              │                  │                 │── Associer ─>│
  │              │                  │                 │              │── [EmpruntCreate]
  │              │                  │                 │              │
```

- Le **Membre** se connecte via `accounts`.  
- Redirection vers l’espace **Bibliothécaire** selon le rôle.  
- Création d’un **Emprunt** associant le Membre et le Media choisi.  
- Le **Logger** enregistre la trace `[EmpruntCreate]` dans `mediatheque.log` ou `mediatheque_test.log`.

---

#### C.3 Commentaire

Ces diagrammes offrent une vision synthétique de :
- la **structure des classes** (héritage et relations principales),  
- la **dynamique des interactions** lors d’un scénario critique (emprunt).  

Ils complètent le tableau des accès et des logs en fournissant une représentation visuelle de la logique métier et de la 
traçabilité.

---

