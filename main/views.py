from django.shortcuts import render,redirect,get_object_or_404
from .models import ProductEntry  
from main.forms import ProductEntryForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime

@login_required(login_url='/login')
def show_main(request):
    products = ProductEntry.objects.filter(user=request.user)

    context = {
        'npm': '2306165654',
        'name': request.user.username,
        'class_name': 'PBP C',
        'shop_name':'Ayo Belanja',  
        'product_entry' : products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_name_entry(request):
    form = ProductEntryForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        name_entry = form.save(commit=False)
        name_entry.user = request.user
        name_entry.save()
        return redirect('main:show_main')
    context={'form':form}
    return render(request,'create_name_entry.html',context)

@login_required(login_url='/login')
def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml",data),content_type='application/xml')

@login_required(login_url='/login')
def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type='application/json')

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    print("Logout successful, redirecting to login page") 
    return response

@login_required(login_url='/login')
def delete_product(request, id):
    mood = ProductEntry.objects.get(pk = id)
    mood.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def edit_product(request, id):
    mood = ProductEntry.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=mood)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_product.html", context)





