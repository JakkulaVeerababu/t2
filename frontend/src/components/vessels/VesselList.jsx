import React from 'react';

const VesselList = ({ vessels, onSelectVessel }) => {
    return (
        <div className="bg-white shadow-lg h-full overflow-y-auto w-full">
            <div className="p-4 border-b">
                <h2 className="text-xl font-bold text-gray-800">Vessels ({vessels.length})</h2>
                <input
                    type="text"
                    placeholder="Search vessels..."
                    className="w-full mt-2 px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
            </div>
            <ul>
                {vessels.map(vessel => (
                    <li
                        key={vessel.id}
                        className="p-4 border-b hover:bg-blue-50 cursor-pointer transition-colors"
                        onClick={() => onSelectVessel(vessel)}
                    >
                        <div className="flex justify-between items-center">
                            <h3 className="font-semibold">{vessel.name}</h3>
                            <span className={`px-2 py-1 text-xs rounded-full ${vessel.status === 'in_transit' ? 'bg-green-100 text-green-800' :
                                    vessel.status === 'anchored' ? 'bg-yellow-100 text-yellow-800' : 'bg-gray-100 text-gray-800'
                                }`}>
                                {vessel.status}
                            </span>
                        </div>
                        <div className="mt-1 flex justify-between text-sm text-gray-600">
                            <span>{vessel.vessel_type}</span>
                            <span>{vessel.flag}</span>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default VesselList;
