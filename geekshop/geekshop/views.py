from django.shortcuts import render

<<<<<<< HEAD
from mainapp.models import Product

links_menu = [
    {'href': 'index', 'title': 'Магазин', 'name': 'домой'},
    {'href': 'products:index', 'title': 'Продукты', 'name': 'продукты'},
    {'href': 'contacts', 'title': 'Контакты', 'name': 'контакты'},
]


def index(request):
    product = Product.objects.all()[:4]
    context = {'links_menu': links_menu, 'title': 'Магазин', 'products': product}
=======
from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:4]

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'главная',
        'products': products,
        'basket': basket,
    }

>>>>>>> e93ebd5 (get all from lesson_6)
    return render(request, 'geekshop/index.html', context)


def contacts(request):
<<<<<<< HEAD
    context = {'links_menu': links_menu}
    return render(request, 'geekshop/contacts.html', context)
=======
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'контакты',
        'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context)
>>>>>>> e93ebd5 (get all from lesson_6)
