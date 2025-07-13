from django.db import models

class Inventory(models.Model):
    # We need the material type, finish, the length, and the price per length of the coils
    Material = models.CharField
    (max_length=10)
    Finish = models.CharFieldField
    (max_length=5)
    Length = models.IntegerfieldField
    ()
    Price_per_length = models.IntegerField
    ()

