
from distutils.command.build import build
from turtle import right
from unicodedata import name
from django.db import models


class Category(models.Model):
    CHIOCES = [
        ("buildings", "1"),
        ("design", "2"),
        ("isolation", "3"),
        
    ]  
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ady")
    slider = models.CharField(max_length=255, choices=CHIOCES, default="buildings", blank=True, null=True, verbose_name="Haryt çalşyrjy slider")
    
    class Meta:
        verbose_name = 'Kategoriýa'
        verbose_name_plural = 'Kategoriýalar'
    

    def __str__(self):
        return self.name  
    
class Banner(models.Model):
    ACTIVE = [
        ("active", "active"),
    ]       
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ady")
    image = models.ImageField(upload_to='banner/', verbose_name='Banner surat', blank=True, null=True,)
    active = models.CharField(max_length=16, choices=ACTIVE, default="no_active", blank=True, null=True)

    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Bannerlar'
    
    
    def __str__(self):
        return self.name
    
    
    
class About(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name="logo")
    title = models.CharField(max_length=255, verbose_name="Ady")
    mini_desc = models.TextField(verbose_name="Gysgaça beýany")
    desc = models.TextField(verbose_name="Giňişleýin beýany")
    prod_about = models.TextField()
    image_one = models.ImageField(upload_to='aboutUs/', verbose_name="kompaniya barada surat", blank=True, null=True)
    image_second = models.ImageField(upload_to='aboutUs/', verbose_name="kompaniya barada surat", blank=True, null=True)
    image_three = models.ImageField(upload_to='aboutUs/', verbose_name="kompaniya barada surat", blank=True, null=True)
    image_last = models.ImageField(upload_to='aboutUs/', verbose_name="kompaniya barada surat", blank=True, null=True)
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
    
    def __str__(self):
        return self.title
    
    
class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ady")
    mini_desc = models.TextField(verbose_name="Gysgaça beýany")
    desc = models.TextField(verbose_name="Giňişleýin beýany")
    right_desc= models.TextField(verbose_name=" Sag tarapdaky gysgaça beýany")
    
    
    class Meta:
        verbose_name = 'Habar'
        verbose_name_plural = 'Habarlar'
        
        
    def __str__(self):
        return self.title

class Product(models.Model):
    CHIOCES = [
        ("buildings", "1"),
        ("design", "2"),
        ("isolation", "3"),
    ]  
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ady")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriýasy")
    image = models.ImageField(upload_to='product/', verbose_name="Harydyň surat", blank=True, null=True)
    mini_desc = models.TextField(blank=True, null=True, verbose_name="Gysgaça beýany")
    description = models.TextField(blank=True, null=True, verbose_name="Giňişleýin beýany")
    line_one = models.CharField(max_length=255, blank=True, null=True)
    line_second = models.CharField(max_length=255, blank=True, null=True)
    line_three = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Bahasy")
    created_at = models.DateTimeField(auto_now_add=True)
    slider = models.CharField(max_length=255, choices=CHIOCES, default="buildings")
    
    class Meta:
        verbose_name = 'Haryt'
        verbose_name_plural = 'Harytlar'


    def __str__(self):
        return self.name
    
    
    
    class Meta:
        ordering = ("-created_at",)
        
class FooterAbout(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ady")
    desc = models.TextField(verbose_name="Gysgaça beýany")
    image = models.ImageField(upload_to='footer about/', verbose_name="Aşakdaky bölekdäki surat", blank=True, null=True)

    class Meta:
        verbose_name = 'Aşakdaky beýan'
        verbose_name_plural = 'Aşakdaky beýanlar'
    
    def __str__(self):
        return self.title
    
    
class Address(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    location = models.CharField(max_length=255, verbose_name="Ýerleşýän ýeri")
    phone = models.IntegerField(verbose_name="Telefon")
    mobile_phone = models.IntegerField(verbose_name="El telefon")
    email = models.EmailField(verbose_name="Email poçtasy")
    
    
    class Meta:
        verbose_name = 'Salgy'
        verbose_name_plural = 'Salgylar'
    
    def __str__(self):
        return self.title


class ContactUs(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Kontak'
        verbose_name_plural = 'Kontaktlar'

    def __str__(self):
        return self.email

    

    class Meta:
        ordering = ("-created_at",)
        
        
class Map(models.Model):
    map = models.TextField(verbose_name="Karta")
    
    
    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
    
    
    
class Certification(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    image = models.ImageField(upload_to='sertifikat about/', verbose_name="sertifikatyň surat")
    


    class Meta:
        verbose_name = 'Sertifikat'
        verbose_name_plural = 'Sertifikatlar'
        
        
    def __str__(self):
        return self.title