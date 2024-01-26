import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def modification_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'modification'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','modification_page.html'), templ_dict)
