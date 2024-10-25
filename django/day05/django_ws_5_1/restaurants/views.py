from django.shortcuts import render, redirect
from .models import Restaurant
# Create your views here.


def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)


def new(request):
    return render(request, 'restaurants/new.html')


def create(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    restaurant = Restaurant(name=name, address=address)
    restaurant.save()

    return redirect('restaurants:index')
