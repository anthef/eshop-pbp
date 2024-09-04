from django.shortcuts import render
from .models import ProductEntry  

def show_main(request):
    products = ProductEntry.objects.all()

    seen = set()
    unique_products = []
    for product in products:
        if product.name not in seen:
            unique_products.append(product)
            seen.add(product.name)

    context = {
        'npm': '2306165654',
        'name': 'Anthony Edbert Feriyanto',
        'class_name': 'PBP C',  
        'products': unique_products  
    }

    return render(request, "main.html", context)
