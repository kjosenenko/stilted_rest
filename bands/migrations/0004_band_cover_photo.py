# Generated by Django 4.2.11 on 2024-11-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0003_band_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='cover_photo',
            field=models.ImageField(null=True, upload_to='bands'),
        ),
    ]
