from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# app_name = "seatbook"

urlpatterns = [
	path('seatbook/',views.seat_book,name='seatbook'),
	path('payment/',views.payment,name='payment'),
	
]