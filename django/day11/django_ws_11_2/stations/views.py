from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Location, Station
from .serializers import LocationSerializer, StationListSerializer, StationSerializer
# Create your views here.


@api_view(['POST'])
def location_create(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def station_list(request):
    stations = Station.objects.all()
    serializer = StationListSerializer(stations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def station_detail(request, station_pk):
    station = Station.objects.get(pk=station_pk)
    serializer = StationSerializer(station)
    return Response(serializer.data)


@api_view(['POST'])
def station_create(request, location_pk):
    address = Location.objects.get(pk=location_pk)
    serializer = StationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(address=address)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
