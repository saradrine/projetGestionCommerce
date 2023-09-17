from django.db import models

# Create your models here.
class Client(models.Model):
    CIN = models.IntegerField()
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Adresse = models.CharField(max_length=150)
    Telephone = models.IntegerField()
    Email = models.CharField(max_length=150)
    MotDePasse = models.CharField(max_length=150)
    def __str__(self):
        return self.Nom + " " + self.Prenom
    
class Produit(models.Model):
    Nom = models.CharField(max_length=50)
    Prix = models.FloatField(default=0.0)
    Quantite = models.IntegerField(default=0)
    Description = models.TextField(blank=True)
    Image = models.ImageField(upload_to="produits", blank=True, null=True)
    def __str__(self):
        return self.Nom + " (" + str(self.Quantite) + ")"
    
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ManyToManyField(Produit)
    date_commande = models.DateTimeField(auto_now_add=True)
    Quantite = models.IntegerField()
    def __str__(self):
        return f"Commande de {self.client.Nom} le {self.date_commande}"