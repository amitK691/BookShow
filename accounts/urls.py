from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('login/',views.login_view,name='login-view'),
	path('register/',views.register,name='register'),
	path('logout/',views.logout_view,name='logout-view'),
	path('otp/',views.otp,name='otp'),
	# path('verify_email/<str:email>/',views.verify_email,name='verify_email'),	
	path(
	'reset_password/', 
	auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"), 
	name ='reset_password'),
	path(
	'reset_password_sent/', 
	auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"),
	name ='password_reset_done'),
	path(
	'reset/<uidb64>/<token>', 
	auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"),
	name ='password_reset_confirm'),
	path(
	'reset_password_complete/', 
	auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), 
	name ='password_reset_complete'),
	
]