from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from myapp.models2.Email import EmailConfirmation


def confirm_email(request):
    key = request.GET.get('key')
    try:
        confirmation = EmailConfirmation.objects.get(key=key)
    except EmailConfirmation.DoesNotExist:
        return render(request, 'confirmation_failed.html')
    user = confirmation.user
    user.email_verified = True
    user.save()
    confirmation.delete()
    return redirect('confirmation_success')


def send_confirmation_email(request, auth_user):
    user = auth_user
    key = get_random_string(length=64)
    confirmation = EmailConfirmation.objects.create(user=user, key=key)
    # Отправка письма с ссылкой подтверждения
    send_mail(
        'Подтверждение электронной почты',
        f'Пройдите по ссылке для подтверждения вашей электронной почты: {request.build_absolute_uri("/confirm-email/")}?key={key}',
        'noreply@example.com',
        [user.email],
        fail_silently=False,
    )
    return render(request, 'confirmation_sent.html')