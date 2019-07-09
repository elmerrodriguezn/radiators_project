from django.shortcuts import render, redirect
from django.contrib import messages
from contact.api_queries import *

def contact(request):
    return render(request, 'contact/index.html')

def send_lead(request):
    fullName = request.POST['fullName']
    email = request.POST['email']
    phone = request.POST['phone']
    msg = request.POST['msg']
    create_lead(fullName, email, phone, msg)
    return redirect('/gracias-por-contactarnos/')