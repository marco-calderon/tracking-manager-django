# Generated by Django 3.0.5 on 2020-12-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20201203_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
