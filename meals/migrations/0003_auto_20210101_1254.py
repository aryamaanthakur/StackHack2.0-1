# Generated by Django 3.1.4 on 2021-01-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_fooditem_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='thumbnail',
            field=models.ImageField(upload_to=''),
        ),
    ]