# Maritime Vessel Tracking Platform - Backend Documentation
## A Complete Guide for B.Tech Interns

---

## TABLE OF CONTENTS
1. [Introduction & Overview](#introduction--overview)
2. [Technology Stack Explained](#technology-stack-explained)
3. [Project Setup & Installation](#project-setup--installation)
4. [Project Structure Breakdown](#project-structure-breakdown)
5. [Milestone 1: Authentication & Database (Week 1-2)](#milestone-1-authentication--database-week-1-2)
6. [Milestone 2: Live Tracking Integration (Week 3-4)](#milestone-2-live-tracking-integration-week-3-4)
7. [Milestone 3: Port & Safety Analytics (Week 5-6)](#milestone-3-port--safety-analytics-week-5-6)
8. [Milestone 4: Historical Data & Deployment (Week 7-8)](#milestone-4-historical-data--deployment-week-7-8)
9. [API Integration Guide](#api-integration-guide)
10. [Database Schema Explained](#database-schema-explained)
11. [Testing & Deployment](#testing--deployment)

---

## Introduction & Overview

### What is Backend?
The backend is the "server-side" of your application - it's the invisible engine that processes data and serves information to the frontend (what users see). Think of it like a restaurant kitchen:
- **Frontend** = The dining area (where customers eat)
- **Backend** = The kitchen (where food is prepared)
- **Database** = The storage (where ingredients are kept)

### Why Django REST Framework?
We're using **Django** (a Python web framework) because:
-  Excellent for building APIs (Application Programming Interfaces)
-  Built-in security features (user authentication, permissions)
-  Powerful database management tools
-  Large community with tutorials and resources
-  Fast deployment options

### What Will Backend Do?
The backend will:
1. **Store data** in the database (vessels, ports, users, positions)
2. **Process requests** from the frontend (search vessels, get port stats)
3. **Integrate with external APIs** (MarineTraffic, NOAA, UNCTAD)
4. **Send real-time updates** to the frontend
5. **Handle user authentication** (login, registration, permissions)
6. **Validate data** before saving to database

---

## Technology Stack Explained

### Prerequisites (What You Need to Know/Install)

#### 1. **Python 3.10+**
- **What it is**: A programming language (simple, easy to learn)
- **Why we use it**: Perfect for web backends, data processing
- **Check installation**:
~~~
  python --version
  # Should show: Python 3.10.x or higher
~~~
- **Install from**: https://www.python.org/downloads/

#### 2. **Virtual Environment (venv)**
- **What it is**: An isolated Python workspace for this project
- **Why we use it**: Different projects need different packages; venv keeps them separate
- **Analogy**: Like different folders for different subjects in school
- **Create virtual environment**:
~~~
  python -m venv venv
  # This creates a folder named 'venv' with isolated Python
~~~

#### 3. **pip (Package Manager)**
- **What it is**: A tool that downloads and installs Python packages
- **Why we use it**: To install Django, DRF, and other libraries
- **Check installation**:
~~~
  pip --version
~~~

#### 4. **PostgreSQL (Production Database)**
- **What it is**: A powerful, reliable database system
- **Why we use it**: Better than SQLite for production; handles many users
- **For development**: We'll use SQLite (lighter, built-in)
- **For production**: We'll switch to PostgreSQL
- **Install from**: https://www.postgresql.org/download/

### Core Technologies

#### **Django 4.2+**
- **What**: Web framework (like building blocks for web apps)
- **Why**: Handles routing (URLs), database management (ORM), authentication, security
- **Install**: pip install django
- **Version**: 4.2 or higher

#### **Django REST Framework (DRF)**
- **What**: Extension of Django for building APIs
- **Why**: Makes REST APIs easy to build, automatic serialization (convert Python objects to JSON)
- **Install**: pip install djangorestframework
- **Usage**: For endpoints like GET /api/vessels/, POST /api/vessels/

A REST API is like a restaurant menu:
- GET = Read the menu (get data)
- POST = Place an order (send data)
- PUT = Modify an order (update data)
- DELETE = Cancel an order (delete data)

---

## Project Setup & Installation

### Step 1: Initial Setup (First Time)

~~~bash
# 1. Create project directory
mkdir maritime_backend
cd maritime_backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# You'll see (venv) at the start of your terminal prompt when activated
~~~

### Step 2: Create Django Project

~~~bash
# 1. Install Django and DRF
pip install django djangorestframework djangorestframework-simplejwt

# 2. Create Django project (named 'core')
django-admin startproject core .

# 3. Understand what was created:
# core/
#    __init__.py
#    settings.py      (Configuration file)
#    urls.py          (URL routing)
#    asgi.py          (For WebSockets)
#    wsgi.py          (For deployment)
# manage.py             (Main management tool)
~~~

### Step 3: Create requirements.txt

Create a file named \equirements.txt\ with all dependencies:

~~~txt
Django==4.2.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
python-dotenv==1.0.0
requests==2.31.0
pandas==2.0.0
celery==5.3.0
psycopg2-binary==2.9.0
django-cors-headers==4.2.0
drf-spectacular==0.26.0
~~~

**Why requirements.txt?**
- Share dependencies with team
- Easy reinstall: \pip install -r requirements.txt\
- Version control (know what versions were used)

~~~bash
# Install all at once:
pip install -r requirements.txt
~~~

### Step 4: Create .env File

Create \.env\ file in project root (same level as manage.py):

~~~env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-change-this
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (Development - SQLite)
DATABASE_URL=sqlite:///db.sqlite3

# Database (Production - PostgreSQL)
# DATABASE_URL=postgresql://user:password@localhost:5432/maritime_db

# JWT Settings
JWT_SECRET_KEY=your-jwt-secret-key

# External API Keys (Get these from respective websites)
MARINETRAFFIC_API_KEY=your-api-key
AIS_HUB_API_KEY=your-api-key
NOAA_API_KEY=your-api-key
UNCTAD_API_KEY=your-api-key

# Email Settings (for notifications)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Celery (if using)
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
~~~

### Step 5: Configure Django Settings

Edit \core/settings.py\ and add:

~~~python
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Security Settings
DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'corsheaders',
    'drf_spectacular',
    
    # Your apps (will create these)
    'apps.authentication',
    'apps.vessels',
    'apps.ports',
    'apps.safety',
    'apps.voyages',
    'apps.notifications',
    'apps.admin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Add this for frontend
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# CORS Settings (Allow frontend to access backend)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',      # React dev server
    'http://localhost:8000',      # Your backend
    'https://yourdomain.com',     # Production domain
]

# JWT Settings
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}
~~~

### Step 6: Initial Migrations & First Run

~~~bash
# 1. Create migration files (blueprint for database)
python manage.py makemigrations

# 2. Apply migrations (create actual database tables)
python manage.py migrate

# 3. Create superuser (admin account)
python manage.py createsuperuser
# Follow the prompts to create username, email, password

# 4. Start development server
python manage.py runserver
# Visit: http://localhost:8000
~~~

---

## Summary for Milestone 1

### What You've Completed
 Created Django project structure
 Set up authentication system with JWT
 Created User and UserProfile models
 Built login/registration endpoints
 Configured database for development

### Database Tables Created
- users (built-in Django)
- user_profiles (custom)

### API Endpoints Available
- POST /api/auth/register/ - Register new user
- POST /api/auth/token/ - Login and get JWT token
- GET /api/auth/profile/me/ - View your profile
- PUT /api/auth/profile/me/ - Update your profile
- POST /api/auth/profile/change_password/ - Change password

### What's Next (Milestone 2)
- Create Vessels app for ship tracking
- Integrate MarineTraffic API
- Store real-time vessel positions
- Build vessel search and filter endpoints

---

**Last Updated**: February 2026
**Backend Version**: 1.0.0
**Framework**: Django 4.2 + DRF 3.14
