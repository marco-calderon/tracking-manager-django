# Generated by Django 3.0.5 on 2020-12-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
