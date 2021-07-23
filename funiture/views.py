from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def AllProduct(request):
    return render(request, 'AllProduct.html')


def product(request):
    return render(request, 'product.html')


# functions for calling home links
def dinnerware(request):
    return render(request, 'Home/dinnerware.html')

def glassware(request):
    return render(request, 'Home/glassware.html')

def AllHome(request):
    return render(request, 'Home/AllProduct.html')


# functions for calling living links
def sofa(request):
    return render(request, 'Living/sofa.html')

def recliner(request):
    return render(request, 'Living/recliner.html')

def tv(request):
    return render(request, 'Living/tv.html')

def AllLiving(request):
    return render(request, 'Living/AllLiving.html')


# functions for calling Bedroom links
def Bed(request):
    return render(request, 'Bedroom/bed.html')

def Study(request):
    return render(request, 'Bedroom/study.html')

def Dressing(request):
    return render(request, 'Bedroom/dressing.html')

def Allbedroom(request):
    return render(request, 'Bedroom/Allbedroom.html')



# functions for calling Office links
def confrence(request):
    return render(request, 'Office/confrence.html')

def executive(request):
    return render(request, 'Office/executive.html')

def office(request):
    return render(request, 'Office/office.html')

def AllOffice(request):
    return render(request, 'Office/Alloffice.html')



# functions for calling Dinning links
def barChair(request):
    return render(request, 'Dinning/barChair.html')

def dinningChair(request):
    return render(request, 'Dinning/dinningChair.html')

def dinningSet(request):
    return render(request, 'Dinning/dinningSet.html')

def AllDinning(request):
    return render(request, 'Dinning/AllDinning.html')