from django import forms
from .models import Customer

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone': 'شماره تماس',
            'email': 'ایمیل',
            'password': 'رمز عبور',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تماس'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور جدید'}),
        }
