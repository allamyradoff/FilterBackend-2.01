# Generated by Django 4.0.4 on 2022-05-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0012_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='right_desc',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
    ]
