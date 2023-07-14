from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

from myapp.models2.Email import EmailConfirmation


def register(email):
    # Получите другие поля из формы регистрации
    user = EmailConfirmation(email=email, is_active=False)

    # Генерация токена для подтверждения
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(user.pk.to_bytes())
    mail_subject = 'Подтверждение регистрации'
    message = render_to_string('activation_email.html', {
        'user': user,
        'domain': 'https://outletavto.ru/',
        'uid': uid,
        'token': token,
    })
    send_mail(mail_subject, message, 'shamemask@gmail.com', [email])
