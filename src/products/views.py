from django.shortcuts import render
from .forms import ProductForm
from .models import Product
# Create your views here.

def product_create_view(request):

	"""
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form': form
	}
	my_list = request.GET
	print("THIS IS THE LIST")
	print(form)
	return render(request, "products/product_create.html", context)
	"""
	my_new_title = request.POST.get('title')
	print(type(my_new_title))
	user_input = str(my_new_title)


	if(isinstance(my_new_title, str)):
		print('13')
	try:

	   val = int(user_input)
	   print("Yes input string is an Integer.")
	   print("Input number value is: ", val)
	except ValueError:
	   print("That's not an int!")
	   print("No.. input string is not an Integer. It's a string")

	context = {}
	return render(request, 'products/product_create.html', context)

def product_detail_view(request):
	obj = Product.objects.get(id = 1)
	context = {
		'object': obj,
	}
	return render(request, "product/detail.html", context)

def product_test_view(request):
	my_a = request.POST.get('a')
	my_b = request.POST.get('b')
	my_c = request.POST.get('c')
	my_xmin = request.POST.get('xmin')
	my_xmax = request.POST.get('xmax')
	
	print(my_a)
	print(type(my_a))
	print(type(my_b))
	print(type(my_c))
	print(type(my_xmin))
	print(type(my_xmax))

	context = {}
	return render(request, 'products/product_test.html', context)
