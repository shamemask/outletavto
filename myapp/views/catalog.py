import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def catalog_page(request):
    """
    Страница каталога
    """
    templ_dict = {}
    templ_dict['page_title'] = 'Каталог'
    templ_dict['page_class'] = 'catalog'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','catalog_page.html'), templ_dict)
