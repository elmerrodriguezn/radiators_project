from django.shortcuts import render, redirect
from products.api_queries import context, context_limit, context_detail, context_search, create_lead

def single(request, default_code):
    return render(request, 'products/single.html', context_detail(default_code))

def search(request):
    q = request.GET['keywords']
    return render(request, 'products/search.html', context_search(q))
def lead(request):
    fullName = request.GET['fullName']
    #city = request.GET['city']
    email = request.GET['email']
    phone = request.GET['phone']
    description = 'Producto: ' + request.GET.get('productName', False), 'Número de parte Mesabi: ' + request.GET.get('mpn', False), 'Número de parte: ' + request.GET.get('oempn', False), 'Mensaje: ' + request.GET['msg']
    create_lead(fullName, email, phone, description)
    return redirect('index')
def handler404(request):
    return render(request, 'products/404.html', status=404)

def handler500(request):
    return render(request, 'products/500.html', status=500)