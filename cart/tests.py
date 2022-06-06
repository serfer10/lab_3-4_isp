from django.contrib.auth import get_user_model
from django.test import TestCase

from .cart import Cart

# Create your tests here.


class Test(TestCase):
    def setUp(self):
        User = get_user_model()

    def test_checkCart(self):
        products = Cart.objects.all()
        self.assertEqual(products, products)
