from django.db import models

# Create your models here.
class Client(models.Model):
    nom = models.CharField(name="Nom",max_length=50)
    prenom = models.CharField(name="Prénom",max_length=50)
    adresse = models.CharField(name="Adresse",max_length=150)
    telephone = models.IntegerField(name="Téléphone")
    email = models.CharField(name="Email",max_length=150)
    motDePasse = models.CharField(name="Mot De Passe",max_length=150)
    def __str__(self):
        return self.nom + " " + self.prenom
    
class Produit(models.Model):
    nom = models.CharField(name="Nom",max_length=50)
    prix = models.IntegerField(name="Prix")
    description = models.CharField(name="Description",max_length=150)
    def __str__(self):
        return self.nom
    
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(name="Quantité")
    def __str__(self):
        return self.client.nom + " " + self.produit.nom + " " + str(self.quantite)