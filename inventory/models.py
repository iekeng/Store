from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=25)
  description = models.TextField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  created_at = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ["name"]

  def __str__(self):
    return self.name
  
class Supplier(models.Model):
  name = models.CharField(max_length=25)
  contact_info = models.CharField(max_length=25)
  items = models.ManyToManyField(Item)

  class Meta:
    ordering = ["name"]

  def __str__(self):
    return self.name
  