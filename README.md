```markdown
# QR Code Generation System

A Flask-based web application that generates QR codes from URLs and stores them in PostgreSQL database.

## Prerequisites

* Python 3.7 or higher
* PostgreSQL 15 or higher
* pip (Python package installer)

## PostgreSQL Setup

### Install PostgreSQL (macOS)
```bash
brew install postgresql@15
brew services start postgresql@15
```

### Create Database and User
Connect to PostgreSQL:
```bash
psql postgres
```

In PostgreSQL prompt, run:
```sql
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE qrdb;
GRANT ALL PRIVILEGES ON DATABASE qrdb TO myuser;
\c qrdb
GRANT ALL ON SCHEMA public TO myuser;
GRANT ALL ON ALL TABLES IN SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO myuser;
ALTER DATABASE qrdb OWNER TO myuser;
```

## Installation

### 1. Clone Repository
```bash
git clone [repository-url]
cd [repository-name]
```

### 2. Virtual Environment Setup
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install Flask==2.0.1
pip install Flask-CORS==3.0.10
pip install SQLAlchemy==1.4.23
pip install psycopg2-binary==2.9.1
pip install qrcode==7.3
pip install Pillow==8.3.1
```

### 4. Configure Database
Update `POSTGRES_URI` in `config.py`:
```python
POSTGRES_URI: str = 'postgresql://myuser:mypassword@localhost:5432/qrdb'
```

## Running the Application

1. Start Flask server:
```bash
flask run
```

2. Access application:
   * Open `http://localhost:5000` in web browser
   * Enter URL in input field
   * Click "Generate QR Code"

## Project Structure
```
.
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── models.py           # Database models
├── services.py         # Business logic
├── static/
│   └── index.html     # Frontend interface
└── requirements.txt    # Python dependencies
```

## Features

* QR code generation from URLs
* PostgreSQL storage of QR codes as binary data
* Simple web interface
* RESTful API endpoint
* Error handling and logging

## API Endpoint

**GET** `/api/qr?url=[url]`
* Generates and returns QR code image for given URL
* Returns stored image if QR code exists
* Generates new QR code and stores if new URL

## Troubleshooting

### Database Connection Issues
Check PostgreSQL service status:
```bash
brew services list | grep postgres
```

Restart PostgreSQL if needed:
```bash
brew services restart postgresql@15
```

### Database Permissions
Check database access:
```bash
psql -U myuser -d qrdb -h localhost
```

Verify table creation:
```sql
\dt  # List all tables
```
```