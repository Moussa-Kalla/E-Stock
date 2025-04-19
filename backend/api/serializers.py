from rest_framework import serializers
from .models import Administrateur, Client, Produit, Categorie, Commande, Paiement, MouvementStock, Panier, ElementPanier

class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'

class MouvementStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MouvementStock
        fields = '__all__'

class PanierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panier
        fields = '__all__'

class ElementPanierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementPanier
        fields = '__all__'