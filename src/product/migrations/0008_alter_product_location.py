# Generated by Django 5.1.6 on 2025-04-25 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_category_parent'),
        ('product', '0007_alter_product_location_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.region'),
        ),
    ]
