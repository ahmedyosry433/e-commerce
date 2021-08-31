from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignupForm(UserCreationForm):

    username = forms.CharField(max_length=30 , label='اسم المستخدم ')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}) , label='كلمة المرور' , )
    password2 = forms.CharField(widget=forms.PasswordInput , label='تأكيد كلمة المرور')

    class Meta:
        model = User
        fields = ['username','password1','password2']


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30 , label='اسم الاول ')
    last_name = forms.CharField(max_length=30 , label='اسم الاخير ')
    email = forms.EmailField(max_length=200 , label='البريد الالكتروني ')
    class Meta:
        model = User
        fields= ['first_name','last_name','email' , ] 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields= ['country', 'address' ,'img']         