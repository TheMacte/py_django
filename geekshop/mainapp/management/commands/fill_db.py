<<<<<<< HEAD
import os
import json
=======
import json
import os
>>>>>>> e93ebd5 (get all from lesson_6)

from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
<<<<<<< HEAD
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
=======
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as infile:
>>>>>>> e93ebd5 (get all from lesson_6)
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

<<<<<<< HEAD
        ShopUser.objects.create_superuser('admin', 'admin@admin.cm', '123', age='21')
=======
        ShopUser.objects.create_superuser('admin', 'admin@django.com', '123', age=28)
>>>>>>> e93ebd5 (get all from lesson_6)
