from django.contrib import admin
from .models import Item, Supplier
from django.urls import reverse
from django.utils.http import urlencode

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  list_display = ("name", "price", "created_at" )

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
  list_display = ("name", "contact_info")

  