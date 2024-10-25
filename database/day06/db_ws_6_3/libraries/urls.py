from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    path('', views.books, name='books'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_book/', views.create_book, name='create_book')
]
