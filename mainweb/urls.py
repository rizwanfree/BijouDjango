
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'mainweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('room-list/', views.room_list, name='room-list'),
    path('room/<slug:slug>/', views.room_details, name='room-details'),
    path('house-list/', views.house_list, name='house-list'),
    path('house/<slug:slug>/', views.house_details, name='house-details'),
    path('payment-methods/', views.payment_methods, name='payment-methods'),
    path('payment-methods-iframe/', views.payment_methods_iframe, name='payment_methods_iframe'),
]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
