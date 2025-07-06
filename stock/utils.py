import tempfile
import polars as pl

from stock.models import Store, Product, Order, CustomUser
from django.http import HttpResponse
from django.contrib import messages


def save_uploaded_file_to_temp(uploaded_file, suffix=".xlsx"):
    """Guarda un archivo subido en un archivo temporal y retorna su ruta."""
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        for chunk in uploaded_file.chunks():
            tmp.write(chunk)
        return tmp.name


def read_file_with_polars(path):
    """Lee un archivo CSV o Excel con Polars según su extensión."""
    if path.endswith(('.xlsx', '.xls')):
        return pl.read_excel(path)
    return pl.read_csv(path)


def iter_users(request, df):
    registered_count = 0

    for row in df.iter_rows(named=True):
        username = row['username']
        email = row['email']

        if CustomUser.objects.filter(username=username).exists() or CustomUser.objects.filter(email=email).exists():
            registered_count += 1
            continue

        user = CustomUser(
            username=username,
            email=email,
            first_name=row['first_name'],
            last_name=row['last_name'],
            password=None,
        )

        user.set_password(row['password'])
        user.save()
    
    if registered_count >= 1:
        messages.error(request, f'Some registers already exists on the database')


def iter_stores(request, df):
    registered_count = 0

    for row in df.iter_rows(named=True):
        store = Store(
            name=row['name'],
            balance_box=row['balance_box'],
            location=row['location'],
        )

        if Store.objects.filter(name=store.name).exists() and \
        Store.objects.filter(balance_box=store.balance_box).exists() and \
        Store.objects.filter(location=store.location).exists():
            registered_count += 1
            continue

        store.save()
    
    messages.success(request, 'Imported stores successfuly')


def users_export():
    users = list(CustomUser.objects.values(
        'username', 'email', 'first_name', 'last_name', 'password'
        ))
    
    df = pl.DataFrame(users)

    with tempfile.NamedTemporaryFile(suffix=".xlsx") as tmp:
        df.write_excel(tmp.name)
        tmp.seek(0)
        response = HttpResponse(tmp.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=users.xlsx'
        return response
        


def stores_export():
    stores = list(Store.objects.values(
        'name', 'balance_box', 'location'
        ))

    df = pl.DataFrame(stores)

    with tempfile.NamedTemporaryFile(suffix=".xlsx") as tmp:
        df.write_excel(tmp.name)
        tmp.seek(0)
        response = HttpResponse(tmp.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=stores.xlsx'
        return response
    
    messages.success(request, 'Exported stores successfuly')

    return redirect('stores')
