from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    return render(request, 'geekshop/contacts.html')