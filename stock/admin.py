from django.contrib import admin
from stock.models import *

# Register your models here.
admin.site.register(Location)
admin.site.register(BalanceBox)
admin.site.register(Store)
admin.site.register(ProductState)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Purchase)
admin.site.register(ProfitLossRecord)
admin.site.register(UserPurchase)
admin.site.register(CustomUser)

admin.site.site_title = "Admin Site"
admin.site.site_header = "Stock Management | Admin"
admin.site.index_title = "Admin"