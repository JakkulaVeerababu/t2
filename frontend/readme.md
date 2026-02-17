# Maritime Vessel Tracking Platform - Frontend Documentation
## A Complete React.js Guide for B.Tech Interns

---

## TABLE OF CONTENTS
1. [Introduction to Frontend](#introduction-to-frontend)
2. [Technology Stack Explained](#technology-stack-explained)
3. [Project Setup & Installation](#project-setup--installation)
4. [Project Structure Breakdown](#project-structure-breakdown)
5. [Milestone 1: Authentication UI (Week 1-2)](#milestone-1-authentication-ui-week-1-2)
6. [Milestone 2: Live Map & Vessel Tracking (Week 3-4)](#milestone-2-live-map--vessel-tracking-week-3-4)
7. [Milestone 3: Analytics Dashboards (Week 5-6)](#milestone-3-analytics-dashboards-week-5-6)
8. [Milestone 4: Polish & Deployment (Week 7-8)](#milestone-4-polish--deployment-week-7-8)
9. [Frontend-Backend Integration](#frontend-backend-integration)
10. [State Management with Redux](#state-management-with-redux)
11. [Deployment Guide](#deployment-guide)

---

## Introduction to Frontend

### What is Frontend?
The frontend is what users see and interact with. It's the visual part of your application:
- Login page
- Map showing vessels
- Charts and statistics
- Notifications
- User profile

### Frontend is Like a Restaurant's Dining Area
- **Users see**: Menu, tables, waiters, food
- **Behind the scenes**: Kitchen (backend) prepares and sends food
- **Our job**: Make the dining experience beautiful and smooth

### Why React.js?
We're using **React** (a JavaScript library) because:
-  Build interactive user interfaces
-  Reusable components (write once, use many times)
-  Fast and efficient rendering
-  Large community and ecosystem
-  Easy to learn with JavaScript knowledge
-  Perfect for single-page applications (SPA)

### What Frontend Will Display
1. **Interactive Map** showing vessel positions in real-time
2. **Vessel Details** with photos, specs, and history
3. **Port Analytics** with charts and graphs
4. **Safety Information** with weather alerts and piracy zones
5. **Voyage History** showing past routes and data
6. **User Dashboards** customized by role
7. **Notifications** for alerts and updates

---

## Technology Stack Explained

### Prerequisites

#### 1. **Node.js 16+ and npm**
- **What it is**: JavaScript runtime (let's you run JS outside browser)
- **npm**: Node Package Manager (downloads JavaScript libraries)
- **Check installation**:
~~~
  node --version
  npm --version
  # Should show versions
~~~
- **Install from**: https://nodejs.org/

#### 2. **Visual Studio Code (Optional but Recommended)**
- **What**: Code editor perfect for React development
- **Extensions**: ES7+ React/Redux/React-Native snippets
- **Download**: https://code.visualstudio.com/

#### 3. **Git (Version Control)**
- **What**: Track changes to your code
- **Check installation**: \git --version\
- **Install from**: https://git-scm.com/

### Core Technologies

#### **React 18.2+**
~~~
What: Library for building user interfaces with reusable components
Why: 
  - Component-based (build once, reuse many times)
  - Virtual DOM (fast rendering)
  - One-way data flow (easier to debug)
  - Huge ecosystem of libraries

Install: npm install react react-dom
~~~

**Components**: Think of them like LEGO blocks
- Each component is a reusable UI piece
- Example: \<VesselMap />\, \<LoginForm />\, \<NotificationBell />\

#### **React Router v6**
~~~
What: Navigation library for multi-page feel
Why: 
  - Switch between pages WITHOUT full reload
  - URL changes match page content
  - Browser back/forward button works

Install: npm install react-router-dom

Example:
  /login  LoginPage
  /vessels  VesselTrackingPage
  /ports  PortAnalyticsPage
  /dashboard  DashboardPage
~~~

#### **Axios**
~~~
What: HTTP client for talking to backend API
Why:
  - Send requests to backend server
  - Get responses (vessel data, port stats, etc.)
  - Handle errors gracefully

Install: npm install axios

Usage:
  axios.get('/api/vessels/')           // Get all vessels
  axios.post('/api/auth/register/', data)  // Register user
  axios.put('/api/vessels/1/', data)  // Update vessel
~~~

#### **Redux (State Management)**
~~~
What: Central store for application data
Why:
  - Manage user data (login state, profile)
  - Manage vessel data (list, selected vessel, filters)
  - Manage UI state (modals, notifications)
  - Easy to debug with Redux DevTools

Install: npm install redux react-redux

Concept:
  Store = Single source of truth for ALL application data
  Actions = Events (USER_LOGGED_IN, VESSEL_SELECTED, etc.)
  Reducers = Functions that update state based on actions
~~~

#### **Leaflet + Mapbox GL**
~~~
What: Mapping libraries for displaying vessel positions
Why:
  - Interactive maps with zoom/pan
  - Add markers for vessels and ports
  - Draw routes on map
  - Real-time updates

Install: npm install leaflet mapbox-gl react-leaflet
~~~

#### **Recharts**
~~~
What: Charting library for visualizing data
Why:
  - Line charts for vessel speed over time
  - Bar charts for port traffic
  - Pie charts for vessel types
  - Responsive and beautiful

Install: npm install recharts
~~~

#### **Tailwind CSS**
~~~
What: Utility-first CSS framework for styling
Why:
  - No need to write custom CSS
  - Pre-built components
  - Responsive design (mobile, tablet, desktop)
  - Fast development

Install: npm install -D tailwindcss postcss autoprefixer
~~~

---

## Project Setup & Installation

### Step 1: Create React App

~~~bash
# Method 1: Using Vite (RECOMMENDED - Faster)
npm create vite@latest maritime_frontend -- --template react
cd maritime_frontend
npm install

# Method 2: Using Create React App (Slower but easier)
npx create-react-app maritime_frontend
cd maritime_frontend
npm install
~~~

### Step 2: Install Dependencies

~~~bash
# Core dependencies
npm install react-router-dom axios redux react-redux

# UI and Maps
npm install leaflet mapbox-gl react-leaflet recharts tailwindcss

# Utils
npm install jwt-decode axios-interceptors

# Development tools
npm install -D tailwindcss postcss autoprefixer
npm install redux-devtools-extension
~~~

Or create **package.json** with all dependencies:

~~~json
{
  "name": "maritime-frontend",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.8.0",
    "axios": "^1.3.0",
    "redux": "^4.2.0",
    "react-redux": "^8.0.0",
    "leaflet": "^1.9.0",
    "react-leaflet": "^4.2.0",
    "recharts": "^2.5.0",
    "tailwindcss": "^3.2.0",
    "jwt-decode": "^3.1.2"
  }
}

# Then run: npm install
~~~

### Step 3: Create .env File

Create \.env\ in project root:

~~~env
# Backend API
VITE_API_BASE_URL=http://localhost:8000/api
VITE_API_WS_URL=ws://localhost:8000/ws

# Map Configuration
VITE_MAPBOX_ACCESS_TOKEN=your-mapbox-token
VITE_MAP_DEFAULT_LAT=20
VITE_MAP_DEFAULT_LON=0
VITE_MAP_DEFAULT_ZOOM=3

# Authentication
VITE_JWT_TOKEN_KEY=access_token
VITE_REFRESH_TOKEN_KEY=refresh_token

# Features
VITE_ENABLE_DARK_MODE=true
VITE_ENABLE_REAL_TIME=true

# API Configuration
VITE_API_TIMEOUT=30000
VITE_REQUEST_RETRY_COUNT=3
~~~

### Step 4: Project Structure

~~~
frontend/
 public/                      # Static files
    index.html
    favicon.ico
    vessel-icon.svg

 src/
    index.jsx               # Application entry point
    App.jsx                 # Main component
   
    pages/                  # Page components (full pages)
       Login.jsx
       Register.jsx
       Dashboard.jsx
       VesselTracking.jsx
       PortAnalytics.jsx
       Safety.jsx
       NotFound.jsx
   
    components/             # Reusable components
       common/
          Header.jsx      # Navigation bar
          Sidebar.jsx     # Side menu
          Loading.jsx     # Loading spinner
          ErrorBoundary.jsx
      
       maps/
          VesselMap.jsx          # Main tracking map
          MapControls.jsx        # Zoom, layers
          VesselMarker.jsx       # Vessel icon on map
          PortMarker.jsx         # Port icon on map
          SafetyOverlay.jsx      # Weather/piracy overlay
      
       vessels/
          VesselList.jsx
          VesselCard.jsx
          VesselDetail.jsx
          VesselFilter.jsx
          VesselSearch.jsx
          VesselSubscribe.jsx
      
       ports/
          PortList.jsx
          PortCard.jsx
          PortDetail.jsx
          CongestionChart.jsx
          PortStatistics.jsx
      
       auth/
          LoginForm.jsx
          RegisterForm.jsx
          ProfileEditor.jsx
          PrivateRoute.jsx
      
       dashboard/
          OperatorDashboard.jsx
          AnalystDashboard.jsx
          AdminDashboard.jsx
      
       charts/
           TimeSeriesChart.jsx
           SpeedChart.jsx
           TrafficChart.jsx
   
    store/                  # Redux store
       index.js           # Store configuration
       actions/           # Action creators
          authActions.js
          vesselActions.js
          portActions.js
       reducers/          # State reducers
          authReducer.js
          vesselReducer.js
          portReducer.js
       middleware/        # Custom middleware
   
    services/              # API service calls
       api.js            # Axios instance
       authService.js    # Login, register, profile
       vesselService.js  # Vessel API calls
       portService.js    # Port API calls
       safetyService.js  # Safety API calls
   
    hooks/                # Custom React hooks
       useAuth.js        # Authentication hook
       useVessels.js     # Fetch vessels
       usePorts.js       # Fetch ports
       useLocalStorage.js
   
    utils/                # Utility functions
       constants.js      # Constants and enums
       validators.js     # Form validators
       formatters.js     # Date, number formatting
       mapUtils.js       # Map calculations
       storage.js        # LocalStorage helpers
   
    styles/               # Global styles
       index.css
       variables.css     # CSS variables
       animations.css
       responsive.css
   
    assets/               # Images, icons
       images/
       icons/
       flags/
   
    tests/                # Test files
        components/
        services/
        utils/

 .env                       # Environment variables
 .gitignore                # Git ignore rules
 package.json              # Dependencies
 vite.config.js           # Vite configuration (if using Vite)
 tailwind.config.js       # Tailwind configuration
~~~

### Step 5: Start Development Server

~~~bash
# Start the development server
npm run dev

# Server will run at: http://localhost:3000
# If using Create React App: npm start
~~~

---

## Milestone 1: Authentication UI (Week 1-2)

### Objective
Build login and registration pages integrated with backend authentication.

### Step 1: Create Authentication Service

**src/services/authService.js**:

~~~javascript
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
const TOKEN_KEY = import.meta.env.VITE_JWT_TOKEN_KEY;
const REFRESH_KEY = import.meta.env.VITE_REFRESH_TOKEN_KEY;

class AuthService {
  // Register new user
  async register(username, email, password, password2) {
    try {
      const response = await axios.post(
        \\/auth/register/\,
        { username, email, password, password2 }
      );
      return response.data;
    } catch (error) {
      throw error.response?.data?.error || 'Registration failed';
    }
  }

  // Login user
  async login(username, password) {
    try {
      const response = await axios.post(
        \\/auth/token/\,
        { username, password }
      );
      
      // Save tokens
      localStorage.setItem(TOKEN_KEY, response.data.access);
      localStorage.setItem(REFRESH_KEY, response.data.refresh);
      
      return response.data;
    } catch (error) {
      throw error.response?.data?.detail || 'Login failed';
    }
  }

  // Get current user profile
  async getProfile() {
    try {
      const response = await axios.get(
        \\/auth/profile/me/\,
        {
          headers: {
            Authorization: \Bearer \\
          }
        }
      );
      return response.data;
    } catch (error) {
      throw error.response?.data?.error || 'Failed to fetch profile';
    }
  }

  // Logout
  logout() {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(REFRESH_KEY);
  }

  // Get stored token
  getToken() {
    return localStorage.getItem(TOKEN_KEY);
  }

  // Check if user is logged in
  isLoggedIn() {
    return !!this.getToken();
  }
}

export default new AuthService();
~~~

### Step 2: Create Redux Store for Auth

**src/store/reducers/authReducer.js**:

~~~javascript
const initialState = {
  user: null,
  isLoading: false,
  error: null,
  isAuthenticated: false,
};

export const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'AUTH_LOGIN_START':
      return { ...state, isLoading: true, error: null };
    
    case 'AUTH_LOGIN_SUCCESS':
      return {
        ...state,
        isLoading: false,
        user: action.payload,
        isAuthenticated: true,
        error: null,
      };
    
    case 'AUTH_LOGIN_FAILURE':
      return {
        ...state,
        isLoading: false,
        error: action.payload,
        isAuthenticated: false,
      };
    
    case 'AUTH_LOGOUT':
      return {
        ...state,
        user: null,
        isAuthenticated: false,
        error: null,
      };
    
    default:
      return state;
  }
};
~~~

**src/store/actions/authActions.js**:

~~~javascript
import authService from '../../services/authService';

export const loginUser = (username, password) => async (dispatch) => {
  dispatch({ type: 'AUTH_LOGIN_START' });
  try {
    const user = await authService.login(username, password);
    dispatch({
      type: 'AUTH_LOGIN_SUCCESS',
      payload: user,
    });
  } catch (error) {
    dispatch({
      type: 'AUTH_LOGIN_FAILURE',
      payload: error.message,
    });
  }
};

export const logoutUser = () => (dispatch) => {
  authService.logout();
  dispatch({ type: 'AUTH_LOGOUT' });
};

export const registerUser = (userData) => async (dispatch) => {
  try {
    const response = await authService.register(
      userData.username,
      userData.email,
      userData.password,
      userData.password2
    );
    return response;
  } catch (error) {
    throw error;
  }
};
~~~

### Step 3: Create Login Component

**src/components/auth/LoginForm.jsx**:

~~~javascript
import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../../store/actions/authActions';

export default function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { isLoading, error } = useSelector(state => state.auth);

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch(loginUser(username, password));
    // On success, navigate to dashboard
    if (!error) {
      setTimeout(() => navigate('/dashboard'), 1000);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center">
      <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md">
        <h2 className="text-2xl font-bold text-center mb-6">Maritime Vessel Tracking</h2>
        
        {error && (
          <div className="bg-red-100 text-red-700 p-3 rounded mb-4">
            {error}
          </div>
        )}
        
        <form onSubmit={handleSubmit}>
          {/* Username Input */}
          <div className="mb-4">
            <label className="block text-gray-700 font-semibold mb-2">
              Username
            </label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your username"
              required
            />
          </div>

          {/* Password Input */}
          <div className="mb-6">
            <label className="block text-gray-700 font-semibold mb-2">
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your password"
              required
            />
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            disabled={isLoading}
            className="w-full bg-blue-600 text-white font-semibold py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50"
          >
            {isLoading ? 'Logging in...' : 'Login'}
          </button>
        </form>

        {/* Register Link */}
        <p className="text-center text-gray-600 mt-4">
          Don't have an account?{' '}
          <a href="/register" className="text-blue-600 hover:underline">
            Register here
          </a>
        </p>
      </div>
    </div>
  );
}
~~~

### Step 4: Create Register Component

**src/components/auth/RegisterForm.jsx**:

~~~javascript
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { registerUser } from '../../store/actions/authActions';

export default function RegisterForm() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    password2: '',
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      await registerUser(formData);
      // Navigate to login on success
      navigate('/login', { state: { message: 'Registration successful! Please login.' } });
    } catch (err) {
      setError(err.message || 'Registration failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-500 to-green-700 flex items-center justify-center">
      <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md">
        <h2 className="text-2xl font-bold text-center mb-6">Create Account</h2>
        
        {error && (
          <div className="bg-red-100 text-red-700 p-3 rounded mb-4">
            {error}
          </div>
        )}
        
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
            className="w-full px-4 py-2 border rounded-lg mb-3 focus:outline-none focus:ring-2 focus:ring-green-500"
            required
          />
          
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            className="w-full px-4 py-2 border rounded-lg mb-3 focus:outline-none focus:ring-2 focus:ring-green-500"
            required
          />
          
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            className="w-full px-4 py-2 border rounded-lg mb-3 focus:outline-none focus:ring-2 focus:ring-green-500"
            required
          />
          
          <input
            type="password"
            name="password2"
            placeholder="Confirm Password"
            value={formData.password2}
            onChange={handleChange}
            className="w-full px-4 py-2 border rounded-lg mb-6 focus:outline-none focus:ring-2 focus:ring-green-500"
            required
          />
          
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-green-600 text-white font-semibold py-2 rounded-lg hover:bg-green-700 disabled:opacity-50"
          >
            {loading ? 'Registering...' : 'Register'}
          </button>
        </form>

        <p className="text-center text-gray-600 mt-4">
          Already have an account?{' '}
          <a href="/login" className="text-green-600 hover:underline">
            Login here
          </a>
        </p>
      </div>
    </div>
  );
}
~~~

### Step 5: Create Protected Route Component

**src/components/auth/PrivateRoute.jsx**:

~~~javascript
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useSelector } from 'react-redux';

export default function PrivateRoute({ children }) {
  const { isAuthenticated } = useSelector(state => state.auth);

  return isAuthenticated ? children : <Navigate to="/login" />;
}
~~~

### Step 6: Create Main App Router

**src/App.jsx**:

~~~javascript
import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import RegisterForm from './components/auth/RegisterForm';
import Dashboard from './pages/Dashboard';
import VesselTracking from './pages/VesselTracking';
import PrivateRoute from './components/auth/PrivateRoute';

function App() {
  const dispatch = useDispatch();

  useEffect(() => {
    // Check if user is already logged in on app load
    const token = localStorage.getItem('access_token');
    if (token) {
      // Could restore user session here
    }
  }, [dispatch]);

  return (
    <Router>
      <Routes>
        {/* Public Routes */}
        <Route path="/login" element={<LoginForm />} />
        <Route path="/register" element={<RegisterForm />} />

        {/* Protected Routes */}
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />
        <Route
          path="/vessels"
          element={
            <PrivateRoute>
              <VesselTracking />
            </PrivateRoute>
          }
        />

        {/* Default Redirect */}
        <Route path="/" element={<Navigate to="/dashboard" />} />
      </Routes>
    </Router>
  );
}

export default App;
~~~

### Step 7: Create Main Store Configuration

**src/store/index.js**:

~~~javascript
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { authReducer } from './reducers/authReducer';

const rootReducer = combineReducers({
  auth: authReducer,
});

const store = createStore(
  rootReducer,
  applyMiddleware(thunk)
);

export default store;
~~~

### Step 8: Update index.jsx

**src/index.jsx**:

~~~javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import App from './App';
import store from './store';
import './styles/index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
);
~~~

### Step 9: Test Authentication Flow

~~~bash
# Start frontend dev server
npm run dev

# Visit http://localhost:3000
# Try to register a new user
# Try to login with credentials
# Should redirect to dashboard after successful login
~~~

---

## Milestone 2: Live Map & Vessel Tracking (Week 3-4)

### Objective
Display vessels on interactive map with real-time updates.

[Additional Milestone 2 content would follow similar format...]

---

## Frontend-Backend Integration

### How Frontend Communicates with Backend

**1. Frontend sends request:**
~~~javascript
// In component
const response = await axios.get('http://localhost:8000/api/vessels/');
~~~

**2. Backend processes request:**
~~~python
# In Django view
def list(self, request):
    vessels = Vessel.objects.all()
    serializer = VesselListSerializer(vessels, many=True)
    return Response(serializer.data)
~~~

**3. Frontend receives response:**
~~~javascript
// Response data
{
  "count": 100,
  "results": [
    { "id": 1, "name": "MAERSK", "latitude": 35.12, "longitude": 139.56 }
  ]
}
~~~

**4. Frontend updates UI:**
~~~javascript
// Display vessels on map
const [vessels, setVessels] = useState([]);

useEffect(() => {
  axios.get('/api/vessels/')
    .then(res => setVessels(res.data.results));
}, []);
~~~

---

## Deployment Guide

### Deploy Frontend to Vercel (Easiest)

~~~bash
# 1. Create account: https://vercel.com
# 2. Connect your GitHub repo
# 3. Vercel auto-deploys on every push!
# 4. Your app is live at: maritime-frontend.vercel.app
~~~

### Deploy Frontend to GitHub Pages

~~~bash
# 1. Build for production
npm run build

# 2. Output in 'dist' folder ready to deploy
# 3. Push 'dist' folder to GitHub Pages

# View at: yourusername.github.io/maritime-frontend
~~~

---

**Last Updated**: February 2026
**Frontend Version**: 1.0.0
**Framework**: React 18.2 + Vite
