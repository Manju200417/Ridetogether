from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Ride
from django.contrib import messages

def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def create_ride(request):
    if request.method == 'POST':
        source = request.POST.get("source")
        destination = request.POST.get("destination")
        date = request.POST.get("date")
        time = request.POST.get("time")
        phone = request.POST.get("phone_number")

        Ride.objects.create(
            user=request.user,
            source=source,
            destination=destination,
            date=date,
            time=time,
            phone_number=phone)
        
        messages.success(request,"Ride created successfully!")
        return redirect("create_ride")

    return render(request,'rides/create_ride.html')

def matches(request):

    # get current user's ride
    my_ride = Ride.objects.filter(user=request.user).last()

    if my_ride:
        rides = Ride.objects.filter(
            source=my_ride.source,
            destination=my_ride.destination,
            date=my_ride.date
        ).exclude(user=request.user)
    else:
        rides = []

    return render(request, "rides/match.html", {"rides": rides})

def search(request):
    pass