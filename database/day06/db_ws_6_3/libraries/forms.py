from django import forms

from libraries.models import Author, Book


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nickname',]

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'