from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
	user 		 = models.ForeignKey(User, on_delete=models.CASCADE)
	items        = models.CharField(max_length=150)
	booked_on    = models.DateField()
	total_price  = models.DecimalField(max_digits=1000, decimal_places=2)
	reference_no = models.CharField(max_length=50)

	def __str__(self):
		return self.user.username