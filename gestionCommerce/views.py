from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Client, Commande, CommandeProduit, Produit
from .forms import ClientRegistration, CommandeRegistration, OrderRegistrationFormSet, ProduitRegistration
# Create your views here.

def index(request):
    client_list = Client.objects.all()
    produit_list=Produit.objects.all()
    commande_list=Commande.objects.all()
    context = {'client_list': client_list,
                'produit_list': produit_list,
                'commande_list': commande_list,
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
    client = Client.objects.get(pk=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('gestionCommerce:index')
    return render(request, 'gestionCommerce/confirm_delete.html',{'client':client})

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
    produit = Produit.objects.get(pk=produit_id)
    if request.method == 'POST':
        produit.delete()
        return redirect('gestionCommerce:index')
    return render(request, 'gestionCommerce/confirm_delete.html',{'produit':produit})

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
            return redirect(reverse('gestionCommerce:index'))
    else:
        fm = ClientRegistration()
    client = Client.objects.all()
    return render(request, 'gestionCommerce/add.html', {'form':fm, 'client':client})

def addP(request):
    if request.method == 'POST':
        f = ProduitRegistration(request.POST, request.FILES)
        if f.is_valid():
            nm = f.cleaned_data['Nom']
            pr = f.cleaned_data['Prix']
            des = f.cleaned_data['Description']
            img = f.cleaned_data['Image']
            reg = Produit(Nom = nm, Prix=pr, Description= des, Image = img)
            reg.save()
            f = ProduitRegistration()
            return redirect(reverse('gestionCommerce:index'))

    else:
        f = ProduitRegistration()
    produit = Produit.objects.all()
    return render(request, 'gestionCommerce/add.html', {'form':f, 'produit':produit})


def commande(request, commande_id):
    commande = get_object_or_404(Commande, pk=commande_id)
    return render(request, "gestionCommerce/commande.html", {"commande":commande})

def addCo(request):
    if request.method == 'POST':
        f = CommandeRegistration(request.POST)
        formset = OrderRegistrationFormSet(request.POST, prefix='order_formset')

        if f.is_valid() and formset.is_valid(): 
            num = f.cleaned_data['num']
            cl = f.cleaned_data['client']
            dt = f.cleaned_data['date_commande']
            tc = f.cleaned_data['type_facture']
            reg = Commande(num = num, client = cl, date_commande = dt, type_facture = tc)
            reg.save()

            for form in formset:
                if form.cleaned_data.get('produit'):
                    commande_produit = form.save(commit=False)
                    commande_produit.commande = reg
                    commande_produit.save()
 
            return redirect(reverse('gestionCommerce:index'))

    else:
        f = CommandeRegistration()
        formset = OrderRegistrationFormSet(prefix='order_formset')
    
    formset = OrderRegistrationFormSet(queryset=CommandeProduit.objects.none(), prefix='order_formset')

    commande = Commande.objects.all()
    return render(request, 'gestionCommerce/addCo.html', {'form':f, 'formset': formset, 'commande':commande})

def updateCo(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)

    if request.method == 'POST':
        fm = CommandeRegistration(request.POST, instance=commande)
        formset = OrderRegistrationFormSet(request.POST, prefix='order_formset', queryset=commande.commandeproduit_set.all())

        if fm.is_valid() and formset.is_valid():
            fm.save()

            # Process each form in the formset
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    # If the form has the DELETE field checked, delete the associated bought product
                    if form.instance.pk is not None:
                        form.instance.delete()
                else:
                    # If the form is not marked for deletion, save it with the updated quantity
                    if form.cleaned_data.get('produit'):
                        form.save(commit=False)
                        form.instance.commande = commande
                        form.save()
            # Add a new form for adding a new bought product
            formset.extra += 1

            fm = CommandeRegistration(instance=commande)
            formset = OrderRegistrationFormSet(prefix='order_formset', queryset=commande.commandeproduit_set.all())
            return redirect(reverse('gestionCommerce:commande', kwargs={'commande_id': commande.id}))
    else:
        fm = CommandeRegistration(instance=commande)
        formset = OrderRegistrationFormSet(prefix='order_formset', queryset=commande.commandeproduit_set.all())

    return render(request, 'gestionCommerce/updateCo.html', {'form': fm, 'formset': formset, 'commande': commande})


def deleteCo(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)
    if request.method == 'POST':
        commande.delete()
        return redirect('gestionCommerce:index')
    return render(request, 'gestionCommerce/confirm_delete.html',{'commande':commande})
    