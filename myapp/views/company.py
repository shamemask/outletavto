import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def company_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Компания'
    templ_dict['page_class'] = 'company'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','company_page.html'), templ_dict)
