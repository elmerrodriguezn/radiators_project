from api_connection import *
from django.shortcuts import redirect

# Template function to query api taking two arguments
api_template = lambda model, operation, query='', fields='' : models.execute_kw(db, uid, password, model, operation,[query], fields)

def create_lead(fullName, email, phone, msg):
    # Template api function parameters
    model = 'crm.lead'
    operation = 'create'
    # Query accepting q parameter requested in the view
    query = {
       'name': 'radiadores-mesabi.com.mx',
       'contact_name': fullName,
       'email_from': email,
       'phone': phone,
       'description': msg
       }
    
    # Template api function
    api_template(model, operation, query)
    pass
    