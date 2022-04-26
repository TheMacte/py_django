from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product

links_menu = [
    {'href': 'index', 'title': 'Магазин', 'name': 'домой'},
    {'href': 'products:index', 'title': 'Продукты', 'name': 'продукты'},
    {'href': 'contacts', 'title': 'Контакты', 'name': 'контакты'},
]


def index(request):
    product = Product.objects.all()[:4]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {'links_menu': links_menu,
               'title': 'Магазин',
               'products': product,
               'basket': basket,
               }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
                'links_menu': links_menu,
                'basket': basket,
               }

    return render(request, 'geekshop/contacts.html', context)
