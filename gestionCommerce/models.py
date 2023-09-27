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
        return f"{self.CIN} {self.Nom} {self.Prenom}"
    
class Produit(models.Model):
    Nom = models.CharField(max_length=50)
    Prix = models.FloatField(default=0.0)
    Description = models.TextField(blank=True)
    Image = models.ImageField(upload_to="produits/", blank=True, null=True)
    def __str__(self):
        return self.Nom + " (" + str(self.Prix) + ")"

class Commande(models.Model):
    num = models.IntegerField(default=0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit, through='CommandeProduit')
    date_commande = models.DateTimeField(blank= True, null=True)
    type_facture = models.CharField(max_length=20, choices=[('recu','Reçu'),('facture_proforma','Facture Proforma'),('facture','Facture')],default='reçu')
    def __str__(self):
        return f"Commande {self.num} de {self.client.Nom} {self.client.Prenom} le {self.date_commande.day}/{self.date_commande.month}/{self.date_commande.year}  "

class CommandeProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)
    Quantite = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.produit.Nom} ({self.Quantite})"
    def montant(self):
        return self.produit.Prix * self.Quantite
        