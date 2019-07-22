from django.shortcuts import render, redirect
from api.queries import *

def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'products/index.html', context(page))

def single(request, default_code):
    return render(request, 'products/single.html', context_detail(default_code))

def search(request):
    q = request.GET['q']
    return render(request, 'search/index.html', context_search(q))

def lead(request):
    fullName = request.POST['fullName']
    email = request.POST['email']
    phone = request.POST['phone']
    description = 'Producto: ' + request.POST['productName'], 'Número de parte Mesabi: ' + request.POST['mpn'], 'Número de parte OEM: ' + request.POST['oempn'], 'Mensaje: ' + request.POST['msg']
    create_product_lead(fullName, email, phone, description)
    return redirect('/gracias-por-contactarnos/')