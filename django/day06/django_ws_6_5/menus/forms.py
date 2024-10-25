from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    price = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        error_messages={
            '제약조건': '출력하고 싶은 메시지를 적어주세요...',
            'invalid': '올바른 가격을 입력해 주세요. 예: 12,34',
            'max_digits': '올바른 가격을 입력해주세요',
            'decimal_places': '가격은 소수점 이하 두 자리여야 합니다.'
        }
    ) 

    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 이름을 작성해 주세요.'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 설명을 작성해 주세요.'
                }
            ),
            'is_vegan': forms.RadioSelect(attrs={'class': 'form-check'}, choices=[(True, 'YES'), (False, "NO")]),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }
