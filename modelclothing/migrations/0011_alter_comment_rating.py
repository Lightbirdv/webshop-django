# Generated by Django 4.0 on 2022-01-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelclothing', '0010_alter_clothing_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(default='5', max_length=1),
        ),
    ]
