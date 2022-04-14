from django.shortcuts import render

links_menu = [
    {'href': 'index', 'title': 'Магазин', 'name': 'домой'},
    {'href': 'products', 'title': 'Продукты', 'name': 'продукты'},
    {'href': 'contacts', 'title': 'Контакты', 'name': 'контакты'},
]


def index(request):
    context = {'links_menu': links_menu}
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    context = {'links_menu': links_menu}
    return render(request, 'geekshop/contacts.html', context)
