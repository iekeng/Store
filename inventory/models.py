from django.db import models

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  created_at = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ["name", "description", "price", "created_at"]

  def __str__(self):
    return self.nameText
  
class Supplier(models.Mode):
  name = models.CharField(max_length=255)
  contact_info = models.CharField(max_length=30)
  items = models.ManyToManyField(Item)

  class Meta:
    ordering = ["name", "contact"]

  def __str__(self):
      return self.name
  