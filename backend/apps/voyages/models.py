from django.db import models

class Voyage(models.Model):
    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    vessel = models.ForeignKey('vessels.Vessel', on_delete=models.CASCADE, related_name='voyages')
    origin_port_id = models.IntegerField(blank=True, null=True) # Linked to Port ID logic
    destination_port_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField()
    estimated_end_date = models.DateTimeField(blank=True, null=True)
    actual_end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='planned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VoyageHistory(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='history')
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    speed = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    heading = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    depth = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['voyage', '-timestamp'])]

class ComplianceRecord(models.Model):
    STATUS_CHOICES = (
        ('compliant', 'Compliant'),
        ('non_compliant', 'Non-Compliant'),
        ('pending', 'Pending'),
    )

    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='compliance_records')
    regulation = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    check_date = models.DateTimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
