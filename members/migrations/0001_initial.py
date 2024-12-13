# Generated by Django 4.2.11 on 2024-12-13 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bands', '0008_band_using_react'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('instrument', models.CharField(blank=True, max_length=128, null=True)),
                ('bio', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.band')),
            ],
        ),
    ]
