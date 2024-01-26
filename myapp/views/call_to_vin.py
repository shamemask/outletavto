import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def call_to_vin_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Движение заказов'
    templ_dict['page_class'] = 'call-to-vin'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','call-to-vin_page.html'), templ_dict)
