# Generated by Django 4.0.4 on 2022-05-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Haryt surat'),
        ),
    ]
