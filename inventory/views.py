from rest_framework import generics
from .models import Supplier, Item
from .serializers import SupplierSerializer, ItemSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class ItemListCreate(generics.ListCreateAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [IsAuthenticated, DjangoModelPermissions]
  
class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [IsAuthenticated, DjangoModelPermissions]

class SupplierListCreate(generics.ListCreateAPIView):
  queryset = Supplier.objects.all()
  serializer_class = SupplierSerializer
  permission_classes = [IsAuthenticated, DjangoModelPermissions]
  
class SupplierRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Supplier.objects.all()
  serializer_class = SupplierSerializer
  permission_classes = [IsAuthenticated, DjangoModelPermissions]
  

