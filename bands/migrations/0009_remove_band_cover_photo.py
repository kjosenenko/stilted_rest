# Generated by Django 4.2.11 on 2024-12-24 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0008_band_using_react'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='cover_photo',
        ),
    ]