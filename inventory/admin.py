from django.contrib import admin
from .models import Item, Supplier

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  list_display = ("name", "price", "created_at", "suppliers")
  list_display_links = ("name", "price", "created_at")
  list_per_page = 25

  def suppliers(self, obj):
    return ', '.join([str(s) for s in obj.supplier_set.all()])

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
  list_display = ("name", "contact_info")
  list_display_links = ("name", "contact_info")



