from django.urls import path
from .views import (SupplierListCreate,
                    SupplierRetrieveUpdateDestroy,
                    ItemListCreate,
                    ItemRetrieveUpdateDestroy)

urlpatterns = [
  path('item/', ItemListCreate.as_view(), name='item-list-create'),
  path('item/<int:pk>/', ItemRetrieveUpdateDestroy.as_view(), name='item-detail'),
  path('supplier/', SupplierListCreate.as_view(), name='supplier-ist-create'),
  path('supplier/<int:pk>/', SupplierRetrieveUpdateDestroy.as_view(), name='supplier-detail')
]
