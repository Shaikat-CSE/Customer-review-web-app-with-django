# Generated by Django 5.1.5 on 2025-02-05 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
