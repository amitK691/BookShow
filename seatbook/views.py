from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from home.models import *

def seat_book(request):
	print("--------------------------------Coding is runing for seatbook")
	# name = request.POST.get('option_text')
	# print("-----------------------------------",name)
	print(request.GET['option_text']);
	print(request.GET['count']);
	print(request.GET['price']);
	# trends = TrendPoster.objects.all()
	# return render(request,'seatbook/seatbook.html',{'trends':trends})

# @login_required
def payment(request):
	print("--------------------------------Coding is runing for payment")
	return render(request,'payment/payment.html')