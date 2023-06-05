from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:image_name>/', views.image_detail, name='image_detail'),
]