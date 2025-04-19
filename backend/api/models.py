from django.db import models
from django.contrib.auth.models import AbstractUser

class Administrateur(AbstractUser):
    pass  # You can add additional fields if needed

class Client(models.Model):
    user = models.OneToOneField(Administrateur, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

class Categorie(models.Model):
    name = models.CharField(max_length=100)

class Produit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Categorie, related_name='produits', on_delete=models.CASCADE)

class Commande(models.Model):
    client = models.ForeignKey(Client, related_name='commandes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)  # e.g., 'pending', 'completed', 'canceled'

class Paiement(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

class MouvementStock(models.Model):
    produit = models.ForeignKey(Produit, related_name='mouvements', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=10)  # e.g., 'in', 'out'
    created_at = models.DateTimeField(auto_now_add=True)

class Panier(models.Model):
    client = models.ForeignKey(Client, related_name='panier', on_delete=models.CASCADE)

class ElementPanier(models.Model):
    panier = models.ForeignKey(Panier, related_name='elements', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name='elements_panier', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()