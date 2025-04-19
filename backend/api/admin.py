from django.contrib import admin
from .models import Administrateur, Client, Produit, Categorie, Commande, Paiement, MouvementStock, Panier, ElementPanier

admin.site.register(Administrateur)
admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Commande)
admin.site.register(Paiement)
admin.site.register(MouvementStock)
admin.site.register(Panier)
admin.site.register(ElementPanier)