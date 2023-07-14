# Generated by Django 4.1.7 on 2023-07-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FizUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('shop_name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('promo_code', models.CharField(blank=True, max_length=255)),
                ('terms_of_service', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UrUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('form', models.CharField(max_length=255)),
                ('shop_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('organization_name', models.CharField(max_length=255)),
                ('legal_address', models.CharField(max_length=255)),
                ('inn', models.CharField(max_length=12)),
                ('kpp', models.CharField(max_length=9)),
                ('bank', models.CharField(max_length=255)),
                ('bik', models.CharField(max_length=9)),
                ('account_number', models.CharField(max_length=20)),
                ('correspondent_account', models.CharField(max_length=20)),
                ('terms_of_service', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
