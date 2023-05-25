from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import CarModel


def add_car(request: HttpRequest):
    if request.method == "POST":
        tmp = request.POST.dict()
        del tmp['csrfmiddlewaretoken']
        CarModel.objects.create(**tmp)
        return redirect('addCar')
    return render(request, 'CarBase/add_car.html')


def all_cars(request: HttpRequest):
    cars = CarModel.objects.all()
    context = {'cars': cars}
    return render(request, 'CarBase/all_cars.html', context)
