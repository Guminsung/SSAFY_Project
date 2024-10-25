from django.contrib import admin

from libraries.models import Author, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)