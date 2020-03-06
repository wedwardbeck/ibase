# Generated by Django 2.2.9 on 2020-03-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200305_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvendor',
            name='name1',
            field=models.CharField(max_length=30, verbose_name='Primary Name'),
        ),
        migrations.AlterField(
            model_name='historicalvendor',
            name='name2',
            field=models.CharField(blank=True, max_length=70, verbose_name='Additional Name '),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name1',
            field=models.CharField(max_length=30, verbose_name='Primary Name'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name2',
            field=models.CharField(blank=True, max_length=70, verbose_name='Additional Name '),
        ),
    ]