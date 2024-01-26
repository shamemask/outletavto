import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


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
            profile_dict[field.name] = [
                templ_dict['user'].__dict__[field.name],
                field.verbose_name
            ]
        if field.name == 'password':
            profile_dict[field.verbose_name] = ['********',field.verbose_name]
    templ_dict['profile_dict'] = profile_dict
    return render(request, os.path.join('outletauto_page','profile_page.html'), templ_dict)
