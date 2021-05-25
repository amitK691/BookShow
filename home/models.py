from django.db import models


# Create your models here.
class TrendPoster(models.Model):
	Title = models.CharField(max_length=255,null=True,blank=True)
	Poster = models.ImageField(upload_to='media/',null=True,blank=True)
	Category = models.CharField(max_length=255,null=True,blank=True)
	Genre = models.CharField(max_length=255,null=True,blank=True)
	Price = models.IntegerField(null=True,blank=True)
	Playlogo = models.ImageField(upload_to='Playlogo/',null=True,blank=True)

	def __str__(self):
		return f"{self.Title}"
		


class Newarrival(models.Model):
	Title = models.CharField(max_length=255,null=True,blank=True)
	Duration = models.CharField(max_length=255,null=True,blank=True)
	Description = models.CharField(max_length=255,null=True,blank=True)
	Price = models.IntegerField(null=True,blank=True)
	Poster = models.ImageField(upload_to='media/')
	
	def __str__(self):
		return f"{self.Title},{self.Duration},{self.Description},{self.Poster}"

class Newarrivalbelow(models.Model):
	Title = models.CharField(max_length=255,null=True,blank=True)
	Duration = models.CharField(max_length=255,null=True,blank=True)
	Description = models.CharField(max_length=255,null=True,blank=True)
	Price = models.IntegerField(null=True,blank=True)
	Poster = models.ImageField(upload_to='media/')

	def __str__(self):
		return f"{self.Title},{self.Duration},{self.Description},{self.Poster}"

class PopularShow(models.Model):
	Title = models.CharField(max_length=255,null=True,blank=True)
	Duration = models.CharField(max_length=255,null=True,blank=True)
	Description = models.CharField(max_length=255,null=True,blank=True)
	Price = models.IntegerField(null=True,blank=True)
	Poster = models.ImageField(upload_to='media/popularShow/')

	def __str__(self):
		return f"{self.Title},{self.Duration},{self.Description},{self.Poster}"

# class Bookseat(models.Model):
# 	Name = models.CharField(max_length=50)
# 	SeatsQuantity = models.CharField(max_length=50)

# 	def __str__(self):
# 		return f"{self.Name},{self.SeatsQuantity}"
		

		

		