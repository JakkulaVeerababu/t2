from django.db import models

class SafetyEvent(models.Model):
    EVENT_TYPES = (
        ('collision', 'Collision'),
        ('grounding', 'Grounding'),
        ('fire', 'Fire'),
        ('explosion', 'Explosion'),
        ('flooding', 'Flooding'),
        ('machinery_failure', 'Machinery Failure'),
        ('other', 'Other'),
    )
    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    location_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    vessel_involved = models.ForeignKey('vessels.Vessel', on_delete=models.SET_NULL, null=True, blank=True, related_name='safety_events')
    event_time = models.DateTimeField()
    resolution_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['event_time'])]

class WeatherAlert(models.Model):
    ALERT_TYPES = (
        ('storm', 'Storm'),
        ('hurricane', 'Hurricane'),
        ('extreme_wind', 'Extreme Wind'),
        ('heavy_rain', 'Heavy Rain'),
        ('fog', 'Fog'),
        ('high_waves', 'High Waves'),
        ('tsunami', 'Tsunami'),
    )
    SEVERITY_CHOICES = (
        ('warning', 'Warning'),
        ('alert', 'Alert'),
        ('emergency', 'Emergency'),
    )

    alert_type = models.CharField(max_length=50, choices=ALERT_TYPES)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    location_name = models.CharField(max_length=255)
    affected_radius_km = models.DecimalField(max_digits=8, decimal_places=2)
    wind_speed = models.IntegerField(blank=True, null=True)
    wind_direction = models.CharField(max_length=10, blank=True, null=True)
    wave_height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    visibility = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    issued_time = models.DateTimeField()
    expires_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    source = models.CharField(max_length=100)

class PiracyZone(models.Model):
    THREAT_LEVELS = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    radius_km = models.DecimalField(max_digits=8, decimal_places=2)
    threat_level = models.CharField(max_length=20, choices=THREAT_LEVELS)
    description = models.TextField()
    last_incident = models.DateTimeField(blank=True, null=True)
    incidents_count = models.IntegerField(default=0)
    recommended_speed = models.IntegerField(blank=True, null=True)
    armed_escort_recommended = models.BooleanField(default=False)
    report_to_ukmto = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AccidentHistory(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    location_name = models.CharField(max_length=255)
    accident_type = models.CharField(max_length=50, choices=SafetyEvent.EVENT_TYPES)
    incident_date = models.DateField()
    description = models.TextField()
    vessels = models.ManyToManyField('vessels.Vessel', related_name='accident_histories')
    casualties = models.IntegerField(default=0)
    total_loss = models.BooleanField(default=False)
    estimated_damage_usd = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
