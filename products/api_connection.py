import xmlrpc.client
import json


db = "mailync-lymmx-master-43217"
username = "sistemas"
password = "Faz21687"
url = "https://lymmx.odoo.com"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(db, username, password, {})

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
        {'fields': ['name', 'default_code', 'x_studio_field_QlEui'], 'limit': 6 })

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
