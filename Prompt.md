Tu es un assistant développeur chargé de générer automatiquement le code source complet d'une application de gestion de stock et de vente. Le projet est divisé en deux parties : un backend Django REST Framework (Python) et un frontend React Native avec support Web (Expo + React Native Web). Voici les instructions détaillées :

=====================================================
I. OBJECTIF DE L'APPLICATION
=====================================================

Créer une application **web et mobile** de gestion de stock et de vente appelée **E-Stock**, avec les fonctionnalités suivantes :

1. **Pour les administrateurs :**
   - Authentification sécurisée (JWT)
   - CRUD Produits, Catégories, Utilisateurs
   - Gestion des mouvements de stock (entrées/sorties)
   - Gestion des commandes (statut, détails)
   - Validation des paiements
   - Gestion des dettes clients
   - Génération de rapports (ventes, stock, paiements)
   - Système d’alertes pour les seuils critiques de stock

2. **Pour les clients :**
   - Inscription / Connexion
   - Consultation du catalogue produits
   - Ajout au panier
   - Passer une commande
   - Paiement (y compris paiement différé à crédit)
   - Historique des commandes et paiements

3. **Autres fonctionnalités :**
   - Notifications push via Firebase
   - Paiement en ligne via Stripe ou MyNITA API
   - Tableau de bord statistique pour l’admin (produit le plus vendu, client le plus actif)

=====================================================
II. STACK TECHNIQUE ET OUTILS
=====================================================

- **Backend** : Django 4, Django REST Framework
- **Base de données** : PostgreSQL 
- **Auth** : JWT (djangorestframework-simplejwt)
- **Frontend** : React Native avec Expo (et React Native Web) 
- **Notifications** : Firebase Cloud Messaging (FCM)
- **Paiement** : Stripe API (et possibilité d’intégrer MyNITA), carte bancaire et autres
- **Déploiement recommandé** :
  - Une image Docker, ecrit le Dockerfile
  - Backend : Render / Railway / VPS (avec Gunicorn + Nginx)
  - Frontend Web : Vercel / Netlify / Render
  - Mobile : Expo Build, Play Store / App Store

=====================================================
III. STRUCTURE DU PROJET À GÉNÉRER
=====================================================

Créer les dossiers et fichiers suivants :


```bash
bayanai-app/
├── backend/
│   ├── bayanai/                 # Projet Django
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── …
│   ├── api/                     # App principale (stock, ventes, etc.)
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── permissions.py
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── App.js
│   ├── app.json
│   ├── assets/
│   ├── components/
│   ├── screens/
│   │   ├── LoginScreen.js
│   │   ├── ProductListScreen.js
│   │   ├── AdminDashboard.js
│   │   └── …
│   ├── navigation/
│   │   └── AppNavigator.js
│   ├── services/               # Appels API backend
│   │   └── api.js
│   └── package.json
│
├── .gitignore
├── README.md
└── docker-compose.yml          # (optionnel mais recommandé)
````

=====================================================
IV. INSTRUCTIONS COMPLÉMENTAIRES POUR LA GÉNÉRATION
=====================================================

- Tous les modèles Django doivent suivre les classes du diagramme de classes :
  - Administrateur, Client, Produit, Categorie, Commande, Paiement, MouvementStock, Panier, ElementPanier
- Utiliser des relations ForeignKey appropriées
- Ajouter une gestion des rôles avec des permissions spécifiques (IsAdmin, IsClient)
- Intégrer la pagination, la recherche et les filtres dans les endpoints
- Prévoir un système de notification via Firebase en cas de seuil critique de stock
- Séparer les rôles avec un système d’authentification centralisé
- Le frontend doit appeler l’API REST du backend via Axios ou Fetch
- Créer des composants réutilisables pour les boutons, champs de formulaire, listes de produits, etc.
- Le style doit être simple, responsive et compatible Web + Mobile
- Prévoir un tableau de bord admin avec quelques KPI visibles

=====================================================

Génère le code de ce projet en respectant la structure, la logique métier, et les technologies spécifiées ci-dessus. Commence par le backend puis passe au frontend. Crée des exemples de données (fixtures) si nécessaire pour faciliter les tests.
