# 🎓 Capstone Project: Enterprise E-commerce REST API Backend

## 1. Project Overview & Goal
This project implements a complete, headless backend for an enterprise-level e-commerce application. The core goal is to provide a highly scalable, secure, and maintainable RESTful API that can be consumed by multiple frontend clients (web, mobile, third-party services).

The API is built using the robust Django framework and the powerful Django REST Framework (DRF), ensuring rapid development and adherence to modern web standards.

**Key Responsibilities:**
- Securely manage user accounts and access tokens.
- Provide comprehensive product catalog and inventory management endpoints.
- Handle stateful logic for shopping carts and transactional order processing.

---

## 2. Core Architecture and Data Flow
The architecture follows a modular, monolithic structure, with distinct Django applications managing specific business domains.

### 2.1 Project Structure
Django-E-commerce-API-project/
│
├─ config/ # Main project settings, root URLs, and application environment config.
├─ core/ # Custom User model, base permissions, and core authentication logic.
├─ item/ # The Product Catalog: Models/Views for Product, Category, and Inventory.
├─ conversation/ # Dedicated functionality for real-time chat between buyers and sellers (Scalability TBD).
├─ dashboard/ # Administrative API endpoints (restricted access for staff/management tools).
├─ media/ # Storage location for user-uploaded assets (product images).
├─ manage.py # Django's management utility.
└─ requirements.txt # Project dependencies list.

pgsql
Copy code

---

## 3. Technology Stack (Backend)

| Technology | Version/Standard | Purpose in Project |
|------------|-----------------|------------------|
| Python/Django | Python 3.x, Django 5.x | Core application logic, ORM, and template-less routing |
| Django REST Framework (DRF) | Latest | Serialization, declarative views, and robust request handling |
| DRF Simple JWT | Latest | Secure, stateless, token-based authentication (Access/Refresh Tokens) |
| SQLite3 | Default | Local development and rapid prototyping (ready for PostgreSQL/MySQL migration) |
| Pillow | Latest | Image manipulation and validation for product media uploads |
| python-decouple | Latest | Secure separation of secrets and configuration parameters from code |
| gunicorn, whitenoise | Latest | Production WSGI server and efficient serving of static/media files |

---

## 4. Key API Endpoints
All API endpoints are prefixed with `/api/v1/`.

| Domain | Endpoint | Method(s) | Description |
|--------|---------|-----------|-------------|
| Auth | `/api/v1/users/register/` | POST | Create a new user account (public) |
| Auth | `/api/v1/token/` | POST | Exchange username/password for JWT tokens (public) |
| Auth | `/api/v1/token/refresh/` | POST | Obtain a new Access Token using the Refresh Token (public) |
| Catalog | `/api/v1/products/` | GET | List all available products (supports filtering/search) (public) |
| Catalog | `/api/v1/products/{id}/` | GET | Retrieve details for a specific product (public) |
| Cart | `/api/v1/cart/` | GET, POST | View or create a new cart entry (required) |
| Cart | `/api/v1/cart/{item_id}/` | PUT, DELETE | Update quantity or remove an item from the cart (required) |
| Order | `/api/v1/orders/` | POST | Finalize checkout and create a new order from the cart (required) |
| Order | `/api/v1/orders/{id}/` | GET | Retrieve a specific order's details (required) |

---

## 5. Setup and Installation Guide

### 5.1 Clone the Repository
```bash
git clone https://github.com/haleluya001/Django-E-commerce-API-project.git
cd Django-E-commerce-API-project
5.2 Set up a Virtual Environment
bash
Copy code
python -m venv env
# Linux/Mac:
source env/bin/activate
# Windows:
.\env\Scripts\activate
5.3 Install Dependencies
bash
Copy code
pip install -r requirements.txt
5.4 Configure Environment Variables
Create a .env file in the root directory:

env
Copy code
SECRET_KEY='YOUR_LONG_RANDOM_SECRET_KEY_HERE'
DEBUG=True
ALLOWED_HOSTS='*'
# DATABASE_URL=... (for production)
5.5 Database Initialization
bash
Copy code
python manage.py migrate
5.6 Create Administrative User
bash
Copy code
python manage.py createsuperuser
5.7 Run the Development Server
bash
Copy code
python manage.py runserver
