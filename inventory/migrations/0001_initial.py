# Generated by Django 5.0.6 on 2024-06-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name', 'description', 'price', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_info', models.CharField(max_length=255)),
                ('items', models.ManyToManyField(to='inventory.item')),
            ],
            options={
                'ordering': ['name', 'contact_info'],
            },
        ),
    ]
