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
            [
            'name', 'ilike', q
            ],
            [
            'default_code', 'ilike', q
            ]
        ]
        
    ]],
    {'fields': ['name', 'default_code', 'x_studio_field_QlEui'] })

    data_search = json.dumps(raw_search)
    data_search = json.loads(data_search)
    context_search = {
        'products': data_search
    }