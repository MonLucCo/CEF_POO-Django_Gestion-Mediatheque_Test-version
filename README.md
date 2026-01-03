# 📚 CEF POO Django – Gestion de Médiathèque

## 🎯 Objectif

Ce projet pédagogique vise à développer une application web de gestion de médiathèque en utilisant **Django** et les principes de la **programmation orientée objet (POO)**.

Le rapport de ce projet : [Rapport](/delivery/rapport/rapport-projet.md).

Configuration du projet : [Requirements](/delivery/rapport/requirements-projet.txt)

---

## 🚀 Installation rapide

```bash
git clone https://github.com/MonLucCo/CEF_POO-Django_Gestion-Mediatheque_Test-version.git
cd CEF_POO-Django_Gestion-Mediatheque_Test-version

cd works
python -m venv venv
venv\Scripts\activate.bat

pip install -r ../requirements.txt

cd mediatheque
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py runserver 8900
```

Accès local : [http://127.0.0.1:8900](http://127.0.0.1:8900)

---

## 📁 Structure du dépôt

```
CEF_POO-Django_Gestion-Mediatheque_Test-version/
├── delivery/           # Livrables
├── docs/               # Documentation technique et fonctionnelle
├── works/              # Projet Django et environnement virtuel
├── requirements.txt    # Dépendances du projet
└── README.md           # Présentation générale du projet
```

---

## 📎 Documentation

La documentation complète est disponible dans le dossier [`/docs`](docs/README.md), organisée par thème :
- [Spécifications fonctionnelles](docs/fonctionnel/README-fonct.md)
- [Documentation technique](docs/technique/README-tech.md)
- [Suivi du développement](docs/developpement/README-dev.md)
- [Architecture du projet](docs/architecture/README-archi.md)

Le [rapport de projet](delivery/rapport/rapport-projet.md) est disponible dans le dossier `/delivery` dans sa version _actualisée_ tout au long du projet.

---

## 🤝 Contribution

Ce projet est réalisé dans un cadre **pédagogique individuel**.  
Aucune contribution externe n’est demandée.

---

## 📄 Licence

Distribué sous la [licence **MIT**](LICENSE).

---

## 👤 Auteur

**PerLucCo**  
Micro-entreprise – Développement Web et Web Mobile  
📍 Vélizy-Villacoublay, France
---
