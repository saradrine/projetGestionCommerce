from django.core import validators
from django import forms
from django.forms import fields, widgets
from .models import Client, Produit

class ClientRegistration(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['Nom', 'Prenom', 'Adresse', 'Email', 'Telephone', 'MotDePasse']
        widgets = {
            'Nom': forms.TextInput(attrs={'class':'form-control'}),
            'Prenom': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control'}),
            'Adresse': forms.TextInput(attrs={'class':'form-control'}),
            'Telephone': forms.NumberInput(attrs={'class':'form-control'}),
            'MotDePasse': forms.PasswordInput(render_value=True,attrs={'class':'form-control'})

        }

class ProduitRegistration(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['Nom', 'Prix']
        widgets = {
            'Nom': forms.TextInput(attrs={'class':'form-control'}),
            'Prix': forms.NumberInput(attrs={'class':'form-control'}),
        }