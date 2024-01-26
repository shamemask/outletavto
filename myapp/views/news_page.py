import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth
from myapp.main_logic.news_parser import get_news, get_new


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
