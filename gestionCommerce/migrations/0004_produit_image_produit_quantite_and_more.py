# Generated by Django 4.2.4 on 2023-09-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestionCommerce", "0003_rename_mot_de_passe_client_motdepasse_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="produit",
            name="Image",
            field=models.ImageField(blank=True, null=True, upload_to="produits"),
        ),
        migrations.AddField(
            model_name="produit",
            name="Quantite",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="produit",
            name="Description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="produit",
            name="Prix",
            field=models.FloatField(default=0.0),
        ),
    ]