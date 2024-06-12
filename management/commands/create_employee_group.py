from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from inventory.models import Item, Supplier

class Command(BaseCommand):
  help = "Create employee group with specific permissions"

  def handle(self, *args: Any, **options: Any) -> str | None:
    group, created = Group.objects.get_or_create(name="Employess")

    if created:
      self.stdout.write(self.style.SUCCESS("Successfully created Employees group"))
    else:
      self.stdout.write(self.style.WARNING("Employees group already exists"))

    permissions = [
      Permission.objects.get(codename="add_item"),
      Permission.objects.get(codename="change_item"),
      Permission.objects.get(codename="delete_item"),
      Permission.objects.get(codename="view_item"),
    ]

    group.permissions.set(permissions)
    group.save()

    self.stdout.write(self.style.SUCCESS('Successfully assigned permissions to Employees group'))