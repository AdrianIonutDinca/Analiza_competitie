# Generated by Django 4.2 on 2025-01-15 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_magazin_rename_genre_produs_categ_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produs',
            name='Magazine',
        ),
        migrations.DeleteModel(
            name='Magazin',
        ),
    ]
