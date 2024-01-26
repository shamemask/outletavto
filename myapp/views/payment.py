import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def payment_page(request):
    """
    Страница оплаты заказа
    """
    templ_dict = {}
    templ_dict['page_title'] = 'Оплата заказа'
    templ_dict['page_class'] = 'payment'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','payment_page.html'), templ_dict)
