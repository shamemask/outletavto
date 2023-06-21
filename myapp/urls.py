from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    # path('<str:image_name>/', views.image_detail, name='image_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)