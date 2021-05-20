from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Am solving the issue of transport money.")


def dashboard(request):
    return render(request, "trackball/dashboard.html")
