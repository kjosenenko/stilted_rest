# Generated by Django 4.2.11 on 2024-12-24 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0012_band_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='logo',
        ),
    ]
