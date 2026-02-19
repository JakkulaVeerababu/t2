import { useContext } from 'react';
import AuthContext from '../context/AuthContext';

const Dashboard = () => {
    let { user, logoutUser } = useContext(AuthContext);

    return (
        <div className="min-h-screen bg-gray-100">
            <nav className="bg-white shadow">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between h-16">
                        <div className="flex">
                            <div className="flex-shrink-0 flex items-center">
                                <h1 className="text-xl font-bold">Maritime Tracker</h1>
                            </div>
                        </div>
                        <div className="flex items-center">
                            <span className="mr-4">Welcome, {user && user.username}</span>
                            <button onClick={logoutUser} className="text-red-600 hover:text-red-900">Logout</button>
                        </div>
                    </div>
                </div>
            </nav>
            <div className="py-10">
                <header>
                    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <h1 className="text-3xl font-bold leading-tight text-gray-900">Dashboard</h1>
                    </div>
                </header>
                <main>
                    <div className="max-w-7xl mx-auto sm:px-6 lg:px-8">
                        <div className="px-4 py-8 sm:px-0">
                            <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 flex items-center justify-center">
                                <p className="text-gray-500">Live Map and Analytics will appear here in Milestone 2.</p>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
        </div>
    );
};

export default Dashboard;
