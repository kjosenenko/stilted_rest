# Generated by Django 4.2.11 on 2024-12-03 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_phone',
            new_name='phone',
        ),
    ]
