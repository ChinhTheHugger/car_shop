# Generated by Django 4.2 on 2024-05-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_category', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('categoryname',), name='unique_category'),
        ),
    ]