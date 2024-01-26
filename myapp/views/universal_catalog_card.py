import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def universal_catalog_card_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'universal-catalog-card'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','universal-catalog-card_page.html'), templ_dict)
