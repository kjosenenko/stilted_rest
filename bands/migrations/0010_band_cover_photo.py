# Generated by Django 4.2.11 on 2024-12-24 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('bands', '0009_remove_band_cover_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='cover_photo',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.image'),
        ),
    ]
