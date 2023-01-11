from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    print(sort)
    if sort == 'name':
        context = {'phones': Phone.objects.order_by('name')}
    elif sort == 'min_price':
        context = {'phones': Phone.objects.order_by('price')}
    elif sort == 'max_price':
        context = {'phones': Phone.objects.order_by('-price')}
    else:
        context = {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_in_bd = Phone.objects.all()
    for phone in phones_in_bd:
        if slug in phone.slug:
            context = {'phone': phone}
    return render(request, template, context)
