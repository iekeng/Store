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


    def test_create_item_with_negative_price(self):
        item = Item.objects.create(name="Negative Price Item", description="This item has a negative price", price=-10.00)
        self.assertEqual(item.price, -10.00)

    def test_create_supplier_with_empty_contact_info(self):
        supplier = Supplier.objects.create(name="Supplier without contact", contact_info="")
        self.assertEqual(supplier.contact_info, "")

    def test_update_item_name(self):
        self.item.name = "Updated Item Name"
        self.item.save()
        self.assertEqual(self.item.name, "Updated Item Name")

    def test_update_supplier_contact_info(self):
        self.supplier.contact_info = "Updated Contact Info"
        self.supplier.save()
        self.assertEqual(self.supplier.contact_info, "Updated Contact Info")

    def test_delete_item(self):
        self.item.delete()
        items = Item.objects.all()
        self.assertEqual(len(items), 0)

    def test_delete_supplier(self):
        self.supplier.delete()
        suppliers = Supplier.objects.all()
        self.assertEqual(len(suppliers), 0)

    def test_item_str_representation(self):
        self.assertEqual(str(self.item), "Test Item")

    def test_supplier_str_representation(self):
        self.assertEqual(str(self.supplier), "John Doe")

    def test_supplier_with_long_contact_info(self):
        long_contact_info = "B" * 256
        supplier = Supplier.objects.create(name="Supplier with long contact", contact_info=long_contact_info)
        self.assertEqual(supplier.contact_info, long_contact_info)
