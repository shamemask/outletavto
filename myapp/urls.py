from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from authentication.views.email import send_confirmation_email, confirm_email
from authentication.views.logout import logout
from .views.main import index, html

urlpatterns = [
    path('', index, name='index'),
    path('<str:html>', html, name='html'),
    # path('accounts/', include('allauth.urls')),
    path('logout', logout, name='logout'),
    path('confirm/', confirm_email, name='confirm_email'),

                  # path('<str:image_name>/', views.image_detail, name='image_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)