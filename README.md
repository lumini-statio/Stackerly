# 📦 Stock App

Stock and Order Management web application built with Django 🧩

---

## ✨ Features

- 🔐 **User management** (registration, login, logout, profile)
- 🏬 **Store management**
- 📦 **Product management per store**
- 📝 **Order management per user**
- 📊 **Interactive tables** using `django-tables2`
- 🎨 **Styled forms** with `django-crispy-forms` + Bootstrap 5

---

## 🧱 Project Structure

```
app/        → Main Django config (settings, urls, wsgi, asgi)
stock/      → Main logic (models, views, forms, templates, components)
static/     → Static assets (CSS, JS, Bootstrap)
templates/  → HTML templates
```

---

## 🚀 Installation

1. **Clone the repository**
    ```sh
    git clone <repo-url>
    cd stock_app
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  
    # On Windows: 
    venv\Scripts\activate
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply database migrations**
    ```sh
    python manage.py migrate
    ```

5. **(Optional) Create a superuser**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```sh
    python manage.py runserver
    ```

---

## 🧪 Usage

Open your browser at 👉 [http://localhost:8000/](http://localhost:8000/)

Sign up or log in to manage stores, products, and orders.

---

## ⚙️ Core Dependencies

- 🌐 Django 4.2
- 📊 django-tables2
- 🎨 django-crispy-forms
- 💠 crispy-bootstrap5
- 🔍 django-filter
- ⚡ polars

---

## 🧬 Model Overview

- 👤 **User**: `username`, `email`, `password`, `is_superuser`
- 🏬 **Store**: `name`, `location`, `capacity`
- 📦 **Product**: `name`, `price`, `type`, `model`, `related_store`
- 🧾 **Order**: `product`, `user`, `date`

---

## 🎨 Customization

- 💅 **Styles**: Located in `stock/static/css/` (uses Bootstrap 4/5)
- 📋 **Tables**: Customizable in `stock/components/tables.py`
- 📝 **Forms**: Built with crispy-forms, editable in `stock/forms.py`

---

Ready to manage your stock like a pro? Let’s go! 🚀