from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('',views.home,name='home'),
	path('password-change/',views.password_change,name='pswdchange'),
	path('search/',views.search_bar,name='search'),
	# url(r'^insert$', views.insert, name='insert'),

]