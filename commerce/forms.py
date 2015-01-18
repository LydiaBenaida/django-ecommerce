# coding=utf-8
from commerce.models import *
from django import forms
from django.forms import ModelForm

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='Votre prénom', required=True)
    last_name = forms.CharField(label='Votre nom', required=True)
    username = forms.CharField(label='Votre nom d\'utilisateur', required=True)
    password = forms.CharField(label='Votre mot de passe',required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='Votre adresse e-mail', required=True)


class AddAddress(ModelForm):
    class Meta:
        model = Address
        fields = ['gender', 'first_name', 'last_name', 'company', 'address', 'additional_address',
                  'postcode', 'city', 'phone', 'mobilephone', 'fax', 'workphone']