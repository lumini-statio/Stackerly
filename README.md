# 📦 Stock App

Stock and Order Management web application built with Django

---

## 📰​ Features

- **User management** (registration, login, logout, profile)
- **Store management**
- **Product management per store**
- **Order management per user**
- **Interactive tables**
- **Styled forms**

---

## 🧱 Project Structure

```
stackerly/
├── app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
|   ├── middlewares.py
│   └── wsgi.py
├── stock/
│   ├── components/
│   ├── management/
│   ├── migrations/
│   ├── static
│   │   ├── css/
│   │   ├── js/
│   │   └── webfonts/
│   ├── templates/
│   ├── views/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── managers.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── utils.py
└── manage.py
```

---

## 🚀 Installation

1. **Clone the repository**
    ```sh
    git clone <repo-url>
    cd Stackerly
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

Open your browser at --> [stackerly.onrender.com](https://stackerly.onrender.com/)

Sign up or log in to manage stores, products, and orders.

---

## ⚙️ Core Dependencies

- Django 4.2
- django-tables2
- django-crispy-forms
- crispy-bootstrap5
- django-filter
- polars
- openpyxl

---

## 👷‍♂️​ Model Overview

- **CustomUser**: `username`, `email`, `first_name`, `last_name`, `is_superuser`, `is_staff`, `is_active`, `date_joined`, `objects`
- **Location**: `name`
- **BalanceBox**: `current_amount`, `last_update`, `location`
- **Store**: `name`, `location`, `balance_box`
- **ProfitLossRecord**: `date`, `amount`, `record_type`, `related_store`
- **Purchase**: `purchase_item`, `spent`, `date`, `related_store`
- **ProductState**: `name`
- **Product**: `name`, `price`, `type`, `model`, `quantity`, `related_store`, `state`, `last_updated_state`
- **UserPurchase**: `product`, `user`, `quantity`
- **Order**: `user`, `date`

---

## 🎨 Customization

- **Styles**: Located in `stock/static/css/` (uses Bootstrap 4/5)
- **Tables**: Customizable in `stock/components/tables.py`
- **Forms**: Built with crispy-forms, editable in `stock/forms.py`

---
