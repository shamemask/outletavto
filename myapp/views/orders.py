import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def orders_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Заказы'
    templ_dict['page_class'] = 'orders'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','orders_page.html'), templ_dict)
