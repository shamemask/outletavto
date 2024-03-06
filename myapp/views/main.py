import json
import os
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from abcp_parser.models import CatalogItem
from authentication.UserModel import FizUser
from authentication.views.main import auth
from authentication.views_api.main import auth_api
from myapp.main_logic.news_parser import get_news,get_new
from django.views.decorators.csrf import csrf_exempt
import os
from django.shortcuts import render, redirect


@csrf_exempt
def logic(request, web_or_api='web'):
    """
    Главная страница сайта
    """

    templ_dict = {}
    templ_dict['page_title'] = 'OutletAvto'
    templ_dict['message'] = 'Запчасти в интернет-магазине'
    if web_or_api == 'web':
        authenticate = auth(request)
    else:
        authenticate = auth_api(request)
    templ_dict.update(authenticate)
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
    # request.session.save()
    return templ_dict

@api_view(['POST'])
@csrf_exempt
def index_api(request):
    templ_dict = logic(request, 'api')
    return Response(templ_dict)


@csrf_exempt
def index(request):
    """
    Главная страница сайта
    """
    template = 'index.html'
    templ_dict = logic(request)
    if templ_dict['fizform'].errors or templ_dict['urform'].errors:
        template = os.path.join('outletauto_page','registration_page.html')
    return render(request, template, templ_dict)


