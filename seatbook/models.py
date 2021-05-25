from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Seatbooked(models.Model):
# 	# user = models.OneToOneField(User,on_delete=models.CASCADE)
# 	name = models.CharField(max_length=255,unique =True,null=True, blank=True)
# 	seat = models.CharField(max_length=255,unique =True,null=True,blank=True)

# 	def __str__(self):
# 		return f"{self.name},{self.seat}"

class Bookseat(models.Model):
	Name = models.CharField(max_length=50,null=True,blank=True)
	SeatsCount = models.CharField(max_length=50,null=True,blank=True)
	Price = models.IntegerField(null=True,blank=True)
	Ticket_confirm = models.BooleanField(null=True,blank=True)

	def __str__(self):
		return f"{self.Name},{self.SeatsCount},{self.Price},{self.Ticket_confirm}"

class Payment(models.Model):
	bookseat = models.ForeignKey(Bookseat,on_delete=models.CASCADE,null=True,blank=True)
	CardNumber = models.IntegerField(null=True,blank=True)
	EDate = models.CharField(max_length=50,null=True,blank=True)
	CV = models.IntegerField(null=True,blank=True)
	DCode = models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return f"{self.CardNumber},{self.EDate},{self.CV},{self.DCode}"
		