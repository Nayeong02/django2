from django.shortcuts import render
from . models import Products

# Create your views here.
def product(request) :
    p = Products.objects.all().values()
    return render(request, 'p_list.html', {'p' : p})

def add(request) :
    return render(request, 'insert.html')