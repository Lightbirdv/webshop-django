# Generated by Django 4.0 on 2022-01-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0005_alter_myuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/profile-default.svg', upload_to='profile_pictures/'),
        ),
    ]
