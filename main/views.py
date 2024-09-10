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
    
    temporary = [
        {
            'name':"Laptop", 
            'price':1200, 
            'description':"A high-performance laptop."
        },
        {
            'name':"Smartphone", 
            'price':1000, 
            'description':"A latest model smartphone."
        },
        {
            'name':"Computer", 
            'price':1000, 
            'description':"A latest model computer."
        }
    ]

    context = {
        'npm': '2306165654',
        'name': 'Anthony Edbert Feriyanto',
        'class_name': 'PBP C',
        'shop_name':'Ayo Belanja',  
        'products': temporary  
    }

    return render(request, "main.html", context)
