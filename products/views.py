from django.shortcuts import render, redirect
from products.api_queries import *

def single(request, default_code):
    return render(request, 'products/single.html', context_detail(default_code))

def search(request):
    q = request.GET['keywords']
    return render(request, 'products/search.html', context_search(q))
    
def lead(request):
    fullName = request.POST['fullName']
    email = request.POST['email']
    phone = request.POST['phone']
    description = 'Producto: ' + request.POST['productName'], 'Número de parte Mesabi: ' + request.POST['mpn'], 'Número de parte OEM: ' + request.POST['oempn'], 'Mensaje: ' + request.POST['msg']
    create_lead(fullName, email, phone, description)
    return redirect('/gracias-por-contactarnos/')