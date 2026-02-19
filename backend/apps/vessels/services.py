import random
from datetime import timedelta
from django.utils import timezone
from .models import Vessel, VesselPosition

class MockAISProvider:
    """
    Simulates live AIS data for demonstration purposes.
    """
    
    def __init__(self):
        self.center_lat = 35.6895 # Tokyo
        self.center_lon = 139.6917
    
    def generate_positions(self):
        vessels = Vessel.objects.all()
        if not vessels.exists():
            self._create_mock_vessels()
            vessels = Vessel.objects.all()
            
        updated_positions = []
        for vessel in vessels:
            # Simulate movement
            lat_opt = float(vessel.last_position_lat) if vessel.last_position_lat else self.center_lat
            lon_opt = float(vessel.last_position_lon) if vessel.last_position_lon else self.center_lon
            
            # Random small movement
            new_lat = lat_opt + random.uniform(-0.01, 0.01)
            new_lon = lon_opt + random.uniform(-0.01, 0.01)
            
            vessel.last_position_lat = new_lat
            vessel.last_position_lon = new_lon
            vessel.last_heading = random.uniform(0, 360)
            vessel.last_speed = random.uniform(10, 20)
            vessel.last_position_update = timezone.now()
            vessel.status = 'in_transit'
            vessel.save()
            
            # Record history
            pos = VesselPosition.objects.create(
                vessel=vessel,
                latitude=new_lat,
                longitude=new_lon,
                speed=vessel.last_speed,
                heading=vessel.last_heading,
                timestamp=timezone.now()
            )
            updated_positions.append(pos)
            
        return updated_positions

    def _create_mock_vessels(self):
        vessel_data = [
            {"name": "MAERSK SEALAND", "imo": 9123456, "mmsi": 211378120, "type": "container", "flag": "DK"},
            {"name": "EVER GIVEN", "imo": 9811000, "mmsi": 353136000, "type": "container", "flag": "PA"},
            {"name": "MSC GULSUN", "imo": 9839430, "mmsi": 357498000, "type": "container", "flag": "PA"},
            {"name": "HMM ALGECIRAS", "imo": 9863297, "mmsi": 440336000, "type": "container", "flag": "KR"},
            {"name": "OOCL HONG KONG", "imo": 9776171, "mmsi": 477333500, "type": "container", "flag": "HK"},
        ]
        
        for data in vessel_data:
            Vessel.objects.get_or_create(
                imo=data['imo'],
                defaults={
                    "mmsi": data['mmsi'],
                    "name": data['name'],
                    "vessel_type": data['type'],
                    "flag": data['flag'],
                    "last_position_lat": self.center_lat + random.uniform(-0.5, 0.5),
                    "last_position_lon": self.center_lon + random.uniform(-0.5, 0.5),
                }
            )
