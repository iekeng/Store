from django.test import TestCase
# from django.urls import reverse
from .models import Item, Supplier
# from django.db import models
# from django.db.models import Q
# from django.db.models.query import QuerySet
from django.http import JsonResponse
from .views import ItemListCreate, ItemRetrieveUpdateDestroy, SupplierListCreate, SupplierRetrieveUpdateDestroy

class ItemTestCase(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="Test Item", description="This is a test item", price=25.00)
        self.supplier = Supplier.objects.create(name="John Doe", contact_info="Brooklyn, NY")

    def test_item_name(self):
        self.assertEqual(self.item.name, "Test Item")

    def test_item_description(self):
        self.assertEqual(self.item.description, "This is a test item")

    def test_item_price(self):
        self.assertEqual(self.item.price, 25.00)

    def test_item_list(self):
        items = Item.objects.all()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].name, "Test Item")
        self.assertEqual(items[0].description, "This is a test item")
        self.assertEqual(items[0].price, 25.00)

    def test_supplier_name(self):
        self.assertEqual(self.supplier.name, "John Doe")

    def test_supplier_contact(self):
        self.assertEqual(self.supplier.contact_info, "Brooklyn, NY")

    def test_supplier_list(self):
        supplier = Supplier.objects.all()
        self.assertEqual(len(supplier), 1)
        self.assertEqual(supplier[0].name, "John Doe")
        self.assertEqual(supplier[0].contact_info, "Brooklyn, NY")

# class MockDatabase(models.Model):
#     name = models.CharField(max_length=25)
#     contact_info = models.CharField(max_length=25)

# class MockQuerySet(QuerySet):
#     def __init__(self, model):
#         self.model = model

#     def filter(self, **kwargs):
#         return self
    
# class MockDatabaseManager(models.Manager):
#     def get_queryset(self):
#         return MockQuerySet(self.model)

# class MockDatabaseModel(models.Model):
#     objects = MockDatabaseManager()

#     def __str__(self):
#         return self.name
    
# class ItemListCreateviewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.mock_database = MockDatabase(name='Supplier')
#         self.mock_database.save()

#     def test_list_items(self):
#         response = self.client.get('/supplier')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Supplier')

    # def test_create_item(self):
    #     data = {'name': 'New Item', 'description': 'This is a new item'}
    #     response = self.content.post(reverse('item_list'), data, format='json')
    #     self.asserEqual(response.status_code, 201)
    #     self.assertJSONEqual(str(response.content, 'utf-8'), {'id': 3, 'name': "New Item", "description": "This is a new item."})

# def ItemListCreate(request):
#     if request.method == 'GET':
#         items = Item.objects.all()
#         items_data = [{"name": item.name, "description": item.description, "price": item.price} for item in items]
#         return JsonResponse(items_data, safe=False)
    # elif request.method == 'POST':
    #     # Assuming JSON input
    #     data = json.loads(request.body)
    #     item = Item.objects.create(name=data['name'], description=data['description'], price=data['price'])
    #     return JsonResponse({"id": item.id, "name": item.name, "description": item.description, "price": item.price}, status=201)

# from django.test import TestCase
# from rest_framework.test import APIClient
# from .views import ItemListCreate, ItemRetrieveUpdateDestroy, SupplierListCreate, SupplierRetrieveUpdateDestroy

# class TestItemViews(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_item_list_create(self):
#         response = self.client.get('/items/')
#         self.assertEqual(response.status_code, 200)
#         # self.assertEqual(len(response.json()), 0)

#         data = {'name': 'Item 1', 'description': 'This is item 1'}
#         response = self.client.post('/items/', data, format='json')
#         self.assertEqual(response.status_code, 201)
#         # self.assertEqual(response.json()['name'], 'Item 1')

#     def test_item_retrieve_update_destroy(self):
#         data = {'name': 'Item 1', 'description': 'This is item 1'}
#         response = self.client.post('/items/', data, format='json')
#         self.assertEqual(response.status_code, 201)
#         item_id = response.json()['id']

#         response = self.client.get(f'/items/{item_id}/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()['name'], 'Item 1')

#         data = {'name': 'Updated Item 1', 'description': 'This is updated item 1'}
#         response = self.client.put(f'/items/{item_id}/', data, format='json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()['name'], 'Updated Item 1')

#         response = self.client.delete(f'/items/{item_id}/')
#         self.assertEqual(response.status_code, 204)

# class TestSupplierViews(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_supplier_list_create(self):
#         response = self.client.get('/suppliers/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.json()), 0)

#         data = {'name': 'Supplier 1', 'address': 'This is supplier 1'}
#         response = self.client.post('/suppliers/', data, format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.json()['name'], 'Supplier 1')

#     def test_supplier_retrieve_update_destroy(self):
#         data = {'name': 'Supplier 1', 'address': 'This is supplier 1'}
#         response = self.client.post('/suppliers/', data, format='json')
#         self.assertEqual(response.status_code, 201)
#         supplier_id = response.json()['id']

#         response = self.client.get(f'/suppliers/{supplier_id}/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()['name'], 'Supplier 1')

#         data = {'name': 'Updated Supplier 1', 'address': 'This is updated supplier 1'}
#         response = self.client.put(f'/suppliers/{supplier_id}/', data, format='json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()['name'], 'Updated Supplier 1')

#         response = self.client.delete(f'/suppliers/{supplier_id}/')
#         self.assertEqual(response.status_code, 204)

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Item, Supplier
from .serializers import ItemSerializer, SupplierSerializer
from .views import ItemListCreate, ItemRetrieveUpdateDestroy, SupplierListCreate, SupplierRetrieveUpdateDestroy

class TestItemViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Item.objects.create(name='Item 1', description='Description 1', price=10.00)
        self.item2 = Item.objects.create(name='Item 2', description='Description 2', price=20.00)

    def test_item_list(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_item_create(self):
        data = {'name': 'Item 3', 'description': 'Description 3', 'price': 30.00}
        response = self.client.post('/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'Item 3')

    def test_item_retrieve(self):
        response = self.client.get(f'/items/{self.item1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Item 1')

    def test_item_update(self):
        data = {'name': 'Updated Item 1', 'description': 'Updated Description 1', 'price': 11.00}
        response = self.client.put(f'/items/{self.item1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Updated Item 1')

    def test_item_delete(self):
        response = self.client.delete(f'/items/{self.item1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TestSupplierViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier1 = Supplier.objects.create(name='Supplier 1', contact_info='Contact 1')
        self.supplier2 = Supplier.objects.create(name='Supplier 2', contact_info='Contact 2')

    def test_supplier_list(self):
        response = self.client.get('/suppliers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_supplier_create(self):
        data = {'name': 'Supplier 3', 'contact_info': 'Contact 3'}
        response = self.client.post('/suppliers/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'Supplier 3')

    def test_supplier_retrieve(self):
        response = self.client.get(f'/suppliers/{self.supplier1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Supplier 1')

    def test_supplier_update(self):
        data = {'name': 'Updated Supplier 1', 'contact_info': 'Updated Contact 1'}
        response = self.client.put(f'/suppliers/{self.supplier1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Updated Supplier 1')

    def test_supplier_delete(self):
        response = self.client.delete(f'/suppliers/{self.supplier1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)