# Maritime Vessel Tracking Platform - Complete Frontend Documentation
## Comprehensive Guide for Frontend Development

---

## 📑 TABLE OF CONTENTS

1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Prerequisites & Requirements](#prerequisites--requirements)
4. [Complete Installation Guide](#complete-installation-guide)
5. [Project Structure & Architecture](#project-structure--architecture)
6. [React Fundamentals for Beginners](#react-fundamentals-for-beginners)
7. [Component Architecture](#component-architecture)
8. [State Management with Redux](#state-management-with-redux)
9. [API Integration & Service Layer](#api-integration--service-layer)
10. [Authentication Flow](#authentication-flow)
11. [Feature Implementation Guide](#feature-implementation-guide)
12. [Styling with Tailwind CSS](#styling-with-tailwind-css)
13. [Testing Strategies](#testing-strategies)
14. [Performance Optimization](#performance-optimization)
15. [Deployment Guide](#deployment-guide)
16. [Troubleshooting & Common Issues](#troubleshooting--common-issues)

---

## 📌 PROJECT OVERVIEW

### What is the Frontend?

The **frontend** is what users see and interact with in their web browser. Think of it like:

```
┌─────────────────────────────────────────────────────┐
│                 WHAT USERS SEE                       │
│  ┌──────────────────────────────────────────────┐   │
│  │  🔵 Login Page                               │   │
│  │  ├─ Username input field                     │   │
│  │  ├─ Password input field                     │   │
│  │  └─ Login button                             │   │
│  └──────────────────────────────────────────────┘   │
│                                                      │
│  ┌──────────────────────────────────────────────┐   │
│  │  Dashboard                                   │   │
│  │  ├─ Interactive Map (showing vessels)       │   │
│  │  ├─ Vessel List (with search)               │   │
│  │  ├─ Port Statistics (graphs and charts)     │   │
│  │  └─ Safety Alerts (real-time updates)       │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                          ↓
                  (Makes HTTP requests)
                          ↓
┌─────────────────────────────────────────────────────┐
│              BACKEND (Django API)                    │
│     (Processes data and returns JSON)                │
└─────────────────────────────────────────────────────┘
```

### Frontend Core Responsibilities

| Responsibility | Description |
|---|---|
| **User Interface** | Display pages and forms users interact with |
| **User Input** | Capture login, search queries, filters |
| **API Communication** | Send requests to backend, handle responses |
| **State Management** | Keep track of logged-in user, vessel data, filters |
| **Real-time Updates** | WebSocket for live vessel positions |
| **Data Visualization** | Maps, charts, and graphs |
| **Navigation** | Handle page routing and navigation |
| **Error Handling** | Show error messages when things fail |

### Key Screens in This Application

```
1. Authentication Screens
   ├─ Login Page (username & password)
   ├─ Registration Page (create account)
   └─ Forget Password (password recovery)

2. Main Dashboard
   ├─ Header (logout, profile settings)
   ├─ Sidebar Navigation
   │  ├─ Dashboard
   │  ├─ Vessels
   │  ├─ Ports
   │  ├─ Safety
   │  └─ Reports
   └─ Content Area (main data display)

3. Vessel Module
   ├─ Vessel List (search, filter)
   ├─ Vessel Map (interactive map with positions)
   ├─ Vessel Details (full information + history)
   └─ Alerts Management (subscribe/unsubscribe)

4. Port Module
   ├─ Port Directory (list of ports)
   ├─ Port Details (statistics, congestion)
   ├─ Port History (graphs of congestion over time)
   └─ Arrivals/Departures (vessel movement)

5. Safety Module
   ├─ Weather Alerts (current storms, warnings)
   ├─ Piracy Zones (high-risk maritime areas)
   ├─ Accident History (past incidents)
   └─ Safety Overlay (on interactive map)

6. Admin Module (visible only to admins)
   ├─ User Management
   ├─ System Settings
   ├─ API Key Management
   └─ System Logs
```

---

## 🛠️ TECHNOLOGY STACK

### React 18.x
**What it is**: A JavaScript library for building user interfaces with reusable components

```javascript
// Think of React like LEGO blocks
// Instead of writing one giant HTML file,
// you build small reusable pieces:

// Piece 1: Button
function LoginButton() {
    return <button>Click to Login</button>
}

// Piece 2: Form
function LoginForm() {
    return (
        <form>
            <input type="text" placeholder="Username" />
            <LoginButton />
        </form>
    )
}

// Piece 3: Page
function LoginPage() {
    return (
        <div className="login-page">
            <h1>Welcome</h1>
            <LoginForm />
        </div>
    )
}

// Each piece is "reusable" - can use LoginButton anywhere
```

**Key Features**:
- Component-based architecture
- Virtual DOM (fast re-renders)
- One-way data flow
- Excellent for interactive UIs
- Large ecosystem and community

### Vite (Build Tool)
**What it is**: A super-fast bundler that packages React code for browsers

```
Your React Code (JavaScript, CSS, JSX)
         ↓
     Vite Bundler
         ↓
Optimized Bundle (HTML, JS, CSS)
         ↓
Browser (Fast loading!)
```

**Why Vite?**
- Lightning-fast development server
- Instant Hot Module Reloading (HMR)
- Optimized production builds
- Way faster than Create React App

### React Router v6
**What it is**: Navigation between different pages without full page reloads

```javascript
// Define routes
<BrowserRouter>
    <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/vessels" element={<VesselList />} />
        <Route path="/vessels/:id" element={<VesselDetail />} />
        <Route path="/ports" element={<PortList />} />
    </Routes>
</BrowserRouter>

// Navigate between pages
<Link to="/vessels">View Vessels</Link>
<Navigate to="/dashboard" replace />
```

### Redux (State Management)
**What it is**: Central storage for all application data

```
Think of Redux like a bank vault:

Normal way (messy):
┌─ Component 1: Has user data
├─ Component 2: Has vessel data
├─ Component 3: Has port data
└─ Component 4: Needs to use data from 1, 2, 3
   (How does it get the data? Complicated!)

Redux way (organized):
┌─────────────────────────────────────┐
│         REDUX STORE (Vault)         │
│  {                                  │
│    user: { id, name, role },        │
│    vessels: [ ... ],                │
│    ports: [ ... ],                  │
│    filters: { type, country }       │
│  }                                  │
└─────────────────────────────────────┘
        ▲    ▲                    │
        │    └────────────────────┴─── All components can READ
        │
        └────── Components DISPATCH actions to update
```

**Benefits**:
- Single source of truth
- Time-travel debugging
- Predictable state updates
- Easy to debug (can see all state changes)

### Axios (HTTP Client)
**What it is**: Makes API requests to the backend

```javascript
// GET request - fetch vessel data
axios.get('/api/vessels/')
    .then(response => console.log(response.data))
    .catch(error => console.log(error))

// POST request - send login credentials
axios.post('/api/auth/token/', {
    username: 'john_doe',
    password: 'SecurePass123!'
})
    .then(response => {
        // Save token
        localStorage.setItem('access_token', response.data.access)
    })
```

### Leaflet.js & Mapbox GL
**What it is**: Interactive mapping libraries for vessel positions

```javascript
// Display map
const map = L.map('map').setView([35.6762, 139.6503], 4)

// Add marker for vessel
L.marker([35.6762, 139.6503])
    .bindPopup('MAERSK - Speed: 12.5 knots')
    .addTo(map)

// Draw route path
const routePoints = [
    [35.1, 139.5],
    [35.2, 139.6],
    [35.3, 139.7]
]
L.polyline(routePoints).addTo(map)
```

### Recharts (Data Visualization)
**What it is**: Charts and graphs for port statistics

```javascript
import { LineChart, Line, XAxis, YAxis } from 'recharts'

const data = [
    { date: 'Feb 10', congestion: 45 },
    { date: 'Feb 11', congestion: 52 },
    { date: 'Feb 12', congestion: 60 }
]

<LineChart width={800} height={400} data={data}>
    <XAxis dataKey="date" />
    <YAxis />
    <Line type="monotone" dataKey="congestion" />
</LineChart>
```

### Tailwind CSS (Styling)
**What it is**: Utility-first CSS framework for styling

```html
<!-- Normal CSS (verbose) -->
<style>
    .button {
        padding: 10px 20px;
        background-color: blue;
        color: white;
        border-radius: 5px;
    }
</style>
<button class="button">Click me</button>

<!-- Tailwind CSS (concise) -->
<button class="px-4 py-2 bg-blue-500 text-white rounded">
    Click me
</button>
```

**Advantages**:
- No need to write CSS files
- Consistent styling
- Easy to customize
- Smaller final bundle size

---

## ✅ PREREQUISITES & REQUIREMENTS

### System Requirements

| Component | Version | Why Needed |
|-----------|---------|-----------|
| Node.js | 16+ | JavaScript runtime for frontend |
| npm or yarn | Latest | Package manager for JavaScript |
| Git | Latest | Version control |
| Browser | Modern (Chrome, Firefox, Safari, Edge) | To run the web app |

### Verify Installation

```bash
# Check Node.js
node --version
# Should show: v16.0.0 or higher

# Check npm
npm --version
# Should show: 8.0.0 or higher

# Check Git
git --version
# Should show: git version 2.x.x
```

### Knowledge Prerequisites

Before starting, be comfortable with:
- ✅ Basic JavaScript (variables, functions, objects)
- ✅ ES6+ features (arrow functions, destructuring, async/await)
- ✅ HTML basics (elements, attributes, forms)
- ✅ CSS basics (selectors, properties, flexbox)
- ✅ API/HTTP concepts (GET, POST requests)
- ✅ JSON format

### Browser DevTools

Install these for debugging:
```
✓ React Developer Tools (Chrome/Firefox extension)
✓ Redux DevTools (Chrome/Firefox extension)
✓ Built-in Browser DevTools (F12)
```

---

## 📦 COMPLETE INSTALLATION GUIDE

### Step 1: Verify Node.js Installation

```bash
# Check versions
node --version
npm --version

# If not installed, download from https://nodejs.org/
# Choose LTS (Long Term Support) version
```

### Step 2: Clone or Initialize Project

```bash
# Navigate to project folder
cd Maritime_Vessel_Tracking/frontend

# If using Vite (recommended):
npm create vite@latest . -- --template react

# Or if folder is not empty:
npm install
```

### Step 3: Install Dependencies

```bash
# Install all required packages
npm install

# Key packages installed by default:
# - react: Core library
# - react-dom: Render React to browser
# - react-router-dom: Routing
# - redux: State management
# - react-redux: Connect Redux to React
# - axios: HTTP client
# - leaflet: Maps
# - recharts: Charts
# - tailwindcss: Styling

# Install missing packages if needed:
npm install react-router-dom
npm install @reduxjs/toolkit react-redux
npm install axios
npm install leaflet react-leaflet
npm install recharts
npm install -D tailwindcss postcss autoprefixer
```

### Step 4: Configure Tailwind CSS

```bash
# Initialize Tailwind
npx tailwindcss init -p

# This creates:
# - tailwind.config.js
# - postcss.config.js
```

**Edit `tailwind.config.js`**:

```javascript
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

**Add to `src/index.css`**:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Step 5: Create .env File

Create `.env` file in project root:

```env
# ============ API CONFIGURATION ============
VITE_API_URL=http://localhost:8000/api
VITE_API_TIMEOUT=10000

# ============ MAP CONFIGURATION ============
VITE_MAPBOX_TOKEN=your-mapbox-token-here

# ============ FEATURE FLAGS ============
VITE_ENABLE_WEBSOCKET=true
VITE_ENABLE_REAL_TIME=true

# ============ LOGGING ============
VITE_LOG_LEVEL=debug
```

### Step 6: Update Vite Configuration

Edit `vite.config.js`:

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '/api')
      }
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
  }
})
```

### Step 7: Create Folder Structure

```bash
# Create required folders
mkdir -p src/components
mkdir -p src/pages
mkdir -p src/redux
mkdir -p src/services
mkdir -p src/hooks
mkdir -p src/utils
mkdir -p src/assets
mkdir -p src/constants
```

### Step 8: Start Development Server

```bash
# Start development server
npm run dev

# Server runs at: http://localhost:3000

# In a new terminal, start backend:
cd ../backend
python manage.py runserver

# Backend runs at: http://localhost:8000
```

---

## 🏗️ PROJECT STRUCTURE & ARCHITECTURE

### Complete Directory Layout

```
frontend/
│
├── public/                              # Static files (images, icons)
│   ├── favicon.ico
│   └── manifest.json
│
├── src/                                 # All source code
│   │
│   ├── index.html                       # Main HTML file (entry point)
│   ├── main.jsx                         # React app initialization
│   ├── App.jsx                          # Root component
│   ├── index.css                        # Global styles
│   │
│   ├── components/                      # Reusable components
│   │   ├── Navbar.jsx                  # Top navigation bar
│   │   ├── Sidebar.jsx                 # Left sidebar navigation
│   │   ├── LoadingSpinner.jsx           # Loading indicator
│   │   ├── ErrorBoundary.jsx            # Error handling
│   │   ├── PrivateRoute.jsx             # Protected routes
│   │   │
│   │   ├── auth/                        # Authentication components
│   │   │   ├── LoginForm.jsx
│   │   │   ├── RegisterForm.jsx
│   │   │   └── ForgotPassword.jsx
│   │   │
│   │   ├── vessels/                     # Vessel-related components
│   │   │   ├── VesselList.jsx
│   │   │   ├── VesselItem.jsx
│   │   │   ├── VesselDetail.jsx
│   │   │   ├── VesselMap.jsx
│   │   │   ├── VesselSearch.jsx
│   │   │   └── VesselAlerts.jsx
│   │   │
│   │   ├── ports/                       # Port-related components
│   │   │   ├── PortList.jsx
│   │   │   ├── PortDetail.jsx
│   │   │   ├── PortCongestionChart.jsx
│   │   │   └── PortArrivals.jsx
│   │   │
│   │   ├── safety/                      # Safety-related components
│   │   │   ├── WeatherAlerts.jsx
│   │   │   ├── PiracyZones.jsx
│   │   │   └── SafetyOverlay.jsx
│   │   │
│   │   └── common/                      # Shared components
│   │       ├── Card.jsx
│   │       ├── Button.jsx
│   │       ├── Modal.jsx
│   │       └── Pagination.jsx
│   │
│   ├── pages/                           # Full page components
│   │   ├── LoginPage.jsx
│   │   ├── DashboardPage.jsx
│   │   ├── VesselPage.jsx
│   │   ├── PortPage.jsx
│   │   ├── SafetyPage.jsx
│   │   ├── NotFoundPage.jsx
│   │   └── AdminPage.jsx
│   │
│   ├── redux/                           # State management
│   │   ├── store.js                     # Redux store configuration
│   │   │
│   │   ├── slices/                      # Redux slices
│   │   │   ├── authSlice.js             # Auth state
│   │   │   ├── vesselSlice.js           # Vessel state
│   │   │   ├── portSlice.js             # Port state
│   │   │   ├── safetySlice.js           # Safety state
│   │   │   ├── filtersSlice.js          # Filters state
│   │   │   └── uiSlice.js               # UI state (loading, errors)
│   │   │
│   │   └── selectors/                   # Redux selectors
│   │       ├── authSelectors.js
│   │       ├── vesselSelectors.js
│   │       └── portSelectors.js
│   │
│   ├── services/                        # API communication
│   │   ├── api.js                       # Axios instance setup
│   │   ├── authService.js               # Auth API calls
│   │   ├── vesselService.js             # Vessel API calls
│   │   ├── portService.js               # Port API calls
│   │   ├── safetyService.js             # Safety API calls
│   │   └── websocketService.js          # Real-time WebSocket
│   │
│   ├── hooks/                           # Custom React hooks
│   │   ├── useAuth.js                   # Auth context hook
│   │   ├── useFetch.js                  # Data fetching hook
│   │   ├── useLocalStorage.js           # Local storage hook
│   │   └── useDebounce.js               # Debounce hook
│   │
│   ├── utils/                           # Utility functions
│   │   ├── constants.js                 # App constants
│   │   ├── helpers.js                   # Helper functions
│   │   ├── validators.js                # Form validation
│   │   ├── formatters.js                # Data formatting
│   │   └── storage.js                   # LocalStorage wrapper
│   │
│   ├── assets/                          # Images, icons, fonts
│   │   ├── images/
│   │   ├── icons/
│   │   └── fonts/
│   │
│   └── constants/                       # Constants
│       ├── api.js                       # API endpoints
│       ├── colors.js                    # Color scheme
│       └── messages.js                  # Error/success messages
│
├── .env                                 # Environment variables
├── .gitignore                           # Files to ignore
├── package.json                         # Dependencies and scripts
├── package-lock.json                    # Locked versions
├── vite.config.js                       # Vite configuration
├── tailwind.config.js                   # Tailwind configuration
├── postcss.config.js                    # PostCSS configuration
└── README.md                            # Project documentation
```

---

## ⚛️ REACT FUNDAMENTALS FOR BEGINNERS

### Core Concepts

#### 1. Components

A component is a reusable piece of UI:

```javascript
// Function Component (modern way)
function Welcome() {
    return <h1>Welcome to Maritime Tracking</h1>
}

// Using the component
export default function App() {
    return (
        <div>
            <Welcome />
            <Welcome />  {/* Can reuse multiple times */}
        </div>
    )
}
```

#### 2. JSX (JavaScript + HTML)

Write HTML-like syntax in JavaScript:

```javascript
// JSX syntax
const element = (
    <div className="container">
        <h1>Hello World</h1>
        <p>This is JSX</p>
    </div>
)

// Gets compiled to:
// React.createElement('div', { className: 'container' },
//     React.createElement('h1', null, 'Hello World'),
//     React.createElement('p', null, 'This is JSX')
// )
```

#### 3. Props (Component Properties)

Pass data from parent to child:

```javascript
// Parent component
function App() {
    return <VesselCard name="MAERSK" speed={12.5} />
}

// Child component (receives props)
function VesselCard(props) {
    return (
        <div>
            <h2>{props.name}</h2>
            <p>Speed: {props.speed} knots</p>
        </div>
    )
}

// Or use destructuring (cleaner):
function VesselCard({ name, speed }) {
    return (
        <div>
            <h2>{name}</h2>
            <p>Speed: {speed} knots</p>
        </div>
    )
}
```

#### 4. State (Component Memory)

Components can store and update data:

```javascript
import { useState } from 'react'

function Counter() {
    // [currentValue, functionToUpdate] = useState(initialValue)
    const [count, setCount] = useState(0)
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>
                Increment
            </button>
        </div>
    )
}

// How it works:
// 1. Initial: count = 0, displays "Count: 0"
// 2. Click button: setCount(1) called
// 3. Component re-renders with count = 1
// 4. Display updates: "Count: 1"
```

#### 5. Effects (Side Effects)

Run code when component loads or updates:

```javascript
import { useState, useEffect } from 'react'

function VesselList() {
    const [vessels, setVessels] = useState([])
    const [loading, setLoading] = useState(true)
    
    // Run once when component mounts
    useEffect(() => {
        fetch('/api/vessels/')
            .then(res => res.json())
            .then(data => {
                setVessels(data)
                setLoading(false)
            })
    }, [])  // [] = run only once
    
    if (loading) return <p>Loading...</p>
    
    return (
        <div>
            {vessels.map(vessel => (
                <div key={vessel.id}>{vessel.name}</div>
            ))}
        </div>
    )
}

// Different dependency arrays:
useEffect(() => { ... }, [])           // Run once on mount
useEffect(() => { ... }, [id])         // Run when 'id' changes
useEffect(() => { ... }, [a, b, c])    // Run when any of a, b, c changes
useEffect(() => { ... })               // Run on every render (risk!)
```

#### 6. Conditional Rendering

Show/hide elements based on conditions:

```javascript
function User({ isLoggedIn, userName }) {
    // Method 1: if-else
    if (isLoggedIn) {
        return <p>Welcome back, {userName}!</p>
    } else {
        return <p>Please log in</p>
    }
}

// Method 2: Ternary operator
function User({ isLoggedIn, userName }) {
    return (
        <p>
            {isLoggedIn ? `Welcome back, ${userName}!` : 'Please log in'}
        </p>
    )
}

// Method 3: Logical AND (&&)
function Notification({ hasUnread, count }) {
    return (
        <div>
            {hasUnread && <span className="badge">{count}</span>}
        </div>
    )
}
```

#### 7. Lists and Keys

Render lists efficiently:

```javascript
function VesselList({ vessels }) {
    return (
        <div>
            {vessels.map((vessel) => (
                // MUST have unique 'key' for performance
                <div key={vessel.id}>
                    <h3>{vessel.name}</h3>
                    <p>IMO: {vessel.imo}</p>
                </div>
            ))}
        </div>
    )
}

// Bad (don't do this):
{vessels.map((vessel, index) => (
    <div key={index}>  // DON'T use index as key!
        {vessel.name}
    </div>
))}
```

---

## 🧩 COMPONENT ARCHITECTURE

### Component Types

#### 1. Page Components (Full Page)

```javascript
// src/pages/DashboardPage.jsx
import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import Navbar from '../components/Navbar'
import Sidebar from '../components/Sidebar'
import VesselMap from '../components/vessels/VesselMap'
import PortStats from '../components/ports/PortStats'

function DashboardPage() {
    const dispatch = useDispatch()
    const user = useSelector(state => state.auth.user)
    const [loading, setLoading] = useState(true)
    
    useEffect(() => {
        // Load all dashboard data
        dispatch(fetchVessels())
        dispatch(fetchPorts())
        dispatch(fetchSafetyAlerts())
        setLoading(false)
    }, [dispatch])
    
    return (
        <div className="flex h-screen bg-gray-100">
            <Sidebar />
            
            <div className="flex-1 flex flex-col">
                <Navbar user={user} />
                
                <main className="flex-1 overflow-auto p-6">
                    {loading ? (
                        <LoadingSpinner />
                    ) : (
                        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                            <VesselMap />
                            <PortStats />
                        </div>
                    )}
                </main>
            </div>
        </div>
    )
}

export default DashboardPage
```

#### 2. Feature Components (Specific Feature)

```javascript
// src/components/vessels/VesselList.jsx
import { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import VesselItem from './VesselItem'
import VesselSearch from './VesselSearch'
import Pagination from '../common/Pagination'

function VesselList() {
    const dispatch = useDispatch()
    const vessels = useSelector(state => state.vessels.list)
    const filters = useSelector(state => state.filters)
    const [page, setPage] = useState(1)
    
    useEffect(() => {
        // Fetch vessels with current filters
        dispatch(fetchVessels({
            page: page,
            type: filters.type,
            country: filters.country,
            search: filters.search
        }))
    }, [dispatch, page, filters])
    
    return (
        <div className="vessel-list">
            <VesselSearch />
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {vessels.map(vessel => (
                    <VesselItem key={vessel.id} vessel={vessel} />
                ))}
            </div>
            
            <Pagination 
                currentPage={page}
                onPageChange={setPage}
            />
        </div>
    )
}

export default VesselList
```

#### 3. Presentational Components (Dumb Components)

```javascript
// src/components/vessels/VesselItem.jsx
// This component just displays data (no logic)

function VesselItem({ vessel, onClick, variant = 'default' }) {
    return (
        <div 
            className={`
                p-4 border rounded cursor-pointer
                ${variant === 'compact' ? 'small' : 'large'}
            `}
            onClick={onClick}
        >
            <h3 className="font-bold">{vessel.name}</h3>
            
            <div className="grid grid-cols-2 gap-2 text-sm">
                <p>IMO: {vessel.imo}</p>
                <p>Type: {vessel.vessel_type}</p>
                <p>Flag: {vessel.flag}</p>
                <p>Speed: {vessel.last_speed} knots</p>
            </div>
            
            <div className="mt-3">
                <span className={`
                    px-2 py-1 rounded text-white text-xs
                    ${vessel.status === 'in_transit' ? 'bg-blue-500' : 'bg-green-500'}
                `}>
                    {vessel.status}
                </span>
            </div>
        </div>
    )
}

export default VesselItem
```

#### 4. Container Components (Smart Components)

```javascript
// src/components/vessels/VesselDetailContainer.jsx
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import VesselDetailView from './VesselDetailView'

function VesselDetailContainer() {
    const { id } = useParams()
    const dispatch = useDispatch()
    const vessel = useSelector(state => 
        state.vessels.list.find(v => v.id === parseInt(id))
    )
    const loading = useSelector(state => state.vessels.loading)
    
    useEffect(() => {
        if (!vessel) {
            dispatch(fetchVesselDetail(id))
        }
    }, [id, dispatch, vessel])
    
    if (loading) return <LoadingSpinner />
    if (!vessel) return <p>Vessel not found</p>
    
    return <VesselDetailView vessel={vessel} />
}

export default VesselDetailContainer
```

### Component Hierarchy Example

```
App
├─ Navbar
│  ├─ Logo
│  ├─ Navigation Links
│  └─ UserMenu
│
├─ Sidebar
│  ├─ NavItem
│  ├─ NavItem
│  └─ NavItem
│
├─ Layout
│  └─ MainContent
│     ├─ DashboardPage
│     │  ├─ VesselMapContainer
│     │  │  ├─ Map
│     │  │  └─ MapControls
│     │  │
│     │  └─ PortStatsContainer
│     │     ├─ StatCard
│     │     ├─ StatCard
│     │     └─ CongestionChart
│     │
│     ├─ VesselPage
│     │  ├─ VesselListContainer
│     │  │  ├─ VesselSearch
│     │  │  ├─ VesselItem
│     │  │  ├─ VesselItem
│     │  │  └─ Pagination
│     │  │
│     │  └─ VesselDetailContainer
│     │     └─ VesselDetailView
│     │
│     └─ PortPage
│        └─ ...
│
└─ ErrorBoundary
```

---

## 🔄 STATE MANAGEMENT WITH REDUX

### What is Redux?

Redux is a **predictable state container**:

```
Current State
     ↓
  Action (user clicks "Login")
     ↓
  Reducer (update state based on action)
     ↓
  New State
     ↓
  Components re-render
```

### Redux Store Setup

**File**: `src/redux/store.js`

```javascript
import { configureStore } from '@reduxjs/toolkit'
import authReducer from './slices/authSlice'
import vesselReducer from './slices/vesselSlice'
import portReducer from './slices/portSlice'
import safetyReducer from './slices/safetySlice'
import filtersReducer from './slices/filtersSlice'
import uiReducer from './slices/uiSlice'

// Create store with all reducers
const store = configureStore({
    reducer: {
        auth: authReducer,
        vessels: vesselReducer,
        ports: portReducer,
        safety: safetyReducer,
        filters: filtersReducer,
        ui: uiReducer,
    }
})

export default store
```

### Redux Slices

**File**: `src/redux/slices/authSlice.js`

```javascript
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import authService from '../../services/authService'

// Async action to login
export const loginUser = createAsyncThunk(
    'auth/loginUser',
    async (credentials, { rejectWithValue }) => {
        try {
            const response = await authService.login(
                credentials.username,
                credentials.password
            )
            // Store token in localStorage
            localStorage.setItem('access_token', response.data.access)
            localStorage.setItem('refresh_token', response.data.refresh)
            return response.data
        } catch (error) {
            return rejectWithValue(error.response.data)
        }
    }
)

// Async action to register
export const registerUser = createAsyncThunk(
    'auth/registerUser',
    async (userData, { rejectWithValue }) => {
        try {
            const response = await authService.register(
                userData.username,
                userData.email,
                userData.password
            )
            return response.data
        } catch (error) {
            return rejectWithValue(error.response.data)
        }
    }
)

// Create the slice
const authSlice = createSlice({
    name: 'auth',
    initialState: {
        user: null,
        token: localStorage.getItem('access_token'),
        loading: false,
        error: null,
        isAuthenticated: !!localStorage.getItem('access_token'),
    },
    reducers: {
        logout: (state) => {
            state.user = null
            state.token = null
            state.isAuthenticated = false
            localStorage.removeItem('access_token')
            localStorage.removeItem('refresh_token')
        },
        clearError: (state) => {
            state.error = null
        }
    },
    extraReducers: (builder) => {
        // Handle login
        builder
            .addCase(loginUser.pending, (state) => {
                state.loading = true
                state.error = null
            })
            .addCase(loginUser.fulfilled, (state, action) => {
                state.loading = false
                state.user = action.payload
                state.token = action.payload.access
                state.isAuthenticated = true
            })
            .addCase(loginUser.rejected, (state, action) => {
                state.loading = false
                state.error = action.payload
            })
        
        // Handle register
        builder
            .addCase(registerUser.pending, (state) => {
                state.loading = true
                state.error = null
            })
            .addCase(registerUser.fulfilled, (state, action) => {
                state.loading = false
                // Auto-login after registration
                state.user = action.payload
                state.isAuthenticated = true
            })
            .addCase(registerUser.rejected, (state, action) => {
                state.loading = false
                state.error = action.payload
            })
    }
})

export const { logout, clearError } = authSlice.actions
export default authSlice.reducer
```

**File**: `src/redux/slices/vesselSlice.js`

```javascript
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import vesselService from '../../services/vesselService'

export const fetchVessels = createAsyncThunk(
    'vessels/fetchVessels',
    async (params, { rejectWithValue }) => {
        try {
            const response = await vesselService.getVessels(params)
            return response.data
        } catch (error) {
            return rejectWithValue(error.message)
        }
    }
)

export const fetchVesselDetail = createAsyncThunk(
    'vessels/fetchVesselDetail',
    async (vesselId, { rejectWithValue }) => {
        try {
            const response = await vesselService.getVessel(vesselId)
            return response.data
        } catch (error) {
            return rejectWithValue(error.message)
        }
    }
)

const vesselSlice = createSlice({
    name: 'vessels',
    initialState: {
        list: [],
        detail: null,
        loading: false,
        error: null,
        pagination: {
            page: 1,
            count: 0,
            pageSize: 20,
        }
    },
    reducers: {
        addVessel: (state, action) => {
            state.list.push(action.payload)
        },
        updateVessel: (state, action) => {
            const index = state.list.findIndex(v => v.id === action.payload.id)
            if (index !== -1) {
                state.list[index] = action.payload
            }
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchVessels.pending, (state) => {
                state.loading = true
                state.error = null
            })
            .addCase(fetchVessels.fulfilled, (state, action) => {
                state.loading = false
                state.list = action.payload.results
                state.pagination.count = action.payload.count
            })
            .addCase(fetchVessels.rejected, (state, action) => {
                state.loading = false
                state.error = action.payload
            })
            
            .addCase(fetchVesselDetail.pending, (state) => {
                state.loading = true
            })
            .addCase(fetchVesselDetail.fulfilled, (state, action) => {
                state.loading = false
                state.detail = action.payload
            })
    }
})

export const { addVessel, updateVessel } = vesselSlice.actions
export default vesselSlice.reducer
```

### Using Redux in Components

```javascript
// src/components/vessels/VesselList.jsx
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchVessels } from '../../redux/slices/vesselSlice'

function VesselList() {
    const dispatch = useDispatch()
    
    // Get data from Redux store
    const vessels = useSelector(state => state.vessels.list)
    const loading = useSelector(state => state.vessels.loading)
    const error = useSelector(state => state.vessels.error)
    
    useEffect(() => {
        // Dispatch action to fetch vessels
        dispatch(fetchVessels({ page: 1 }))
    }, [dispatch])
    
    if (loading) return <p>Loading vessels...</p>
    if (error) return <p>Error: {error}</p>
    
    return (
        <div>
            {vessels.map(vessel => (
                <div key={vessel.id}>{vessel.name}</div>
            ))}
        </div>
    )
}

export default VesselList
```

### Redux DevTools

Debug Redux state changes:

```javascript
// Already configured in store.js with Redux Toolkit
// No additional setup needed!

// To use:
// 1. Install Redux DevTools browser extension
// 2. Open browser DevTools (F12)
// 3. Find "Redux" tab
// 4. Watch actions and state changes in real-time
```

---

## 📡 API INTEGRATION & SERVICE LAYER

### Axios Setup

**File**: `src/services/api.js`

```javascript
import axios from 'axios'
import store from '../redux/store'
import { logout } from '../redux/slices/authSlice'

// Create axios instance with base config
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
    timeout: parseInt(import.meta.env.VITE_API_TIMEOUT) || 10000,
})

// Request interceptor - add token to every request
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token')
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => Promise.reject(error)
)

// Response interceptor - handle token expiration
api.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response?.status === 401) {
            // Token expired, logout user
            store.dispatch(logout())
            window.location.href = '/login'
        }
        return Promise.reject(error)
    }
)

export default api
```

### Service Layer Pattern

**File**: `src/services/authService.js`

```javascript
import api from './api'

const authService = {
    // Register new user
    register: async (username, email, password) => {
        return api.post('/auth/register/', {
            username,
            email,
            password,
            password2: password,
        })
    },
    
    // Login user
    login: async (username, password) => {
        return api.post('/auth/token/', {
            username,
            password,
        })
    },
    
    // Refresh access token
    refreshToken: async (refreshToken) => {
        return api.post('/auth/token/refresh/', {
            refresh: refreshToken,
        })
    },
    
    // Get current user profile
    getProfile: async () => {
        return api.get('/auth/profile/me/')
    },
    
    // Update user profile
    updateProfile: async (profileData) => {
        return api.put('/auth/profile/me/', profileData)
    },
    
    // Change password
    changePassword: async (oldPassword, newPassword) => {
        return api.post('/auth/profile/change_password/', {
            old_password: oldPassword,
            new_password: newPassword,
        })
    },
    
    // Logout
    logout: () => {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
    }
}

export default authService
```

**File**: `src/services/vesselService.js`

```javascript
import api from './api'

const vesselService = {
    // Get all vessels
    getVessels: async (params = {}) => {
        return api.get('/vessels/', { params })
    },
    
    // Get single vessel details
    getVessel: async (id) => {
        return api.get(`/vessels/${id}/`)
    },
    
    // Search vessels
    searchVessels: async (query) => {
        return api.get('/vessels/search/', {
            params: { q: query }
        })
    },
    
    // Get vessel position history
    getVesselPositions: async (vesselId, days = 7) => {
        return api.get(`/vessels/${vesselId}/positions/`, {
            params: { days }
        })
    },
    
    // Subscribe to vessel alerts
    subscribeAlert: async (vesselId, alertType) => {
        return api.post(`/vessels/${vesselId}/subscribe/`, {
            alert_type: alertType
        })
    },
    
    // Unsubscribe from vessel alerts
    unsubscribeAlert: async (vesselId, alertType) => {
        return api.post(`/vessels/${vesselId}/unsubscribe/`, {
            alert_type: alertType
        })
    },
}

export default vesselService
```

**File**: `src/services/portService.js`

```javascript
import api from './api'

const portService = {
    // Get all ports
    getPorts: async (params = {}) => {
        return api.get('/ports/', { params })
    },
    
    // Get port details
    getPort: async (id) => {
        return api.get(`/ports/${id}/`)
    },
    
    // Get port congestion history
    getCongestionHistory: async (portId, days = 7) => {
        return api.get(`/ports/${portId}/congestion_history/`, {
            params: { days }
        })
    },
    
    // Get arrivals/departures
    getArrivals: async (portId, days = 30) => {
        return api.get(`/ports/${portId}/arrivals_departures/`, {
            params: { days }
        })
    },
}

export default portService
```

**File**: `src/services/safetyService.js`

```javascript
import api from './api'

const safetyService = {
    // Get weather alerts
    getWeatherAlerts: async () => {
        return api.get('/safety/weather/')
    },
    
    // Get weather alerts near location
    getWeatherNearby: async (lat, lon, range = 100) => {
        return api.get('/safety/weather/nearby/', {
            params: { lat, lon, range }
        })
    },
    
    // Get piracy zones
    getPiracyZones: async () => {
        return api.get('/safety/piracy/')
    },
    
    // Get accident history
    getAccidents: async (params = {}) => {
        return api.get('/safety/accidents/', { params })
    },
}

export default safetyService
```

---

## 🔐 AUTHENTICATION FLOW

### Complete Login Flow

**Step 1**: User enters credentials

```javascript
// src/components/auth/LoginForm.jsx
import { useState } from 'react'
import { useDispatch } from 'react-redux'
import { loginUser } from '../../redux/slices/authSlice'
import { useNavigate } from 'react-router-dom'

function LoginForm() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState('')
    const dispatch = useDispatch()
    const navigate = useNavigate()
    
    const handleSubmit = async (e) => {
        e.preventDefault()
        setError('')
        
        try {
            // Dispatch login action
            const result = await dispatch(loginUser({
                username,
                password
            })).unwrap()
            
            // Success - redirect to dashboard
            navigate('/dashboard')
        } catch (err) {
            // Show error message
            setError(err.username ? err.username[0] : 'Login failed')
        }
    }
    
    return (
        <form onSubmit={handleSubmit} className="space-y-4">
            <div>
                <label htmlFor="username">Username</label>
                <input
                    id="username"
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
            </div>
            
            <div>
                <label htmlFor="password">Password</label>
                <input
                    id="password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </div>
            
            {error && <p className="text-red-500">{error}</p>}
            
            <button type="submit" className="bg-blue-500 text-white px-4 py-2">
                Login
            </button>
        </form>
    )
}

export default LoginForm
```

**Step 2**: Redux handles the request

```javascript
// Redux automatically:
// 1. Dispatches loginUser.pending action
// 2. Calls authService.login(username, password)
// 3. Receives tokens from backend
// 4. Saves tokens to localStorage
// 5. Updates Redux state with user data
// 6. Dispatches loginUser.fulfilled action
```

**Step 3**: Axios adds token to future requests

```javascript
// For every request after login:
// Header automatically includes:
// Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Step 4**: Protected routes check authentication

```javascript
// src/components/PrivateRoute.jsx
import { Navigate } from 'react-router-dom'
import { useSelector } from 'react-redux'

function PrivateRoute({ children }) {
    const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
    
    if (!isAuthenticated) {
        return <Navigate to="/login" replace />
    }
    
    return children
}

export default PrivateRoute

// Usage in routing:
<Route 
    path="/dashboard" 
    element={
        <PrivateRoute>
            <DashboardPage />
        </PrivateRoute>
    } 
/>
```

---

## 🎨 STYLING WITH TAILWIND CSS

### Basic Tailwind Classes

```html
<!-- Spacing -->
<div class="p-4">Padding: 1rem</div>
<div class="m-2">Margin: 0.5rem</div>
<div class="px-2 py-4">Padding X: 0.5rem, Y: 1rem</div>

<!-- Colors -->
<button class="bg-blue-500 text-white">Blue Button</button>
<div class="bg-red-100 border-2 border-red-500">Alert Box</div>

<!-- Typography -->
<h1 class="text-3xl font-bold">Heading 1</h1>
<p class="text-gray-600">Gray text</p>

<!-- Flexbox -->
<div class="flex justify-between items-center">
    <div>Left</div>
    <div>Center</div>
    <div>Right</div>
</div>

<!-- Grid -->
<div class="grid grid-cols-3 gap-4">
    <div>Column 1</div>
    <div>Column 2</div>
    <div>Column 3</div>
</div>

<!-- Responsive -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
    <!-- 1 column on mobile, 2 on tablet, 3 on desktop -->
</div>

<!-- Hover Effects -->
<button class="bg-blue-500 hover:bg-blue-700 transition">
    Hover me
</button>
```

### Common Component Patterns

```javascript
// Button Component
function Button({ 
    children, 
    variant = 'primary', 
    size = 'md', 
    onClick,
    disabled = false 
}) {
    const baseClasses = 'font-semibold rounded transition'
    
    const sizeClasses = {
        sm: 'px-2 py-1 text-sm',
        md: 'px-4 py-2 text-base',
        lg: 'px-6 py-3 text-lg',
    }
    
    const variantClasses = {
        primary: 'bg-blue-500 text-white hover:bg-blue-700',
        secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
        danger: 'bg-red-500 text-white hover:bg-red-700',
    }
    
    const disabledClasses = disabled ? 'opacity-50 cursor-not-allowed' : ''
    
    return (
        <button
            className={`
                ${baseClasses}
                ${sizeClasses[size]}
                ${variantClasses[variant]}
                ${disabledClasses}
            `}
            onClick={onClick}
            disabled={disabled}
        >
            {children}
        </button>
    )
}

// Card Component
function Card({ title, children, className = '' }) {
    return (
        <div className={`
            bg-white rounded-lg shadow-md p-4
            ${className}
        `}>
            {title && <h3 className="font-bold mb-3">{title}</h3>}
            {children}
        </div>
    )
}

// Modal Component
function Modal({ isOpen, onClose, title, children }) {
    if (!isOpen) return null
    
    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <div className="bg-white rounded-lg p-6 max-w-md w-full">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-bold">{title}</h2>
                    <button onClick={onClose} className="text-gray-500">✕</button>
                </div>
                {children}
            </div>
        </div>
    )
}
```

---

## 🧪 TESTING STRATEGIES

### Unit Tests with Vitest

**File**: `src/components/vessels/VesselItem.test.jsx`

```javascript
import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import VesselItem from './VesselItem'

describe('VesselItem Component', () => {
    const mockVessel = {
        id: 1,
        name: 'MAERSK',
        imo: 9123456,
        vessel_type: 'Container Ship',
        status: 'in_transit'
    }
    
    it('renders vessel name', () => {
        render(<VesselItem vessel={mockVessel} />)
        expect(screen.getByText('MAERSK')).toBeInTheDocument()
    })
    
    it('displays vessel IMO', () => {
        render(<VesselItem vessel={mockVessel} />)
        expect(screen.getByText(/IMO: 9123456/)).toBeInTheDocument()
    })
    
    it('shows correct status badge', () => {
        render(<VesselItem vessel={mockVessel} />)
        expect(screen.getByText('in_transit')).toBeInTheDocument()
    })
    
    it('calls onClick when clicked', () => {
        const handleClick = vitest.fn()
        render(<VesselItem vessel={mockVessel} onClick={handleClick} />)
        
        screen.getByRole('button').click()
        expect(handleClick).toHaveBeenCalled()
    })
})
```

### Integration Tests

```javascript
// tests/auth.integration.test.js
import { describe, it, expect, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import { Provider } from 'react-redux'
import store from '../src/redux/store'
import LoginForm from '../src/components/auth/LoginForm'

describe('Login Flow', () => {
    it('logs in user successfully', async () => {
        render(
            <Provider store={store}>
                <LoginForm />
            </Provider>
        )
        
        // Fill in login form
        fireEvent.change(screen.getByLabelText('Username'), {
            target: { value: 'testuser' }
        })
        fireEvent.change(screen.getByLabelText('Password'), {
            target: { value: 'testpass123' }
        })
        
        // Submit form
        fireEvent.click(screen.getByText('Login'))
        
        // Wait for success
        await waitFor(() => {
            expect(store.getState().auth.isAuthenticated).toBe(true)
        })
    })
})
```

### Running Tests

```bash
# Install test dependencies
npm install -D vitest @testing-library/react @testing-library/jest-dom

# Run tests
npm run test

# Run tests in watch mode
npm run test:watch

# Generate coverage report
npm run test:coverage
```

---

## ⚡ PERFORMANCE OPTIMIZATION

### Code Splitting

```javascript
// src/App.jsx
import { lazy, Suspense } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import LoadingSpinner from './components/LoadingSpinner'

// Lazy load pages (loaded only when needed)
const DashboardPage = lazy(() => import('./pages/DashboardPage'))
const VesselPage = lazy(() => import('./pages/VesselPage'))
const PortPage = lazy(() => import('./pages/PortPage'))

function App() {
    return (
        <BrowserRouter>
            <Suspense fallback={<LoadingSpinner />}>
                <Routes>
                    <Route path="/dashboard" element={<DashboardPage />} />
                    <Route path="/vessels" element={<VesselPage />} />
                    <Route path="/ports" element={<PortPage />} />
                </Routes>
            </Suspense>
        </BrowserRouter>
    )
}

export default App
```

### Memoization

```javascript
import { memo, useMemo, useCallback } from 'react'

// Prevent unnecessary re-renders
const VesselItem = memo(function VesselItem({ vessel, onSelect }) {
    return (
        <div onClick={() => onSelect(vessel)}>
            {vessel.name}
        </div>
    )
})

// Memoize expensive computations
function VesselList({ vessels }) {
    const sortedVessels = useMemo(() => {
        // Expensive sorting
        return [...vessels].sort((a, b) => a.name.localeCompare(b.name))
    }, [vessels])
    
    // Memoize callback to prevent child re-renders
    const handleSelect = useCallback((vessel) => {
        console.log('Selected:', vessel)
    }, [])
    
    return (
        <div>
            {sortedVessels.map(vessel => (
                <VesselItem 
                    key={vessel.id} 
                    vessel={vessel}
                    onSelect={handleSelect}
                />
            ))}
        </div>
    )
}
```

### Pagination & Virtual Lists

```javascript
// Load only visible items
import { FixedSizeList } from 'react-window'

function LargeVesselList({ vessels }) {
    return (
        <FixedSizeList
            height={600}
            itemCount={vessels.length}
            itemSize={50}
            width="100%"
        >
            {({ index, style }) => (
                <div style={style}>
                    {vessels[index].name}
                </div>
            )}
        </FixedSizeList>
    )
}
```

---

## 🚀 DEPLOYMENT GUIDE

### Build for Production

```bash
# Create optimized production build
npm run build

# Output in dist/ folder - files are minified and optimized
# dist/
# ├── index.html
# ├── assets/
# │   ├── main-abc123.js
# │   ├── main-def456.css
# │   └── vendor-ghi789.js
```

### Deploy to Netlify

```bash
# 1. Install Netlify CLI
npm install -g netlify-cli

# 2. Build project
npm run build

# 3. Deploy
netlify deploy --prod --dir=dist

# That's it! Your app is live!
```

### Deploy to Vercel

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Deploy (Vercel detects Vite automatically)
vercel --prod

# Follow prompts and your app is deployed!
```

### Deploy to GitHub Pages

```bash
# 1. Update vite.config.js
export default {
  base: '/Maritime_Vessel_Tracking/',
  ...
}

# 2. Build and deploy
npm run build
npx gh-pages -d dist
```

### Deploy with Docker

**Dockerfile**:

```dockerfile
# Build stage
FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
RUN npm install -g serve
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]
```

```bash
# Build image
docker build -t maritime-frontend .

# Run container
docker run -p 3000:3000 maritime-frontend
```

---

## ❌ TROUBLESHOOTING & COMMON ISSUES

### Issue 1: "Module not found"

```bash
# Error: Cannot find module 'react'

# Solution: Install dependencies
npm install

# Or install specific package
npm install react
```

### Issue 2: API CORS Error

```
Access to XMLHttpRequest at 'http://localhost:8000/api/...'
from origin 'http://localhost:3000' has been blocked by CORS policy
```

**Solution**: Check backend CORS settings

```python
# backend/settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
]
```

Or use Vite proxy in development:

```javascript
// vite.config.js
export default {
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
}
```

### Issue 3: Redux State Not Updating

```javascript
// Check if reducer properly handles action:

// ❌ Wrong - modifying state directly
state.user = action.payload  // Don't modify!

// ✅ Correct - Redux Toolkit uses Immer (handles copies)
state.user = action.payload  // Redux Toolkit makes copy automatically

// Or if using vanilla Redux:
return {
    ...state,
    user: action.payload
}
```

### Issue 4: VITE_API_URL Not Working

```bash
# Environment variables must start with VITE_
VITE_API_URL=http://localhost:8000/api  ✅

# Won't work (not visible to frontend):
API_URL=http://localhost:8000/api  ❌

# Access in code:
import.meta.env.VITE_API_URL
```

### Issue 5: Token Expired

```javascript
// Already handled by Axios interceptor:
api.interceptors.response.use(
    response => response,
    error => {
        if (error.response?.status === 401) {
            // Automatically logout and redirect
            store.dispatch(logout())
            window.location.href = '/login'
        }
    }
)
```

### Issue 6: Components Not Re-rendering

```javascript
// Possible causes:

// 1. Keys in lists
{items.map((item, index) => (
    <div key={index}>  // ❌ Don't use index!
        {item.name}
    </div>
))}

// 2. State not updating properly
setState(prev => ({ ...prev, field: value }))  // ✅ Use updater function

// 3. Redux selector not memoized
const data = useSelector(state => state.items.filter(...))  // ❌ Creates new array
const data = useSelector(state => state.items)  // ✅ Returns same reference
```

### Debugging Tips

```javascript
// 1. Console logging
console.log('User state:', user)
console.log('Vessels:', vessels)

// 2. React DevTools
// Browser Extension shows component tree and props

// 3. Redux DevTools
// Shows all actions and state changes

// 4. Network tab (F12)
// See all API requests and responses

// 5. Local storage
localStorage.getItem('access_token')  // Check if token is saved

// 6. Check token format
const token = localStorage.getItem('access_token')
const decoded = JSON.parse(atob(token.split('.')[1]))
console.log(decoded)  // See token contents
```

---

## 📚 ADDITIONAL RESOURCES

### Official Documentation
- React: https://react.dev
- Vite: https://vitejs.dev
- Redux: https://redux.js.org
- Tailwind CSS: https://tailwindcss.com
- React Router: https://reactrouter.com

### Useful Libraries
```bash
# State management alternatives
npm install zustand                 # Lighter Redux alternative
npm install jotai                   # Atomic state management

# Form handling
npm install react-hook-form         # Lightweight form library
npm install formik                  # Heavier but feature-rich

# Maps
npm install mapbox-gl               # Advanced mapping
npm install google-maps-react       # Google Maps integration

# WebSockets
npm install socket.io-client        # Real-time communication

# Data fetching
npm install react-query             # Advanced caching and fetching
npm install swr                     # Simple fetching with cache
```

### Best Practices Checklist

```
✅ Component Structure:
   └─ One component per file
   └─ Use functional components with hooks
   └─ Keep components small and focused
   └─ Props validation with PropTypes or TypeScript

✅ State Management:
   └─ Use Redux for global state
   └─ Use useState for local component state
   └─ Avoid prop drilling (passing through multiple levels)
   └─ Memoize expensive selectors

✅ Performance:
   └─ Code split with lazy loading
   └─ Memoize components when needed
   └─ Optimize images and assets
   └─ Use virtual lists for large datasets

✅ Styling:
   └─ Use Tailwind for consistent styling
   └─ Avoid inline styles
   └─ Create reusable component classes
   └─ Keep color palette consistent

✅ Testing:
   └─ Test business logic
   └─ Test user interactions
   └─ Test error states
   └─ Aim for 70%+ coverage

✅ Security:
   └─ Never hardcode API keys/secrets
   └─ Use HTTPS in production
   └─ Validate user input
   └─ Store tokens securely

✅ Accessibility:
   └─ Add alt text to images
   └─ Use semantic HTML
   └─ Support keyboard navigation
   └─ Test with screen readers

✅ Code Quality:
   └─ Use ESLint for code style
   └─ Format with Prettier
   └─ Remove console.log in production
   └─ Handle errors gracefully
```

---

## 📋 QUICK START SUMMARY

### From Zero to Running

```bash
# 1. Install Node.js (https://nodejs.org/)

# 2. Create React app with Vite
npm create vite@latest maritime-frontend -- --template react
cd maritime-frontend

# 3. Install dependencies
npm install
npm install react-router-dom @reduxjs/toolkit react-redux axios leaflet recharts
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# 4. Create .env file
echo "VITE_API_URL=http://localhost:8000/api" > .env

# 5. Start development server
npm run dev

# 6. Open browser
# http://localhost:3000
```

### Folder Structure Quick Setup

```bash
# Create folder structure
mkdir -p src/{components,pages,redux/slices,services,hooks,utils,assets}

# Key files to create:
# src/redux/store.js
# src/redux/slices/auth.js
# src/services/api.js
# src/pages/LoginPage.jsx
# src/pages/DashboardPage.jsx
```

---

**Last Updated**: February 2026  
**Frontend Version**: 1.0.0  
**Framework**: React 18 + Vite  
**Styling**: Tailwind CSS  
**State Management**: Redux Toolkit

