# Generated by Django 4.2 on 2024-05-20 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_car', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='car',
            constraint=models.UniqueConstraint(fields=('brand', 'model', 'year'), name='unique_brand_model_year'),
        ),
    ]
