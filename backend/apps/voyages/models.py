from django.db import models

class Voyage(models.Model):
    vessel_name = models.CharField(max_length=255)
    departure = models.DateTimeField()
    arrival = models.DateTimeField(null=True, blank=True)
