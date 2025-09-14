E-commerce API - Setup and Running Instructions
Prerequisites
Python 3.8 or higher

MySQL Server 8.0 or higher

Git (for cloning the repository)

Installation Steps

1. Clone or Download the Project
   bash
   git clone <your-repository-url>
   cd ecommerce-api
2. Set Up Virtual Environment
   Windows:

bash
python -m venv venv
venv\\Scripts\\activate
macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Set Up MySQL Database
Start MySQL service

Log into MySQL: mysql -u root -p

Create database: CREATE DATABASE ecommerce\_store;

Exit MySQL and run: mysql -u root -p ecommerce\_store < database/ecommerce\_store.sql

5. Configure Environment
   bash
   cp .env.example .env

# Edit .env file with your database credentials

6. Run the Application
   bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
7. Access the API
   Main endpoint: http://localhost:8000

Interactive docs: http://localhost:8000/docs

Alternative docs: http://localhost:8000/redoc

Testing the API
Use the interactive documentation or curl commands to test endpoints:

bash

# Test API is running

curl http://localhost:8000/

# Get all products

curl http://localhost:8000/products/
Troubleshooting
Ensure MySQL service is running

Verify database credentials in .env file

Check if port 8000 is available

The API will automatically reload when you make code changes during development.

