# Generated by Django 5.0.1 on 2024-02-01 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='add_item.png', height_field=100, upload_to='uplaods/', width_field=100),
        ),
    ]
