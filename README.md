**Django Calculator Project**

A simple web-based calculator built using Django, HTML, CSS.

**Features**

    Perform basic arithmetic operations (Addition, Subtraction, Multiplication, Division)
    
    User-friendly interface
    
    Built with Django for backend logic
    
    Project Structure

calculator_project/          # Root project directory
│── calculator/              # Django app for the calculator
│   │── migrations/          # Database migrations (auto-generated)
│   │── static/              # Static files (CSS, JS, images)
│   │   └── style.css        # CSS for styling the calculator
│   │── templates/           # HTML templates
│   │   └── calculator.html  # Calculator UI
│   │── __init__.py          # Marks this as a Python package
│   │── admin.py             # Admin panel configurations (optional)
│   │── apps.py              # App configuration
│   │── models.py            # Database models (not needed for this project)
│   │── tests.py             # Test cases (optional)
│   │── urls.py              # URL routing for the app
│   │── views.py             # Logic for handling calculations
│── calculator_project/      # Main Django project directory
│   │── __init__.py          # Marks this as a Python package
│   │── asgi.py              # ASGI config (for async servers)
│   │── settings.py          # Project settings (add calculator app here)
│   │── urls.py              # Main project URLs (includes calculator app URLs)
│   │── wsgi.py              # WSGI config (for deployment)
│── db.sqlite3               # SQLite database file (auto-generated)
│── manage.py                # Django project management script

**Installation & Setup**

1. Clone the repository

git clone https://github.com/vemularajesh225/django-calculator.git
cd django-calculator

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3. Install dependencies

pip install -r requirements.txt

4. Run database migrations

python manage.py migrate

5. Run the development server

python manage.py runserver

Access the calculator at: http://127.0.0.1:8000/

**Usage**

Enter a mathematical expression in the input field.

Click the "Calculate" button.

The result will be displayed below.

**Contributing**

Feel free to fork the repository and submit pull requests!

**License**

This project is open-source and available under the MIT License.
