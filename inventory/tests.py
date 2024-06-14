from django.test import TestCase
from .models import Item, Supplier

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
