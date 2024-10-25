from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    is_completed = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Todo
        fields = '__all__'