# Generated by Django 4.0.4 on 2022-05-18 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0013_news_right_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
