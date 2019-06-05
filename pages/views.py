from django.shortcuts import render
from django.http import HttpResponse
from products.api_queries import context_limit

def index(request):
    return render(request, 'pages/index.html', context_limit())
