from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
<<<<<<< HEAD
=======

>>>>>>> e93ebd5 (get all from lesson_6)
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    title = 'вход'
<<<<<<< HEAD
    login_form = ShopUserLoginForm(data=request.POST)
=======
    login_form = ShopUserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

>>>>>>> e93ebd5 (get all from lesson_6)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
<<<<<<< HEAD
            return HttpResponseRedirect(reverse('index'))
=======
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))
>>>>>>> e93ebd5 (get all from lesson_6)

    context = {
        'title': title,
        'login_form': login_form,
<<<<<<< HEAD
=======
        'next': next,
>>>>>>> e93ebd5 (get all from lesson_6)
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистрация'
<<<<<<< HEAD
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
=======

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

>>>>>>> e93ebd5 (get all from lesson_6)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
<<<<<<< HEAD
    context = {'title': title, 'register_form': register_form}
=======

    context = {'title': title, 'register_form': register_form}

>>>>>>> e93ebd5 (get all from lesson_6)
    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

<<<<<<< HEAD
    context = {'title': title,
               'edit_form': edit_form,
               }
=======
    context = {'title': title, 'edit_form': edit_form}
>>>>>>> e93ebd5 (get all from lesson_6)

    return render(request, 'authapp/edit.html', context)
