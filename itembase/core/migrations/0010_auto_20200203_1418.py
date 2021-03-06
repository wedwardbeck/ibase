# Generated by Django 2.2.9 on 2020-02-03 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200203_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffroles',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='staff_roles_created', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='systemtype',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='system_type_created', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='vendoritem',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_created', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='addr1',
            field=models.CharField(max_length=150, verbose_name='Address 1'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='addr2',
            field=models.CharField(max_length=150, verbose_name='Address 2'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='addr3',
            field=models.CharField(max_length=150, verbose_name='Address 3'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='city',
            field=models.CharField(max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='extension',
            field=models.CharField(max_length=50, verbose_name='Extension'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='salesperson_email',
            field=models.CharField(max_length=100, verbose_name='Salesperson Email'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='salesperson_name',
            field=models.CharField(max_length=100, verbose_name='Salesperson Name'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='salesperson_phone',
            field=models.CharField(max_length=50, verbose_name='Salesperson Phone'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='source',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='state',
            field=models.CharField(max_length=25, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='vendor_code',
            field=models.CharField(max_length=50, verbose_name='Vendor Code'),
        ),
        migrations.AlterField(
            model_name='vinevendorimport',
            name='zipcode',
            field=models.CharField(max_length=25, verbose_name='Postal Code'),
        ),
    ]
