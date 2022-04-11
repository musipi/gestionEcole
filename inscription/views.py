import datetime

from django.shortcuts import render, redirect

from inscription.models import Etudiant, Promotion, Inscription


def index(request):
    return render(request, 'index.html')


def etudiantVue(request):
    getAll = Etudiant.objects.all()
    return render(request, "etudiant.html", {'formGet': getAll})


def addEtudiant(request):
    nomEtudiant = request.POST.get("nomEtudiant", False)
    postnomEtu = request.POST.get("postnomEtu", False)
    prenomEtud = request.POST.get("prenomEtud", False)
    telephone = request.POST.get("telephone", False)
    genre = request.POST.get("genre", False)
    dateNaissance = request.POST.get("dataNaissance")
    lieuNaissance = request.POST.get("lieuNaissance", False)
    adresseDomicile = request.POST.get("adresseDomicile", False)
    nomTuteur = request.POST.get("nomTuteur", False)

    etude = Etudiant(nomEtudiant=nomEtudiant, postnomEtu=postnomEtu, prenomEtud=prenomEtud,
                     telephone=telephone, genre=genre, dateNaissance=datetime.datetime.now(dateNaissance),
                     lieuNaissaince=lieuNaissance, adresseDomicile=adresseDomicile, nomTuteur=nomTuteur
                     )
    etude.save()
    return redirect('promotion')
    #getAll = Etudiant.objects.all()
    #return render(request, "etudiant.html", {'formGet': getAll})


def deleteData(request, id):
    data = Etudiant.objects.get(id=id)
    data.delete()
    return render(request, "etudiant.html")


def promotion(request):
    return render(request, 'promotion.html')


def addpromotion(request):
    nomPromotion = request.POST.get('nomPromotion', False)
    filiere = request.POST.get('filiere', False)
    createdAt = request.POST.get('creatdeAt')
    promotion = Promotion(nomPromotion=nomPromotion, filiere=filiere, createdAt=datetime.datetime.now(createdAt))
    promotion.save()
    return render(request, 'promotion.html')


def inscription(request):
    getall = Etudiant.objects.all()
    selectall = Promotion.objects.all()
    nomEtudiant = request.POST.get('nomEtudiant_id')
    promotion = request.POST.get('promotion')
    montantPayer = request.POST.get('montantPayer', False)
    designation = request.POST.get('designation', False)
    createdAt = request.POST.get('createdAt ')

    Inscrit=Inscription(nomEtudiant=nomEtudiant , promotion=promotion, montantPayer=montantPayer,
                        designation=designation, createdAt=datetime.datetime.now(createdAt))

    Inscrit.save()
    return render(request, 'inscription.html', locals())
