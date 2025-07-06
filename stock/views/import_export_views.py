from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import tempfile

from stock.models import Store, Product, Order, CustomUser
from stock.utils import *

import polars as pl


@login_required
def import_data(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        temp_path = save_uploaded_file_to_temp(uploaded_file)
        df = read_file_with_polars(temp_path)

        redirect_to = 'users' if '/users/import' in request.path else 'stores'

        if '/users/import' in request.path:
            try:
                iter_users(request, df)
                messages.success(request, 'Imported users successfuly')
            except (KeyError, Exception) as e:
                messages.error(request, f"Error to handle import: user don't have {e} field, check your file, please.")
        elif '/stores/import' in request.path:
            try:
                iter_stores(request, df)
                messages.success(request, 'Imported users successfuly')
            except (KeyError, Exception) as e:
                messages.error(request, f"Error to handle import: store don't have {e} field, check your file, please.")

    return redirect(redirect_to)


@login_required
def export_data(request):
    if '/users/export' in request.path:
        return users_export()
    elif 'stores/export' in request.path:
        return stores_export()
