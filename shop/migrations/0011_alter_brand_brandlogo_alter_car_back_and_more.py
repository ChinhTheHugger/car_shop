# Generated by Django 4.2 on 2024-04-12 09:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_contract_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brandlogo',
            field=models.ImageField(upload_to='uploads/brands/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='car',
            name='back',
            field=models.ImageField(upload_to='uploads/backs/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='car',
            name='desintext',
            field=models.TextField(default='No description'),
        ),
        migrations.AlterField(
            model_name='car',
            name='front',
            field=models.ImageField(upload_to='uploads/fronts/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='car',
            name='interior',
            field=models.ImageField(upload_to='uploads/interiors/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryimage',
            field=models.ImageField(upload_to='uploads/categories/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='carbackbefore',
            field=models.ImageField(upload_to='uploads/contracts/backstatusbefore/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='carfrontbefore',
            field=models.ImageField(upload_to='uploads/contracts/frontstatusbefore/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='carinteriorbefore',
            field=models.ImageField(upload_to='uploads/contracts/interiorstatusbefore/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='driverlicense',
            field=models.ImageField(upload_to='uploads/contracts/driverlicences/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='idcard',
            field=models.ImageField(upload_to='uploads/contracts/idcards/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='residence',
            field=models.ImageField(upload_to='uploads/contracts/residences/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])]),
        ),
    ]
