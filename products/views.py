from django.shortcuts import render, redirect
from django.contrib import messages
from products.api_queries import *

def single(request, default_code):
    return render(request, 'products/single.html', context_detail(default_code))

def search(request):
    q = request.GET['keywords']
    return render(request, 'products/search.html', context_search(q))
def lead(request):
    fullName = request.GET['fullName']
    email = request.GET['email']
    phone = request.GET['phone']
    description = 'Producto: ' + request.GET.get('productName', False), 'Número de parte Mesabi: ' + request.GET.get('mpn', False), 'Número de parte OEM: ' + request.GET.get('oempn', False), 'Mensaje: ' + request.GET['msg']
    create_lead(fullName, email, phone, description)
    messages.success(request, 'Gracias por contáctaros, nuestro equipo de ventas se comunicará contigo a la brevedad.')
    return redirect('/productos/'+request.GET.get('mpn', False))

def contact(request):
    re
def handler404(request):
    return render(request, 'products/404.html', status=404)

def handler500(request):
    return render(request, 'products/500.html', status=500)