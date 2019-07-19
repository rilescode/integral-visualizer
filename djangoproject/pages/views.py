from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>hi</h1>")
    return render(request, "base.html", {})

def test_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is a test",
        "my_number": 123,
        "my_list": [1, 'a', 6]
    }
    return render(request, "test.html", my_context)