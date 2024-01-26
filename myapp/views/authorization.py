import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def authorization_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Авторизация'
    templ_dict['page_class'] = 'authorization'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','authorization_page.html'), templ_dict)
