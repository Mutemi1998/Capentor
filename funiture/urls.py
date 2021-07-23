from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product', views.product, name='product'),
    path('AllProduct', views.AllProduct, name='AllProduct'),

    path('AllHome', views.AllHome, name='AllHome'),
    path('dinnerware', views.dinnerware, name='dinnerware'),
    path('glassware', views.glassware, name='glassware'),

    path('AllLiving', views.AllLiving, name='AllLiving'),
    path('recliner', views.recliner, name='recliner'),
    path('sofa', views.sofa, name='sofa'),
    path('tv', views.tv, name='tv'),

    path('Allbedroom', views.Allbedroom, name='Allbedroom'),
    path('bed', views.recliner, name='bed'),
    path('study', views.sofa, name='study'),
    path('dressing', views.tv, name='dressing'),

    path('AllOffice', views.AllOffice, name='AllOffice'),
    path('confrence', views.confrence, name='confrence'),
    path('executive', views.executive, name='executive'),
    path('office', views.office, name='office'),

    path('AllDinning', views.AllDinning, name='AllDinning'),
    path('barChair', views.barChair, name='barChair'),
    path('dinningChair', views.dinningChair, name='dinningChair'),
    path('dinningSet', views.dinningSet, name='dinningSet'),
]