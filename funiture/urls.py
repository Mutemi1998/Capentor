from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('AllProduct', views.AllProduct, name='AllProduct'),
]