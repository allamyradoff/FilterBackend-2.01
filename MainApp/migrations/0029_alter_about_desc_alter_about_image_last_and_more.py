# Generated by Django 4.0.4 on 2022-05-20 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0028_alter_product_line_one_alter_product_line_second'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='desc',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_last',
            field=models.ImageField(blank=True, null=True, upload_to='aboutUs/', verbose_name='Изобрание О компании'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_one',
            field=models.ImageField(blank=True, null=True, upload_to='aboutUs/', verbose_name='Изобрание О компании'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_second',
            field=models.ImageField(blank=True, null=True, upload_to='aboutUs/', verbose_name='Изобрание О компании'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_three',
            field=models.ImageField(blank=True, null=True, upload_to='aboutUs/', verbose_name='Изобрание О компании'),
        ),
        migrations.AlterField(
            model_name='about',
            name='logo',
            field=models.ImageField(upload_to='logo/', verbose_name='Лого'),
        ),
        migrations.AlterField(
            model_name='about',
            name='mini_desc',
            field=models.TextField(verbose_name='Короткая описание'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email почта'),
        ),
        migrations.AlterField(
            model_name='address',
            name='location',
            field=models.CharField(max_length=255, verbose_name='Местоположение'),
        ),
        migrations.AlterField(
            model_name='address',
            name='mobile_phone',
            field=models.IntegerField(verbose_name='Мобилбный номер'),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.IntegerField(verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='address',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Изображение баннера'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slider',
            field=models.CharField(blank=True, choices=[('buildings', '1'), ('design', '2'), ('isolation', '3')], default='buildings', max_length=255, null=True, verbose_name='Слайдер для смены продукта'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='image',
            field=models.ImageField(upload_to='sertifikat about/', verbose_name=' Название сертификата'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='footerabout',
            name='desc',
            field=models.TextField(verbose_name='Короткая описание'),
        ),
        migrations.AlterField(
            model_name='footerabout',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='footer about/', verbose_name='Изоброжение с нижней строны'),
        ),
        migrations.AlterField(
            model_name='footerabout',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='map',
            name='map',
            field=models.TextField(verbose_name='Карта'),
        ),
        migrations.AlterField(
            model_name='news',
            name='desc',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='mini_desc',
            field=models.TextField(verbose_name='Короткая описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='right_desc',
            field=models.TextField(verbose_name='Описание в правой строны'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Имя продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mini_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Короткая описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
    ]