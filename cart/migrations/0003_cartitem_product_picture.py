# Generated by Django 4.0 on 2022-01-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product_picture',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
