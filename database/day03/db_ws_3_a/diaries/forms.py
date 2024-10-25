from django import forms
from .models import Comment, Diary


class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]