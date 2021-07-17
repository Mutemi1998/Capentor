from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product', views.product, name='product'),
    path('AllProduct', views.AllProduct, name='AllProduct'),
    path('AllHome', views.AllHome, name='AllHome'),
    path('dinnerware', views.dinnerware, name='dinnerware'),
    path('glassware', views.glassware, name='glassware'),

]