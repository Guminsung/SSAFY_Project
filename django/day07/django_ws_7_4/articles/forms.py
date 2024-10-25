from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label = 'Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    content = forms.CharField(
        max_length=250,
        label = 'Content',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )
    image_description = forms.CharField(
        label = 'Image_description',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'