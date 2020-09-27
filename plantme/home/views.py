from django.shortcuts import render, reverse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from plantme.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages


def index_view(request):
	if request.method == 'POST' and 'login' in request.POST :
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		if user is not None:
			login(request, user)
			request.session['username'] = request.POST["username"]
		else:
			messages.error(request, 'Invalid credentials')


	if request.method == 'POST' and 'signup' in request.POST :
		user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
		user.profile.first_name=request.POST["first_name"]
		user.profile.last_name=request.POST["last_name"] 
		user.profile.email=request.POST["email"]
		user.profile.phone=request.POST["phone"]
		user.save()
		subject = "Welcome to Plantme"
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

	return render(request, 'index.html', {})

def about_view(request):
	return render(request, 'about.html', {})
