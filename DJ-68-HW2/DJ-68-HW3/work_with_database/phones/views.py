from django.shortcuts import render, redirect, Http404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    phones = Phone.objects.all()
    if sort == 'name':
        phones = phones.order_by('name')
    if sort == 'min_price':
        phones = phones.order_by('price')
    if sort == 'max_price':
        phones = phones.order_by('price').reverse()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
        context = {'phone': phone}
    except Phone.DoesNotExist:
        raise Http404()
    return render(request, template, context)
