# Generated by Django 4.0.4 on 2022-05-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_alter_banner_active_alter_banner_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('mini_desc', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
    ]