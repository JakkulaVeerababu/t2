from django.db import models

class Port(models.Model):
    PORT_TYPES = (
        ('container', 'Container Port'),
        ('bulk_cargo', 'Bulk Cargo'),
        ('general_cargo', 'General Cargo'),
        ('oil_lng', 'Oil/LNG'),
        ('multipurpose', 'Multipurpose'),
    )

    name = models.CharField(max_length=255, unique=True)
    unlocode = models.CharField(max_length=5, unique=True, help_text="UN/LOCODE")
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    port_type = models.CharField(max_length=50, choices=PORT_TYPES, default='multipurpose')
    number_of_berths = models.IntegerField(default=0)
    average_depth = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    annual_container_capacity = models.IntegerField(blank=True, null=True, help_text="TEU")
    annual_cargo_capacity = models.IntegerField(blank=True, null=True, help_text="Tons")
    operating_hours = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.unlocode})"

class PortStatistics(models.Model):
    CONGESTION_LEVELS = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    port = models.OneToOneField(Port, on_delete=models.CASCADE, related_name='statistics')
    total_arrivals = models.IntegerField(default=0)
    total_departures = models.IntegerField(default=0)
    current_vessels = models.IntegerField(default=0)
    average_wait_time = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Hours")
    average_berth_time = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Hours")
    occupied_berths = models.IntegerField(default=0)
    free_berths = models.IntegerField(default=0)
    congestion_level = models.CharField(max_length=20, choices=CONGESTION_LEVELS, default='low')
    efficiency_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    last_updated = models.DateTimeField(auto_now=True)

class CongestionMetric(models.Model):
    port = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='congestion_history')
    congestion_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    queue_length = models.IntegerField(default=0)
    estimated_wait_time = models.DecimalField(max_digits=6, decimal_places=2)
    berths_available = models.IntegerField(default=0)
    berths_occupied = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['port', '-timestamp']),
        ]

class ArrivalDeparture(models.Model):
    vessel = models.ForeignKey('vessels.Vessel', on_delete=models.CASCADE, related_name='port_calls')
    port = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='vessel_movements')
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField(blank=True, null=True)
    berth_number = models.CharField(max_length=50, blank=True, null=True)
    cargo_loaded = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Tons")
    cargo_unloaded = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Tons")
    turnaround_time = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Hours")
    created_at = models.DateTimeField(auto_now_add=True)
