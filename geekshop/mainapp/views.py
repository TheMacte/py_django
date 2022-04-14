from django.shortcuts import render

links_menu = [
    {'href': 'index', 'title': 'Магазин', 'name': 'домой'},
    {'href': 'products', 'title': 'Продукты', 'name': 'продукты'},
    {'href': 'contacts', 'title': 'Контакты', 'name': 'контакты'},
]


def products(request):
    context = {'links_menu': links_menu}
    return render(request, 'mainapp/products.html', context)
