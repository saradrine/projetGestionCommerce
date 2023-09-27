from django import forms
from .models import Client, Commande, CommandeProduit, Produit
from django.forms import modelformset_factory

class ClientRegistration(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['CIN', 'Nom', 'Prenom', 'Adresse', 'Email', 'Telephone', 'MotDePasse']
        widgets = {
            'CIN': forms.NumberInput(attrs={'class':'form-control'}),
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
        fields = ['Nom', 'Prix','Description', 'Image']
        widgets = {
            'Nom': forms.TextInput(attrs={'class':'form-control'}),
            'Prix': forms.NumberInput(attrs={'class':'form-control'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'Image': forms.FileInput(attrs={'class':'form-control'}),
        }

class orderRegistration(forms.ModelForm):
    class Meta:
        model = CommandeProduit
        fields = ['produit', 'Quantite']
        widgets = {
            'produit': forms.Select(attrs={'class':'form-control'}),
            'Quantite': forms.NumberInput(attrs={'class':'form-control'}),
        }

OrderRegistrationFormSet = modelformset_factory(
    CommandeProduit,
    form=orderRegistration,
    extra=5, 
    can_delete=True,
)

class CommandeRegistration(forms.ModelForm):
    date_commande = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        input_formats=['%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y'],
    )
    class Meta:
        model = Commande
        fields = ['num', 'client', 'date_commande', 'type_facture']
        widgets = {
            'num': forms.NumberInput(attrs={'class':'form-control'}),
            'client': forms.Select(attrs={'class':'form-control'}),
            'date_commande': forms.DateTimeInput(attrs={'class':'form-control'}),
            'type_facture': forms.Select(attrs={'class':'form-control'}),
        }
