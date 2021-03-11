# Generated by Django 3.0.5 on 2020-12-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_code',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='cancelled_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='delivered_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='shipped_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='shipping_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
