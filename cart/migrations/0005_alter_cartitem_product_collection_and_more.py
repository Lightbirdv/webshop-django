# Generated by Django 4.0 on 2022-01-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cartitem_product_collection_cartitem_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product_collection',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_color',
            field=models.CharField(max_length=100),
        ),
    ]
