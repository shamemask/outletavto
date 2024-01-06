from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from authentication.views.email import send_confirmation_email, confirm_email
from authentication.views.logout import logout
from main_api.views import AsyncCatalog
from .views.main import index, html, catalog_page, payment_page, news_page, universal_catalog_card_page, \
    universal_catalog_tire_3_page, universal_catalog_tire_2_page, universal_catalog_tire_page, universal_catalog_page, \
    testfilter_page, testcalendar_page, self_call_page, registration_page, recovery_page, promotion_page, profile_page, \
    passenger_car_info_page, passenger_car_page, orders_page, news_page_page, modification_page, garage_page, \
    favorite_page, company_page, club_page, catalog_personal_account_page, call_to_vin_page, basket_page, balance_page, \
    authorization_page, add_auto_page



schema_view = get_schema_view(
   openapi.Info(
      title="Outletavto",
      default_version='v1',
      description="Веб приложение outletavto",
      terms_of_service=None,
      contact=openapi.Contact(email="shamemask@ya.ru"),
      license=None,
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# URLs for myapp

urlpatterns = [
    path('logout', logout, name='logout'), # выход
    path('', index, name='index'), # главная
    path('catalog', catalog_page, name='catalog_page'), # каталог
    path('catalog2', AsyncCatalog.as_view(), name='catalog_api'), # каталог с асинхронным запросом
    path('payment', payment_page, name='payment_page'), # оплата
    path('news', news_page, name='news_page'), # новости
    path('add_auto', add_auto_page, name='add_auto_page'), # добавление авто
    path('authorization', authorization_page, name='authorization_page'), # авторизация
    path('balance', balance_page, name='balance_page'), # баланс
    path('basket', basket_page, name='basket_page'), # корзина
    path('call_to_vin', call_to_vin_page, name='call_to_vin_page'), # движение заказов
    path('catalog_personal_account', catalog_personal_account_page, name='catalog_personal_account_page'), # персональный каталог
    path('club', club_page, name='club_page'), # клуб
    path('company', company_page, name='company_page'), # компания
    path('favorite', favorite_page, name='favorite_page'), # избранное
    path('garage', garage_page, name='garage_page'), # гараж
    path('modification', modification_page, name='modification_page'), # модификации
    path('news_page/<str:index>', news_page_page, name='news_page_page'), # новости
    path('orders', orders_page, name='orders_page'), # заказы
    path('passenger_car', passenger_car_page, name='passenger_car_page'), # автомобиль
    path('passenger_car_info', passenger_car_info_page, name='passenger_car_info_page'), # автомобиль
    path('profile', profile_page, name='profile_page'), # профиль
    path('promotion', promotion_page, name='promotion_page'), # акции
    path('recovery', recovery_page, name='recovery_page'), # восстановление
    path('registration', registration_page, name='registration_page'), # регистрация
    path('authorization', authorization_page, name='authorization_page'), # авторизация
    path('self_call', self_call_page, name='self_call_page'), # собственный вызов
    path('testcalendar', testcalendar_page, name='testcalendar_page'), # тест
    path('testfilter', testfilter_page, name='testfilter_page'), # тест
    path('universal_catalog', universal_catalog_page, name='universal_catalog_page'), # универсальный каталог
    path('universal_catalog_tire', universal_catalog_tire_page, name='universal_catalog_tire_page'), # универсальный каталог
    path('universal_catalog_tire_2', universal_catalog_tire_2_page, name='universal_catalog_tire_2_page'), # универсальный каталог
    path('universal_catalog_tire_3', universal_catalog_tire_3_page, name='universal_catalog_tire_3_page'), # универсальный каталог
    path('universal_catalog_card', universal_catalog_card_page, name='universal_catalog_card_page'), # универсальный каталог
    path('confirm/', confirm_email, name='confirm_email'), # подтверждение почты
    # path('accounts/', include('allauth.urls')), # подтверждение почты
    # path('api/', include('main_api.urls')),
    # path('auth/', include('authentication.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)