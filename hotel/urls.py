# hotel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('room_rates/', views.room_rate_list, name='room_rate_list'),
    path('room_rates/new/', views.room_rate_create, name='room_rate_create'),
    path('room_rates/<int:pk>/edit/', views.room_rate_update, name='room_rate_update'),
    path('room_rates/<int:pk>/delete/', views.room_rate_delete, name='room_rate_delete'),
    path('overridden_rates/', views.overridden_room_rate_list, name='overridden_room_rate_list'),
    path('overridden_rates/new/', views.overridden_room_rate_create, name='overridden_room_rate_create'),
    path('overridden_rates/<int:pk>/edit/', views.overridden_room_rate_update, name='overridden_room_rate_update'),
    path('overridden_rates/<int:pk>/delete/', views.overridden_room_rate_delete, name='overridden_room_rate_delete'),
    path('discounts/', views.discount_list, name='discount_list'),
    path('discounts/new/', views.discount_create, name='discount_create'),
    path('discounts/<int:pk>/edit/', views.discount_update, name='discount_update'),
    path('discounts/<int:pk>/delete/', views.discount_delete, name='discount_delete'),
    path('room_rates/', views.room_rate_list, name='room_rate_list'),
    path('room_rates/new/', views.room_rate_create, name='room_rate_create'),
    path('room_rates/<int:pk>/edit/', views.room_rate_update, name='room_rate_update'),
    path('room_rates/<int:pk>/delete/', views.room_rate_delete, name='room_rate_delete'),
    path('lowest_rate/', views.lowest_rate_view, name='lowest_rate_form'),
]
