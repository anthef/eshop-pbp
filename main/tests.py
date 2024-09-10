from django.db import models
from django.test import TestCase, Client
from .models import ProductEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_create_product_entry(self):
        product = ProductEntry.objects.create(
            name="Test Product",
            price=100,
            description="This is a test product."
        )
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.description, "This is a test product.")

    def test_product_entry_str(self):
        product = ProductEntry.objects.create(
            name="Test Product",
            price=100,
            description="This is a test product."
        )
        self.assertEqual(str(product), "Test Product")

    def test_product_entry_can_be_saved_and_retrieved(self):
        product = ProductEntry.objects.create(
            name="Another Test Product",
            price=200,
            description="This is another test product."
        )
        saved_product = ProductEntry.objects.get(id=product.id)
        self.assertEqual(saved_product.name, "Another Test Product")
        self.assertEqual(saved_product.price, 200)
        self.assertEqual(saved_product.description, "This is another test product.")
