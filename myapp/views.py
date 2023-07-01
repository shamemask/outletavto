from django.shortcuts import render
import os

from django.shortcuts import render, redirect
from myapp.forms import RegistrationForm
from myapp.main_logic.news_parser import get_news
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async
from django.views.decorators.csrf import csrf_protect

# @sync_to_async
# @login_required
@csrf_protect
def index(request):
    image_names = os.listdir('./images')
    news = get_news("https://dvizhok.su/dvizhok-rss.rss")
    signup_form = SignupForm()
    login_form = LoginForm()
    return render(request, 'index.html', {'signup_form': signup_form, 'login_form':login_form, 'news': news})

def image_detail(request, image_name):
    image_names = os.listdir('./images')
    image_names = [x.replace('.png','') for x in image_names if x.endswith('.png')]
    return render(request, 'image_detail.html', {'image_name': image_name, 'image_names': image_names})


# @sync_to_async
@login_required
def profile_view(request):
    return render(request, 'profile.html')