from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
<<<<<<< HEAD
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
]
=======
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    path('logout/', authapp.logout, name='logout'),
]
>>>>>>> e93ebd5 (get all from lesson_6)
