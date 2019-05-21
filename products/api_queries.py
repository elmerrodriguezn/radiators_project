from api_connection import *
import json
from django.shortcuts import redirect

def context():
    raw = models.execute_kw(
        db,
        uid,
        password,
        'product.template', 'search_read',
        [[
            [
                'type', '=', 'product'
            ],
            [
                'categ_id', '=', 139
            ],
            [
                'x_studio_field_OaF3K', '=', True
            ]
        ]],
        {'fields': ['name', 'default_code', 'x_studio_field_QlEui']})

    data = json.dumps(raw)
    data = json.loads(data)
    context = {
        "products": data
    }
    return context

def context_limit():
    raw_limit = models.execute_kw(
        db,
        uid,
        password,
        'product.template', 'search_read',
        [[
            [
                'type', '=', 'product'
            ],
            [
                'categ_id', '=', 139
            ],
            [
                'x_studio_field_OaF3K', '=', True
            ]
        ]],
        {'fields': ['name', 'default_code', 'x_studio_field_QlEui', 'create_date'], 'limit': 6, 'order': 'create_date'  })

    data_limit = json.dumps(raw_limit)
    data_limit = json.loads(data_limit)
    context_limit = {
        "products": data_limit
    }
    return context_limit

def context_detail(default_code):
    raw_detail= models.execute_kw(
    db,
    uid,
    password,
    'product.template', 'search_read',
    [[
        [
            'type', '=', 'product'
        ],
        [
            'categ_id', '=', 139
        ],
        [
            'x_studio_field_OaF3K', '=', True
        ],
        [
            'default_code', '=', default_code
        ],
    ]],
    {'fields': ['name', 'default_code', 'x_studio_field_QlEui'], 'limit': 6 })

    data_detail = json.dumps(raw_detail)
    data_detail = json.loads(data_detail)
    context_detail = {
        "details": data_detail
    }

    return context_detail

def context_search(q):
    raw_search= models.execute_kw(
    db,
    uid,
    password,
   'product.template', 'search_read',
    [[
        [
            'type', '=', 'product'
        ],
        [
            'categ_id', '=', 139
        ],
        [
            'x_studio_field_OaF3K', '=', True
        ],
        [
            'default_code', 'ilike', q
        ],
    ]],
    {'fields': ['name', 'default_code', 'x_studio_field_QlEui'], 'limit': 6 })

    data_search = json.dumps(raw_search)
    data_search = json.loads(data_search)
    context_search = {
        'products': data_search
    }

    return context_search

def create_lead(fullName, email, phone, description):
    raw_search= models.execute_kw(
    db,
    uid,
    password,
   'crm.lead', 'create', [{
       'name': 'Contacto sitio web',
       'contact_name': fullName,
       'email_from': email,
       'phone': phone,
       'description': description
   }])

    return print('succefull')
    
