from django.shortcuts import redirect, render

from libraries.forms import CreateAuthorForm, CreateBookForm
from libraries.models import Book

# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')


def create_author(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('libraries:books')
    else:
        form = CreateAuthorForm()
    context = {
        'form':form
    }
    return render(request, 'libraries/create_author.html', context)

def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('libraries:books')
    else:
        form = CreateBookForm()
    context = {
        'form':form
    }
    return render(request, 'libraries/create_book.html', context)

def books(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request, 'libraries/books.html', context)