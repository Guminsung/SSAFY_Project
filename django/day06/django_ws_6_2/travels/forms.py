from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    location = forms.CharField(
        label='Location',
        max_length=10,
        widget=forms.DateInput(
            attrs={
                'class': 'location',
                'placeholder': 'ex)제주도',
            }
        )
    )
    start_date = forms.DateField(
        label='Start date',
        widget=forms.DateInput(
            attrs={
                'class': 'start_date',
                'placeholder': 'ex)2022-02-22',
            }
        )
    )
    end_date = forms.DateField(
        label='End_date',
        widget=forms.DateInput(
            attrs={
                'class': 'end_date',
                'placeholder': 'ex)2022-02-22',
            }
        )
    )
    class Meta:
        model = Travel
        fields = '__all__'