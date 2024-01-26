import os
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from abcp_parser.models import CatalogItem
from authentication.UserModel import FizUser
from authentication.views.main import auth
from myapp.main_logic.news_parser import get_news,get_new
from django.views.decorators.csrf import csrf_exempt
import os
from django.shortcuts import render, redirect


@csrf_exempt
def index(request):
    """
    Главная страница сайта
    """

    templ_dict = {}
    template = 'index.html'
    templ_dict['page_title'] = 'OutletAvto'
    templ_dict['message'] = 'Запчасти в интернет-магазине'
    templ_dict.update(auth(request))
    templ_dict['catalogue'] = [
        'Оригинальные запчасти',
        'Запчасти для ТО',
        'Каталоги TecDoc',
        'Шины и диски',
        'Масла и тех.жидкости',
        'Доб. оборудование',
        'Инструмент',
        'Автохимия и косметика',
        'Щетки, лампы, аксессуары',
    ]
    templ_dict['popular'] = [
        'Свет и электрика',
        'Электроинструменты',
        'Садовая техника',
        'Ручные инструменты',
        'Бытовая химия',
        'Канцтовары',
        'Детские товары',
        'Велосипеды',
        'Туризм, рыбалка',
    ]
    if templ_dict['fizform'].errors or templ_dict['urform'].errors:
        template = os.path.join('outletauto_page','registration_page.html')
    # request.session.save()
    return render(request, template, templ_dict)
