from django.contrib import admin
from .models import Item, Supplier
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
  pass
