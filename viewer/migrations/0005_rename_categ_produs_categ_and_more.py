# Generated by Django 4.2 on 2025-01-15 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_remove_produs_magazine_delete_magazin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produs',
            old_name='Categ',
            new_name='categ',
        ),
        migrations.RenameField(
            model_name='produs',
            old_name='Denumire',
            new_name='denumire',
        ),
        migrations.RenameField(
            model_name='produs',
            old_name='Descriere',
            new_name='descriere',
        ),
        migrations.RenameField(
            model_name='produs',
            old_name='Garantie_luni',
            new_name='garantie_luni',
        ),
        migrations.RenameField(
            model_name='produs',
            old_name='Lansat',
            new_name='lansat',
        ),
    ]
