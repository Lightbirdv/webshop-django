# Generated by Django 4.0 on 2022-01-14 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelclothing', '0013_alter_clothing_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothing',
            name='size',
        ),
    ]
