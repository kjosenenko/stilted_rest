# Generated by Django 4.2.11 on 2024-12-24 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0015_alter_band_cover_photo'),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='band',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bands.band'),
            preserve_default=False,
        ),
    ]