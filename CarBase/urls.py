from django.urls import path

from .views import add_car, all_cars

urlpatterns = [
    path('', add_car, name="addCar"),
    path('turimov', all_cars, name='cars'),
]
