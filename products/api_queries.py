# Importing this module to bring api variables
from api_connection import *
import json
from django.shortcuts import redirect

def context():
    data = models.execute_kw(
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

    context = {
        "products": data
    }
    return context

def context_limit():
    data_limit = models.execute_kw(
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
        {'fields': ['name', 'default_code', 'x_studio_field_QlEui', 'create_date'], 'limit': 12, 'order': 'create_date'  })

    context_limit = {
        "products": data_limit
    }
    return context_limit

def context_detail(default_code):
    data_detail= models.execute_kw(
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
    {'fields': ['name', 'default_code', 'x_studio_field_QlEui'] })

    context_detail = {
        "details": data_detail
    }

    return context_detail

def context_search(q):
    data_search= models.execute_kw(
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
        ['name','ilike', q],
    ]],
    {'fields': ['name', 'default_code', 'x_studio_field_QlEui'], 'limit': 12 })
    if not data_search:
        data_search= models.execute_kw(
        db,
        uid,
        password, 'product.template', 'search_read',
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
                'x_studio_field_QlEui', 'ilike', q
            ]
        ]],
        {'fields': ['name', 'default_code', 'x_studio_field_QlEui'] })

    context_search = {
        'products': data_search
    }

    return context_search

def create_lead(fullName, email, phone, description):
    models.execute_kw(
    db,
    uid,
    password,
   'crm.lead', 'create', [{
       'name': 'Contacto radiators.com.mx',
       'contact_name': fullName,
       'email_from': email,
       'phone': phone,
       'description': description
   }])

    return print('Operacion exitosa')


