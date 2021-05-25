from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(TrendPoster)
class Trend(admin.ModelAdmin):
	list_display =("Title","Price","Category","Genre","Playlogo")
		
@admin.register(Newarrival)
class newcontent(admin.ModelAdmin):
	list_display = ("Title","Duration","Description","Poster")

@admin.register(Newarrivalbelow)
class newcontentbelow(admin.ModelAdmin):
	list_display = ("Title","Duration","Description","Poster")

@admin.register(PopularShow)
class popularShow(admin.ModelAdmin):
	list_display = ("Title","Duration","Description","Poster")
	
# @admin.register(Bookseat)
# class bookshow(admin.ModelAdmin):
# 	list_display = ("Name","SeatsQuantity")



		
