🩺 Diabetes Management System

A simplified platform that helps patients and doctors track and manage diabetes-related data such as glucose readings, medications, diet, and daily activities. The backend is fully developed using Django with clean architecture and secure API endpoints.

📌 Project Summary

This project provides a digital solution for diabetes management, allowing patients to log their daily health data while giving doctors access to monitor patient progress. The backend focuses on data accuracy, security, and scalability.

⚙️ Backend (Django)

The backend handles all operations related to users, health data, authentication, and reporting. It is built using Django REST Framework (DRF) to provide a clean and structured API layer.

Key Backend Features

User registration & login (JWT authentication)

Role-based access (Patient / Doctor)

Glucose level tracking API

Medication & diet logging

Activity tracking (exercise, steps, etc.)

Health reports generation

Full CRUD operations for all health records

Centralized validation through DRF serializers

Django Admin dashboard for system management

📡 Main API Endpoints Authentication

POST /api/auth/register/ – create an account

POST /api/auth/login/ – get JWT token

Glucose

GET /api/glucose/ – fetch patient readings

POST /api/glucose/add/ – add new reading

Medications

GET /api/medications/

POST /api/medications/add/

Diet & Activities

POST /api/diet/add/

POST /api/activity/add/

🏗 Project Structure /backend │── diabetes_project/ │── api/ │ ├── users/ │ ├── glucose/ │ ├── medications/ │ ├── diet/ │ ├── activity/ │ └── reports/ └── manage.py

🚀 Installation Steps

Clone the project

git clone https://github.com/your-username/diabetes-management.git

Create virtual environment

python -m venv venv

Install requirements

pip install -r requirements.txt

Run migrations

python manage.py migrate

Start server

python manage.py runserver

📊 Future Improvements

Mobile app integration

AI-based sugar level predictions

PDF/Excel health reports

Wearable device syncing
