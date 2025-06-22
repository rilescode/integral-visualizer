from django.shortcuts import render
from .forms import ProductForm
from .models import Product
import math
from .riemann import calculateSum
import os
from django.core.cache import cache
import platform
from django.views.decorators.cache import never_cache

# Create your views here.


@never_cache
def improved_view(request):
    other_sum = 0
    graph_url = None

    if request.method == "POST":

        function_type = request.POST.get("function-type")
        a = request.POST.get("a")
        b = request.POST.get("b")
        c = request.POST.get("c")
        d = request.POST.get("d")
        xmin = request.POST.get("xmin")
        xmax = request.POST.get("xmax")
        width_rect = request.POST.get("width-rect")
        rct_amnt = request.POST.get("rct-amnt")
        wdth_amnt = request.POST.get("wdth-amnt")
        sum_type = request.POST.get("sumtype")

        other_sum, graph_url = calculateSum(
            function_type,
            a,
            b,
            c,
            d,
            xmin,
            xmax,
            width_rect,
            rct_amnt,
            wdth_amnt,
            sum_type,
        )

    my_context = {"my_sum": other_sum, "graph_url": graph_url}

    return render(request, "products/index.html", my_context)


@never_cache
def about_view(request):
    return render(request, "products/about.html", {})


@never_cache
def learnmore_view(request):
    return render(request, "products/learnmore.html", {})


@never_cache
def instructions_view(request):
    return render(request, "products/instructions.html", {})


@never_cache
def egg_view(request):
    return render(request, "products/egg.html", {})


def image_view(request):
    return render(request, "products/image_view.html")
