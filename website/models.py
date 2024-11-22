from django.db import models

# Yeah I'm keeping this up cuz I'm too lazy to edit :p and I have finals coming please god
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)


# I did migrate again to make this work
class Airline(models.Model):
	airline_name = models.CharField(max_length=50)
	a_length = models.IntegerField(blank=True)
	a_width = models.IntegerField(blank=True)
	a_depth = models.IntegerField(blank=True)
	a_weight = models.IntegerField(blank=True)

class Backpack(models.Model):
	brand = models.CharField(max_length=50)
	backpack_name = models.CharField(max_length=50)
	b_length = models.IntegerField(blank=True)
	b_width = models.IntegerField(blank=True)
	b_depth = models.IntegerField(blank=True)
	b_weight = models.IntegerField(blank=True)