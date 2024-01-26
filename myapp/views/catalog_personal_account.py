import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def catalog_personal_account_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'catalog-personal-account'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','catalog-personal-account_page.html'), templ_dict)
