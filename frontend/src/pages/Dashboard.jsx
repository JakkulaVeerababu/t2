import { useState, useEffect, useContext } from 'react';
import AuthContext from '../context/AuthContext';
import VesselMap from '../components/vessels/VesselMap';
import VesselList from '../components/vessels/VesselList';
import api from '../api/axios';

const Dashboard = () => {
    let { user, logoutUser } = useContext(AuthContext);
    const [vessels, setVessels] = useState([]);
    const [selectedVessel, setSelectedVessel] = useState(null);
    const [loading, setLoading] = useState(true);

    const fetchVessels = async () => {
        try {
            const response = await api.get('/vessels/');
            // Ensure response.data.results exists for pagination, or response.data if list
            const data = response.data.results ? response.data.results : response.data;
            setVessels(data);
            setLoading(false);
        } catch (error) {
            console.error("Error fetching vessels:", error);
            setLoading(false);
        }
    };

    const syncMockData = async () => {
        try {
            await api.post('/vessels/sync_mock_data/');
            fetchVessels();
        } catch (error) {
            console.error("Error syncing mock data:", error);
        }
    }

    useEffect(() => {
        fetchVessels();
        // Poll every 30 seconds for updates
        const interval = setInterval(fetchVessels, 30000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="flex flex-col h-screen bg-gray-100 overflow-hidden">
            {/* Navbar */}
            <nav className="bg-white shadow z-10">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between h-16">
                        <div className="flex items-center">
                            <h1 className="text-xl font-bold text-blue-900">Maritime Tracker</h1>
                        </div>
                        <div className="flex items-center space-x-4">
                            <button
                                onClick={syncMockData}
                                className="px-3 py-1 bg-green-600 text-white rounded-md text-sm hover:bg-green-700"
                            >
                                Sync Live Data
                            </button>
                            <span className="text-gray-700">Welcome, {user && user.username}</span>
                            <button onClick={logoutUser} className="text-red-600 hover:text-red-900">Logout</button>
                        </div>
                    </div>
                </div>
            </nav>

            {/* Main Content */}
            <div className="flex flex-1 overflow-hidden">
                {/* Sidebar */}
                <div className="w-1/4 h-full border-r bg-white hidden md:block z-0">
                    <VesselList vessels={vessels} onSelectVessel={setSelectedVessel} />
                </div>

                {/* Map Area */}
                <div className="flex-1 relative z-0">
                    {loading ? (
                        <div className="flex items-center justify-center h-full">
                            <p className="text-xl text-gray-500">Loading Vessel Data...</p>
                        </div>
                    ) : (
                        <VesselMap vessels={vessels} />
                    )}

                    {/* Mobile List Toggle or Overlay could go here */}
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
