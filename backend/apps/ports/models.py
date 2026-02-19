from django.db import models

class Port(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    country = models.CharField(max_length=255)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.name
