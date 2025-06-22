from django.shortcuts import render
import math
from .riemann import calculateSum
import os
from django.core.cache import cache
import platform
from django.views.decorators.cache import never_cache

# Create your views here.


@cache_page(60)  # Cache for 1 minute
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

    return render(request, "index.html", my_context)


@cache_page(60 * 15)  # Cache for 15 minutes
def about_view(request):
    return render(request, "about.html", {})


@cache_page(60 * 15)  # Cache for 15 minutes
def learnmore_view(request):
    return render(request, "learnmore.html", {})


@cache_page(60 * 15)  # Cache for 15 minutes
def instructions_view(request):
    return render(request, "instructions.html", {})


def image_view(request):
    return render(request, "image_view.html")
