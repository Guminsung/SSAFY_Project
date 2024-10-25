from django.urls import path
from . import views

urlpatterns = [
    path('stations/', views.station_list),
    path('stations/<int:station_pk>/', views.station_detail),
    path('locations/', views.location_create),
    path('locations/<int:location_pk>/stations/', views.station_create),
]
