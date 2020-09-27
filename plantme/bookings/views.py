from django.shortcuts import render
from .models import Booking
import datetime
from twilio.rest import Client
from django.conf import settings

# Create your views here.

def checkout_view(request):
	usr = request.user
	item = request.COOKIES.get('myObj')
	print(item)
	tot = request.COOKIES.get('tot')
	print(tot)
	date = datetime.date.today()
	ref = (datetime.datetime.now().strftime("%y%m%d%H%M%S"))
	client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN )


	if request.method == 'POST':

		booking = Booking.objects.create(user = usr,
										 items = item,
										 booked_on = date,
										 total_price = tot,
										 reference_no = ref
		)
		
		booking.save()

		message = client.messages.create(
			to= "+91" + str(usr.profile.phone), 
			from_="+12059646384", # insert trial number 
			body="Thanks for booking plants.Here's reference no " + ref + " it will be needed in time of purchase.") # insert message

	return render(request, 'checkout.html', {})