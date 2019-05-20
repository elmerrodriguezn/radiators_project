from django.shortcuts import render
from products.api_connection import context_limit

def index(request):
    return render(request, 'pages/index.html', context_limit())
