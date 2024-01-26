import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from abcp_parser.models import CatalogItem
from authentication.views.main import auth


@csrf_exempt
def universal_catalog_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'universal-catalog'
    catalog = 'oils_catalog'
    # получить все данные полей catalog из таблицы CatalogItem
    catalog_items = CatalogItem.objects.filter(catalog=catalog)
    # queryset to list, row to dict
    catalog_items = list(catalog_items.values())
    for i in range(len(catalog_items)):
        other_info = catalog_items[i]['other_info']
        catalog_items[i]['other_info'] = {}
        for info_text in other_info.split('\n'):
            if not info_text: continue
            slt = info_text.split(':')
            catalog_items[i]['other_info'][slt[0]] = slt[1]
    page_count = 6
    paginator = Paginator(catalog_items, page_count)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, установите на первую страницу
        objects = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше максимального, установите на последнюю страницу
        objects = paginator.page(paginator.num_pages)
    templ_dict['catalog_items'] = objects
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','universal-catalog_page.html'), templ_dict)
