# Generated by Django 4.0.4 on 2022-05-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slider',
            field=models.CharField(choices=[('buildings', '1'), ('design', '2')], default='buildings', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='slider',
            field=models.CharField(choices=[('buildings', '1'), ('design', '2')], default='buildings', max_length=255),
        ),
    ]
