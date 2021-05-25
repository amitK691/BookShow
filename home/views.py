from django.shortcuts import render,redirect
from .models import *
from accounts.models import CustomModel
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

def home(request):
	dests = Newarrival.objects.all()
	trends = TrendPoster.objects.all()
	newarrives = Newarrivalbelow.objects.all()
	popularshow = PopularShow.objects.all()
	return render(request,'home/home.html',{'dests':dests,'trends':trends,'newarrives':newarrives,'popularshow':popularshow})
	# return render(request,'home/home.html',final=zip(dests,trends,newarrives))
	# return render(request,'home/home.html',{'dests':dests,'media_url':settings.MEDIA_URL})

@login_required
def password_change(request):
	# if request.method == 'POST':
	# 	form = PasswordChangeForm(request.user, request.POST)
	# 	if form.is_valid():
	# 		user = form.save()
	# 		update_session_auth_hash(request, user)  # Important!
	# 		messages.success(request, 'Your password was successfully updated!')
	# 		return redirect('pswdchange')
	# 	else:
	# 		messages.error(request, 'Please correct the error below.')
	# else:
	# 	form = PasswordChangeForm(request.user)
	# return render(request, 'registration/pc.html', {
	# 	'form': form
	# 	})
	context={}
	ch = CustomModel.objects.filter(user__id=request.user.id)
	if len(ch)>0:
		data = CustomModel.objects.get(user__id=request.user.id)
		print('user.id ----------------',data)
		context['data'] = data
	if request.method == "POST":
		current = request.POST['cpwd']
		new_pas = request.POST['npwd']
		print('user.id ----------------line 42',request.user.id)
		user = User.objects.get(id=request.user.id)
		# backend='django.contrib.auth.backends.ModelBackend'
		un = user.username
		check = user.check_password(current)
		if check == True:
			user.set_password(new_pas)
			user.save()
			context["msz"]="Password Change successfully"
			context["col"]="alert-success"
			user = User.objects.get(username=un)
			login(request,user,backend='django.contrib.auth.backends.ModelBackend')
			return redirect('/')
		else:
			context["msz"] = "Password is incorrect"
			context["col"] = "alert-danger"

	return render(request,'registration/pc.html',context)
	

def search_bar(request):
	if request.method == "GET":
		search = request.GET.get('search')
		post = Newarrival.objects.all().filter(Title=search)
		print('This is ----------------',post)
	return render(request, 'search/search.html', {'post':post})


# def insert(request):
# 	seatbook = Bookseat(name=request.POST['name'],SeatsQuantity=request.POST['numberseat'])
# 	print("-------------------Seatbook",seatbook)
# 	seatbook.save()
# 	return redirect('/')

