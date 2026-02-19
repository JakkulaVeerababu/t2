from django.db import models
from django.contrib.auth.models import User

class Vessel(models.Model):
    VESSEL_TYPES = (
        ('container', 'Container Ship'),
        ('tanker', 'Tanker'),
        ('bulk', 'Bulk Carrier'),
        ('fishing', 'Fishing Vessel'),
        ('passenger', 'Passenger Ship'),
        ('other', 'Other'),
    )
    STATUS_CHOICES = (
        ('in_transit', 'In Transit'),
        ('in_port', 'In Port'),
        ('anchored', 'Anchored'),
        ('offline', 'Offline'),
    )

    imo = models.IntegerField(unique=True, help_text="International Maritime Organization number")
    mmsi = models.BigIntegerField(unique=True, help_text="Maritime Mobile Service Identity")
    name = models.CharField(max_length=255)
    vessel_type = models.CharField(max_length=50, choices=VESSEL_TYPES)
    flag = models.CharField(max_length=3, help_text="Country ISO code")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='offline')
    owner = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    length = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Length in meters")
    beam = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Width in meters")
    draft = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Depth in meters")
    
    last_position_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    last_position_lon = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    last_speed = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Speed in knots")
    last_heading = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Heading in degrees")
    last_position_update = models.DateTimeField(blank=True, null=True)
    
    external_api_source = models.CharField(max_length=50, blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (IMO: {self.imo})"

class VesselPosition(models.Model):
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, related_name='positions')
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    speed = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    heading = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    timestamp = models.DateTimeField()
    recorded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['vessel', '-timestamp']),
        ]
        ordering = ['-timestamp']

class VesselRoute(models.Model):
    vessel = models.OneToOneField(Vessel, on_delete=models.CASCADE, related_name='current_route')
    origin_port = models.CharField(max_length=255)
    destination_port = models.CharField(max_length=255)
    departure_time = models.DateTimeField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    expected_duration = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Duration in hours")
    status = models.CharField(max_length=50, choices=(('active', 'Active'), ('completed', 'Completed'), ('cancelled', 'Cancelled')), default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VesselAlert(models.Model):
    ALERT_TYPES = (
        ('position_change', 'Position Change'),
        ('port_arrival', 'Port Arrival'),
        ('port_departure', 'Port Departure'),
        ('speed_change', 'Speed Change'),
        ('heading_change', 'Heading Change'),
        ('status_change', 'Status Change'),
    )
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, related_name='alerts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vessel_alerts')
    alert_type = models.CharField(max_length=50, choices=ALERT_TYPES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('vessel', 'user', 'alert_type')
