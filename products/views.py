from django.shortcuts import render
from products.api_connection import context, context_limit, context_detail

# Create your views here.
def index(request):
    x = slice(3)
    return render(request, 'products/index.html', context_limit())


def single(request, default_code):
    return render(request, 'products/single.html', context_detail(default_code))


def search(request):
    return render(request, 'products/search.html', context())
