from django.shortcuts import render
import os

from myapp.main_logic.news_parser import get_news


def index(request):
    image_names = os.listdir('./images')
    news = get_news("https://dvizhok.su/dvizhok-rss.rss")
    image_names = [x.replace('.png','') for x in image_names if x.endswith('.png')]
    return render(request, 'index.html', {'news': news})

def image_detail(request, image_name):
    image_names = os.listdir('./images')
    image_names = [x.replace('.png','') for x in image_names if x.endswith('.png')]
    return render(request, 'image_detail.html', {'image_name': image_name, 'image_names': image_names})