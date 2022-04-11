from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("addetudiant", views.addEtudiant, name="addEtudiant"),
    path("promotion", views.promotion, name="promotion"),
    path("prom", views.addpromotion, name="addPromotion"),
    path("delete/<int:id>",views.deleteData, name="deleteData"),
    path("etu", views.etudiantVue, name="voir"),
    path("paiement", views.inscription, name="inscription"),
]