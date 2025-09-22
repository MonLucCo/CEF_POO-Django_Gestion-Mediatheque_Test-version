# 🧾 Note technique – Mémento des commandes Django liées aux migrations

| Commande         | Usage                                                                               | Exemple                                           |
|------------------|-------------------------------------------------------------------------------------|---------------------------------------------------|
| `check`          | Vérifie la cohérence du projet (modèles, config) sans toucher à la base             | `python manage.py check`                          |
| `makemigrations` | Génère les fichiers de migration à partir des modèles                               | `python manage.py makemigrations bibliothecaire`  |
| `showmigrations` | Affiche toutes les migrations disponibles et leur statut                            | `python manage.py showmigrations`                 |
| `migrate`        | Applique les migrations à la base de données                                        | `python manage.py migrate`                        |
| `sqlmigrate`     | Affiche le SQL généré par une migration (sans l’exécuter)                           | `python manage.py sqlmigrate bibliothecaire 0001` |
| `flush`          | Réinitialise la base en supprimant toutes les données (sans toucher aux migrations) | `python manage.py flush`                          |

💡 Ces commandes sont à utiliser dans l’ordre suivant :

1. Modifier les modèles (`models.py`)
2. `makemigrations`
3. `sqlmigrate` (optionnel, pour inspection)
4. `migrate`
5. `flush` (optionnel, pour réinitialiser les données sans supprimer les migrations)
6. `check` (à tout moment pour valider la cohérence)

---
