# Generated by Django 4.0.4 on 2022-05-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0021_map_alter_contactus_message_alter_contactus_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='footer about/', verbose_name='sertifikat surat')),
            ],
        ),
    ]