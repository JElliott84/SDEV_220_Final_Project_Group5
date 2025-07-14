from django.db import models

class Inventory(models.Model):
    # We need the material type, finish, the length, and the price per length of the coils
    Material = models.CharField(max_length=10)
    Finish = models.CharField(max_length=5)
    Length = models.IntegerField()
    Price_per_length = models.IntegerField()

