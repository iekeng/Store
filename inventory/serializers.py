from rest_framework import serializers
from .models import Item, Supplier

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supplier
    fields = '__all__'