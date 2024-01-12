"""
URL configuration for outletavto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from allauth.account.views import SignupView, LoginView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from myapp.profile.UserDetailView import FizUserDetailView, UrUserDetailView
from myapp.views.profile_view import profile_view



urlpatterns = [

    path('admin/', admin.site.urls),
    # path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    # path('accounts/login/', LoginView.as_view(), name='account_login'),
    # path('accounts/profile/', profile_view, name='account_profile'),
    path('account/dashboard/fiz/', FizUserDetailView.as_view(), name='fiz_user_detail_view'),
    path('account/dashboard/ur/', UrUserDetailView.as_view(), name='ur_user_detail_view'),
    path('accounts/', include('allauth.urls')),
    path('', include('myapp.urls')),
    path('api/', include('main_api.urls')),
    path('parser/', include('abcp_parser.urls')),

    
]
