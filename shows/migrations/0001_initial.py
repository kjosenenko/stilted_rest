# Generated by Django 4.2.3 on 2023-08-12 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(blank=True, max_length=128, null=True)),
                ('presale_link', models.CharField(blank=True, max_length=128, null=True)),
                ('has_presale', models.BooleanField(default=False)),
                ('supporting_acts', models.CharField(blank=True, max_length=500, null=True)),
                ('show_time', models.TimeField()),
                ('show_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]