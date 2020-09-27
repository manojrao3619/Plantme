from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact_view(request):
	if request.method == 'POST':
		form = ContactForm(data=request.POST)
		if form.is_valid():
			form.save()	
			messages.success(request, 'Your message have been sent.')
	return render(request, 'contact.html', {})
