from django.contrib import admin

from restaurants.models import Category, Menu, Restaurant

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Category)