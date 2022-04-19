from django.urls import path, include
from .views import products, product

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('<int:pk>/', product, name='product')
]
