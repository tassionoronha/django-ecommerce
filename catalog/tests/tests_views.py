from django.test import TestCase, Client
from catalog.models import Product, Category
from django.urls import reverse
from model_mommy import mommy

class ProductListTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('catalog:product_list')
        self.products = mommy.make(Product, _quantity=10)

    def tearDown(self):
        for p in self.products:
            p.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        product_list = response.context['products']
        self.assertEquals(len(product_list), 10)
