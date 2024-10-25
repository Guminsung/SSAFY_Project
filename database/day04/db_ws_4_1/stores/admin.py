from django.contrib import admin

from stores.models import Product, Store

# Register your models here.
admin.site.register(Store)
admin.site.register(Product)
