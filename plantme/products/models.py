from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Plant(models.Model):
	plant_name = models.CharField(max_length=50)
	plant_type = models.CharField(max_length=50)
	quantity   = models.IntegerField()
	price      = models.DecimalField(max_digits=1000, decimal_places=2)
	arrived_on = models.DateField()
	image      = models.ImageField(upload_to='plants', null=True)

	def __str__(self):
		return self.plant_name
		
	def get_absolute_url(self):
		return reverse("plant-detail", kwargs={"id": self.id})
