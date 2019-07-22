from django.core.paginator import Paginator
# Importing api_connection from root project to bring api variables
from api_connection import *
import random

# Template function to query api taking arguments
api_template = lambda model, operation, query='', fields='' : models.execute_kw(db, uid, password, model, operation,[query], fields)

def context(page):
    # Template api function parameters
    model = 'product.template'
    operation = 'search_read'
    query = [['type', '=', 'product'],['categ_id', '=', 153],['x_studio_field_OaF3K', '=', True]]
    fields = {'fields': ['name', 'default_code', 'x_studio_field_QlEui', 'create_date'], 'order': 'create_date'  }

    # Template api function
    data = api_template(model, operation, query, fields)

    # Django pagination
    paginator = Paginator(data, 12)
    pages = paginator.get_page(page)

    context = {
        'products': pages
    }
    
    return context

def context_limit():
    # Template api function parameters
    model = 'product.template'
    operation = 'search_read'
    query = [['type', '=', 'product'],['categ_id', '=', 153],['x_studio_field_OaF3K', '=', True]]
    fields = {'fields': ['name', 'default_code', 'x_studio_field_QlEui', 'create_date'], 'limit': 12, 'order': ''  }

    # Template api function
    data_limit = api_template(model, operation, query, fields)

    context_limit = {
        "products": data_limit
    }
    return context_limit

def context_detail(default_code):
    # Template api function parameters
    model = 'product.template'
    operation = 'search_read'
    query = [['type', '=', 'product'],['categ_id', '=', 153],['x_studio_field_OaF3K', '=', True],['default_code', '=', default_code]]
    fields = {'fields': ['name', 'default_code', 'x_studio_field_QlEui'] }

    # Template api function
    data_detail= api_template(model, operation, query, fields)
    random_number = random.randint(0, 3)
    context_detail = {
        "detail": data_detail[0],
        "content_random": 'products/content/{}.html'.format(random_number)
    }

    return context_detail

def context_search(q):
    # Template api function parameters
    model = 'product.template'
    operation = 'search_read'
    # Query accepting q parameter requested in the view
    query = [['type', '=', 'product'],['categ_id', '=', 153],['x_studio_field_OaF3K', '=', True],['name','ilike', q]]
    #x_studio_field_QlEui
    fields = {'fields': ['name', 'default_code', 'x_studio_field_QlEui'], 'limit': 12 }
    
    # Template api function
    data_search = api_template(model, operation, query, fields)
    
    context_search = {
        'products': data_search
    }

    return context_search

def create_product_lead(fullName, email, phone, description):
    # Template api function parameters
    model = 'crm.lead'
    operation = 'create'
    # Query accepting q parameter requested in the view
    query = {
       'name': 'radiadores-mesabi.com.mx',
       'contact_name': fullName,
       'email_from': email,
       'phone': phone,
       'description': description 
       }
    
    # Template api function
    api_template(model, operation, query)
    pass

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