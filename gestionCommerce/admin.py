from django.contrib import admin
from .models import Client, CommandeProduit, Produit, Commande

# Register your models here.
admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(CommandeProduit)