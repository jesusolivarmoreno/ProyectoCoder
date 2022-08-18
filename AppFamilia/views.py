from django.shortcuts import render
from AppFamilia.models import Familia
from django.db import models

# Create your views here.
#Este primer View es para agregar a la base de datos 
def miembros(request):
    datos = Familia(nombre="Mirleth", apellido="Rodriguez Garcia", edad=30, nacimiento="1992-02-06")
    datos.save()
    contexto = {
        "miembros1": datos
    }
    return render(request, "familiaweb.html", contexto)
#Este primer View es para ver los registros en el numero de ID creo que para cumplir con la consigna podria agregar mas y mostrarlos todos como se hizo en el anterior a la base de datos 
def verfamilia(request):
    datos = Familia.objects.get(id=36)
    datos2 = Familia.objects.get(id=37)
    datos3 = Familia.objects.get(id=38)
    datos4 = Familia.objects.get(id=39)
    conexto = {
        "ver": datos,
        "ver2": datos2,
        "ver3": datos3,
        "ver4": datos4
    }
    return render(request,"verfamilia.html",conexto)
#Falta crear otro para eliminar los datos para asi no tener datos demas
def eliminarMiembros(request):
    miembro = Familia.objects.get(id=35)
    miembro.delete()
    miembros = Familia.objects.all()
    contexto = {
        "verificar": miembros
    }
    return render(request,"deletefamila.html",contexto)
