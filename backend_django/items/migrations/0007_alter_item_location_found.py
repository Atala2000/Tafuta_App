# Generated by Django 5.0.1 on 2024-02-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location_found',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]