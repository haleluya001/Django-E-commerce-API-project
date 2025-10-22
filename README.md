Django E-commerce Core API (ALX Capstone Project)

🎯 Project Overview

This is a robust, secure, and scalable RESTful API designed to serve as the back-end foundation (the "engine room") for a modern e-commerce platform. Built on industry-standard frameworks, the API handles all core business logic, including product catalog management, administrative access control, and user authentication, ensuring a reliable data layer for any client (web, mobile, or third-party service).

The primary goal is to provide a clean separation of concerns, delivering a secure, JSON-based API that is deployment-ready.

✨ Core Features (Completed)

The API currently implements the essential functionalities for catalog and administrative management:

Secure User Authentication: Implements token-based authentication (auth/token/login/) to secure all administrative endpoints.

Categories Management: CRUD (Create, Read, Update, Delete) operations for product categorization.

Endpoint: /api/v1/items/categories/

Product Management: Full CRUD operations for detailed product information (name, price, category, images, etc.).

Endpoint: /api/v1/items/products/

Separated Data Logic: Clear division of features into dedicated Django applications (item, core, dashboard).

Media Handling: Configuration to handle product image uploads and storage.

🛠️ Tech Stack and Dependencies

This project leverages modern Python and Django best practices.

Component

Technology

Role

Backend Framework

Python 3.x, Django 5.x

Core application logic and ORM.

API

Django REST Framework (DRF)

Handling serialization, views, and routing for RESTful endpoints.

Authentication

Django Rest Auth / Djoser (or similar)

Secure token-based user authentication.

Database (Development)

SQLite 3

Lightweight database for local development. (Easily swapped for PostgreSQL/MySQL in production.)

🚀 Installation and Setup

Follow these steps to get a local copy of the project running on your machine.

Prerequisites

Python 3.x

pip (Python package installer)

1. Clone the Repository

git clone [https://github.com/haleluya001/Django-E-commerce-API-project.git](https://github.com/haleluya001/Django-E-commerce-API-project.git)
cd Django-E-commerce-API-project


2. Configure Environment

Create a virtual environment (recommended) and install dependencies.

# Create and activate virtual environment
python -m venv env
source env/bin/activate 

# Install django on your virtual environment
pip install django

#Install crispy_forms
pip install django-crispy-forms 

#Install Pillow 
pip install pillow 


3. Database Setup and Migration

Apply the database schema changes:

python manage.py migrate


4. Create an Administrator User

Create a superuser to access protected endpoints and the Django Admin:

python manage.py createsuperuser


5. Run the Server

Start the local development server:

python manage.py runserver


The API will now be accessible at http://127.0.0.1:8000/.

⏭️ Next Steps and Future Work

The immediate focus for future development will be to complete the full e-commerce lifecycle:

Shopping Cart and Order Logic: Implement models and views for adding items to a cart, calculating totals, and finalizing orders.

Payment Service Integration: Connect to a third-party payment gateway (e.g., Stripe, PayPal) for processing transactions.

Optimizing API Performance: Implement caching and query optimization strategies for high traffic.

📁 Project Structure

Django-E-commerce-API-project/
│
├─ config/           # Project settings and URL routing
├─ core/             # User and Authentication logic
├─ dashboard/        # Administrative interfaces / logic
├─ item/             # Product and Category management application
├─ media/            # Stores uploaded product images (ignored by Git)
├─ manage.py
└─ requirements.txt
