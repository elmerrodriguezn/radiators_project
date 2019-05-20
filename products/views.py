from django.shortcuts import render
from products.api_connection import context, context_limit, context_detail, context_search

def single(request, default_code):
    return render(request, 'products/single.html', context_detail(default_code))

def search(request):
    q = request.GET['keywords']
    return render(request, 'products/search.html', context_search(q))

def handler404(request):
    return render(request, 'products/404.html', status=404)

def handler500(request):
    return render(request, 'products/500.html', status=500)