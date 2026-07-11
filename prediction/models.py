
from django.db import models

class CarData(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    region = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    engine_size_l = models.FloatField()
    mileage_km = models.IntegerField()
    price_usd = models.FloatField()
    sales_volume = models.IntegerField()
    sales_classification = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.model} - {self.year}"


# Create your models here.
