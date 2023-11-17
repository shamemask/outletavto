import os

from authentication.UserModel import FizUser
from authentication.views.main import auth
from myapp.main_logic.news_parser import get_news,get_new
from django.views.decorators.csrf import csrf_exempt
import os
from django.shortcuts import render


# @sync_to_async
# @login_required
@csrf_exempt
def index(request):
    templ_dict = {}
    templ_dict['page_title'] = 'OutletAvto'
    templ_dict['message'] = 'Запчасти в интернет-магазине'
    # path = os.getcwd() + '/static/outletauto/pages'
    # files = os.listdir(path)
    # files_list = [file.replace('.html','') for file in files if file != 'favicon.ico']
    # files_dict = {}
    # count = '0'
    # i = 0
    # for file in files_list:
    #     i += 1
    #     if i == 1 or i % 10 == 0:
    #         count = f'{i // 10}1-{1 + (i // 10)}0'
    #         files_dict[count] = []
    #     files_dict[count].append(file)
    # templ_dict['files_dict2'] = files_dict
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
    request.session.save()
    return render(request, 'index.html', templ_dict)

@csrf_exempt
def catalog_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Каталог'
    templ_dict['page_class'] = 'catalog'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','catalog_page.html'), templ_dict)

@csrf_exempt
def payment_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Оплата заказа'
    templ_dict['page_class'] = 'payment'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','payment_page.html'), templ_dict)

@csrf_exempt
def news_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Новости'
    templ_dict['page_class'] = 'news'
    templ_dict.update(auth(request))
    request.session.save()
    templ_dict['news'] = get_news("https://dvizhok.su/dvizhok-rss.rss")
    return render(request, os.path.join('outletauto_page','news_page.html'), templ_dict)


@csrf_exempt
def add_auto_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Баланс'
    templ_dict['page_class'] = 'add-auto'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','add-auto_page.html'), templ_dict)
@csrf_exempt
def authorization_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Авторизация'
    templ_dict['page_class'] = 'authorization'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','authorization_page.html'), templ_dict)
@csrf_exempt
def balance_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Баланс'
    templ_dict['page_class'] = 'balance'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','balance_page.html'), templ_dict)
@csrf_exempt
def basket_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Корзина'
    templ_dict['page_class'] = 'basket'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','basket_page.html'), templ_dict)
@csrf_exempt
def call_to_vin_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Движение заказов'
    templ_dict['page_class'] = 'call-to-vin'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','call-to-vin_page.html'), templ_dict)
@csrf_exempt
def catalog_personal_account_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'catalog-personal-account'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','catalog-personal-account_page.html'), templ_dict)
@csrf_exempt
def club_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Клуб'
    templ_dict['page_class'] = 'club'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','club_page.html'), templ_dict)
@csrf_exempt
def company_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Компания'
    templ_dict['page_class'] = 'company'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','company_page.html'), templ_dict)
@csrf_exempt
def favorite_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Избранное'
    templ_dict['page_class'] = 'favorite'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','favorite_page.html'), templ_dict)
@csrf_exempt
def garage_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Гараж'
    templ_dict['page_class'] = 'garage'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','garage_page.html'), templ_dict)
@csrf_exempt
def modification_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'modification'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','modification_page.html'), templ_dict)
@csrf_exempt
def news_page_page(request, index):
    templ_dict = {}

    templ_dict['page_class'] = 'news-page'
    templ_dict.update(auth(request))
    news = get_news("https://dvizhok.su/dvizhok-rss.rss")
    templ_dict['news'] = news
    # news = get_news_autoparts("https://autoparts.webnode.page/rss/stati.xml")
    templ_dict['new'] = get_new(news[int(index)-1]['link'])
    templ_dict['page_title'] = templ_dict['new']['title']
    return render(request, os.path.join('outletauto_page','news-page_page.html'), templ_dict)
@csrf_exempt
def orders_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Заказы'
    templ_dict['page_class'] = 'orders'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','orders_page.html'), templ_dict)
@csrf_exempt
def passenger_car_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Поиск автомобиля'
    templ_dict['page_class'] = 'passenger-car'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','passenger-car_page.html'), templ_dict)
@csrf_exempt
def passenger_car_info_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Подбор запчастей по параметрам'
    templ_dict['page_class'] = 'passenger-car-info'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','passenger-car-info_page.html'), templ_dict)
@csrf_exempt
def profile_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Профиль'
    templ_dict['page_class'] = 'profile'
    templ_dict.update(auth(request))
    fields = templ_dict['user']._meta.fields
    profile_dict = {}
    for field in fields:
        if field.name not in ['_state', 'id', 'last_login','password', 'promo_code','terms_of_service','is_active']:
            profile_dict[field.name] = [templ_dict['user'].__dict__[field.name],field.verbose_name]
        if field.name == 'password':
            profile_dict[field.verbose_name] = ['********',field.verbose_name]
    templ_dict['profile_dict'] = profile_dict
    return render(request, os.path.join('outletauto_page','profile_page.html'), templ_dict)
@csrf_exempt
def promotion_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'promotion'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','promotion_page.html'), templ_dict)
@csrf_exempt
def recovery_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'recovery'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','recovery_page.html'), templ_dict)
@csrf_exempt
def registration_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'registration'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','registration_page.html'), templ_dict)
@csrf_exempt
def self_call_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'self-call'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','self-call_page.html'), templ_dict)
@csrf_exempt
def testcalendar_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = ''
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','TESTCALENDAR_page.html'), templ_dict)
@csrf_exempt
def testfilter_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = ''
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','TESTFILTER_page.html'), templ_dict)
@csrf_exempt
def universal_catalog_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'universal-catalog'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, os.path.join('outletauto_page','universal-catalog_page.html'), templ_dict)
@csrf_exempt
def universal_catalog_tire_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'universal-catalog-tire'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','universal-catalog-tire_page.html'), templ_dict)
@csrf_exempt
def universal_catalog_tire_2_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'universal-catalog-tire-2'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','universal-catalog-tire-2_page.html'), templ_dict)
@csrf_exempt
def universal_catalog_tire_3_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'universal-catalog-tire-3'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','universal-catalog-tire-3_page.html'), templ_dict)
@csrf_exempt
def universal_catalog_card_page(request):
    templ_dict = {}
    templ_dict['page_title'] = 'Персональный каталог'
    templ_dict['page_class'] = 'universal-catalog-card'
    templ_dict.update(auth(request))
    return render(request, os.path.join('outletauto_page','universal-catalog-card_page.html'), templ_dict)

@csrf_exempt
def html(request,html):
    return render(request, os.path.join('pages',html+'.html'), {})



