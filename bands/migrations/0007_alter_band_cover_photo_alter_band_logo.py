# Generated by Django 4.2.11 on 2024-11-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0006_rename_contact_email_band_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='bands'),
        ),
        migrations.AlterField(
            model_name='band',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='bands'),
        ),
    ]