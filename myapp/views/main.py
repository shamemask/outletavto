import os

from authentication.views.main import auth
from myapp.main_logic.news_parser import get_news
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render



# @sync_to_async
# @login_required
@csrf_exempt
def index(request):
    templ_dict = {}
    templ_dict['news'] = get_news("https://dvizhok.su/dvizhok-rss.rss")
    templ_dict['message'] = 'Запчасти в интернет-магазине'
    templ_dict.update(auth(request))
    request.session.save()
    return render(request, 'index.html', templ_dict)





