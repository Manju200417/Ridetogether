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

def get_matching_rides(user):
    my_ride = Ride.objects.filter(user=user).last()

    if not my_ride:
        return Ride.objects.none()

    return Ride.objects.filter(
        source=my_ride.source,
        destination=my_ride.destination,
        date=my_ride.date
    ).exclude(user=user) 


@login_required
def matches(request):
    rides = get_matching_rides(request.user)
    return render(request, "rides/match.html", {"rides": rides})

@login_required
def search(request):
    pass

@login_required
def profile(request):
    data = {
    "total_rides" : Ride.objects.filter(user=request.user).count(),
    "total_matches" : get_matching_rides(request.user).count() }

    return render(request,'profile.html',data)