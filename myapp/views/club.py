import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def club_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Клуб'
    templ_dict['page_class'] = 'club'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','club_page.html'), templ_dict)
