# Generated by Django 5.1.2 on 2024-11-02 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Disponible',
            new_name='disponible',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Precio',
            new_name='nrecio',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Unidad',
            new_name='unidad',
        ),
    ]