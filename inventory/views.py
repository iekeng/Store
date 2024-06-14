from rest_framework import generics
from .models import Supplier, Item
from .serializers import SupplierSerializer, ItemSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class ItemListCreate(generics.ListCreateAPIView):
  """
    Create items in the inventory
    **GET /items**
    - Retrieve a list of all items in the inventory.
    - Parameters:
        - `page`: Optional, default is 1. Page number for pagination.
        - `size`: Optional, default is 10. Number of items per page.
    - Responses:
        - 200: List of items in JSON format.
        - 401: Unauthorized access.
        - 500: Internal Server Error.

    **POST /items**
    - Create a new item in the inventory.
    - Request Body: Item data in JSON format.
    - Responses:
        - 201: The created item in JSON format.
        - 400: Bad request.
        - 401: Unauthorized access.
        - 500: Internal Server Error.
  """
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [IsAuthenticated, DjangoModelPermissions]
  
class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  """
    Retrive, update and delete items from the inventory

     **GET /items/{id}**
    - Retrieve a specific item from the inventory.
    - Parameters:
        - `id`: Required. The ID of the item to retrieve.
    - Responses:
        - 200: The item in JSON format.
        - 401: Unauthorized access.
        - 404: Item not found.
        - 500: Internal Server Error.

    **PUT /items/{id}**
    - Update a specific item in the inventory.
    - Parameters:
        - `id`: Required. The ID of the item to update.
    - Request Body: Updated item data in JSON format.
    - Responses:
        - 200: The updated item in JSON format.
        - 400: Bad request.
        - 401: Unauthorized access.
        - 404: Item not found.
        - 500: Internal Server Error.

    **DELETE /items/{id}**
    - Delete a specific item from the inventory.
    - Parameters:
        - `id`: Required. The ID of the item to delete.
    - Responses:
        - 204: No content.
        - 401: Unauthorized access.
        - 404: Item not found.
        - 500: Internal Server Error.
  """
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [IsAuthenticated, DjangoModelPermissions]

class SupplierListCreate(generics.ListCreateAPIView):
  """
    Create a list of suppliers

    **GET /suppliers**
    - Retrieve a list of all suppliers.
    - Parameters:
        - `page`: Optional, default is 1. Page number for pagination.
        - `size`: Optional, default is 10. Number of suppliers per page.
    - Responses:
        - 200: List of suppliers in JSON format.
        - 401: Unauthorized access.
        - 500: Internal Server Error.

    **POST /suppliers**
    - Create a new supplier.
    - Request Body: Supplier data in JSON format.
    - Responses:
        - 201: The created supplier in JSON format.
        - 400: Bad request.
        - 401: Unauthorized access.
        - 500: Internal Server Error.
  """
  queryset = Supplier.objects.all()
  serializer_class = SupplierSerializer
  permission_classes = [IsAuthenticated, DjangoModelPermissions]
  
class SupplierRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  """
    Retrive, update and delete suppliers in inventory.

    **GET /suppliers/{id}**
    - Retrieve a specific supplier.
    - Parameters:
        - `id`: Required. The ID of the supplier to retrieve.
    - Responses:
        - 200: The supplier in JSON format.
        - 401: Unauthorized access.
        - 404: Supplier not found.
        - 500: Internal Server Error.

    **PUT /suppliers/{id}**
    - Update a specific supplier.
    - Parameters:
        - `id`: Required. The ID of the supplier to update.
    - Request Body: Updated supplier data in JSON format.
    - Responses:
        - 200: The updated supplier in JSON format.
        - 400: Bad request.
        - 401: Unauthorized access.
        - 404: Supplier not found.
        - 500: Internal Server Error.

    **DELETE /suppliers/{id}**
    - Delete a specific supplier.
    - Parameters:
      - `id`: Required. The ID of the supplier to delete.
    - Responses:
        - 204: No content.
        - 401: Unauthorized access.
        - 404: Supplier not found.
        - 500: Internal Server Error.
  """
  queryset = Supplier.objects.all()
  serializer_class = SupplierSerializer
  permission_classes = [IsAuthenticated, DjangoModelPermissions]
