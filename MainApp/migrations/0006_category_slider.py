# Generated by Django 4.0.4 on 2022-05-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_product_slider_alter_banner_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slider',
            field=models.CharField(choices=[('buildings', 'buildings'), ('design', 'design')], default='buildings', max_length=255),
        ),
    ]