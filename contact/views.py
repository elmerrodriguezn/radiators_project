from django.shortcuts import render, redirect
from django.contrib import messages
from contact.api_queries import *

def contact(request):
    return render(request, 'contact/index.html')

def send_lead(request):
    fullName = request.GET.get('fullName', False)
    email = request.GET.get('email', False)
    phone = request.GET.get('phone', False)
    msg = request.GET.get('msg', False)
    create_lead(fullName, email, phone, msg)
    return redirect('/gracias-por-contactarnos/')