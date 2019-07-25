from django.shortcuts import render
from .forms import ProductForm
from .models import Product
import math
from .riemann import calculateSum
import os

# Create your views here.

def improved_view(request):
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
		print(calculateSum(function_type, a, b, c, d, xmin, xmax, width_rect, rct_amnt, wdth_amnt, sum_type))
		#simp()

	return render(request, 'products/improved.html', {})
	os.remove('C:/Users/CRELL/OneDrive/Documents/GitHub/integral-visualizer/src/products/static/img/graphtry.png')

def image_view(request):
	return render(request, 'products/image_view.html')
