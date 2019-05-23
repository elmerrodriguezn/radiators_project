from api_connection import *
import json
from django.shortcuts import redirect

def create_lead(fullName, email, phone, description):
    raw_search= models.execute_kw(
    db,
    uid,
    password,
   'crm.lead', 'create', [{
       'name': 'Contacto radiators.com.mx',
       'contact_name': fullName,
       'email_from': email,
       'phone': phone,
       'description': msg
   }])

    return redirect('/contacto')
    