from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomModel
from django.core.mail import send_mail
from django.contrib import messages
import random
from accounts.Twillio import *

# Create your views here.

def  login_view(request):
	if request.method =="POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		print("----------------",username,password)
		user = authenticate(request,username=username,password=password)
		print(user)
		backend='django.contrib.auth.backends.ModelBackend'
		if user is not None:
			login(request,user,backend)
			return redirect('/')
		else:
			messages.error(request,"username or password incorrect")
	return render(request,'LR/loginSignup.html')

def register(request):
	if request.method =="POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		mobile = request.POST.get("number")
		email = request.POST.get("email")
		print("----------*******-------",username,password,mobile,email)

		check_user = User.objects.filter(email=email,username=username).first()
		if check_user:
			context = {'messages':'user already exist','class':'danger'}
			return render(request,'LR/loginSignup.html')
		user = User.objects.create_user(username=username,password=password,email=email,is_active=False)
		user.save()
	# return render(request,'LR/loginSignup.html')
		# messages.success(request,"Email has been sent to you registered email please verify")
		# link ="http://127.0.0.1:8000/accounts/verify_email/{}".format(user.email)
		# send_mail(
		# 	'Please verify your email',
		# 	link, 
		# 	'anaconda.wb@gmail.com', 
		# 	[user.email]
		# 	)

		otp = str(random.randint(999,10000))
		twilio(otp)
		custommodel = CustomModel(user=user,mobile=mobile,otp=otp)
		custommodel.save()
		request.session['mobile'] = mobile
		return redirect('otp')
	return render(request,'LR/loginSignup.html')


def logout_view(request):
	logout(request)
	return redirect('login-view')

def verify_email(request,email):
	user_obj = User.objects.get(email=email)
	user_obj.is_active = True
	user_obj.save()
	return redirect('/accounts/login')

def otp(request):
	phone = request.session['mobile']
	context = {'phone':phone}
	if request.method == "POST":
 		otp = request.POST.get('num_otp')
 		custommodel = CustomModel.objects.filter(mobile=phone).first()
 		backend='django.contrib.auth.backends.ModelBackend'
	 	if otp == custommodel.otp:
	 		user = User.objects.get(email=custommodel.user.email)
	 		user.is_active = True
	 		user.save()
	 		login(request,user,backend)
	 		return redirect('/')
	 	else:
	 		context = {'message' : 'Wrong OTP' , 'class' : 'danger' }
	 		return render(request,'otp/otp.html' , context)
	return render(request,'otp/otp.html')
