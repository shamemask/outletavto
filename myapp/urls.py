from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:image_name>/', views.image_detail, name='image_detail'),
]