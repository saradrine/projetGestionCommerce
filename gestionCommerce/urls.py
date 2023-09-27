from django.urls import path
from . import views

app_name= "gestionCommerce"
urlpatterns = [
    path("", views.index, name="index"),
    path("addClient/", views.addC, name="addC"),
    path("addProduit/", views.addP, name="addP"),
    path("client/<int:client_id>/", views.clientt, name="client"),
    path("client/<int:client_id>/update/", views.updateC, name="updateC"),
    path("deleteC/<int:client_id>/", views.deleteC, name="deleteC"),
    path("client/<int:client_id>/commande/", views.commande, name="commande"),
    path("produit/<int:produit_id>/", views.produit, name="produit"),
    path("produit/<int:produit_id>/update/", views.updateP, name="updateP"),
    path("deleteP/<int:produit_id>/", views.deleteP, name="deleteP"),
    path("commande/<int:commande_id>/", views.commande, name="commande"),
    path("addCommande/", views.addCo, name="addCo"),
    path("commande/<int:commande_id>/update/", views.updateCo, name="updateCo"),
    path("deleteCo/<int:commande_id>/", views.deleteCo, name="deleteCo"),
]