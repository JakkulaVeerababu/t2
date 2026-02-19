import { useContext } from 'react';
import AuthContext from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import bgImage from '../assets/images/maritime-bg.png';

const Register = () => {
    let { registerUser } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const success = await registerUser(e);
        if (success) {
            navigate('/login');
        } else {
            alert("Registration failed");
        }
    };

    return (
        <div
            className="flex items-center justify-center min-h-screen bg-cover bg-center"
            style={{ backgroundImage: `url(${bgImage})` }}
        >
            <div className="absolute inset-0 bg-black opacity-40"></div>
            <div className="relative z-10 px-8 py-6 mt-4 text-left bg-white/90 backdrop-blur-md shadow-2xl rounded-xl w-full max-w-lg">
                <div className="text-center mb-6">
                    <h1 className="text-3xl font-bold text-blue-900">Maritime Tracker</h1>
                    <p className="text-gray-600">Create a new account</p>
                </div>
                <h3 className="text-xl font-bold text-center mb-4">Register</h3>
                <form onSubmit={handleSubmit}>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label className="block text-gray-700 font-medium" htmlFor="first_name">First Name</label>
                            <input type="text" placeholder="John" name="first_name" required
                                className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-600 bg-white/80" />
                        </div>
                        <div>
                            <label className="block text-gray-700 font-medium" htmlFor="last_name">Last Name</label>
                            <input type="text" placeholder="Doe" name="last_name" required
                                className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-600 bg-white/80" />
                        </div>
                    </div>
                    <div className="mt-4">
                        <label className="block text-gray-700 font-medium" htmlFor="username">Username</label>
                        <input type="text" placeholder="johndoe" name="username" required
                            className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-600 bg-white/80" />
                    </div>
                    <div className="mt-4">
                        <label className="block text-gray-700 font-medium" htmlFor="email">Email</label>
                        <input type="email" placeholder="john@example.com" name="email" required
                            className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-600 bg-white/80" />
                    </div>
                    <div className="mt-4">
                        <label className="block text-gray-700 font-medium">Password</label>
                        <input type="password" placeholder="********" name="password" required
                            className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-600 bg-white/80" />
                    </div>
                    <div className="mt-6 flex flex-col gap-3">
                        <button className="w-full px-6 py-2 text-white bg-blue-700 rounded-lg hover:bg-blue-800 transition-colors shadow-lg font-semibold">Register</button>
                        <div className="flex justify-between items-center text-sm">
                            <span className="text-gray-600">Already have an account?</span>
                            <a href="/login" className="text-blue-700 hover:underline font-medium">Login here</a>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default Register;
