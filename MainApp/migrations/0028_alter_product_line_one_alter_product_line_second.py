# Generated by Django 4.0.4 on 2022-05-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0027_alter_product_line_one_alter_product_line_second'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='line_one',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='line_second',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]