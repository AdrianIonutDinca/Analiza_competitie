# Generated by Django 4.2 on 2025-01-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_magazin'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazin',
            name='judet',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
