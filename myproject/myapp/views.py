from django.shortcuts import render

# Create your views here.

# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'myapp/home.html')


def hello_world(request):
    return HttpResponse("Hello, World!")