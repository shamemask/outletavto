import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def passenger_car_info_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Подбор запчастей по параметрам'
    templ_dict['page_class'] = 'passenger-car-info'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','passenger-car-info_page.html'), templ_dict)
