from django.db import models

# Create your models here.


class CarModel(models.Model):
    model = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=50)
    millage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.model} - {self.year} - {self.color.title()} - {self.millage:,d} - {self.price:,d}"
