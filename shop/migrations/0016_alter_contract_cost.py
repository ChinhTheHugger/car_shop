# Generated by Django 4.2 on 2024-07-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]
