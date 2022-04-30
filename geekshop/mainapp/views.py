import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'title': 'Магазин', 'name': 'домой'},
    {'href': 'products:index', 'title': 'Продукты', 'name': 'продукты'},
    {'href': 'contacts', 'title': 'Контакты', 'name': 'контакты'},
]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk).order_by('price')
    return same_products


def products(request, pk=None):
    title = 'Каталог'
    links_menu_sub = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        hot_product = get_hot_product()
        same_product = get_same_product(hot_product)

        context = {
            'title': title,
            'links_menu': links_menu,
            'links_menu_sub': links_menu_sub,
            'category': category,
            # 'hot_product': hot_product,
            'same_product': same_product,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_product = get_same_product(hot_product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'links_menu_sub': links_menu_sub,
        'same_products': same_product,
        'hot_product': hot_product,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    title = "детали продукта"
    links_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)

    basket = get_basket(request.user)

    hot_product = get_hot_product()
    same_product = get_same_product(hot_product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'same_products': same_product,
        'basket': basket,
    }

    return render(request, 'mainapp/product.html', context=context)
