import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def passenger_car_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Поиск автомобиля'
    templ_dict['page_class'] = 'passenger-car'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','passenger-car_page.html'), templ_dict)
