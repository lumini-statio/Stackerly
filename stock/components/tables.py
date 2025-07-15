import django_tables2 as tables
from stock.models import Order, Product, Store, CustomUser, BalanceBox


class UserTable(tables.Table):

    edit = tables.TemplateColumn(
        template_code='''
            {% if request.user.is_superuser %}
            <a href="{% url 'user_item' record.id %}" >
                <i class="fa fa-pen fa-sm text-success"></i>
            </a>
            {% endif %}''',
        orderable=False,
        verbose_name='Actions'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
        attrs = {'class': 'table mx-auto text-light'}


class BalanceBoxesTable(tables.Table):
    class Meta:
        model = BalanceBox
        fields = ('current_amount', 'last_updated', 'location')
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
            {% if request.user.is_superuser %}
            <a href="{% url 'store_item' record.id %}" >
                <i class="fa fa-pen fa-sm text-success"></i>
            </a>
            {% endif %}''',
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
            {% if request.user.is_superuser %}
            <a href="{% url 'product_item' store.id record.id %}" >
                <i class="fa fa-pen fa-sm text-success"></i>
            </a>
            {% endif %}''',
        orderable=False,
        verbose_name='Actions'
    )

    class Meta:
        model = Product
        fields = ('name', 'price', 'type', 'related_store')
        attrs = {'class': 'table mx-auto text-light'}


class AllProductsTable(tables.Table):
    buy = tables.TemplateColumn(
        template_code='''
            {% if record.state.name == "Not Available" %}
                <span class="text-danger">-----</span>
            {% else %}
                <a href="{% url 'buy_product' record.id %}" style="view-transition-name: buy-product;">
                    <i class="fa fa-plus fa-sm text-success"></i>
                </a>
            {% endif %}
            ''',
        orderable=False,
        verbose_name='Buy'
    )

    class Meta:
        model = Product
        fields = ('name', 'price', 'type', 'quantity', 'state', 'related_store')
        attrs = {'class': 'table mx-auto text-light'}
    
class OrderTable(tables.Table):
    class Meta:
        model = Order
        fields = ('user', 'date')
        attrs = {'class': 'table mx-auto text-light'}
        