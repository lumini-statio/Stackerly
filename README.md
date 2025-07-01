# Stock App

Aplicación web de gestión de stock y órdenes, construida con Django.

## Características

- Gestión de usuarios (registro, login, logout, perfil)
- Gestión de tiendas (Stores)
- Gestión de productos por tienda
- Gestión de órdenes por usuario
- Tablas interactivas usando [django-tables2](https://django-tables2.readthedocs.io/)
- Formularios estilizados con [django-crispy-forms](https://django-crispy-forms.readthedocs.io/) y Bootstrap 5

## Estructura del Proyecto

- `app/`: Configuración principal de Django (settings, urls, wsgi, asgi)
- `stock/`: Aplicación principal con modelos, vistas, formularios, componentes y templates
- `static/`: Archivos estáticos (CSS, JS, Bootstrap)
- `templates/`: Plantillas HTML

## Instalación

1. **Clona el repositorio**
    ```sh
    git clone <url-del-repo>
    cd stock_app
    ```

2. **Crea un entorno virtual y actívalo**
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. **Instala las dependencias**
    ```sh
    pip install -r requirements.txt
    ```

4. **Aplica las migraciones**
    ```sh
    python manage.py migrate
    ```

5. **Crea un superusuario (opcional)**
    ```sh
    python manage.py createsuperuser
    ```

6. **Ejecuta el servidor**
    ```sh
    python manage.py runserver
    ```

## Uso

- Accede a la aplicación en [http://localhost:8000/](http://localhost:8000/)
- Regístrate o inicia sesión para gestionar tiendas, productos y órdenes.

## Dependencias principales

- Django 4.2
- django-tables2
- django-crispy-forms
- crispy-bootstrap5
- django-filter
- polars

## Estructura de modelos

- **Store**: nombre, ubicación, capacidad
- **Product**: nombre, precio, tipo, modelo, tienda relacionada
- **Order**: producto, usuario, fecha

## Personalización

- Los estilos usan Bootstrap 4/5 y pueden modificarse en `stock/static/css/`.
- Las tablas pueden personalizarse en `stock/components/tables.py`.
- Los formularios usan crispy-forms y pueden personalizarse en `stock/forms.py`.