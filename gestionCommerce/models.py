from django.db import models

# Create your models here.
class Client(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Adresse = models.CharField(max_length=150)
    Telephone = models.IntegerField()
    Email = models.CharField(max_length=150)
    MotDePasse = models.CharField(max_length=150)
    def __str__(self):
        return self.Nom + " " + self.Prenom + " | " + str(self.Telephone) + " | " + self.Email
    
class Produit(models.Model):
    Nom = models.CharField(max_length=50)
    Prix = models.IntegerField()
    Description = models.CharField(max_length=150)
    def __str__(self):
        return self.Nom + " " + str(self.Prix) + " " + self.Description
    
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    Quantite = models.IntegerField(name="Quantité")
    def __str__(self):
        return self.client.Nom + " " + self.produit.Nom + " " + str(self.Quantite)