# Generated by Django 4.2 on 2024-05-08 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_brand_brandlogo_alter_car_back_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='createdate',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
