# Generated by Django 3.0.3 on 2023-02-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersdata',
            name='profile_picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
