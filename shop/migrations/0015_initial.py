# Generated by Django 4.2 on 2024-07-04 07:34

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0014_delete_account_delete_brand_delete_car_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(default='customer', max_length=50)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('desintext', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('brandlogo', models.ImageField(upload_to='uploads/brands/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, null=True)),
                ('model', models.CharField(max_length=50, null=True)),
                ('year', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=50, null=True)),
                ('desintext', models.TextField(default='No description')),
                ('front', models.ImageField(upload_to='uploads/fronts/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('back', models.ImageField(upload_to='uploads/backs/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('interior', models.ImageField(upload_to='uploads/interiors/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('instock', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50)),
                ('categoryimage', models.ImageField(upload_to='uploads/categories/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=50)),
                ('customer', models.CharField(max_length=50)),
                ('manager', models.CharField(max_length=50)),
                ('car', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=1)),
                ('purpose', models.TextField(max_length=50)),
                ('startdate', models.DateField(default=datetime.datetime.today)),
                ('enddate', models.DateField(default=datetime.datetime.today)),
                ('residence', models.ImageField(upload_to='uploads/contracts/residences/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('idcard', models.ImageField(upload_to='uploads/contracts/idcards/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('driverlicense', models.ImageField(upload_to='uploads/contracts/driverlicences/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('carodometerbefore', models.IntegerField(default=1)),
                ('carsystemstatusbefore', models.TextField(default='Functional')),
                ('carfrontbefore', models.ImageField(upload_to='uploads/contracts/frontstatusbefore/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('carbackbefore', models.ImageField(upload_to='uploads/contracts/backstatusbefore/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('carinteriorbefore', models.ImageField(upload_to='uploads/contracts/interiorstatusbefore/', validators=[django.core.validators.FileExtensionValidator(['apng', 'png', 'gif', 'svg', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'webp'])])),
                ('cost', models.IntegerField(default=0)),
                ('createdate', models.DateField(default=datetime.datetime.today)),
            ],
            options={
                'db_table': 'contract',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=50)),
                ('car', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('status', models.CharField(default=False, max_length=50)),
            ],
            options={
                'db_table': 'request',
            },
        ),
        migrations.AddConstraint(
            model_name='request',
            constraint=models.UniqueConstraint(fields=('customer', 'car', 'date'), name='unique_customer_car_date'),
        ),
        migrations.AddConstraint(
            model_name='contract',
            constraint=models.UniqueConstraint(fields=('request',), name='unique_request'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('categoryname',), name='unique_category'),
        ),
        migrations.AddConstraint(
            model_name='car',
            constraint=models.UniqueConstraint(fields=('brand', 'model', 'year'), name='unique_brand_model_year'),
        ),
        migrations.AddConstraint(
            model_name='brand',
            constraint=models.UniqueConstraint(fields=('brandname',), name='unique_brand'),
        ),
    ]