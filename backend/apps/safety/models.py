from django.db import models

class SafetyEvent(models.Model):
    TYPE_CHOICES = (('accident', 'Accident'), ('piracy', 'Piracy'), ('weather', 'Weather'))
    event_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
