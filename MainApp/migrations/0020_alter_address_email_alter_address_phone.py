# Generated by Django 4.0.4 on 2022-05-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0019_alter_address_mobile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.IntegerField(),
        ),
    ]