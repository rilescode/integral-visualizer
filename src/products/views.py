from django.shortcuts import render
from .forms import ProductForm
from .models import Product
import math
from .riemann import calculateSum
import os
from django.core.cache import cache
import platform

# Create your views here.

def improved_view(request):
	other_sum = 0

   #gets the system the person is running to see bkslash or fwdslash
	my_platform = str(platform.system())
	if my_platform == "Darwin" or my_platform == "Linux":
		slash = "/"
	else:
		slash = "\\"

	# Root directory
	fileDir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
	print(fileDir)

   	# Path where I want the file to be
	epic_path = fileDir + slash + "products" + slash + "static" + slash + "img" + slash + "graphTest3.png"
	print("epic path: %s" % epic_path)

   	# Delete old file, and create new one in root directory
	os.remove(epic_path)
	open("graphTest3.png", "w+")

	# Path in root directory
	old_path = fileDir + slash + "graphTest3.png"
	print("old path: %s" %old_path)

	# Move file to correct directory
	os.rename(old_path, epic_path)
	
	
	if request.method == "POST":
		
		function_type = request.POST.get('function-type')
		a = request.POST.get('a')
		b = request.POST.get('b')
		c = request.POST.get('c')
		d = request.POST.get('d')
		xmin = request.POST.get('xmin')
		xmax = request.POST.get('xmax')
		width_rect = request.POST.get('width-rect')
		rct_amnt = request.POST.get('rct-amnt')
		wdth_amnt = request.POST.get('wdth-amnt')
		sum_type = request.POST.get('sumtype')


		#os.remove("/Users/riley/Desktop/test_NWAPW/integral-visualizer/src/products/static/img/graphTest4.png")
		other_sum = calculateSum(function_type, a, b, c, d, xmin, xmax, width_rect, rct_amnt, wdth_amnt, sum_type)
		#simp()

	my_context = {
		'my_sum' : other_sum
	}

	return render(request, 'products/improved.html', my_context)

	

def image_view(request):
	return render(request, 'products/image_view.html')
