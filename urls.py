from django.urls import path
from .views import *

urlpatterns =[
    path('salom/',asosiy, name='home'),
    path('login/',login, name = 'login'),
    path('',ulash, name= 'news'),
    path('single/<slug:slug>',single, name='single')
]