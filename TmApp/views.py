from django.shortcuts import render, redirect
from TmApp.form import ContactUsForm
from TmApp.models import *
from TmApp.models import Banner


def index(request):
    banners = Banner.objects.all()
    category = Category.objects.all()
    prod = Product.objects.all()
    about = About.objects.all()
    product = Product.objects.all()
    news = News.objects.all()
    footer = FooterAbout.objects.all()
    address = Address.objects.all()
    map = Map.objects.all()
    certificataion = Certification.objects.all()
    form = ContactUsForm()
    if request.method=="POST":
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    
    context = {
        "banners": banners,
        "categories":category,
        "product":prod,
        "about":about,
        "product" : product,
        "news": news,
        "footer": footer,
        "address": address,
        "form":form,
        "map":map,
        "certificataion":certificataion
    }
    return render(request, 'tmIndex.html', context)




