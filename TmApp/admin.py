from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image', 'price']



admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(About)
admin.site.register(Product, ProductAdmin)
admin.site.register(News)
admin.site.register(FooterAbout)
admin.site.register(Address)
admin.site.register(ContactUs)
admin.site.register(Map)
admin.site.register(Certification)

