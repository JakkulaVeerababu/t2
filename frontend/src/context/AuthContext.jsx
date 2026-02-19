import { createContext, useState, useEffect } from 'react';
import { jwtDecode } from 'jwt-decode';
import api from '../api/axios';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
    let [user, setUser] = useState(() => localStorage.getItem('access_token') ? jwtDecode(localStorage.getItem('access_token')) : null);
    let [loading, setLoading] = useState(true);

    const loginUser = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post('/auth/login/', {
                username: e.target.username.value,
                password: e.target.password.value
            });
            if (response.status === 200) {
                localStorage.setItem('access_token', response.data.access);
                localStorage.setItem('refresh_token', response.data.refresh);
                setUser(jwtDecode(response.data.access));
                // Optional: Fetch full profile
                // const profileRes = await api.get('/auth/profile/');
                // setUser(prev => ({...prev, ...profileRes.data}));
                return true;
            } else {
                alert('Something went wrong!');
                return false;
            }
        } catch (error) {
            alert('Login failed!');
            return false;
        }
    };

    const logoutUser = () => {
        setUser(null);
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
    };

    const registerUser = async (e) => {
        e.preventDefault();
        try {
            // Implement registration logic
            const response = await api.post('/auth/register/', {
                username: e.target.username.value,
                password: e.target.password.value,
                email: e.target.email.value,
                first_name: e.target.first_name.value,
                last_name: e.target.last_name.value
            });
            if (response.status === 201) {
                return true;
            }
            return false;
        } catch (error) {
            console.error(error);
            return false;
        }
    }

    let contextData = {
        user: user,
        loginUser: loginUser,
        logoutUser: logoutUser,
        registerUser: registerUser
    };

    useEffect(() => {
        setLoading(false);
    }, []);

    return (
        <AuthContext.Provider value={contextData}>
            {loading ? <p>Loading...</p> : children}
        </AuthContext.Provider>
    );
}
