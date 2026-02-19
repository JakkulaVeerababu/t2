import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';

// Fix for default marker icon in React Leaflet
let DefaultIcon = L.icon({
    iconUrl: icon,
    shadowUrl: iconShadow,
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

L.Marker.prototype.options.icon = DefaultIcon;

const VesselMap = ({ vessels }) => {
    const center = [35.6895, 139.6917]; // Tokyo as default center

    return (
        <MapContainer center={center} zoom={5} scrollWheelZoom={true} style={{ height: "100%", width: "100%" }}>
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {vessels.map(vessel => (
                vessel.last_position_lat && vessel.last_position_lon && (
                    <Marker
                        key={vessel.id}
                        position={[vessel.last_position_lat, vessel.last_position_lon]}
                    >
                        <Popup>
                            <div className="p-2">
                                <h3 className="font-bold text-lg">{vessel.name}</h3>
                                <p className="text-sm">Type: {vessel.vessel_type}</p>
                                <p className="text-sm">Flag: {vessel.flag}</p>
                                <p className="text-sm">Speed: {vessel.last_speed} kn</p>
                                <p className="text-sm">Status: {vessel.status}</p>
                                <p className="text-xs text-gray-500 mt-1">Last Updated: {new Date(vessel.last_position_update).toLocaleString()}</p>
                            </div>
                        </Popup>
                    </Marker>
                )
            ))}
        </MapContainer>
    );
};

export default VesselMap;
