# Generated by Django 4.0.4 on 2022-05-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0026_remove_product_price_product_line_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='line_one',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='line_second',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
