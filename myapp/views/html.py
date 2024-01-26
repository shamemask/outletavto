import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authentication.views.main import auth


@csrf_exempt
def html(request,html):
    return render(request, os.path.join('pages',html+'.html'), {})
