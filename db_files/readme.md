# Maritime Vessel Tracking Platform - Database Documentation
## A Complete Guide for B.Tech Interns

---

## TABLE OF CONTENTS
1. [Introduction to Databases](#introduction-to-databases)
2. [SQLite vs PostgreSQL](#sqlite-vs-postgresql)
3. [Database Design Principles](#database-design-principles)
4. [Complete Schema Design](#complete-schema-design)
5. [Setting Up Development Database](#setting-up-development-database)
6. [Data Relationships Explained](#data-relationships-explained)
7. [Milestone-wise Database Evolution](#milestone-wise-database-evolution)
8. [Backup, Security & Optimization](#backup-security--optimization)
9. [Integration with Backend](#integration-with-backend)

---

## Introduction to Databases

### What is a Database?
A database is an organized collection of data:
- **Like a filing cabinet**: Files organized in folders
- **Like a library**: Books organized by category
- **Like Excel spreadsheet**: Rows and columns with data

### Why Do We Need Databases?
1. **Store data permanently** (even after app closes)
2. **Organize data** (by type, date, user, etc.)
3. **Search quickly** (find vessels, ports, users)
4. **Prevent duplicates** (one vessel record)
5. **Set relationships** (user has many vessel alerts)
6. **Security** (encrypt passwords, limit access)

### Key Database Concepts

**Table**: Like a spreadsheet with rows and columns
~~~
Vessels Table:

 ID    Name      Type     Flag  

 1   MAERSK   Container  DE     
 2   SHELL     Tanker    GB     
 3   COSCO    Container  CN     

~~~

**Column (Field)**: A property of the data
- Vessels: ID, Name, Type, Flag, Length, Width...
- Users: Username, Email, Password, Role...

**Row (Record)**: One complete entry
- One vessel: "MAERSK" Container Ship from Germany
- One user: "john" with email "john@example.com"

**Primary Key**: Unique identifier for each row
- Vessel ID: 1, 2, 3... (each vessel has unique ID)
- User ID: 1, 2, 3... (each user has unique ID)

**Foreign Key**: Link between tables
- Vessel Alert has user_id  Connects to Users table
- Vessel Position has vessel_id  Connects to Vessels table

---

## SQLite vs PostgreSQL

### SQLite (Development)
~~~
What: Lightweight, file-based database
When to use: Development and testing
Store location: Single db.sqlite3 file on disk
Setup: No installation needed!
Scalability: Good for 1-3 users
Performance: Fast for small datasets
Best for: Learning, prototyping, small projects

Pros:
   No setup required
   Zero configuration
   Perfect for development
   Built into Django
   Small file size

Cons:
   Not suitable for production
   Limited concurrent users
   No user management
   Slower with large datasets
~~~

### PostgreSQL (Production)
~~~
What: Industrial-strength, server-based database
When to use: Production and real applications
Setup: Requires installation and configuration
Scalability: Handles thousands of concurrent users
Performance: Optimized for large datasets
Best for: Real applications, business systems

Pros:
   Handles many users simultaneously
   Advanced features (JSON, arrays, etc.)
   Very reliable and stable
   Excellent performance
   Professional backup/recovery tools

Cons:
   Requires server setup
   More complex configuration
   Need system administrator knowledge
   Higher resource usage
~~~

### Comparison Table
~~~
Feature            SQLite       PostgreSQL

Setup Time        < 1 minute   10-30 minutes
Users Support     1-3          Unlimited
Data Size         Up to GB     Unlimited
Concurrent Ops    Limited      Thousands
Transactions      Basic        Advanced
Backup Tools      Simple       Advanced
Production Ready  No           Yes
~~~

### Our Migration Plan
~~~
Weeks 1-8 (Development):
  Use SQLite for fast iteration

Week 8+ (Production):
  Migrate to PostgreSQL
  One simple command: Change DATABASE_URL in .env
~~~

---

## Database Design Principles

### 1. Normalization (Avoid Duplication)

**BAD - Data Duplication:**
~~~
Vessels Table:

 ID    Name      All_Related_Data_Here        

 1   MAERSK    Owner: Maersk, Length: 399,... 
 2   SHELL     Owner: Shell, Length: 280,...  
 1   MAERSK    Owner: Maersk, Length: 399,...   DUPLICATE!

~~~

**GOOD - Normalized:**
~~~
Vessels Table:           Companies Table:
       
 ID    Name           ID  Name   
       
 1   MAERSK    1   Maersk 
 2   SHELL     2   Shell  
       
~~~

### 2. Data Integrity (Ensure Consistency)

~~~ python
# Vessel MUST have a valid name
name = models.CharField(max_length=255)  # Required

# Vessel status MUST be one of predefined values
status = models.CharField(
    max_length=50,
    choices=[('in_transit', 'In Transit'), ('in_port', 'In Port')]
)

# Vessel owner is optional
owner = models.CharField(max_length=255, blank=True)

# If vessel is deleted, remove related positions
positions = models.ForeignKey(
    Vessel,
    on_delete=models.CASCADE
)
~~~

### 3. Relationships

**One-to-One (1:1)**
~~~
User  UserProfile
One user has exactly one profile
One profile belongs to one user

In database:
UserProfile.user_id = User.id
~~~

**One-to-Many (1:N)**
~~~
Vessel  VesselPosition (Multiple)
One vessel has many position records
One position belongs to one vessel

In database:
VesselPosition.vessel_id = Vessel.id
~~~

**Many-to-Many (M:N)**
~~~
Vessel  Port (Via ArrivalDeparture)
One vessel can visit many ports
One port can have many vessels

In database:
VesselPort table:
vessel_id | port_id
~~~

---

## Complete Schema Design

### User Management System

**Users Table:**
~~~sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example data:
-- 1, 'john_doe', 'john@example.com', 'hashed_password...', 'John', 'Doe'
-- 2, 'jane_smith', 'jane@example.com', 'hashed_password...', 'Jane', 'Smith'
~~~

**UserProfile Table:**
~~~sql
CREATE TABLE user_profiles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL,  -- 'operator', 'analyst', 'admin'
    company VARCHAR(255),
    phone_number VARCHAR(20),
    is_email_verified BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Example data:
-- 1, 1, 'operator', 'Shipping Co', '+1234567890', true
-- 2, 2, 'analyst', 'Port Authority', '+0987654321', false
~~~

**Why two tables?**
- User table: Authentication (username, password, email)
- Profile table: Extended info (role, company, phone)
- Keeps concerns separate
- Reuse if needed

### Vessel Tracking System

**Vessels Table:**
~~~sql
CREATE TABLE vessels (
    id INT PRIMARY KEY AUTO_INCREMENT,
    imo INT UNIQUE NOT NULL,           -- International Maritime Org number
    mmsi BIGINT UNIQUE NOT NULL,       -- Maritime ID for AIS
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50),                  -- 'Container', 'Tanker', 'Bulk'
    flag VARCHAR(3),                   -- Country code: 'US', 'UK', 'CN'
    status VARCHAR(50),                -- 'in_transit', 'in_port', 'anchored'
    owner VARCHAR(255),
    year_built INT,
    length DECIMAL(8,2),
    beam DECIMAL(8,2),
    last_position_lat DECIMAL(10,8),
    last_position_lon DECIMAL(11,8),
    last_position_update TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
~~~

**VesselPositions Table:**
~~~sql
CREATE TABLE vessel_positions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vessel_id INT NOT NULL,
    latitude DECIMAL(10,8) NOT NULL,
    longitude DECIMAL(11,8) NOT NULL,
    speed DECIMAL(5,2),                -- Knots
    heading DECIMAL(5,2),              -- 0-360 degrees
    timestamp TIMESTAMP NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vessel_id) REFERENCES vessels(id) ON DELETE CASCADE,
    INDEX (vessel_id, timestamp)       -- For fast queries
);

-- Example data:
-- 1, 1, 35.6895, 139.6917, 12.5, 180, '2024-02-12 10:30:00'
-- 2, 1, 35.6900, 139.6920, 12.5, 180, '2024-02-12 10:40:00'
-- Position history shows vessel's journey over time
~~~

**Why VesselPositions separate table?**
- Vessels table: Static info (name, type, owner)
- Positions table: Dynamic data (changing location)
- Separation for performance
- Easy to query historical data

### Port Management System

**Ports Table:**
~~~sql
CREATE TABLE ports (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    unlocode VARCHAR(5) UNIQUE,         -- UN/LOCODE e.g., 'JPTYO'
    city VARCHAR(255),
    country VARCHAR(100),
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    port_type VARCHAR(50),              -- 'Container', 'Bulk', 'Oil'
    number_of_berths INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example data:
-- 1, 'Tokyo Port', 'JPTYO', 'Tokyo', 'Japan', 35.4437, 139.6655
-- 2, 'Shanghai Port', 'CNSHA', 'Shanghai', 'China', 30.8801, 121.6147
~~~

**PortStatistics Table:**
~~~sql
CREATE TABLE port_statistics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    port_id INT UNIQUE NOT NULL,
    total_arrivals INT DEFAULT 0,
    total_departures INT DEFAULT 0,
    current_vessels INT DEFAULT 0,
    average_wait_time DECIMAL(8,2),     -- Hours
    average_berth_time DECIMAL(8,2),    -- Hours
    congestion_level VARCHAR(20),       -- 'low', 'medium', 'high'
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (port_id) REFERENCES ports(id) ON DELETE CASCADE
);
~~~

**CongestionMetrics Table:**
~~~sql
CREATE TABLE congestion_metrics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    port_id INT NOT NULL,
    congestion_percentage DECIMAL(5,2), -- 0-100%
    queue_length INT,                   -- Number of waiting vessels
    estimated_wait_time DECIMAL(8,2),   -- Hours
    timestamp TIMESTAMP NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (port_id) REFERENCES ports(id) ON DELETE CASCADE,
    INDEX (port_id, timestamp)          -- For time-series queries
);

-- Example: Port congestion over time for analytics
-- Day 1: 45% congestion, 3 vessels waiting
-- Day 2: 62% congestion, 5 vessels waiting
-- Day 3: 35% congestion, 2 vessels waiting
~~~

### Safety & Events System

**SafetyEvents Table:**
~~~sql
CREATE TABLE safety_events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(100),                  -- 'collision', 'grounding', 'fire'
    severity VARCHAR(50),               -- 'low', 'medium', 'high', 'critical'
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    description TEXT,
    vessel_id INT,                      -- NULL if no specific vessel
    event_time TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vessel_id) REFERENCES vessels(id) ON DELETE SET NULL
);
~~~

**WeatherAlerts Table:**
~~~sql
CREATE TABLE weather_alerts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    alert_type VARCHAR(100),            -- 'storm', 'high_wind', 'fog'
    severity VARCHAR(50),               -- 'warning', 'alert', 'emergency'
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    location_name VARCHAR(255),
    affected_radius_km DECIMAL(5,1),
    wind_speed INT,                     -- Knots
    wave_height DECIMAL(5,2),           -- Meters
    issued_time TIMESTAMP,
    expires_time TIMESTAMP,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX (is_active, issued_time)     -- For active alerts queries
);
~~~

**PiracyZones Table:**
~~~sql
CREATE TABLE piracy_zones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),                  -- 'Gulf of Aden', 'Malacca Strait'
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    radius_km DECIMAL(5,1),
    threat_level VARCHAR(50),           -- 'low', 'medium', 'high', 'critical'
    description TEXT,
    last_incident TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX (threat_level)
);
~~~

---

## Setting Up Development Database

### With SQLite (Recommended for Development)

**Step 1: No installation needed!**
SQLite comes with Django. Just configure Django:

~~~python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
~~~

**Step 2: Create tables**
~~~bash
python manage.py makemigrations
python manage.py migrate

# Creates db.sqlite3 file with all tables
~~~

**Step 3: View database (Optional)**
~~~bash
# Install SQLite browser
pip install sqlitebrowser

# View the database GUI
sqlitebrowser db.sqlite3
~~~

### With PostgreSQL (For Production)

**Step 1: Install PostgreSQL**
~~~bash
# Windows
# Download from https://www.postgresql.org/download/windows/

# macOS
brew install postgresql

# Linux (Ubuntu)
sudo apt-get install postgresql postgresql-contrib
~~~

**Step 2: Create database and user**
~~~bash
# Open PostgreSQL terminal
psql -U postgres

# Create database
CREATE DATABASE maritime_db;

# Create user
CREATE USER maritime_user WITH PASSWORD 'your_password_here';

# Grant permissions
ALTER ROLE maritime_user SET client_encoding TO 'utf8';
ALTER ROLE maritime_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE maritime_user SET default_transaction_deferrable TO on;
ALTER ROLE maritime_user SET default_transaction_read_only TO off;
ALTER ROLE maritime_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE maritime_db TO maritime_user;

# Exit
\\q
~~~

**Step 3: Connect Django to PostgreSQL**
~~~python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'maritime_db',
        'USER': 'maritime_user',
        'PASSWORD': 'your_password_here',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
~~~

**Step 4: Install PostgreSQL adapter**
~~~bash
pip install psycopg2-binary
~~~

**Step 5: Run migrations**
~~~bash
python manage.py migrate
~~~

---

## Data Relationships Explained

### Example: User Subscribes to Vessel Alerts

**Scenario:**
- User 'john_doe' wants alerts for vessel 'MAERSK'
- When MAERSK changes position, john_doe gets notified

**Database tables involved:**
~~~
users (id=1, username='john_doe')
     
vessel_alerts (user_id=1, vessel_id=5, alert_type='position_change')
     
vessels (id=5, name='MAERSK')
~~~

**Data in each table:**
~~~
users:

 id  username   email            

 1   john_doe   john@example.com 


vessel_alerts:

 id  user_id  vessel_id  alert_type         

 1   1        5          position_change    
 2   1        5          port_arrival       


vessels:

 id  name     type   

 5   MAERSK   Container 

~~~

**How backend handles this:**
~~~python
# Get all alerts for user 'john_doe'
user = User.objects.get(username='john_doe')
alerts = user.vessel_alerts.all()  # Works because of ForeignKey!

# Get all users subscribed to MAERSK
vessel = Vessel.objects.get(name='MAERSK')
subscribers = vessel.alerts.all()  # Reverse relationship

# Send notification to john_doe about MAERSK
for alert in alerts:
    if alert.vessel.name == 'MAERSK':
        send_notification(user, f"{alert.vessel.name} position changed!")
~~~

---

## Milestone-wise Database Evolution

### Milestone 1 (Week 1-2): Authentication
**Tables created:**
- users (Django built-in)
- user_profiles (custom)

**Operations:**
- Register users
- Login/logout
- Store passwords (hashed, not plain!)

### Milestone 2 (Week 3-4): Vessel Tracking
**Tables created:**
- vessels
- vessel_positions
- vessel_routes
- vessel_alerts

**Operations:**
- Store vessel data from MarineTraffic API
- Store position history
- Track user subscriptions

### Milestone 3 (Week 5-6): Port & Safety Analytics
**Tables created:**
- ports
- port_statistics
- congestion_metrics
- safety_events
- weather_alerts
- piracy_zones
- accident_history

**Operations:**
- Calculate port congestion
- Store weather data from NOAA
- Manage safety zone information

### Milestone 4 (Week 7-8): Historical Data
**Tables created:**
- voyages
- voyage_history
- compliance_records

**Operations:**
- Store voyage records
- Historical playback data
- Compliance audit trails

---

## Backup, Security & Optimization

### Creating Backups

**SQLite Backup:**
~~~bash
# Simple file copy (SQLite is just a file!)
cp db.sqlite3 db.sqlite3.backup_2024_02_12

# That's it! File is safe
~~~

**PostgreSQL Backup:**
~~~bash
# Full database dump
pg_dump -U maritime_user maritime_db > backup_2024_02_12.sql

# Compressed backup (smaller file)
pg_dump -U maritime_user -F c maritime_db > backup_2024_02_12.dump

# Restore from backup
psql -U maritime_user maritime_db < backup_2024_02_12.sql
~~~

**Automated daily backups (Linux/macOS):**
~~~bash
#!/bin/bash
# save as backup.sh

TIMESTAMP=\
BACKUP_DIR="/backups/maritime"

mkdir -p \
pg_dump -U maritime_user maritime_db > \/backup_\.sql

# Keep only last 30 days
find \ -name "backup_*.sql" -mtime +30 -delete

echo "Backup completed: \/backup_\.sql"
~~~

Add to crontab (runs daily at 2 AM):
~~~bash
crontab -e
# Add line:
0 2 * * * /path/to/backup.sh
~~~

### Database Security

**1. Password Hashing:**
~~~python
# NEVER store plain passwords!
user.set_password('mypassword')  # Django hashes it
user.save()

# To verify password during login:
user.check_password('mypassword')  # Returns True/False
~~~

**2. SQL Injection Prevention:**
~~~python
# DANGEROUS - Don't do this!
query = f"SELECT * FROM users WHERE username = '{username}'"
User.objects.raw(query)  # Vulnerable!

# SAFE - Use Django ORM
User.objects.filter(username=username)  # ORM handles escaping
~~~

**3. Access Control:**
~~~python
# Only authorized users can access their data
def get_vessels(request):
    if request.user.role == 'admin':
        return Vessel.objects.all()
    elif request.user.role == 'analyst':
        return Vessel.objects.filter(flag=request.user.company_country)
    else:  # operator
        return Vessel.objects.filter(is_public=True)
~~~

### Database Optimization

**Add Indexes for Speed:**
~~~sql
-- Queries look up vessels by MMSI often
CREATE INDEX idx_vessels_mmsi ON vessels(mmsi);

-- Queries filter positions by vessel and time
CREATE INDEX idx_positions_vessel_time ON vessel_positions(vessel_id, timestamp DESC);

-- Queries get active alerts
CREATE INDEX idx_alerts_active ON vessel_alerts(is_active, created_at);
~~~

**Query Optimization:**
~~~python
# SLOW - N+1 query problem
vessels = Vessel.objects.all()
for vessel in vessels:
    print(vessel.owner.company)  # Queries database for EACH vessel!
# Runs 101 queries (1 for vessels + 100 for owners)

# FAST - Use select_related
vessels = Vessel.objects.select_related('owner').all()
for vessel in vessels:
    print(vessel.owner.company)  # Already loaded!
# Runs only 1 query

# FAST - Use prefetch_related for many-to-many
vessels = Vessel.objects.prefetch_related('positions').all()
for vessel in vessels:
    for pos in vessel.positions.all():  # Already loaded!
        print(pos.latitude)
# Runs only 2 queries total
~~~

---

## Integration with Backend

### How Backend Uses Database

**Example 1: Get all vessels**
~~~python
# views.py
def list_vessels(request):
    # Query: Get all vessels from database
    vessels = Vessel.objects.all()
    
    # Serialize: Convert Python objects to JSON
    serializer = VesselSerializer(vessels, many=True)
    
    # Return JSON to frontend
    return Response(serializer.data)
~~~

**Frontend receives:**
~~~json
{
  "results": [
    {"id": 1, "name": "MAERSK", "lat": 35.6, "lon": 139.6},
    {"id": 2, "name": "COSCO", "lat": 33.1, "lon": 130.2}
  ]
}
~~~

**Example 2: Save vessel position**
~~~python
# When receiving data from MarineTraffic API
from apps.vessels.models import VesselPosition

# Create and save new position record
position = VesselPosition.objects.create(
    vessel_id=1,
    latitude=35.6895,
    longitude=139.6917,
    speed=12.5,
    heading=180,
    timestamp=timezone.now()
)
# Data saved to database automatically!
~~~

**Example 3: Filter vessels**
~~~python
# Frontend sends filter: show only Container Ships
vessels = Vessel.objects.filter(
    type='container',        # Type is Container
    status='in_transit',     # Currently sailing
    flag='DE'                # German flagged
)

# Returns matching vessels
~~~

---

## Common Issues & Solutions

**Issue: "Relation does not exist"**
~~~
Solution: Run migrations!
python manage.py migrate
~~~

**Issue: "Duplicate key violation"**
~~~
Solution: Ensure unique fields have unique values
Check for duplicate entries:
select username, count(*) from users group by username having count(*) > 1;
~~~

**Issue: "Database is locked"**
~~~
Solution: SQLite issue - only one write at a time
# Not a problem with PostgreSQL in production
~~~

**Issue: Slow queries**
~~~
Solution: Add indexes and optimize queries
python manage.py shell
from django.db import connections
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connections['default']) as context:
    # Your code here
    vessels = Vessel.objects.all()

print(f"Number of queries: {len(context)}")
for query in context:
    print(query['sql'])
~~~

---

## Database Migration Best Practices

**When making schema changes:**

~~~bash
# 1. Make changes to models.py file
# Example: Add new field to Vessel
vessel_length = models.DecimalField(max_digits=8, decimal_places=2, null=True)

# 2. Create migration file
python manage.py makemigrations vessels

# 3. Review the SQL that will be executed
python manage.py sqlmigrate vessels 0002

# 4. Apply migration
python manage.py migrate

# 5. Never edit migration files manually!
# Always create new migrations for changes
~~~

---

## Summary

**Key Takeaways:**
1.  Database stores ALL your application data
2.  Use SQLite for development (0 setup)
3.  Migrate to PostgreSQL for production
4.  Design schemas with relationships (1:1, 1:N, M:N)
5.  Always normalize data (no duplication)
6.  Use Django ORM (safe from SQL injection)
7.  Add indexes for frequently queried fields
8.  Backup regularly (daily!)
9.  Never store plain passwords (always hash)
10.  Implement proper access control

---

**Last Updated**: February 2026
**Database Version**: 1.0.0
**Development**: SQLite | Production: PostgreSQL 13+
