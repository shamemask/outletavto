import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from abcp_parser.models import CatalogItem
from authentication.views.main import auth
from myapp.logging import logger

catalog_dict = {
    'compressors_catalog': 'Компрессоры',
    'oils_catalog': 'Масла',
    'jacks_catalog': 'Штанги',
    'poly_v_belts_catalog': 'Ремни поликлиновые',
    'gear_oils_catalog': 'Приводные масла',
    'tires_catalog': 'Шины',
    'sockets_catalog': 'Разъемы',
    'disks_catalog': 'Диски',
    'batteries_catalog': 'Аккумуляторы',
    'truck_tires_catalog': 'Шины для грузовиков',
    'wipers_catalog': 'Вибраторы',
}

@csrf_exempt
def universal_catalog_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'universal-catalog'

    catalog = request.GET.get('catalog')
    if not catalog:
        catalog = 'oils_catalog'
    templ_dict['catalog'] = catalog
    # Получить все уникальные значения из колонки catalog
    # all_catalog_names = list(CatalogItem.objects.values_list('catalog').distinct())
    # all_catalog_names = [ cell[0] for cell in all_catalog_names ]
    templ_dict['all_catalog_names'] = catalog_dict
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
            catalog_items[i]['other_info'][slt[0]] = slt[1] if len(slt)>1 else ''
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
