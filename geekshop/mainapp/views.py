from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'title': 'Магазин', 'name': 'домой'},
    {'href': 'products:index', 'title': 'Продукты', 'name': 'продукты'},
    {'href': 'contacts', 'title': 'Контакты', 'name': 'контакты'},
]


def product(request, pk):
    print(pk)
    return


def products(request, pk=None):
    title = 'Каталог'
    links_menu_sub = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = ProductCategory.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'links_menu_sub': links_menu_sub,
            'category': category,
            'products': products
            # 'object': Product.objects.get(id=2)
        }
        return render(request, 'mainapp/products_list.html', context)

    same_product = Product.objects.all()[3:5]
    context = {
        'title': title,
        'links_menu': links_menu,
        'links_menu_sub': links_menu_sub,
        'same_products': same_product
        # 'object': Product.objects.get(id=2)
    }

    return render(request, 'mainapp/products.html', context=context)
