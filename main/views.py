from django.shortcuts import render,redirect,get_object_or_404
from .models import ProductEntry  
from main.forms import ProductEntryForm
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    products = ProductEntry.objects.all()

    context = {
        'npm': '2306165654',
        'name': 'Anthony Edbert Feriyanto',
        'class_name': 'PBP C',
        'shop_name':'Ayo Belanja',  
        'product_entry' : products
    }

    return render(request, "main.html", context)

def create_name_entry(request):
    form = ProductEntryForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context={'form':form}
    return render(request,'create_name_entry.html',context)


def delete_product_entry(request, id):
    if request.method == 'POST':
        product = get_object_or_404(ProductEntry, id=id)
        product.delete()
        return redirect('main:show_main')
    return redirect('main:show_main')


def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml",data),content_type='application/xml')

def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type='application/json')

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
