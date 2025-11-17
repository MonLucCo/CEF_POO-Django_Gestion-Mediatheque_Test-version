### Annexe A – Extraits de code clés

---

> 📎 **Annexe liée au rapport principal**  
> Cette annexe fait partie intégrante du rapport de projet *Application Médiathèque Django*.  
> Elle est référencée dans le sommaire du rapport principal (`rapport-projet.md`) et documente les extraits de code emblématiques liés aux règles métier et aux vues stratégiques.  
>  
> 🔗 Pour le contexte complet, se reporter à la section :  
> `[4.1 – Application bibliothécaire]`

---

> 📌 Cette annexe sera enrichie dans l’issue #7 avec les extraits finaux des tests, des templates et des vues de 
> consultation.

Cette annexe regroupe les extraits emblématiques du projet, sélectionnés pour illustrer les règles métier, les vues 
stratégiques et les requêtes typiques.  
Chaque extrait est accompagné d’un commentaire succinct et d’un renvoi vers le fichier source ou la section du rapport 
concernée.

---

#### A.1 Méthodes métier – Modèle `Membre`

```python
def peut_emprunter(self):
    return (
        self.is_emprunteur
        and not (self.is_max_emprunt or self.is_retard)
    )
```

> 📌 Vérifie si le membre est autorisé à emprunter selon son statut, ses retards et ses emprunts en cours.  
> 📄 Source : `models.py` – Section [4.1.1.1](rapport-projet.md#4111-modélisation---code-partiel-de-la-structure-et-des-méthodes-et-propriétés-du-modèle)

---

#### A.2 Méthode métier – Modèle `Emprunt`

```python
def enregistrer_retour(self):
    if not self.date_retour:
        self.date_retour = timezone.now().date()
        self.media.rendre_disponible()
        self.save()
        return True
    return False
```

> 📌 Enregistre le retour d’un emprunt et rend le média disponible.  
> 📄 Source : `models.py` – Section [4.1.3.1](rapport-projet.md#4131-modélisation-de-lemprunt--contraintes-métier)

---

#### A.3 Vue de confirmation – `EmpruntRetourConfirmView`

```python
def form_valid(self, form):
    emprunt = self.get_object()
    if emprunt.enregistrer_retour():
        messages.success(self.request, f"Emprunt rendu : {emprunt.emprunteur.name} → {emprunt.media.name}")
    else:
        messages.warning(self.request, "Cet emprunt ne peut pas être rendu.")
    return redirect(self.get_success_url())
```

> 📌 Gère la validation du retour d’un emprunt avec message UX et redirection.  
> 📄 Source : `views.py` – Section [4.1.3.3](rapport-projet.md#4133-vues-des-retours)

---

#### A.4 Requête ORM – Emprunts rendus

```python
Emprunt.objects.filter(date_retour__isnull=False)
```

> 📌 Sélectionne tous les emprunts ayant été rendus.  
> 📄 Utilisé dans le shell Django – Section [6.3](rapport-projet.md#63-exemple-dinsertion-et-requêtes-de-vérification)

---

#### A.5 Accès à l’objet typé – Héritage multi-table

```python
def get_object(self):
    obj = super().get_object()
    if hasattr(obj, 'livre'):
        return obj.livre
    elif hasattr(obj, 'dvd'):
        return obj.dvd
    elif hasattr(obj, 'cd'):
        return obj.cd
    return obj
```

> 📌 Permet d’accéder à l’instance réelle du sous-type `Media` dans une vue Django.  
> 📄 Source : `views.py` – Décrit dans `devMC.md` §9.4

---

#### A.6 Création d’un média typé – Shell Django

```python
livre = Livre.objects.create(
    name="1984",
    media_type="LIVRE",
    disponible=True,
    consultable=True,
    auteur="George Orwell"
    resume="Histoire extraordinaire : à lire absolument !"
)
```

> 📌 Création d’un `Livre` avec héritage multi-table, directement depuis le shell Django.  
> 📄 Section [6.3](rapport-projet.md#63-exemple-dinsertion-et-requêtes-de-vérification)

---
