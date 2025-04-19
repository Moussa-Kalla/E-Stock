from django.test import TestCase
from .models import Administrateur, Client, Produit, Categorie, Commande, Paiement, MouvementStock, Panier, ElementPanier

class ModelTests(TestCase):

    def setUp(self):
        self.admin = Administrateur.objects.create(username='admin', password='adminpass')
        self.client = Client.objects.create(username='client', password='clientpass')
        self.category = Categorie.objects.create(name='Electronics')
        self.product = Produit.objects.create(name='Smartphone', price=699.99, category=self.category)
        self.order = Commande.objects.create(client=self.client, status='Pending')
        self.payment = Paiement.objects.create(order=self.order, amount=699.99, status='Completed')
        self.stock_movement = MouvementStock.objects.create(product=self.product, quantity=10, movement_type='in')
        self.cart = Panier.objects.create(client=self.client)
        self.cart_item = ElementPanier.objects.create(cart=self.cart, product=self.product, quantity=1)

    def test_admin_creation(self):
        self.assertEqual(self.admin.username, 'admin')

    def test_client_creation(self):
        self.assertEqual(self.client.username, 'client')

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Smartphone')
        self.assertEqual(self.product.price, 699.99)

    def test_order_creation(self):
        self.assertEqual(self.order.client, self.client)
        self.assertEqual(self.order.status, 'Pending')

    def test_payment_creation(self):
        self.assertEqual(self.payment.order, self.order)
        self.assertEqual(self.payment.amount, 699.99)

    def test_stock_movement_creation(self):
        self.assertEqual(self.stock_movement.product, self.product)
        self.assertEqual(self.stock_movement.quantity, 10)

    def test_cart_creation(self):
        self.assertEqual(self.cart.client, self.client)

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.cart, self.cart)
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.quantity, 1)