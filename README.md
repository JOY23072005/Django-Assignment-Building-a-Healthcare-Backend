# 🏥 Healthcare Backend API

A RESTful Healthcare Backend built using **Django**, **Django REST Framework (DRF)**, **PostgreSQL**, and **JWT Authentication**. This project provides secure authentication and APIs for managing patients, doctors, and patient-doctor mappings.

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- User Login
- JWT Authentication using SimpleJWT
- Refresh Token Support

### 👨‍⚕️ Patient Management
- Add Patient
- View All Patients (created by authenticated user)
- View Patient by ID
- Update Patient
- Delete Patient

### 🩺 Doctor Management
- Add Doctor
- View All Doctors
- View Doctor by ID
- Update Doctor
- Delete Doctor

### 🔗 Patient-Doctor Mapping
- Assign Doctor to Patient
- View All Patient-Doctor Mappings
- View Doctors Assigned to a Patient
- Remove Doctor from Patient

### 🛡 Security
- JWT Protected APIs
- Password Hashing using Django Authentication
- Environment Variables for Sensitive Data
- Input Validation using DRF Serializers

---

# 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework (DRF)
- PostgreSQL (Supabase)
- Django ORM
- SimpleJWT
- python-dotenv / django-environ

---

# 📁 Project Structure

```
healthcare-backend/
│
├── accounts/
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
├── patients/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
├── doctors/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
├── mappings/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
├── common/
│   └── models.py
│
├── config/
│
├── manage.py
├── requirements.txt
└── .env
```

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/JOY23072005/Django-Assignment-Building-a-Healthcare-Backend.git
```

```bash
cd Django-Assignment-Building-a-Healthcare-Backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=postgres

DB_USER=your_database_user

DB_PASSWORD=your_database_password

DB_HOST=your_database_host

DB_PORT=5432
```

---

# 🗄 Database Migration

```bash
python manage.py migrate
```

---

# ▶️ Run Server

```bash
python manage.py runserver
```

Server will start at

```
http://127.0.0.1:8000/
```

---

# 🔐 Authentication

## Register User

**POST**

```
/api/auth/register/
```

Request

```json
{
    "username": "joydeep",
    "email": "joy@example.com",
    "password": "Password@123",
    "first_name": "Joy",
    "last_name": "Hans"
}
```

Response

```json
{
    "message": "User registered successfully."
}
```

---

## Login

**POST**

```
/api/auth/login/
```

Request

```json
{
    "username": "joydeep",
    "password": "Password@123"
}
```

Response

```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

---

## Refresh Token

**POST**

```
/api/auth/refresh/
```

Request

```json
{
    "refresh": "your_refresh_token"
}
```

---

# 🔑 Authorization

Include the access token in every protected request.

```
Authorization: Bearer <access_token>
```

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/api/auth/register/` |
| POST | `/api/auth/login/` |
| POST | `/api/auth/refresh/` |

---

## Patient APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/patients/` | Create Patient |
| GET | `/api/patients/` | Get All Patients |
| GET | `/api/patients/<id>/` | Get Patient Details |
| PUT | `/api/patients/<id>/` | Update Patient |
| DELETE | `/api/patients/<id>/` | Delete Patient |

---

## Doctor APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/doctors/` | Create Doctor |
| GET | `/api/doctors/` | Get All Doctors |
| GET | `/api/doctors/<id>/` | Get Doctor Details |
| PUT | `/api/doctors/<id>/` | Update Doctor |
| DELETE | `/api/doctors/<id>/` | Delete Doctor |

---

## Patient-Doctor Mapping APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/mappings/` | Assign Doctor to Patient |
| GET | `/api/mappings/` | Get All Mappings |
| GET | `/api/mappings/<patient_id>/` | Get Doctors Assigned to Patient |
| DELETE | `/api/mappings/delete/<id>/` | Remove Doctor from Patient |

---

# 🧩 Database Models

## User

Django's built-in `User` model is used for authentication.

---

## Patient

| Field | Type |
|--------|------|
| id | Integer |
| created_by | ForeignKey(User) |
| name | CharField |
| age | PositiveIntegerField |
| gender | CharField |
| phone | CharField |
| address | TextField |
| created_at | DateTime |
| updated_at | DateTime |

---

## Doctor

| Field | Type |
|--------|------|
| id | Integer |
| name | CharField |
| specialization | CharField |
| email | EmailField |
| phone | CharField |
| experience | PositiveIntegerField |
| created_at | DateTime |
| updated_at | DateTime |

---

## PatientDoctorMapping

| Field | Type |
|--------|------|
| id | Integer |
| patient | ForeignKey(Patient) |
| doctor | ForeignKey(Doctor) |
| created_at | DateTime |
| updated_at | DateTime |

---

# 🧪 Testing

The APIs were tested using **Postman**.

### Tested Scenarios

- User Registration
- User Login
- JWT Authentication
- Create Patient
- Get Patients
- Update Patient
- Delete Patient
- Create Doctor
- Get Doctors
- Update Doctor
- Delete Doctor
- Assign Doctor to Patient
- Get All Mappings
- Get Patient's Doctors
- Delete Mapping

---

# 📌 Validation

Implemented using Django REST Framework Serializers.

Examples:

- Email uniqueness
- Username uniqueness
- Phone number validation
- Age validation
- Experience validation

---

# 🔒 Security Features

- JWT Authentication
- Password Hashing
- Protected APIs
- User-specific Patient Records
- Environment Variables
- PostgreSQL Database

---

# 📄 Future Improvements

- Pagination
- Search & Filtering
- Swagger/OpenAPI Documentation
- Docker Support
- Role-Based Access Control (RBAC)
- API Rate Limiting
- Unit Testing
- CI/CD Pipeline

---

# 👨‍💻 Author

**Joydeep Hans**

Backend Developer

- Django
- Django REST Framework
- PostgreSQL
- Python

---

# 📜 License

This project is developed for learning and educational purposes.