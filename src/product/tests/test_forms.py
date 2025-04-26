from django.test import TestCase
from product.forms import ProductForm
from category.models import Category, Region
from django.contrib.auth.models import User
from product.models import Product

class ProductFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.region = Region.objects.create(name='Tashkent', sorting=1)

    def test_product_form_valid_data(self):
        form_data = {
            'title': 'Smartphone',
            'category': self.category.id,
            'location': self.region.id,  # bu joy to‘g‘ri
            'description': 'Brand new smartphone with awesome features',
            'price': 250.00,
            'condition': 'new'  # bu yerda condition qo‘shdik!
        }
        form = ProductForm(data=form_data)
        print("FORM ERRORS:", form.errors)
        self.assertTrue(form.is_valid())

    def test_product_form_invalid_data(self):
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())



