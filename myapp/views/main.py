import os

from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.base_user import AbstractBaseUser

from myapp.EmailConfirm import send_token_email
from myapp.backends import FizUserBackend, UrUserBackend
from myapp.forms.FizForm import FizUserRegistrationForm
from myapp.forms.UrForm import UrUserRegistrationForm
from myapp.main_logic.news_parser import get_news
from allauth.account.forms import LoginForm, SignupForm
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

from myapp.UserModel import UrUser, FizUser
from myapp.views.email import send_confirmation_email


# @sync_to_async
# @login_required
@csrf_exempt
def index(request):
    def registration(request_in: request, user_model: AbstractBaseUser,
                     form: forms.ModelForm):
        user_model.is_active = False
        user_model.save()

        if 'password' in form:
            email = urform['email'].value()
            company_name = urform['company_name'].value()
            password = urform['password'].value()
            auth_user = UrUserBackend().authenticate(request_in,email=email,
                                     company_name=company_name,
                                     password=password)

        else:
            email = fizform['email'].value()
            full_name = fizform['full_name'].value()
            auth_user = FizUserBackend().authenticate(request_in, email=email, full_name=full_name)
        send_token_email(auth_user)
        if auth_user is not None:
            login(request_in, auth_user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request_in, 'index.html',
                          {'user': auth_user,
                          'signup_form': signup_form,
                          'login_form': login_form,
                          'news': news})
    image_names = os.listdir('./images')
    news = get_news("https://dvizhok.su/dvizhok-rss.rss")
    signup_form = SignupForm()
    login_form = LoginForm()
    if request.method == 'POST':
        data = request.POST
        if 'promo_code' not in data:
            fizform = FizUserRegistrationForm()
            urform = UrUserRegistrationForm(request.POST)
            if urform.is_valid():
                user = UrUser.objects.create_ur(
                    email=urform['email'].value(),
                    password=urform['password'].value(),
                    forma=urform['forma'].value(),
                    city=urform['city'].value(),
                    legal_address=urform['legal_address'].value(),
                    company_name=urform['company_name'].value(),
                    inn=urform['inn'].value(),
                    kpp=urform['kpp'].value(),
                    bank=urform['bank'].value(),
                    bik=urform['bik'].value(),
                    account_number=urform['account_number'].value(),
                    correspondent_account=urform['correspondent_account'].value(),
                    shop=urform['shop'].value(),
                    full_name=urform['full_name'].value(),
                    phone=urform['phone'].value(),
                    terms_of_service=urform['terms_of_service'].value(),
                )
                registration(request, user, urform)
        else:
            fizform = FizUserRegistrationForm(request.POST)
            urform = UrUserRegistrationForm()
            if fizform.is_valid():
                user = FizUser.objects.create_fiz(
                    email=fizform['email'].value(),
                    shop_name=fizform['shop_name'].value(),
                    full_name=fizform['full_name'].value(),
                    phone=fizform['phone'].value(),
                    promo_code=fizform['promo_code'].value(),
                    terms_of_service=fizform['terms_of_service'].value(),
                )
                registration(request, user, fizform)

    fizform = FizUserRegistrationForm()
    urform = UrUserRegistrationForm()
    return render(request, 'index.html', { 'fizform': fizform,
                                             'urform': urform,
                                           'signup_form': signup_form,
                                           'login_form':login_form,
                                           'news': news})







