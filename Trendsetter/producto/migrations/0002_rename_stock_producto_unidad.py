# Generated by Django 5.1.2 on 2024-10-26 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='stock',
            new_name='Unidad',
        ),
    ]
