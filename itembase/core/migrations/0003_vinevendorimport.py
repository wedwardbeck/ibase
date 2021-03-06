# Generated by Django 2.2.9 on 2020-01-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200127_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='VineVendorImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=50, verbose_name='Item')),
                ('name', models.CharField(max_length=50, verbose_name='Item')),
                ('addr1', models.CharField(max_length=150, verbose_name='Item')),
                ('addr2', models.CharField(max_length=150, verbose_name='Item')),
                ('addr3', models.CharField(max_length=150, verbose_name='Item')),
                ('city', models.CharField(max_length=50, verbose_name='Item')),
                ('state', models.CharField(max_length=25, verbose_name='Item')),
                ('zipcode', models.CharField(max_length=25, verbose_name='Item')),
                ('phone', models.CharField(max_length=50, verbose_name='Item')),
                ('extension', models.CharField(max_length=50, verbose_name='Item')),
                ('salesperson_name', models.CharField(max_length=100, verbose_name='Item')),
                ('salesperson_email', models.CharField(max_length=100, verbose_name='Item')),
                ('salesperson_phone', models.CharField(max_length=50, verbose_name='Item')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('source', models.CharField(max_length=150, verbose_name='Item')),
            ],
        ),
    ]
