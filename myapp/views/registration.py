import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def registration_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'registration'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','registration_page.html'), templ_dict)
