from django.shortcuts import render, redirect
from django.contrib import messages
from contact.api_queries import *

def lead(request):
    #fullName = request.GET['fullName']
    #email = request.GET['email']
    #phone = request.GET['phone']
    #msg = request.GET['msg']
    #create_lead(fullName, email, phone, msg)
    #messages.success(request, 'Gracias por contáctaros, nuestro equipo de ventas se comunicará contigo a la brevedad.')
    return render(request, 'contact/index.html')