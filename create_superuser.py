import os
import django
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    
    username = 'eluna'
    email = 'lunaemilio2003@gmail.com'
    password = 'Behelit1566#'
    first_name = 'Emilio'
    last_name = 'Luna'
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        print(f"Superusuario {username} creado exitosamente")
    else:
        print(f"El usuario {username} ya existe")

if __name__ == '__main__':
    create_superuser()