from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from trackball.forms import CustomUserCreationForm


def index(request):
    return HttpResponse("Am solving the issue of transport money.")


def dashboard(request):
    return render(request, "trackball/dashboard.html")


def register(request):

    if request.method == "GET":

        return render(request, "trackball/register.html",{"form": CustomUserCreationForm})

    elif request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect(reverse("dashboard"))
