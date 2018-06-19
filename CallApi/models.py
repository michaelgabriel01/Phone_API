from django.db import models
from django.db.models.fields import DateTimeField

class Staff(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	number = models.DecimalField(max_digits=5, decimal_places=2) 
	salary = models.IntegerField() 

	def __str__(self):
		return self.first_name


class Company(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	number_of_employees = models.IntegerField() 
	employees_avarage_salary = models.IntegerField() 


	def __str__(self):
		return self.first_name

class Empressa(models.Model):
	company_name = models.CharField(max_length=20)
	company_location = models.CharField(max_length=20)
	number_of_employees = models.IntegerField() 
	employees_avarage_salary = models. BigIntegerField()
	created_day_and_time = DateTimeField(auto_now=True)

	def __str__(self):
		return self.company_name


class Album(models.Model):
	album_name = models.CharField(max_length=100)
	artist = models.CharField(max_length=100)

	def __str__(self):
		return self.album_name

class Track(models.Model):
	album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
	order = models.IntegerField()
	title = models.CharField(max_length=100)
	duration = models.IntegerField()

	class Meta:
		unique_together = ('album', 'order')
		ordering = ['order']

	def __unicode__(self):
		return '%d: %s' % (self.order, self.title)

	def __str__(self):
		return self.album


class Call(models.Model):
	# order = models.IntegerField()
	record_type = models.CharField(max_length=100)
	call_identifier = models.DateTimeField()
	origin_phone_number = models.IntegerField()
	destination_phone_number = models.IntegerField()
	record_timestamp = models.DateTimeField()
	duration = models.IntegerField()

	def __str__(self):
		return self.record_type

