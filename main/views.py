from django.shortcuts import render
from .models import ProductEntry  

def show_main(request):
    products = ProductEntry.objects.all()
    context = {
        'npm': '2306165654',
        'name': 'Anthony Edbert Feriyanto',
        'class': 'PBP C',
        'products': products  
    }

    return render(request, "main.html", context)
