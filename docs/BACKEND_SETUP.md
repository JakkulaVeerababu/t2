# Maritime Vessel Tracking Platform - Complete Backend Documentation
## Comprehensive Guide for Backend Development

---

## 📑 TABLE OF CONTENTS

1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Prerequisites & Requirements](#prerequisites--requirements)
4. [Complete Installation Guide](#complete-installation-guide)
5. [Project Structure & Architecture](#project-structure--architecture)
6. [Database Models - Complete Reference](#database-models---complete-reference)
7. [App Modules - Detailed Breakdown](#app-modules---detailed-breakdown)
8. [API Endpoints Documentation](#api-endpoints-documentation)
9. [Authentication & Authorization](#authentication--authorization)
10. [External API Integration](#external-api-integration)
11. [Development Workflow](#development-workflow)
12. [Testing & Quality Assurance](#testing--quality-assurance)
13. [Deployment Guide](#deployment-guide)
14. [Troubleshooting & Common Issues](#troubleshooting--common-issues)

---

## 📌 PROJECT OVERVIEW

### What is This Project?

The Maritime Vessel Tracking Platform is a comprehensive web application designed to:

- **Track vessels in real-time** across global maritime routes
- **Monitor port congestion** and provide analytics
- **Overlay safety information** including weather alerts, piracy zones, and accident history
- **Maintain historical voyage data** for audit and compliance tracking
- **Provide role-based dashboards** for operators, analysts, and administrators

### Backend Responsibilities

The backend serves as the central "brain" of the application:

```
┌─────────────────────────────────────────────────────────────┐
│                       FRONTEND (React)                       │
│                   (What users see & interact with)           │
└────────────────────────────┬────────────────────────────────┘
                             │
                    HTTP/REST API Calls
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              BACKEND (Django REST Framework)                 │
│                                                              │
│  • Processes requests from frontend                         │
│  • Validates data                                           │
│  • Calls external APIs (MarineTraffic, NOAA, UNCTAD)       │
│  • Manages business logic                                   │
│  • Returns JSON responses                                   │
└────────────────────────────┬────────────────────────────────┘
                             │
        Reads/Writes Data
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              DATABASE (SQLite/PostgreSQL)                    │
│              (Where all data is stored)                      │
└─────────────────────────────────────────────────────────────┘
```

### Key Features the Backend Provides

| Feature | Description |
|---------|-------------|
| **User Authentication** | Secure login with JWT tokens |
| **Vessel Tracking** | Real-time position updates from AIS data |
| **Port Analytics** | Congestion metrics and statistics |
| **Safety Overlays** | Weather alerts, piracy zones, accident data |
| **Historical Data** | Complete voyage history and audit trails |
| **Role-Based Access** | Different permissions for operators, analysts, admins |
| **Real-time Notifications** | WebSocket support for instant updates |
| **API Integration** | Connects with external maritime data providers |

---

## 🛠️ TECHNOLOGY STACK

### Core Framework: Django 4.2+

**Django** is a Python web framework that handles:
- URL routing (mapping URLs to functions)
- Database management (ORM - Object-Relational Mapping)
- User authentication
- Admin interface
- Security features

```bash
# What it is:
Python web framework providing structure and tools for building web apps

# Key benefits:
✓ Comes with authentication system
✓ Built-in admin interface for data management
✓ Excellent ORM for database queries
✓ Strong security (CSRF, XSS protection)
✓ Comprehensive documentation and large community
```

### Django REST Framework (DRF) 3.14+

**DRF** extends Django to build robust APIs:

```python
# Example: Converting Python objects to JSON automatically
Vessel object in Python:
{
    id: 1,
    name: "MAERSK",
    imo: 9123456,
    mmsi: 211378120,
    type: "Container Ship"
}

↓ DRF Serializer converts to JSON ↓

REST API Response:
{
    "id": 1,
    "name": "MAERSK",
    "imo": 9123456,
    "mmsi": 211378120,
    "type": "Container Ship"
}
```

**Key capabilities:**
- Automatic serialization/deserialization
- Built-in pagination
- Permissions and authentication
- API documentation generation
- Support for nested relationships

### JWT Authentication (djangorestframework-simplejwt)

**JWT (JSON Web Token)** is a secure way to authenticate users:

```
1. User logs in with username/password
                    ↓
2. Backend creates JWT token (like a session key)
                    ↓
3. Frontend stores token in localStorage
                    ↓
4. Frontend sends token with every request
   Header: Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
                    ↓
5. Backend verifies token is valid and hasn't expired
                    ↓
6. Request is processed or rejected
```

**Advantages:**
- Stateless (no session storage on server)
- Mobile-friendly
- Scalable for distributed systems
- Can be used across multiple domains

### Database: SQLite (Dev) → PostgreSQL (Production)

#### SQLite (Development)
```
What: Lightweight, file-based database
Stored as: Single db.sqlite3 file
Setup: Zero configuration needed
Perfect for: Testing and development
```

#### PostgreSQL (Production)
```
What: Enterprise-grade database server
Stored as: Data on server (need to install database software)
Setup: Requires configuration and username/password
Perfect for: Production with multiple concurrent users
```

### Other Essential Libraries

```python
python-dotenv          # Load environment variables from .env file
requests               # Make HTTP requests to external APIs
pandas                 # Data analysis and manipulation
celery                 # Task queue for background jobs (async tasks)
psycopg2-binary        # PostgreSQL adapter for Python
django-cors-headers    # Allow frontend to call backend API
drf-spectacular        # Auto-generate API documentation
```

---

## ✅ PREREQUISITES & REQUIREMENTS

### System Requirements

| Component | Version | Why Needed |
|-----------|---------|-----------|
| Python | 3.10+ | Backend programming language |
| pip | Latest | Package manager for Python |
| Git | Latest | Version control |
| PostgreSQL | 13+ | Production database (optional for dev) |

### Knowledge Prerequisites

Before starting, you should be comfortable with:
- Basic Python programming (variables, functions, classes)
- HTTP concepts (GET, POST, PUT, DELETE requests)
- JSON format
- Command line/terminal usage
- Basic database concepts (tables, rows, columns)

### Required Accounts

```
✓ GitHub - for version control
✓ MarineTraffic - for API key (vessel tracking)
✓ NOAA - for API key (weather data)
✓ UNCTAD - for API key (port data)
✓ AIS Hub - for API key (AIS data)
```

---

## 📦 COMPLETE INSTALLATION GUIDE

### Step 1: Verify Python Installation

```bash
# Check if Python is installed
python --version

# Should show: Python 3.10.x or higher
# If not, download from https://www.python.org/downloads/

# Check pip
pip --version

# Should show: pip x.x.x
```

### Step 2: Clone Repository

```bash
# Create a folder for your project
mkdir maritime_projects
cd maritime_projects

# Clone the repository (if exists, otherwise create new project)
git clone <repository-url>
cd Maritime_Vessel_Tracking/backend

# Or create new Django project from scratch:
# django-admin startproject core .
```

### Step 3: Create Virtual Environment

**Why virtual environment?**
- Isolates project dependencies
- Different projects can use different versions
- Prevents conflicts between projects

```bash
# Create virtual environment
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# You should see (venv) at the start of your terminal:
# (venv) C:\Maritime_Vessel_Tracking\backend>
```

### Step 4: Install Dependencies

```bash
# First, upgrade pip to latest version
pip install --upgrade pip

# Install from requirements.txt
pip install -r requirements.txt

# Or install manually (if requirements.txt doesn't exist):
pip install Django==4.2.0
pip install djangorestframework==3.14.0
pip install djangorestframework-simplejwt==5.2.2
pip install python-dotenv==1.0.0
pip install requests==2.31.0
pip install pandas==2.0.0
pip install celery==5.3.0
pip install psycopg2-binary==2.9.0
pip install django-cors-headers==4.2.0
pip install drf-spectacular==0.26.0
pip install pytest==7.4.0
pip install pytest-django==4.7.0
```

### Step 5: Create Environment Configuration

Create `.env` file in project root (same directory as manage.py):

```env
# ============ DJANGO SETTINGS ============
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# ============ DATABASE SETTINGS ============
# For Development (SQLite):
DATABASE_URL=sqlite:///db.sqlite3

# For Production (PostgreSQL) - Uncomment and modify:
# DATABASE_URL=postgresql://maritime_user:password@localhost:5432/maritime_db

# ============ JWT CONFIGURATION ============
JWT_SECRET_KEY=your-jwt-secret-key-change-this
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=1
REFRESH_TOKEN_EXPIRATION_DAYS=7

# ============ EXTERNAL API KEYS ============
# Get these from respective provider websites
MARINETRAFFIC_API_KEY=your-marinetraffic-api-key
AIS_HUB_API_KEY=your-aishub-api-key
NOAA_API_KEY=your-noaa-api-key
UNCTAD_API_KEY=your-unctad-api-key

# ============ EMAIL CONFIGURATION ============
# For sending notifications and password reset
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
DEFAULT_FROM_EMAIL=your-email@gmail.com

# ============ CORS SETTINGS ============
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

# ============ REDIS SETTINGS (for Celery) ============
# Uncomment if using Celery for background tasks
# CELERY_BROKER_URL=redis://localhost:6379/0
# CELERY_RESULT_BACKEND=redis://localhost:6379/0

# ============ LOGGING ============
LOG_LEVEL=INFO
```

### Step 6: Configure Django Settings

Edit `core/settings.py` and add/modify:

```python
import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# ============ SECURITY ============
DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# ============ INSTALLED APPLICATIONS ============
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_spectacular',
    
    # Your custom apps
    'apps.authentication',      # User management
    'apps.vessels',             # Vessel tracking
    'apps.ports',               # Port analytics
    'apps.safety',              # Safety overlays
    'apps.voyages',             # Voyage history
    'apps.notifications',       # Event notifications
    'apps.admin_tools',         # Admin management
]

# ============ MIDDLEWARE ============
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',        # CORS support
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ============ DATABASE ============
if 'postgresql' in os.getenv('DATABASE_URL', ''):
    # PostgreSQL configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DATABASE_NAME', 'maritime_db'),
            'USER': os.getenv('DATABASE_USER', 'maritime_user'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD', ''),
            'HOST': os.getenv('DATABASE_HOST', 'localhost'),
            'PORT': os.getenv('DATABASE_PORT', '5432'),
        }
    }
else:
    # SQLite configuration (default for development)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ============ REST FRAMEWORK CONFIGURATION ============
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# ============ SIMPLE JWT CONFIGURATION ============
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=int(os.getenv('JWT_EXPIRATION_HOURS', 1))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.getenv('REFRESH_TOKEN_EXPIRATION_DAYS', 7))),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ============ CORS CONFIGURATION ============
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')

# ============ STATIC & MEDIA FILES ============
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ============ LOGGING ============
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': os.getenv('LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
```

### Step 7: Run Migrations

```bash
# Create migration files from models
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Check migration status
python manage.py showmigrations

# You should see all migrations marked as [X] (applied)
```

### Step 8: Create Superuser (Admin)

```bash
# Create admin account
python manage.py createsuperuser

# Follow prompts:
# Username: admin
# Email: admin@example.com
# Password: (enter secure password)
# Password (again): (confirm)
```

### Step 9: Start Development Server

```bash
# Run the development server
python manage.py runserver

# Server runs at: http://localhost:8000

# Access Django Admin at: http://localhost:8000/admin/
# Login with superuser credentials created above

# API will be accessible at: http://localhost:8000/api/
```

---

## 🏗️ PROJECT STRUCTURE & ARCHITECTURE

### Complete Directory Layout

```
backend/
│
├── manage.py                              # Main Django management tool
├── requirements.txt                       # Python dependencies
├── .env                                   # Environment variables (NEVER commit!)
├── .gitignore                             # Files to ignore in Git
│
├── core/                                  # Main Django configuration
│   ├── __init__.py
│   ├── settings.py                       # Django settings and configuration
│   ├── urls.py                           # Main URL routing
│   ├── asgi.py                           # ASGI configuration (WebSockets)
│   ├── wsgi.py                           # WSGI configuration (deployment)
│   └── celery.py                         # Celery configuration (optional)
│
├── apps/                                  # Custom Django applications
│   │
│   ├── authentication/                   # ★ User authentication module
│   │   ├── __init__.py
│   │   ├── models.py                     # User and UserProfile models
│   │   ├── serializers.py                # Convert objects to/from JSON
│   │   ├── views.py                      # API endpoints for auth
│   │   ├── urls.py                       # URL routing for auth endpoints
│   │   ├── permissions.py                # Custom permission classes
│   │   ├── authentication.py             # Custom authentication logic
│   │   ├── tests.py                      # Unit tests
│   │   └── migrations/                   # Database migration files
│   │
│   ├── vessels/                          # ★ Vessel tracking module
│   │   ├── __init__.py
│   │   ├── models.py                     # Vessel, Position, Route, Alert models
│   │   ├── serializers.py                # Serialize vessel data
│   │   ├── views.py                      # ViewSets for vessel operations
│   │   ├── urls.py                       # Vessel API endpoints
│   │   ├── filters.py                    # Custom filtering logic
│   │   ├── tasks.py                      # Celery tasks for async operations
│   │   ├── tests.py                      # Unit tests
│   │   └── migrations/                   # Database migrations
│   │
│   ├── ports/                            # ★ Port analytics module
│   │   ├── __init__.py
│   │   ├── models.py                     # Port, Statistics, Congestion models
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── analytics.py                  # Port analytics calculations
│   │   ├── tests.py
│   │   └── migrations/
│   │
│   ├── safety/                           # ★ Safety overlays module
│   │   ├── __init__.py
│   │   ├── models.py                     # SafetyEvent, WeatherAlert, PiracyZone
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── tests.py
│   │   └── migrations/
│   │
│   ├── voyages/                          # ★ Voyage history module
│   │   ├── __init__.py
│   │   ├── models.py                     # Voyage, VoyageHistory, Compliance
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── tests.py
│   │   └── migrations/
│   │
│   ├── notifications/                    # Event notifications
│   │   ├── __init__.py
│   │   ├── models.py                     # Notification model
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── tasks.py                      # Email/SMS sending tasks
│   │   ├── tests.py
│   │   └── migrations/
│   │
│   └── admin_tools/                      # Admin management
│       ├── __init__.py
│       ├── models.py                     # APIStatus, SystemLog
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── migrations/
│
├── integrations/                          # External API clients
│   ├── __init__.py
│   ├── base.py                           # Base API client class
│   ├── marinetraffic.py                  # MarineTraffic API wrapper
│   ├── aishub.py                         # AIS Hub API wrapper
│   ├── noaa.py                           # NOAA weather API wrapper
│   └── unctad.py                         # UNCTAD port data API wrapper
│
├── utils/                                 # Shared utilities
│   ├── __init__.py
│   ├── decorators.py                     # Custom decorators
│   ├── permissions.py                    # Custom permission classes
│   ├── validators.py                     # Data validators
│   ├── serializers.py                    # Common serializers
│   ├── helpers.py                        # Helper functions
│   └── exceptions.py                     # Custom exceptions
│
├── static/                                # Static files (CSS, JS, images)
│   └── admin/                             # Admin customization
│
├── media/                                 # User uploads (documents, images)
│   ├── avatars/
│   ├── documents/
│   └── exports/
│
├── fixtures/                              # Sample data for testing
│   ├── users.json
│   ├── vessels.json
│   ├── ports.json
│   └── safety_zones.json
│
├── logs/                                  # Application logs
│   ├── debug.log
│   └── error.log
│
├── tests/                                 # Integration tests
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_models.py
│   └── test_integrations.py
│
├── docs/                                  # Documentation
│   ├── API.md                             # API documentation
│   ├── DATABASE.md                        # Database schema
│   ├── DEPLOYMENT.md                      # Deployment guide
│   └── ARCHITECTURE.md                    # Architecture diagrams
│
└── docker/                                # Docker configuration
    ├── Dockerfile
    ├── docker-compose.yml
    └── nginx.conf
```

---

## 🗄️ DATABASE MODELS - COMPLETE REFERENCE

### Model 1: User Authentication

```python
# apps/authentication/models.py

class User (Django Built-in)
Fields:
├── id: AutoField (primary key)
├── username: CharField(150, unique=True)
├── email: EmailField(unique=True)
├── password_hash: CharField(255)  [automatically hashed by Django]
├── first_name: CharField(150)
├── last_name: CharField(150)
├── is_active: BooleanField(default=True)
├── is_staff: BooleanField(default=False)
├── is_superuser: BooleanField(default=False)
├── last_login: DateTimeField(null=True)
├── date_joined: DateTimeField(auto_now_add=True)
└── updated_at: DateTimeField(auto_now=True)

Methods:
├── set_password(password) → Hashes password for storage
├── check_password(password) → Verifies password during login
└── get_full_name() → Returns "First Last"


class UserProfile
Foreign Key: user (1-1 relationship with User)

Fields:
├── id: AutoField (primary key)
├── user: OneToOneField → links to User
├── role: CharField(choices: 'operator', 'analyst', 'admin')
├── company: CharField(255, optional)
├── phone_number: CharField(20, optional)
├── avatar: ImageField(optional)
├── is_email_verified: BooleanField(default=False)
├── created_at: DateTimeField(auto_now_add=True)
├── updated_at: DateTimeField(auto_now=True)
└── last_login_ip: GenericIPAddressField(optional)

Methods:
├── has_permission(permission) → Check if user can do action
├── get_full_name() → Return user's full name
└── __str__ → Return "username (role)"
```

### Model 2: Vessel Management

```python
class Vessel
Represents a ship

Fields:
├── id: AutoField (primary key)
├── imo: IntegerField(unique=True)         [International Maritime Org number]
├── mmsi: BigIntegerField(unique=True)    [AIS identifier]
├── name: CharField(255)                   [Ship name]
├── vessel_type: CharField(50, choices)    ['container', 'tanker', 'bulk', etc.]
├── flag: CharField(3)                     [Country code: 'US', 'BR', 'CH']
├── status: CharField(50, choices)         ['in_transit', 'in_port', 'anchored']
├── owner: CharField(255, optional)
├── operator: CharField(255, optional)
├── year_built: IntegerField(optional)
├── length: DecimalField(8,2, optional)   [meters]
├── beam: DecimalField(8,2, optional)     [width in meters]
├── draft: DecimalField(8,2, optional)    [depth in meters]
├── last_position_lat: DecimalField(10,8)
├── last_position_lon: DecimalField(11,8)
├── last_speed: DecimalField(5,2)         [knots]
├── last_heading: DecimalField(5,2)       [degrees 0-360]
├── last_position_update: DateTimeField(optional)
├── external_api_source: CharField(['marinetraffic', 'aishub'])
├── external_id: CharField(optional)      [ID in external system]
├── created_at: DateTimeField(auto_now_add=True)
└── updated_at: DateTimeField(auto_now=True)

Methods:
├── is_recent() → Check if position data < 1 hour old
├── get_distance_to(lat, lon) → Calculate distance (km)
├── __str__ → Return "MAERSK (IMO: 9123456)"
└── to_dict() → Convert to dictionary


class VesselPosition
Stores position history

Fields:
├── id: AutoField (primary key)
├── vessel: ForeignKey → links to Vessel
├── latitude: DecimalField(10,8)
├── longitude: DecimalField(11,8)
├── speed: DecimalField(5,2, optional)   [knots]
├── heading: DecimalField(5,2, optional) [degrees]
├── timestamp: DateTimeField()           [when position was recorded]
├── recorded_at: DateTimeField(auto_now_add=True)
└── created_at: DateTimeField(auto_now_add=True)

Indexes:
└── (vessel_id, -timestamp) → For fast time-based queries

Use Cases:
├── Get last 100 positions for vessel
├── Plot historical route on map
├── Calculate speed changes
└── Analyze voyage patterns


class VesselRoute
Current/planned voyage route

Fields:
├── id: AutoField (primary key)
├── vessel: OneToOneField → current route for vessel
├── origin_port: CharField(255)
├── destination_port: CharField(255)
├── departure_time: DateTimeField(optional)
├── eta: DateTimeField(optional)        [estimated arrival]
├── expected_duration: DecimalField(optional) [hours]
├── status: CharField(choices: 'active', 'completed', 'cancelled')
├── created_at: DateTimeField(auto_now_add=True)
└── updated_at: DateTimeField(auto_now=True)

Methods:
├── is_active() → Check if route is in progress
├── days_remaining() → Calculate how many days until arrival
└── __str__ → "MAERSK: Shanghai → Rotterdam"


class VesselAlert
User subscription to vessel events

Fields:
├── id: AutoField (primary key)
├── vessel: ForeignKey → which vessel
├── user: ForeignKey → which user
├── alert_type: CharField (choices:
│   ├── 'position_change'
│   ├── 'port_arrival'
│   ├── 'port_departure'
│   ├── 'speed_change'
│   ├── 'heading_change'
│   └── 'status_change'
├── is_active: BooleanField(default=True)
├── created_at: DateTimeField(auto_now_add=True)
└── unique_together → (vessel, user, alert_type)

Use:
├── User says "Notify me if MAERSK changes position"
├── System sends email/push when position changes
└── User can manage which alerts are active
```

### Model 3: Port Management

```python
class Port
Represents a seaport

Fields:
├── id: AutoField (primary key)
├── name: CharField(255, unique=True)
├── unlocode: CharField(5, unique=True)  [UN/LOCODE like 'JPTYO']
├── city: CharField(255)
├── country: CharField(100)
├── latitude: DecimalField(10,8)
├── longitude: DecimalField(11,8)
├── port_type: CharField (choices:
│   ├── 'container'
│   ├── 'bulk_cargo'
│   ├── 'general_cargo'
│   ├── 'oil_lng'
│   └── 'multipurpose'
├── number_of_berths: IntegerField(default=0)
├── average_depth: DecimalField(5,2, optional)
├── annual_container_capacity: IntegerField         [TEU units]
├── annual_cargo_capacity: IntegerField            [tons]
├── operating_hours: CharField(optional)            [e.g., "24/7"]
├── created_at: DateTimeField(auto_now_add=True)
└── updated_at: DateTimeField(auto_now=True)

Methods:
├── get_current_congestion() → Current congestion %
├── get_avg_wait_time() → Average wait in hours
├── get_arrivals_today() → Vessels arriving today
└── __str__ → "Tokyo Port, Japan"


class PortStatistics
Aggregated statistics for port

Fields:
├── id: AutoField (primary key)
├── port: OneToOneField → unique statistics per port
├── total_arrivals: IntegerField(default=0)
├── total_departures: IntegerField(default=0)
├── current_vessels: IntegerField(default=0)
├── average_wait_time: DecimalField              [hours]
├── average_berth_time: DecimalField             [hours]
├── occupied_berths: IntegerField(default=0)
├── free_berths: IntegerField(default=0)
├── congestion_level: CharField (choices:
│   ├── 'low'      (< 30%)
│   ├── 'medium'   (30-60%)
│   ├── 'high'     (60-85%)
│   └── 'critical' (> 85%)
├── efficiency_score: DecimalField(0-100)
└── last_updated: DateTimeField(auto_now=True)

Use:
├── Display port status on dashboard
├── Show congestion alerts
├── Historical comparison
└── Optimize port operations


class CongestionMetric
Historical congestion data (time-series)

Fields:
├── id: AutoField (primary key)
├── port: ForeignKey → which port
├── congestion_percentage: DecimalField(0-100)
├── queue_length: IntegerField              [vessels waiting]
├── estimated_wait_time: DecimalField       [hours]
├── berths_available: IntegerField
├── berths_occupied: IntegerField
├── timestamp: DateTimeField()              [when recorded]
├── recorded_at: DateTimeField(auto_now_add=True)
└── index → (port_id, -timestamp) for fast queries

Use:
├── Track congestion over time
├── Generate congestion graphs
├── Forecast future congestion
└── Identify peak hours


class ArrivalDeparture
Records of ship arrivals/departures

Fields:
├── id: AutoField (primary key)
├── vessel: ForeignKey → which ship
├── port: ForeignKey → which port
├── arrival_time: DateTimeField()
├── departure_time: DateTimeField(optional)
├── berth_number: CharField(optional)
├── cargo_loaded: DecimalField              [tons]
├── cargo_unloaded: DecimalField            [tons]
├── turnaround_time: DecimalField(optional) [hours]
├── created_at: DateTimeField(auto_now_add=True)
└── auto-calculated on save

Use:
├── Track vessel movement history
├── Calculate turnaround time
├── Port traffic analytics
└── Vessel schedule planning
```

### Model 4: Safety & Events

```python
class SafetyEvent
Accident/incident records

Fields:
├── id: AutoField (primary key)
├── event_type: CharField (choices:
│   ├── 'collision'
│   ├── 'grounding'
│   ├── 'fire'
│   ├── 'explosion'
│   ├── 'flooding'
│   └── 'machinery_failure'
├── severity: CharField (choices:
│   ├── 'low' — minor damage
│   ├── 'medium' — moderate damage
│   ├── 'high' — severe damage
│   └── 'critical' — life-threatening
├── latitude: DecimalField(optional)
├── longitude: DecimalField(optional)
├── location_description: CharField(optional)
├── description: TextField()
├── vessel_involved: ForeignKey(optional)  [null if not ship-specific]
├── event_time: DateTimeField()
├── resolution_time: DateTimeField(optional)
├── created_at: DateTimeField(auto_now_add=True)
└── updated_at: DateTimeField(auto_now=True)

Indexes:
├── event_time (for chronological queries)
└── severity (for filtering critical events)


class WeatherAlert
Active weather warnings

Fields:
├── id: AutoField (primary key)
├── alert_type: CharField (choices:
│   ├── 'storm'
│   ├── 'hurricane'
│   ├── 'extreme_wind'
│   ├── 'heavy_rain'
│   ├── 'fog'
│   ├── 'high_waves'
│   └── 'tsunami'
├── severity: CharField (choices:
│   ├── 'warning' — caution
│   ├── 'alert' — avoid area
│   └── 'emergency' — severe threat
├── latitude: DecimalField()              [center of alert]
├── longitude: DecimalField()
├── location_name: CharField(255)
├── affected_radius_km: DecimalField()    [warning zone size]
├── wind_speed: IntegerField(optional)    [knots]
├── wind_direction: CharField(optional)   ['N', 'NE', 'E', etc.]
├── wave_height: DecimalField(optional)   [meters]
├── visibility: DecimalField(optional)    [kilometers]
├── issued_time: DateTimeField()
├── expires_time: DateTimeField()
├── is_active: BooleanField()
└── source: CharField()                   ['NOAA', 'MeteoService']

Methods:
├── is_expired() → Check if alert is still valid
├── affects_vessel(vessel) → Check if vessel in alert zone
└── __str__ → "Storm Warning - SE Asia"


class PiracyZone
Maritime security risk zones

Fields:
├── id: AutoField (primary key)
├── name: CharField(255)         [e.g., "Gulf of Aden"]
├── latitude: DecimalField()     [zone center]
├── longitude: DecimalField()
├── radius_km: DecimalField()    [danger zone radius]
├── threat_level: CharField (choices:
│   ├── 'low'
│   ├── 'medium'
│   ├── 'high'
│   └── 'critical'
├── description: TextField()
├── last_incident: DateTimeField(optional)
├── incidents_count: IntegerField(default=0)
├── recommended_speed: IntegerField(optional)  [knots]
├── armed_escort_recommended: BooleanField
├── report_to_ukmto: BooleanField              [UK Maritime Trade Ops]
├── created_at: DateTimeField(auto_now_add=True)
└── updated_at: DateTimeField(auto_now=True)


class AccidentHistory
Historical accident records

Fields:
├── id: AutoField (primary key)
├── latitude: DecimalField()
├── longitude: DecimalField()
├── location_name: CharField(255)
├── accident_type: CharField (choices: same as SafetyEvent)
├── incident_date: DateField()
├── description: TextField()
├── vessels: ManyToManyField(Vessel)  [multiple ships involved]
├── casualties: IntegerField(default=0)  [fatalities]
├── total_loss: BooleanField(default=False) [vessel sunk/destroyed]
├── estimated_damage_usd: BigIntegerField(optional)
└── created_at: DateTimeField(auto_now_add=True)
```

### Model 5: Voyage History

```python
class Voyage
Complete voyage record

Fields:
├── id: AutoField (primary key)
├── vessel: ForeignKey
├── origin_port_id: IntegerField(optional)
├── destination_port_id: IntegerField(optional)
├── start_date: DateTimeField()
├── estimated_end_date: DateTimeField(optional)
├── actual_end_date: DateTimeField(optional)
├── status: CharField (choices:
│   ├── 'planned'
│   ├── 'in_progress'
│   └── 'completed'
├── created_at: DateTimeField(auto_now_add=True)
└── updated_at: DateTimeField(auto_now=True)

Use:
├── Track complete vessel journeys
├── Historical analysis
└── Compliance auditing


class VoyageHistory
Position tracking during voyage

Fields:
├── id: AutoField (primary key)
├── voyage: ForeignKey
├── latitude: DecimalField()
├── longitude: DecimalField()
├── speed: DecimalField(optional)
├── heading: DecimalField(optional)
├── depth: DecimalField(optional)  [water depth]
├── timestamp: DateTimeField()
├── created_at: DateTimeField(auto_now_add=True)
└── index → (voyage_id, -timestamp)


class ComplianceRecord
Voyage compliance and regulations

Fields:
├── id: AutoField (primary key)
├── voyage: ForeignKey
├── regulation: CharField()         [MARPOL, SOLAS, ISM, etc.]
├── status: CharField (choices:
│   ├── 'compliant'
│   ├── 'non_compliant'
│   └── 'pending'
├── check_date: DateTimeField()
├── notes: TextField()
├── created_at: DateTimeField(auto_now_add=True)
└── updated_at: DateTimeField(auto_now=True)

Use:
├── Audit trail for maritime regulations
├── Compliance verification
└── Insurance documentation
```

---

## 👥 APP MODULES - DETAILED BREAKDOWN

### Module 1: Authentication App
**Location**: `apps/authentication/`

**Responsibilities**:
- Handle user registration
- Process login/logout
- Manage JWT tokens
- Control user roles and permissions
- Verify email addresses

**Key Files**:

**models.py** - Defines User and UserProfile

```python
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('operator', 'Vessel Operator'),
        ('analyst', 'Data Analyst'),
        ('admin', 'Administrator'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operator')
    company = models.CharField(max_length=255, blank=True)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
```

**serializers.py** - Convert objects to JSON

```python
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords do not match"}
            )
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        UserProfile.objects.create(user=user)
        return user
```

**views.py** - API endpoints

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from .models import UserProfile

class RegisterViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    
    def create(self, request):
        """Register new user"""
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully',
                'user_id': user.id,
                'username': user.username
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get', 'put'])
    def me(self, request):
        """Get or update current user's profile"""
        profile = UserProfile.objects.get(user=request.user)
        
        if request.method == 'GET':
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = self.get_serializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**urls.py** - Endpoint routes

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, UserProfileViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'profile', UserProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### Module 2: Vessels App
**Location**: `apps/vessels/`

**Responsibilities**:
- Manage vessel data
- Store position history
- Handle route information
- Process user alerts
- Integrate with MarineTraffic API

**Key Components**:

**tasks.py** - Async tasks (Celery)

```python
from celery import shared_task
from .models import Vessel, VesselPosition
from integrations.marinetraffic import MarineTrafficAPI

@shared_task
def sync_vessel_positions():
    """Fetch latest positions from MarineTraffic every 5 minutes"""
    api = MarineTrafficAPI()
    vessels = Vessel.objects.all()
    
    for vessel in vessels:
        try:
            # Get position from API
            position_data = api.get_vessel_position(vessel.mmsi)
            
            # Save to database
            VesselPosition.objects.create(
                vessel=vessel,
                latitude=position_data['lat'],
                longitude=position_data['lon'],
                speed=position_data['speed'],
                heading=position_data['heading'],
                timestamp=position_data['timestamp']
            )
            
            # Update vessel's last position
            vessel.last_position_lat = position_data['lat']
            vessel.last_position_lon = position_data['lon']
            vessel.save()
            
        except Exception as e:
            print(f"Error syncing {vessel.name}: {e}")

# Schedule this task to run every 5 minutes
# In celery config: CELERY_BEAT_SCHEDULE = {
#     'sync-vessel-positions': {
#         'task': 'apps.vessels.tasks.sync_vessel_positions',
#         'schedule': crontab(minute='*/5'),
#     },
# }
```

---

## 📡 API ENDPOINTS DOCUMENTATION

### Authentication Endpoints

```
POST    /api/auth/register/
├── Description: Register new user
├── Auth Required: No
├── Request Body:
│   {
│       "username": "john_doe",
│       "email": "john@example.com",
│       "password": "SecurePass123!",
│       "password2": "SecurePass123!"
│   }
├── Response (201):
│   {
│       "message": "User registered successfully",
│       "user_id": 1,
│       "username": "john_doe"
│   }
└── Response (400): Validation errors


POST    /api/auth/token/
├── Description: Login and get JWT tokens
├── Auth Required: No
├── Request Body:
│   {
│       "username": "john_doe",
│       "password": "SecurePass123!"
│   }
├── Response (200):
│   {
│       "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
│       "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
│       "user_id": 1,
│       "username": "john_doe",
│       "role": "operator",
│       "company": "ShipCo Inc"
│   }
└── Response (401): Invalid credentials


POST    /api/auth/token/refresh/
├── Description: Get new access token using refresh token
├── Auth Required: No
├── Request Body:
│   {
│       "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
│   }
├── Response (200):
│   {
│       "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
│   }
└── Use when: access_token expires but refresh_token is still valid


GET     /api/auth/profile/me/
├── Description: Get current user's profile
├── Auth Required: Yes (Bearer token)
├── Response (200):
│   {
│       "id": 1,
│       "username": "john_doe",
│       "email": "john@example.com",
│       "first_name": "John",
│       "last_name": "Doe",
│       "role": "operator",
│       "company": "ShipCo Inc",
│       "is_email_verified": true
│   }
└── Response (401): Unauthorized


PUT     /api/auth/profile/me/
├── Description: Update current user's profile
├── Auth Required: Yes
├── Request Body (partial update allowed):
│   {
│       "first_name": "John",
│       "company": "Updated ShipCo",
│       "phone_number": "+1234567890"
│   }
├── Response (200): Updated profile data
└── Response (400): Validation errors


POST    /api/auth/profile/change_password/
├── Description: Change user password
├── Auth Required: Yes
├── Request Body:
│   {
│       "old_password": "CurrentPass123!",
│       "new_password": "NewPass456!"
│   }
├── Response (200):
│   {
│       "message": "Password changed successfully"
│   }
└── Response (400): Old password incorrect
```

### Vessel Endpoints

```
GET     /api/vessels/
├── Description: List all vessels (paginated)
├── Auth Required: No
├── Query Parameters:
│   ?type=container          Filter by vessel type
│   ?flag=US                 Filter by flag (country)
│   ?status=in_transit       Filter by status
│   ?search=MAERSK          Search by name
│   ?page=2                  Pagination (20 per page)
├── Response (200):
│   {
│       "count": 5000,
│       "next": "/api/vessels/?page=2",
│       "previous": null,
│       "results": [
│           {
│               "id": 1,
│               "imo": 9123456,
│               "mmsi": 211378120,
│               "name": "MAERSK",
│               "type": "Container Ship",
│               "flag": "DE",
│               "status": "in_transit",
│               "latitude": 35.6895,
│               "longitude": 139.6917,
│               "speed": 12.5,
│               "heading": 180,
│               "last_position_update": "2024-02-12T10:30:00Z"
│           }
│       ]
│   }
└── Pagination: REST framework handles automatically


GET     /api/vessels/{id}/
├── Description: Get detailed vessel information
├── Auth Required: No
├── Response (200):
│   {
│       "id": 1,
│       "imo": 9123456,
│       "mmsi": 211378120,
│       "name": "MAERSK SEALAND",
│       "type": "Container Ship",
│       "flag": "DE",
│       "owner": "A.P. Moller - Maersk",
│       "operator": "Maersk Line",
│       "year_built": 2013,
│       "length": 399,
│       "beam": 59,
│       "draft": 15.5,
│       "status": "in_transit",
│       "latitude": 35.6895,
│       "longitude": 139.6917,
│       "speed": 12.5,
│       "heading": 180,
│       "last_position_update": "2024-02-12T10:30:00Z",
│       "current_route": {
│           "origin_port": "Shanghai",
│           "destination_port": "Rotterdam",
│           "departure_time": "2024-02-01T08:00:00Z",
│           "eta": "2024-03-05T15:00:00Z",
│           "status": "active"
│       },
│       "positions": [
│           {
│               "latitude": 35.6882,
│               "longitude": 139.6910,
│               "speed": 12.5,
│               "heading": 180,
│               "timestamp": "2024-02-12T10:25:00Z",
│               "time_ago": "5 minutes ago"
│           },
│           {
│               "latitude": 35.6895,
│               "longitude": 139.6917,
│               "speed": 12.5,
│               "heading": 180,
│               "timestamp": "2024-02-12T10:30:00Z",
│               "time_ago": "Just now"
│           }
│       ],
│       "user_alerts": [
│           {
│               "id": 1,
│               "alert_type": "position_change",
│               "is_active": true,
│               "created_at": "2024-02-10T14:00:00Z"
│           }
│       ]
│   }
└── Includes: Route, position history, user alerts


GET     /api/vessels/{id}/positions/
├── Description: Get position history for a vessel
├── Auth Required: No
├── Query Parameters:
│   ?days=7     Get last 7 days (default)
│   ?days=30    Get last 30 days
├── Response (200):
│   {
│       "vessel_id": 1,
│       "vessel_name": "MAERSK",
│       "period_days": 7,
│       "count": 336,
│       "positions": [
│           {
│               "latitude": 35.6895,
│               "longitude": 139.6917,
│               "speed": 12.5,
│               "heading": 180,
│               "timestamp": "2024-02-12T10:30:00Z"
│           },
│           ...
│       ]
│   }
└── 336 = 7 days × 24 hours × 2 positions/hour


POST    /api/vessels/{id}/subscribe/
├── Description: Subscribe to vessel alerts
├── Auth Required: Yes (Bearer token)
├── Request Body:
│   {
│       "alert_type": "position_change"
│   }
├── Alert Types:
│   ├── "position_change"    Notify on position update
│   ├── "port_arrival"       Notify on port arrival
│   ├── "port_departure"     Notify on port departure
│   ├── "speed_change"       Notify on speed change
│   ├── "heading_change"     Notify on heading change
│   └── "status_change"      Notify on status change
├── Response (201):
│   {
│       "id": 1,
│       "alert_type": "position_change",
│       "is_active": true,
│       "created_at": "2024-02-12T10:30:00Z"
│   }
└── Response (409): Already subscribed to this alert


POST    /api/vessels/{id}/unsubscribe/
├── Description: Unsubscribe from vessel alerts
├── Auth Required: Yes
├── Request Body:
│   {
│       "alert_type": "position_change"
│   }
├── Response (200):
│   {
│       "message": "Unsubscribed successfully"
│   }
└── Response (404): Alert not found


GET     /api/vessels/search/
├── Description: Search vessels by name, IMO, or MMSI
├── Auth Required: No
├── Query Parameters:
│   ?q=MAERSK       Search by name
│   ?q=9123456      Search by IMO number
│   ?q=211378120    Search by MMSI
├── Response (200):
│   {
│       "count": 5,
│       "results": [
│           {vessel data}
│       ]
│   }
└── Minimum 2 characters required
```

### Port Endpoints

```
GET     /api/ports/
├── Description: List all ports
├── Auth Required: No
├── Query Parameters:
│   ?country=Japan        Filter by country
│   ?type=container       Filter by port type
│   ?search=Tokyo        Search by name
├── Response: List of ports with statistics


GET     /api/ports/{id}/
├── Description: Get detailed port information
├── Auth Required: No
├── Response (200):
│   {
│       "id": 1,
│       "name": "Tokyo Port",
│       "unlocode": "JPTYO",
│       "city": "Tokyo",
│       "country": "Japan",
│       "latitude": 35.4437,
│       "longitude": 139.6655,
│       "port_type": "container",
│       "number_of_berths": 40,
│       "statistics": {
│           "total_arrivals": 12450,
│           "total_departures": 12450,
│           "current_vessels": 15,
│           "average_wait_time": 2.5,
│           "average_berth_time": 24.0,
│           "congestion_level": "medium",
│           "efficiency_score": 85.5,
│           "last_updated": "2024-02-12T10:30:00Z"
│       }
│   }
└── Includes current and historical statistics


GET     /api/ports/{id}/congestion_history/
├── Description: Get congestion history for port
├── Auth Required: No
├── Query Parameters:
│   ?days=7     Last 7 days (default)
│   ?days=30    Last 30 days
├── Response (200):
│   {
│       "port": "Tokyo Port",
│       "period_days": 7,
│       "count": 168,
│       "metrics": [
│           {
│               "congestion_percentage": 45.5,
│               "queue_length": 3,
│               "estimated_wait_time": 2.5,
│               "berths_available": 10,
│               "berths_occupied": 15,
│               "timestamp": "2024-02-12T10:00:00Z"
│           }
│       ]
│   }
└── Use for: Congestion trend analysis


GET     /api/ports/{id}/arrivals_departures/
├── Description: Get arrivals/departures for port
├── Auth Required: No
├── Query Parameters:
│   ?days=30    Last 30 days
├── Response (200):
│   {
│       "port": "Tokyo Port",
│       "period_days": 30,
│       "count": 450,
│       "arrivals_departures": [
│           {
│               "vessel_name": "MAERSK",
│               "port_name": "Tokyo Port",
│               "arrival_time": "2024-02-10T08:30:00Z",
│               "departure_time": "2024-02-12T14:00:00Z",
│               "berth_number": "B-15",
│               "cargo_loaded": 15000,
│               "cargo_unloaded": 12000,
│               "turnaround_time": 53.5
│           }
│       ]
│   }
└── turnaround_time = time in port (hours)
```

### Safety Endpoints

```
GET     /api/safety/weather/
├── Description: Get active weather alerts
├── Auth Required: No
├── Query Parameters:
│   ?severity=alert     Filter by severity
│   ?type=storm        Filter by alert type
├── Response (200):
│   {
│       "count": 5,
│       "results": [
│           {
│               "id": 1,
│               "alert_type": "storm",
│               "severity": "alert",
│               "latitude": 35.5,
│               "longitude": 139.5,
│               "location_name": "Southeast Japan",
│               "affected_radius_km": 500,
│               "wind_speed": 85,
│               "wind_direction": "NE",
│               "wave_height": 12.5,
│               "visibility": 2,
│               "issued_time": "2024-02-12T08:00:00Z",
│               "expires_time": "2024-02-13T08:00:00Z",
│               "is_active": true
│           }
│       ]
│   }
└── Always returns only active alerts


GET     /api/safety/weather/nearby/
├── Description: Get weather alerts near location
├── Auth Required: No
├── Query Parameters (Required):
│   ?lat=35.65          Latitude
│   ?lon=139.75         Longitude
│   ?range=100          Range in km (default 100)
├── Response (200):
│   {
│       "location": {"latitude": 35.65, "longitude": 139.75},
│       "range_km": 100,
│       "count": 2,
│       "alerts": [...]
│   }
└── Uses haversine formula for distance calculation


GET     /api/safety/piracy/
├── Description: Get piracy risk zones
├── Auth Required: No
├── Query Parameters:
│   ?threat_level=high  Filter by threat level
├── Response (200):
│   {
│       "count": 10,
│       "results": [
│           {
│               "id": 1,
│               "name": "Gulf of Aden",
│               "latitude": 13.0,
│               "longitude": 48.0,
│               "radius_km": 500,
│               "threat_level": "critical",
│               "description": "Active piracy operations",
│               "last_incident": "2024-02-08T14:30:00Z",
│               "incidents_count": 5,
│               "recommended_speed": 15,
│               "armed_escort_recommended": true,
│               "report_to_ukmto": true
│           }
│       ]
│   }
└── For voyage planning and risk assessment


GET     /api/safety/piracy/high_risk/
├── Description: Get only critical/high threat zones
├── Auth Required: No
├── Response (200):
│   {
│       "count": 3,
│       "zones": [...]
│   }
└── Shortcut endpoint for critical zones


GET     /api/safety/accidents/
├── Description: Get accident history
├── Auth Required: No
├── Query Parameters:
│   ?type=collision     Filter by accident type
│   ?days=365          Last N days
├── Response (200):
│   {
│       "count": 45,
│       "results": [
│           {
│               "id": 1,
│               "location_name": "Malacca Strait",
│               "latitude": 1.5,
│               "longitude": 103.0,
│               "accident_type": "collision",
│               "incident_date": "2023-06-15",
│               "description": "Two container ships collided...",
│               "casualties": 0,
│               "total_loss": false,
│               "estimated_damage_usd": 5000000
│           }
│       ]
│   }
└── Historical data only (last 5 years)
```

---

## 🔒 AUTHENTICATION & AUTHORIZATION

### How JWT Authentication Works

```
Step 1: User Registration
┌─────────────────────────────────────┐
│ User submits registration form       │
│ - Username: john_doe                │
│ - Email: john@example.com           │
│ - Password: SecurePass123!          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Backend processes (POST /register)   │
│ - Validates email format            │
│ - Checks password strength          │
│ - Hashes password (never plain!)    │
│ - Creates User record               │
│ - Creates UserProfile               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Response: User created successfully  │
│ Now user can login                  │
└─────────────────────────────────────┘


Step 2: User Login (Get JWT Tokens)
┌─────────────────────────────────────┐
│ User submits login form              │
│ - Username: john_doe                │
│ - Password: SecurePass123!          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Backend verifies credentials         │
│ - Find user by username             │
│ - Check password hash matches       │
│ - If matches, create JWT tokens     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Response: Two tokens provided        │
│                                     │
│ access_token (expires in 1 hour)    │
│ eyJhbGciOiJIUzI1NiIsInR5cCI6IkpX │
│ VCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmF │
│ ...truncated...                     │
│                                     │
│ refresh_token (expires in 7 days)   │
│ eyJhbGciOiJIUzI1NiIsInR5cCI6IkpX │
│ VCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmV │
│ ...truncated...                     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Frontend stores tokens in            │
│ localStorage (browser storage)       │
└─────────────────────────────────────┘


Step 3: Using Token in Requests
┌─────────────────────────────────────┐
│ Frontend makes API request           │
│ GET /api/profile/                   │
│ Header: Authorization:              │
│ Bearer eyJhbGciOiJIUzI1NiIsInR5cCI │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Backend receives request             │
│ 1. Extracts token from header       │
│ 2. Validates token signature        │
│ 3. Checks if token is expired       │
│ 4. Identifies user from token       │
│ 5. Checks user permissions          │
└──────────────┬──────────────────────┘
               │
      ┌────────┴────────┐
      │                 │
      ▼                 ▼
┌──────────────┐  ┌──────────────┐
│ Valid & OK   │  │ Invalid/     │
│ Process      │  │ Expired      │
│ request      │  │ Deny access  │
└──────────────┘  └──────────────┘


Step 4: Token Refresh (When Expired)
┌─────────────────────────────────────┐
│ Access token expires after 1 hour    │
│ User gets 401 Unauthorized error    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Frontend sends refresh token         │
│ POST /api/token/refresh/            │
│                                     │
│ {                                   │
│   "refresh": "eyJhbGciOi..."        │
│ }                                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Backend validates refresh token      │
│ Creates new access_token            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Frontend gets new access_token      │
│ Continues with request              │
└─────────────────────────────────────┘


Step 5: Logout
┌─────────────────────────────────────┐
│ User clicks logout                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ Frontend deletes tokens from         │
│ localStorage                         │
│                                     │
│ localStorage.removeItem('access')   │
│ localStorage.removeItem('refresh')  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ User is logged out                   │
│ No tokens = Cannot access protected  │
│ endpoints                            │
└─────────────────────────────────────┘
```

### Role-Based Permissions

```python
class IsOperator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.role == 'operator'

class IsAnalyst(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.role == 'analyst'

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.role == 'admin'


# Usage in views:
class VesselViewSet(viewsets.ModelViewSet):
    
    @action(detail=True, methods=['post'], permission_classes=[IsAnalyst])
    def generate_report(self, request, pk=None):
        """Only analysts can generate reports"""
        # Generate report...
        return Response(report_data)
    
    @action(detail=True, methods=['delete'], permission_classes=[IsAdmin])
    def delete_vessel(self, request, pk=None):
        """Only admins can delete vessels"""
        # Delete vessel...
        return Response({'message': 'Deleted'})


# Permission Matrix:
┌─────────────────────┬──────────┬────────┬────────┬───────┐
│ Action              │ Operator │ Analyst│ Admin  │ Guest │
├─────────────────────┼──────────┼────────┼────────┼───────┤
│ View Vessels        │ ✓        │ ✓      │ ✓      │ ✓     │
│ View Port Stats     │ ✓        │ ✓      │ ✓      │ ✓     │
│ View Safety Data    │ ✓        │ ✓      │ ✓      │ ✓     │
│ Subscribe Alerts    │ ✓        │ ✗      │ ✓      │ ✗     │
│ Generate Reports    │ ✗        │ ✓      │ ✓      │ ✗     │
│ Export Data         │ ✗        │ ✓      │ ✓      │ ✗     │
│ Manage Users        │ ✗        │ ✗      │ ✓      │ ✗     │
│ System Config       │ ✗        │ ✗      │ ✓      │ ✗     │
└─────────────────────┴──────────┴────────┴────────┴───────┘
```

---

## 🔌 EXTERNAL API INTEGRATION

### MarineTraffic API

**Purpose**: Real-time vessel positions and metadata

```python
# integrations/marinetraffic.py

class MarineTrafficAPI:
    BASE_URL = "https://services.marinetraffic.com/api"
    
    def get_vessel_position(self, mmsi):
        """
        Get current position for vessel
        
        Args:
            mmsi: Maritime Mobile Service Identity (e.g., 211378120)
        
        Returns:
            {
                'mmsi': 211378120,
                'position': {'lat': 35.6895, 'lon': 139.6917},
                'speed': 12.5,  # Knots
                'heading': 180,  # Degrees
                'timestamp': '2024-02-12T10:30:00Z'
            }
        """
        params = {
            'mmsi': mmsi,
            'apikey': self.api_key,
        }
        response = self.get('v3/vessel-positions', params=params)
        return self._parse_position(response)
    
    def get_vessel_details(self, mmsi):
        """
        Get static vessel information
        
        Returns:
            {
                'imo': '9123456',
                'mmsi': 211378120,
                'name': 'MAERSK SEALAND',
                'type': 'Container Ship',
                'flag': 'DE',
                'owner': 'A.P. Moller - Maersk',
                'year_built': 2013,
                'length': 399,
                'beam': 59
            }
        """
        params = {'mmsi': mmsi, 'apikey': self.api_key}
        response = self.get('v3/vessel-info', params=params)
        return self._parse_details(response)
```

**Integration in Django**:

```python
# apps/vessels/tasks.py - Celery task

@shared_task
def sync_vessel_from_marinetraffic(mmsi):
    """Sync vessel data from MarineTraffic API"""
    try:
        api = MarineTrafficAPI()
        
        # Get vessel details
        details = api.get_vessel_details(mmsi)
        vessel, created = Vessel.objects.update_or_create(
            mmsi=mmsi,
            defaults={
                'imo': details['imo'],
                'name': details['name'],
                'flag': details['flag'],
                'owner': details['owner'],
                'external_api_source': 'marinetraffic'
            }
        )
        
        # Get current position
        position = api.get_vessel_position(mmsi)
        if position:
            VesselPosition.objects.create(
                vessel=vessel,
                latitude=position['lat'],
                longitude=position['lon'],
                speed=position['speed'],
                heading=position['heading'],
                timestamp=position['timestamp']
            )
            
            # Update vessel's last known position
            vessel.last_position_lat = position['lat']
            vessel.last_position_lon = position['lon']
            vessel.save()
        
        return {
            'status': 'success',
            'vessel': vessel.name,
            'created': created
        }
    
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
```

### NOAA Weather API

**Purpose**: Weather alerts and ocean conditions

```python
# integrations/noaa.py

class NOAAAPI:
    BASE_URL = "https://api.weather.gov"
    
    def get_weather_alerts(self, latitude, longitude):
        """
        Get weather alerts for location
        
        Returns:
            {
                'alerts': [
                    {
                        'id': 'alert_id',
                        'event': 'Storm Warning',
                        'headline': 'Storm Warning issued Feb 12...',
                        'severity': 'Severe',
                        'area': 'Southeast Japan',
                        'onset': '2024-02-12T08:00:00Z',
                        'expires': '2024-02-13T08:00:00Z'
                    }
                ]
            }
        """
        params = {
            'lat': latitude,
            'lon': longitude,
            'apikey': self.api_key,
        }
        return self.get('alerts', params=params)
    
    def get_ocean_data(self, latitude, longitude):
        """
        Get ocean conditions (waves, wind, temp)
        
        Returns:
            {
                'water_temp': 18.5,        # Celsius
                'wave_height': 4.5,        # Meters
                'wind_speed': 15,          # Knots
                'wind_direction': 'NE',
                'tide': 1.2                # Meters
            }
        """
        # Implementation...
```

### Database Sync Pattern

```python
# Settings: Update CELERY_BEAT_SCHEDULE periodic tasks

CELERY_BEAT_SCHEDULE = {
    'sync-vessel-positions': {
        'task': 'apps.vessels.tasks.sync_vessel_positions',
        'schedule': crontab(minute='*/5'),  # Every 5 minutes
    },
    'sync-weather-alerts': {
        'task': 'apps.safety.tasks.sync_weather_alerts',
        'schedule': crontab(minute='*/30'),  # Every 30 minutes
    },
    'update-port-statistics': {
        'task': 'apps.ports.tasks.update_port_statistics',
        'schedule': crontab(minute='*/60'),  # Every hour
    },
}


# apps/vessels/tasks.py

@periodic_task(run_every=crontab(minute='*/5'))
def sync_vessel_positions():
    """
    Synchronize vessel positions every 5 minutes
    
    This task:
    1. Gets all tracked vessels
    2. Queries MarineTraffic API for each
    3. Stores new positions in database
    4. Triggers alerts if needed
    """
    vessels = Vessel.objects.all()
    api = MarineTrafficAPI()
    
    for vessel in vessels:
        try:
            position = api.get_vessel_position(vessel.mmsi)
            
            # Create position record
            VesselPosition.objects.create(
                vessel=vessel,
                latitude=position['lat'],
                longitude=position['lon'],
                speed=position['speed'],
                heading=position['heading'],
                timestamp=position['timestamp']
            )
            
            # Check if alerts should be triggered
            check_and_trigger_alerts.delay(vessel.id, position)
            
        except Exception as e:
            logger.error(f"Error syncing vessel {vessel.name}: {e}")
```

---

## 💻 DEVELOPMENT WORKFLOW

### Creating a New Endpoint

**Step 1**: Define the Model (if needed)

```python
# apps/myapp/models.py

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'my_models'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
```

**Step 2**: Create Serializer

```python
# apps/myapp/serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']
```

**Step 3**: Create View

```python
# apps/myapp/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

**Step 4**: Register URL

```python
# apps/myapp/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# In core/urls.py, add:
# path('api/myapp/', include('apps.myapp.urls')),
```

**Step 5**: Run Migrations

```bash
python manage.py makemigrations myapp
python manage.py migrate myapp
```

**Step 6**: Test

```bash
# Start server
python manage.py runserver

# Test endpoint
curl http://localhost:8000/api/myapp/mymodels/
```

### Common Development Commands

```bash
# Create new app
python manage.py startapp appname

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run specific migration backwards
python manage.py migrate appname 0001_initial

# Create migration without models
python manage.py makemigrations --empty appname --name describe_change

# Show SQL that will run
python manage.py sqlmigrate appname 0002

# Check migration status
python manage.py showmigrations

# Django shell (interactive Python)
python manage.py shell

# Create admin user
python manage.py createsuperuser

# Load fixture data
python manage.py loaddata fixture_name

# Dump data to fixture
python manage.py dumpdata appname > backup.json

# Clear database completely
python manage.py flush

# Check for issues
python manage.py check

# Collect static files
python manage.py collectstatic
```

---

## 🧪 TESTING & QUALITY ASSURANCE

### Unit Tests

```python
# apps/vessels/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Vessel, VesselPosition

class VesselModelTest(TestCase):
    def setUp(self):
        """Create test data"""
        self.vessel = Vessel.objects.create(
            imo=9123456,
            mmsi=211378120,
            name='Test Ship',
            vessel_type='container',
            flag='US'
        )
    
    def test_vessel_creation(self):
        """Test vessel can be created"""
        self.assertEqual(self.vessel.name, 'Test Ship')
        self.assertEqual(self.vessel.mmsi, 211378120)
    
    def test_str_method(self):
        """Test __str__ method"""
        self.assertEqual(str(self.vessel), 'Test Ship (IMO: 9123456)')
    
    def test_is_recent(self):
        """Test is_recent() method"""
        # Without position update
        self.assertFalse(self.vessel.is_recent())
        
        # With recent position
        from django.utils import timezone
        self.vessel.last_position_update = timezone.now()
        self.vessel.save()
        self.assertTrue(self.vessel.is_recent())


class VesselAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.vessel = Vessel.objects.create(
            imo=9123456,
            mmsi=211378120,
            name='API Test Ship',
            vessel_type='container',
            flag='US'
        )
    
    def test_list_vessels(self):
        """Test GET /api/vessels/"""
        response = self.client.get('/api/vessels/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
    
    def test_get_vessel_detail(self):
        """Test GET /api/vessels/{id}/"""
        response = self.client.get(f'/api/vessels/{self.vessel.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'API Test Ship')
    
    def test_search_vessels(self):
        """Test GET /api/vessels/search/?q="""
        response = self.client.get('/api/vessels/search/?q=API')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.vessels

# Run with verbosity
python manage.py test -v 2

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Code Quality Tools

```bash
# Lint code (check for style issues)
pip install flake8
flake8 .

# Code formatting
pip install black
black .

# Check code complexity
pip install radon
radon cc apps/ -a

# Type checking (optional)
pip install mypy
mypy .
```

---

## 🚀 DEPLOYMENT GUIDE

### Preparation

**1. Update requirements.txt**

```bash
# Generate production requirements
pip freeze > requirements.txt

# Then manually edit and remove unnecessary packages:
```

```txt
Django==4.2.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
psycopg2-binary==2.9.0
django-cors-headers==4.2.0
drf-spectacular==0.26.0
gunicorn==21.2.0
python-dotenv==1.0.0
requests==2.31.0
celery==5.3.0
redis==5.0.0
```

**2. Create Production .env**

```env
DEBUG=False
SECRET_KEY=generate-long-random-string-here-change-this
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DATABASE_URL=postgresql://user:password@db-host:5432/maritime_db

STATIC_ROOT=/var/www/maritime/static
MEDIA_ROOT=/var/www/maritime/media

SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

MARINETRAFFIC_API_KEY=your-production-key
NOAA_API_KEY=your-production-key

LOG_LEVEL=WARNING
```

### Deploy to Heroku

```bash
# 1. Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Login to Heroku
heroku login

# 3. Create Heroku app
heroku create maritime-vessel-tracking

# 4. Add PostgreSQL
heroku addons:create heroku-postgresql:standard-0

# 5. Add Redis for Celery (optional)
heroku addons:create heroku-redis:premium-0

# 6. Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key
heroku config:set ALLOWED_HOSTS=maritime-vessel-tracking.herokuapp.com

# 7. Create Procfile
# web: gunicorn core.wsgi
# worker: celery -A core worker -l info
# beat: celery -A core beat -l info

# 8. Deploy
git push heroku main

# 9. Run migrations on Heroku
heroku run python manage.py migrate

# 10. Create superuser
heroku run python manage.py createsuperuser

# 11. View logs
heroku logs --tail
```

### Deploy to AWS (EC2)

```bash
# 1. SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-instance-ip

# 2. Update system
sudo apt-get update && sudo apt-get upgrade -y

# 3. Install dependencies
sudo apt-get install -y python3-pip python3-venv postgresql postgresql-contrib nginx

# 4. Clone your repository
git clone <your-repo-url>
cd Maritime_Vessel_Tracking/backend

# 5. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 6. Install Python packages
pip install -r requirements.txt

# 7. Create .env file
nano .env  # Add all environment variables

# 8. Run migrations
python manage.py migrate

# 9. Collect static files
python manage.py collectstatic --noinput

# 10. Create systemd service file
sudo nano /etc/systemd/system/maritime.service

# Add content:
[Unit]
Description=Maritime Vessel Tracking API
After=network.target

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/home/ubuntu/Maritime_Vessel_Tracking/backend
Environment="PATH=/home/ubuntu/Maritime_Vessel_Tracking/backend/venv/bin"
ExecStart=/home/ubuntu/Maritime_Vessel_Tracking/backend/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/run/maritime.sock \
          core.wsgi:application

[Install]
WantedBy=multi-user.target

# 11. Start service
sudo systemctl daemon-reload
sudo systemctl start maritime
sudo systemctl enable maritime

# 12. Configure Nginx
sudo nano /etc/nginx/sites-available/maritime

# Add content:
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://unix:/run/maritime.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location /static/ {
        alias /home/ubuntu/Maritime_Vessel_Tracking/backend/staticfiles/;
    }
    
    location /media/ {
        alias /home/ubuntu/Maritime_Vessel_Tracking/backend/media/;
    }
}

# 13. Enable Nginx site
sudo ln -s /etc/nginx/sites-available/maritime /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# 14. Setup SSL with Let's Encrypt
sudo apt-get install -y certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

---

## ❌ TROUBLESHOOTING & COMMON ISSUES

### Issue 1: "Port 8000 is already in use"

```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use different port
python manage.py runserver 8001
```

### Issue 2: "ModuleNotFoundError: No module named 'django'"

```bash
# Check if virtual environment is activated
# Should see (venv) at start of terminal

# If not activated:
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue 3: "Migrate error: Relation does not exist"

```bash
# Check migrations
python manage.py showmigrations

# Run pending migrations
python manage.py migrate

# If still issues, reset database
python manage.py migrate --fake
python manage.py migrate
```

### Issue 4: "CORS error from frontend"

```python
# Add frontend URL to CORS_ALLOWED_ORIGINS in settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://yourdomain.com",
    "https://yourdomain.com",
]
```

### Issue 5: "JSON decode error from external API"

```python
# Add error handling in integration

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    logger.error("API timeout")
except requests.exceptions.ConnectionError:
    logger.error("API connection error")
except ValueError:
    logger.error("Invalid JSON response")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
```

### Issue 6: "Static files not loading in production"

```bash
# Collect static files
python manage.py collectstatic --noinput --clear

# Check STATIC_ROOT setting
STATIC_ROOT = BASE_DIR / 'staticfiles'

# In Nginx configuration
location /static/ {
    alias /path/to/staticfiles/;
}
```

### Debugging Techniques

```python
# Use Django shell to test queries
python manage.py shell

>>> from apps.vessels.models import Vessel
>>> vessels = Vessel.objects.all()
>>> print(vessels.query)  # See SQL query
>>> vessels.first().__dict__  # See object attributes

# Use logging
import logging
logger = logging.getLogger(__name__)

logger.info(f"Processing vessel: {vessel_name}")
logger.warning("This might be an issue")
logger.error(f"Something went wrong: {error}")

# Enable query logging (development only!)
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as context:
    vessels = Vessel.objects.all()

print(f"Number of queries: {len(context)}")
for query in context:
    print(query['sql'])
```

---

## 📚 ADDITIONAL RESOURCES

### Official Documentation
- Django: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- JWT: https://django-rest-framework-simplejwt.readthedocs.io/

### Useful Packages
```bash
# Database visualization
pip install pgadmin4

# API testing
pip install insomnia-cli

# Task scheduling
pip install django-celery-beat

# Email functionality
pip install django-anymail

# File uploading
pip install django-storages
```

### Best Practices
1. ✅ Use virtual environment for each project
2. ✅ Keep SECRET_KEY in environment variables
3. ✅ Use PostgreSQL for production
4. ✅ Write tests for critical functionality
5. ✅ Use pagination for large datasets
6. ✅ Add database indexes for frequent queries
7. ✅ Enable logging in production
8. ✅ Regular database backups
9. ✅ Use HTTPS in production
10. ✅ Keep dependencies updated

---

**Last Updated**: February 2026  
**Backend Version**: 1.0.0  
**Framework**: Django 4.2 + DRF 3.14  
**Database**: SQLite (dev) / PostgreSQL (production)

