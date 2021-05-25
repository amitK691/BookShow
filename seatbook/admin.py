from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(Seatbooked)
# class Seat_booked(admin.ModelAdmin):
# 	list_display = ("name","seat")

@admin.register(Bookseat)
class bookshow(admin.ModelAdmin):
	list_display = ("Name","SeatsCount","Price","Ticket_confirm")

@admin.register(Payment)
class payment(admin.ModelAdmin):
	list_display = ("CardNumber","EDate","CV","DCode")
