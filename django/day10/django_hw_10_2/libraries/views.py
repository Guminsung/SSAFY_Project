from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from libraries.serializers import BookSerializers, BookListSerializers
from .models import Book
# Create your views here.


@api_view(['GET'])
def book_list(request):
    books = get_list_or_404(Book)
    serializer = BookListSerializers(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    serializer = BookSerializers(book)
    return Response(serializer.data)
