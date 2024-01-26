import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth
from myapp.main_logic.news_parser import get_news


@csrf_exempt
def news_page(request):
    """
    Страница новостей
    """
    templ_dict = {}
    templ_dict['page_title'] = 'Новости'
    templ_dict['page_class'] = 'news'
    templ_dict.update(auth(request))
    request.session.save()
    templ_dict['news'] = get_news("https://dvizhok.su/dvizhok-rss.rss")
    return render(request, os.path.join('outletauto_page','news_page.html'), templ_dict)
