from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from api.query import Query
import random
from modules.recaptcha import recaptcha


def index(request):
    page = request.GET.get('page', 1)

    query = Query()

    data = query.get(
        'product.template',
        'search_read', [
            ['type', '=', 'product'],
            ['categ_id', '=', 139],
            ['x_studio_field_OaF3K', '=', True]
        ],
        {
            'fields': ['id', 'name', 'default_code', 'x_studio_field_QlEui', 'create_date', 'create_date'],
            'order': 'create_date'
        })

    # Django pagination
    paginator = Paginator(data, 20)
    pages = paginator.get_page(page)

    context = {"products": pages}

    return render(request, 'products/index.html', context)


def single(request, product_id):
    query = Query()

    data = query.get('product.template', 'search_read',
                     [['type', '=', 'product'], ['categ_id', '=', 139], ['x_studio_field_OaF3K', '=', True],
                      ['id', '=', product_id]],
                     {
                         'fields': ['id', 'name', 'default_code', 'x_studio_field_QlEui', 'create_date', 'create_date']
                     }
                     )

    random_number = random.randint(0, 3)

    context = {
        "product": data[0],
        "content_random": 'products/content/{}.html'.format(random_number)
    }

    return render(request, 'products/single.html', context)


def search(request):
    q = request.GET['q']

    query = Query()

    data = query.get('product.template', 'search_read',
                     [['type', '=', 'product'], ['categ_id', '=', 139], ['x_studio_field_OaF3K', '=', True],
                      ['x_studio_field_QlEui', 'ilike', q]],
                     {
                         'fields':  ['id', 'name', 'default_code', 'x_studio_field_QlEui', 'create_date', 'create_date'],
                         'limit': 20
                     }
                     )

    context = {"products": data}

    return render(request, 'products/search.html', context)


def lead(request):
    if request.method == 'POST' and recaptcha(request):
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        description = 'Producto: ' + request.POST['product_name'], 'Número de parte Mesabi: ' + request.POST['mpn'], 'Número de parte OEM: ' + request.POST['oempn'], 'Mensaje: ' + request.POST['msg']

        query = Query()

        data = query.create('crm.lead', 'create',
                            {
                                'name': 'radiadores-mesabi.com.mx',
                                'user_id': 110,
                                'contact_name': full_name,
                                'email_from': email,
                                'phone': phone,
                                'description': description
                             })
        return redirect('thanks')
    else:
        return redirect('index')
