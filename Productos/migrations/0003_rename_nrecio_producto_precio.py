# Generated by Django 5.1.2 on 2024-11-02 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_rename_descripcion_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nrecio',
            new_name='precio',
        ),
    ]
