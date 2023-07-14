from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views.activate import activate
from .views.email import send_confirmation_email, confirm_email
from .views.main import index
from .views.register import register

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('send-confirmation-email/', send_confirmation_email, name='send_confirmation_email'),
    path('confirm-email/', confirm_email, name='confirm_email'),
    path('register/', register, name='register'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),

                  # path('<str:image_name>/', views.image_detail, name='image_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)