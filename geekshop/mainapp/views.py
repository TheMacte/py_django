from django.shortcuts import render

from mainapp.models import Product

links_menu = [
    {'href': 'index', 'title': 'Магазин', 'name': 'домой'},
    {'href': 'products:index', 'title': 'Продукты', 'name': 'продукты'},
    {'href': 'contacts', 'title': 'Контакты', 'name': 'контакты'},
]

def product(request, pk):
    print(pk)
    return


def products(request):
    context = {'links_menu': links_menu, 'object': Product.objects.get(id=2)}
    return render(request, 'mainapp/products.html', context)
