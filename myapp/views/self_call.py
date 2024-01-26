import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def self_call_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'self-call'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','self-call_page.html'), templ_dict)
