from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def AllProduct(request):
    return render(request, 'AllProduct.html')


def product(request):
    return render(request, 'product.html')

def dinnerware(request):
    return render(request, 'Home/dinnerware.html')

def glassware(request):
    return render(request, 'Home/glassware.html')

def AllHome(request):
    return render(request, 'Home/AllProduct.html')