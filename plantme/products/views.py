from django.shortcuts import render, reverse
from home.models import Profile
from .models import Plant
# from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from plantme.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages

def plant_buy_view(request):
	if request.method == 'POST' and 'login' in request.POST :
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		if user is not None:
			print("success")
			login(request, user)
			request.session['username'] = request.POST["username"]
		else:
			messages.error(request, 'Invalid credentials')


	if request.method == 'POST' and 'signup' in request.POST :
		user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
		user.profile.first_name=request.POST["first_name"]
		user.profile.last_name=request.POST["last_name"] 
		user.profile.email=request.POST["email"]
		user.profile.phone=request.POST["phone"]
		user.save()
		subject = "welcome to Plantme"
		message = "Thanks for joining us"
		recipent = request.POST["email"]
		send_mail(subject, message, EMAIL_HOST_USER, [recipent], fail_silently=False)
		messages.success(request, f'Your account has been created! You are now able to log in')

	if request.method == 'POST' and 'logout' in request.POST:
		try:
			logout(request)
			del request.session['username']	
		except KeyError:
			pass

	plants = Plant.objects.all()
	flowers = Plant.objects.filter(plant_type='flower')
	fruits	= Plant.objects.filter(plant_type='fruit')
	vegetables = Plant.objects.filter(plant_type='vegetable')
	medicinals = Plant.objects.filter(plant_type='medicinal')
	decoratives = Plant.objects.filter(plant_type='decorative')

	context = { "plants": plants , 
				"flowers": flowers, 
				"fruits": fruits , 
				"vegetables": vegetables, 
				"medicinals": medicinals, 
				"decoratives": decoratives
				}
	return render(request, 'shop_plants.html', context)

def plant_detail_view(request, id):

	single_plant = Plant.objects.get(id=id)
	context = {"single_plant": single_plant}
	return render(request, 'detail.html', context)