# Django E-commerce API Project

A RESTful API built with Django and Django REST Framework (DRF) for an e-commerce platform. This project allows users to view, create, update, and manage products, categories, and orders.

## Features

- User authentication and registration
- Product listing and details
- Categories management
- Shopping cart functionality
- Order management
- Media support for product images
- Admin dashboard for managing products and orders

## Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- SQLite (default; can be changed to PostgreSQL or MySQL)
- JWT Authentication (optional, if implemented)

## Project Structure

Django-E-commerce-API-project/
│
├─ config/ # Project settings
├─ core/ # Core app (e.g., user management)
├─ dashboard/ # Admin dashboard
├─ item/ # Product and category management
├─ media/items_images/ # Product images
├─ db.sqlite3 # Database
└─ manage.py # Django management script


## Installation

1. Clone the repository:


git clone https://github.com/haleluya001/Django-E-commerce-API-project.git
cd Django-E-commerce-API-project


2. Create a virtual environment and activate it:

python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

3. Install dependencies:

pip install -r requirements.txt


4. Apply migrations:

python manage.py migrate


5. Create a superuser:

python manage.py createsuperuser


6. Run the development server:

python manage.py runserver
