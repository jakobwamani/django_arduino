from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from trackball.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from trackball.models import pool_table , action_table 
import datetime
from .utilis import get_plot


def index(request):
    return HttpResponse("Am solving the issue of transport money.")


def dashboard(request):

    #Pull user
    user = request.user
    print(user)
    #change object to string to make it a string to make it easier to work with
    user_into_string = str(user)

    print(type( user_into_string))

    print(user_into_string)

    if user_into_string == "AnonymousUser":
        print("Amonymous")
        game = 0
        shilling = 0

        context_dict =  {'game':game,'shilling':shilling}


        return render(request, "trackball/dashboard.html" ,context=context_dict)

    else:
        unique_user = User.objects.get(username=user)
        unique_user_id = unique_user.id

        #Pull the pool table ,he or she owns
        unique_pool_table = pool_table.objects.get(user_id=unique_user_id)
        unique_pool_tab_id = unique_pool_table.id


        #current date
        y = datetime.datetime.now()
        currentdate = y.strftime("%Y-%m-%d")
        print(currentdate)

        #pull the data in the pooltable of the current date
        # pool_data = action_table.objects.filter(date = currentdate).values_list('date', 'time','status')
        pool_data = action_table.objects.filter(date = currentdate)

        print("data type of pool_data is")
        print(type(pool_data))
        # print(pool_data)

        x = [x.time for x in pool_data]

        y = [y.status for y in pool_data]

        # chart = get_plot(x,y)
        chart = get_plot(y)

    return render(request, "trackball/dashboard.html" ,{'chart':chart})


def register(request):

    if request.method == "GET":

        return render(request, "trackball/register.html",{"form": CustomUserCreationForm})

    elif request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect(reverse("dashboard"))
