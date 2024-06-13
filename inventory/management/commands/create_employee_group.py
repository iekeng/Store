from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
  help = "Create staff group with specific permissions"

  def handle(self, *args, **options):
    staff_group, created = Group.objects.get_or_create(name="Staff")

    if created:
      self.stdout.write(self.style.SUCCESS("Successfully created Staff group"))
    else:
      self.stdout.write(self.style.WARNING("Staff group already exists"))

    
    permissions = [
      Permission.objects.get(codename="add_item"),
      Permission.objects.get(codename="change_item"),
      Permission.objects.get(codename="delete_item"),
      Permission.objects.get(codename="view_item"),
      Permission.objects.get(codename="add_supplier"),
      Permission.objects.get(codename="change_supplier"),
      Permission.objects.get(codename="view_supplier")
    ]

    staff_group.permissions.set(permissions)
    