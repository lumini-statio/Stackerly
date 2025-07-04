import django_tables2 as tables
from stock.models import Order, Product, Store, CustomUser


class UserTable(tables.Table):

    edit = tables.TemplateColumn(
        template_code='''
            <a href="{% url 'user_item' record.id %}" >
                <i class="fa fa-pen fa-sm text-success"></i>
            </a>''',
        orderable=False,
        verbose_name='Actions',
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
        attrs = {'class': 'table mx-auto text-light'}


class StoreTable(tables.Table):

    products = tables.TemplateColumn(
        template_code='''
            <a href="{% url 'products' record.id %}" >
                <i class="fa fa-eye fa-sm text-light"></i>
            </a>''',
        orderable=False,
        verbose_name='Products'
    )

    edit = tables.TemplateColumn(
        template_code='''
            <a href="{% url 'store_item' record.id %}" >
                <i class="fa fa-pen fa-sm text-success"></i>
            </a>''',
        orderable=False,
        verbose_name='Actions'
    )

    class Meta:
        model = Store
        fields = ('name', 'location', 'capacity')
        attrs = {'class': 'table mx-auto text-light'}


class ProductTable(tables.Table):

    edit = tables.TemplateColumn(
        template_code='''
            <a href="{% url 'product_item' store.id record.id %}" >
                <i class="fa fa-pen fa-sm text-success"></i>
            </a>''',
        orderable=False,
        verbose_name='Actions'
    )

    class Meta:
        model = Product
        fields = ('name', 'price', 'type', 'related_store')
        attrs = {'class': 'table mx-auto text-light'}
        
    
class OrderTable(tables.Table):

    create = tables.TemplateColumn(
        template_code='''
            <a class="link" href="{% url 'form_Personas' %}" class="btn btn-success btn-sm">Create</a>''',
        orderable=False,
        verbose_name='Acciones'
    )

    edit = tables.TemplateColumn(
        template_code='''
            <a class="link" href="{% url 'Personas' %}" class="btn btn-primary btn-sm">Edit</a>''',
        orderable=False,
        verbose_name=''
    )

    class Meta:
        model = Order
        fields = ('product', 'user', 'date')
        attrs = {'class': 'table mx-auto text-light'}
        