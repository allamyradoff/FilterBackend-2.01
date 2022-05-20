
from django.db import models


class Category(models.Model):
    CHIOCES = [
        ("buildings", "1"),
        ("design", "2"),
        ("isolation", "3"),
        
    ]  
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    slider = models.CharField(max_length=255, choices=CHIOCES, default="buildings", blank=True, null=True, verbose_name="Слайдер для смены продукта")
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

    def __str__(self):
        return self.name  
    
class Banner(models.Model):
    ACTIVE = [
        ("active", "active"),
    ]       
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    image = models.ImageField(upload_to='banner/', verbose_name='Изображение баннера', blank=True, null=True,)
    active = models.CharField(max_length=16, choices=ACTIVE, default="no_active", blank=True, null=True)

    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
    
    
    def __str__(self):
        return self.name
    
    
    
class About(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name="Лого")
    title = models.CharField(max_length=255, verbose_name="Имя")
    mini_desc = models.TextField(verbose_name="Короткая описание")
    desc = models.TextField(verbose_name="Описание")
    prod_about = models.TextField()
    image_one = models.ImageField(upload_to='aboutUs/', verbose_name="Изобрание О компании", blank=True, null=True)
    image_second = models.ImageField(upload_to='aboutUs/', verbose_name="Изобрание О компании", blank=True, null=True)
    image_three = models.ImageField(upload_to='aboutUs/', verbose_name="Изобрание О компании", blank=True, null=True)
    image_last = models.ImageField(upload_to='aboutUs/', verbose_name="Изобрание О компании", blank=True, null=True)
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
    
    def __str__(self):
        return self.title
    
    
class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    mini_desc = models.TextField(verbose_name="Короткая описание")
    desc = models.TextField(verbose_name="Описание")
    right_desc= models.TextField(verbose_name="Описание в правой строны")
    
    
    class Meta:
        verbose_name = 'Новосить'
        verbose_name_plural = 'Новости'
        
        
    def __str__(self):
        return self.title

class Product(models.Model):
    CHIOCES = [
        ("buildings", "1"),
        ("design", "2"),
        ("isolation", "3"),
    ]  
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(upload_to='product/', verbose_name="Имя продукта", blank=True, null=True)
    mini_desc = models.TextField(blank=True, null=True, verbose_name="Короткая описание")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    line_one = models.CharField(max_length=255, blank=True, null=True)
    line_second = models.CharField(max_length=255, blank=True, null=True)
    line_three = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slider = models.CharField(max_length=255, choices=CHIOCES, default="buildings")
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.name
    
    
    
    class Meta:
        ordering = ("-created_at",)
        
class FooterAbout(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    desc = models.TextField(verbose_name="Короткая описание")
    image = models.ImageField(upload_to='footer about/', verbose_name="Изоброжение с нижней строны", blank=True, null=True)

    class Meta:
        verbose_name = 'Нижнее описание'
        verbose_name_plural = 'Нижнее описание'
    
    def __str__(self):
        return self.title
    
    
class Address(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    phone = models.IntegerField(verbose_name="Телефон")
    mobile_phone = models.IntegerField(verbose_name="Мобилбный номер")
    email = models.EmailField(verbose_name="Email почта")
    
    
    class Meta:
        verbose_name = 'Адресс'
        verbose_name_plural = 'Адрессы'
    
    def __str__(self):
        return self.title


class ContactUs(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email

    

    class Meta:
        ordering = ("-created_at",)
        
        
class Map(models.Model):
    map = models.TextField(verbose_name="Карта")
    
    
    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
    
    
    
class Certification(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    image = models.ImageField(upload_to='sertifikat about/', verbose_name=" Название сертификата")
    


    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        
        
    def __str__(self):
        return self.title