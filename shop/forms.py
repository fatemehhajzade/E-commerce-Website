from django import forms
from .models import Customer
from .models import Profile,User


class UpdateUserInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone','address1','address2','city','state','zipcode','country']
        labels = {
            'phone':'شماره تلفن',
            'address1':'آدرس 1',
            'address2':'آدرس 2',
            'city':'شهر',
            'state':'استان',
            'zipcode':'کد پستی',
            'country':'کشور'
        }

        widgets = {
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address1':forms.TextInput(attrs={'class':'form-control'}),
            'address2':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['phone'].required = False
            self.fields['address1'].required = False
            self.fields['address2'].required = False
            self.fields['city'].required = False
            self.fields['state'].required = False
            self.fields['zipcode'].required = False
            self.fields['country'].required = False

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'password': 'رمز عبور',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
