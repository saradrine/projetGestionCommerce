from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from django.http import HttpResponse
from .models import Client, Produit
from .forms import ClientRegistration, ProduitRegistration
# Create your views here.

def index(request):
    client_list = Client.objects.all()
    produit_list=Produit.objects.all()
    context = {'client_list': client_list,
                'produit_list': produit_list,
               }
    return render(request, "gestionCommerce/index.html",context)

def clientt(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, "gestionCommerce/client.html", {"client":client})

def produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, "gestionCommerce/produit.html", {"produit":produit})

def updateC(request, client_id):
    if request.method == 'POST':
        client = Client.objects.get(pk=client_id)
        fm = ClientRegistration(request.POST, instance=client)
        if fm.is_valid():
            fm.save()
    else:
        client = Client.objects.get(pk = client_id)
        fm = ClientRegistration(instance=client)

    return render(request, 'gestionCommerce/update.html',{'form':fm})

def deleteC(request, client_id):
    if request.method == 'POST':
        client = Client.objects.get(pk=client_id)
        client.delete()
    return HttpResponseRedirect('/gestionCommerce/')

def updateP(request, produit_id):
    if request.method == 'POST':
        produit = Produit.objects.get(pk=produit_id)
        f = ProduitRegistration(request.POST, instance=produit)
        if f.is_valid():
            f.save()
    else:
        produit = Produit.objects.get(pk = produit_id)
        f = ProduitRegistration(instance=produit)

    return render(request, 'gestionCommerce/update.html',{'form':f})

def deleteP(request, produit_id):
    if request.method == 'POST':
        produit = Produit.objects.get(pk=produit_id)
        produit.delete()
    return HttpResponseRedirect('/gestionCommerce/')

def addC(request):
    if request.method == 'POST':
        fm = ClientRegistration(request.POST)
        if fm.is_valid():
            cim = fm.cleaned_data['CIN']
            nm = fm.cleaned_data['Nom']
            pm = fm.cleaned_data['Prenom']
            em = fm.cleaned_data['Email']
            adr = fm.cleaned_data['Adresse']
            tm = fm.cleaned_data['Telephone']
            pw = fm.cleaned_data['MotDePasse']
            reg = Client(CIN = cim, Nom = nm, Prenom=pm, Email = em, Adresse= adr, Telephone= tm, MotDePasse = pw)
            reg.save()
            fm = ClientRegistration()
    else:
        fm = ClientRegistration()
    client = Client.objects.all()
    return render(request, 'gestionCommerce/add.html', {'form':fm, 'client':client})

def addP(request):
    if request.method == 'POST':
        f = ProduitRegistration(request.POST)
        if f.is_valid():
            nm = f.cleaned_data['Nom']
            pr = f.cleaned_data['Prix']
            des = f.cleaned_data['Description']
            qt = f.cleaned_data['Quantite']
            img = f.cleaned_data['Image']
            reg = Produit(Nom = nm, Prix=pr, Description= des, Quantite = qt, Image = img)
            reg.save()
            f = ProduitRegistration()
    else:
        f = ProduitRegistration()
    produit = Produit.objects.all()
    return render(request, 'gestionCommerce/add.html', {'form':f, 'produit':produit})







def commande(request, client_id):
    response = "You're looking at the commandes of client %s."
    return HttpResponse(response % client_id)