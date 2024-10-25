from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        label='Summary',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'summary',
                'placeholder': 'summary',
            }
        )
    )
    memo = forms.CharField(
        label='Memo',
        widget=forms.Textarea(
            attrs={
                'class': 'memo',
                'placeholder': 'memo',
                'cols': '50',
                'rows': '5',
            }
        )
    )
    class Meta:
        model = Memo
        fields = '__all__'