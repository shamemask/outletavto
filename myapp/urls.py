from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from authentication.views.email import send_confirmation_email, confirm_email
from authentication.views.logout import logout
from .views.main import index, html, catalog_page, payment_page, news_page, universal_catalog_card_page, \
    universal_catalog_tire_3_page, universal_catalog_tire_2_page, universal_catalog_tire_page, universal_catalog_page, \
    testfilter_page, testcalendar_page, self_call_page, registration_page, recovery_page, promotion_page, profile_page, \
    passenger_car_info_page, passenger_car_page, orders_page, news_page_page, modification_page, garage_page, \
    favorite_page, company_page, club_page, catalog_personal_account_page, call_to_vin_page, basket_page, balance_page, \
    authorization_page, add_auto_page

urlpatterns = [
    path('logout', logout, name='logout'),
    path('', index, name='index'),
    path('catalog', catalog_page, name='catalog_page'),
    path('payment', payment_page, name='payment_page'),
    path('news', news_page, name='news_page'),
    path('add_auto', add_auto_page, name='add_auto_page'),
    path('authorization', authorization_page, name='authorization_page'),
    path('balance', balance_page, name='balance_page'),
    path('basket', basket_page, name='basket_page'),
    path('call_to_vin', call_to_vin_page, name='call_to_vin_page'),
    path('catalog_personal_account', catalog_personal_account_page, name='catalog_personal_account_page'),
    path('club', club_page, name='club_page'),
    path('company', company_page, name='company_page'),
    path('favorite', favorite_page, name='favorite_page'),
    path('garage', garage_page, name='garage_page'),
    path('modification', modification_page, name='modification_page'),
    path('news_page/<str:index>', news_page_page, name='news_page_page'),
    path('orders', orders_page, name='orders_page'),
    path('passenger_car', passenger_car_page, name='passenger_car_page'),
    path('passenger_car_info', passenger_car_info_page, name='passenger_car_info_page'),
    path('profile', profile_page, name='profile_page'),
    path('promotion', promotion_page, name='promotion_page'),
    path('recovery', recovery_page, name='recovery_page'),
    path('registration', registration_page, name='registration_page'),
    path('authorization', authorization_page, name='authorization_page'),
    path('self_call', self_call_page, name='self_call_page'),
    path('testcalendar', testcalendar_page, name='testcalendar_page'),
    path('testfilter', testfilter_page, name='testfilter_page'),
    path('universal_catalog', universal_catalog_page, name='universal_catalog_page'),
    path('universal_catalog_tire', universal_catalog_tire_page, name='universal_catalog_tire_page'),
    path('universal_catalog_tire_2', universal_catalog_tire_2_page, name='universal_catalog_tire_2_page'),
    path('universal_catalog_tire_3', universal_catalog_tire_3_page, name='universal_catalog_tire_3_page'),
    path('universal_catalog_card', universal_catalog_card_page, name='universal_catalog_card_page'),
    # path('<str:html>', html, name='html'),

    path('confirm/', confirm_email, name='confirm_email'),
    path('accounts/', include('allauth.urls')),



                  # path('<str:image_name>/', views.image_detail, name='image_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)