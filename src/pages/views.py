from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home_view(request, *args, **kwargs):
	print(request.user)
	my_context = {
		"anon_name": 'AnonymousUser',
	}
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	my_context = {
		"my_text": "this is from my_text",
		"my_number": 7733,
		"my_list": [7, 6, 23, "freeze"],

	}
	return render(request, "contact.html", my_context)

def integral_view(request, *args, **kwargs):
	print(request.GET)
	print(request.POST)
	return render(request, 'integral.html', {})


