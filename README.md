#Stock App

Stock and order management web application, built with Django.

## Features

- User management (registration, login, logout, profile)
- Store management
- Product management per store
- Order management per user
- Interactive tables using [django-tables2](https://django-tables2.readthedocs.io/)
- Styled forms with [django-crispy-forms](https://django-crispy-forms.readthedocs.io/) and Bootstrap 5

## Project Structure

- `app/`: Main Django configuration (settings, urls, wsgi, asgi)
- `stock/`: Main application with models, views, forms, components, and templates
- `static/`: Static files (CSS, JS, Bootstrap)
- `templates/`: HTML templates

## Installation

1. **Clone the repository**
```sh
git clone <repo-url>
cd stock_app
```

2. **Create a virtual environment and activate it**
```sh
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```sh
pip install -r requirements.txt
```

4. **Apply migrations**
```sh
python manage.py migrate
```

5. **Create a superuser (optional)**
```sh
python manage.py createsuperuser
```

6. **Run the server**
```sh
python manage.py runserver
```

## Usage

- Access the application at http://localhost:8000/
- Sign up or log in to manage stores, products, and orders.

## Core Dependencies

- Django 4.2
- django-tables2
- django-crispy-forms
- crispy-bootstrap5
- django-filter
- polars

## Model Structure

- **Store**: name, location, capacity
- **Product**: name, price, type, model, related store
- **Order**: product, user, date

## Customization

- Styles use Bootstrap 4/5 and can be modified in `stock/static/css/`.
- Tables can be customized in `stock/components/tables.py`.
- Forms use crispy-forms and can be customized in `stock/forms.py`.