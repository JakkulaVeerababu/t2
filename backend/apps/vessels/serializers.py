from rest_framework import serializers
from .models import Vessel, VesselPosition, VesselRoute, VesselAlert

class VesselPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VesselPosition
        fields = ['latitude', 'longitude', 'speed', 'heading', 'timestamp']

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = '__all__'
