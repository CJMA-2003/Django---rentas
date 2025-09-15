from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from .models import Casa, Inquilino,Pago


def inicio(request):
    return render(request, "menu.html")


def Modulocasa(request):
    data = Casa.objects.all()
    return render(request, "modulo_casa/listarCasa.html", {"casas": data})


def crearCasas(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        direccion = request.POST.get("direccion")
        habitaciones = request.POST.get("habitaciones")
        precio = request.POST.get("precio")
        casa = Casa(
            nombre=nombre, direccion=direccion, habitaciones=habitaciones, precio=precio
        )
        casa.save()
        messages.success(request, f'Casa "{nombre}" registrada correctamente.')

    return redirect("modulo_casa")


def editarCasa(request, id):
    if request.method == "POST":
        casa = get_object_or_404(Casa, id=id)

        nombre = request.POST.get("nombre")
        direccion = request.POST.get("direccion")
        habitaciones = request.POST.get("habitaciones")
        precio = request.POST.get("precio")

        casa.nombre = nombre
        casa.direccion = direccion
        casa.habitaciones = habitaciones
        casa.precio = precio
        casa.save()
        messages.success(request, f'Casa "{nombre}" actualizada correctamente.')

        return redirect("modulo_casa")


def eliminarCasa(request, id):
    casa = get_object_or_404(Casa, id=id)
    casa.delete()
    messages.success(
        request, f'La casa "{casa.nombre}" ha sido eliminada correctamente.'
    )
    return redirect("modulo_casa")  # Cambia 'modulo_casa' por el nombre de tu url


def formularioCasa(request, id=None):
    if id == None:
        return render(request, "modulo_casa/FormularioCasa.html")
    else:
        obj = Casa.objects.get(id=id)
        print(obj)
        return render(
            request,
            "modulo_casa/FormularioCasa.html",
            {"data": obj, "tipo_form": "editar", "id": id},
        )


def moduloInquilino(request):
    data = Inquilino.objects.all()
    print(data)
    return render(request, "modulo_inquilino/listarinquilino.html", {"data": data})


def formularioInquilino(request, id=None):
    casa = Casa.objects.all()

    if id == None:
        return render(
            request, "modulo_inquilino/FormularioInquilino.html", {"casas": casa}
        )
    else:
        obj = Inquilino.objects.get(id=id)
        return render(
            request, "modulo_inquilino/FormularioInquilino.html", {"casas": casa,"inquilino":obj,"tipo_form":"editar"}
        )


def crearInquilino(request):
    nombre = request.POST.get("nombre")
    email = request.POST.get("email")
    casa_id = request.POST.get("casa")

    obj = Casa.objects.get(id=casa_id)

    inqui = Inquilino(nombre=nombre, email=email, casa=obj)
    inqui.save()
    messages.success(request, f'"{nombre}" ha sido creado correctamente.')

    return redirect("modulo_inquilino")


def editarInquilino(request,id):
     if request.method == "POST":
        x = get_object_or_404(Inquilino, id=id)

        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        casa_id = request.POST.get("casa")
        y = get_object_or_404(Casa,id=casa_id)
        
        x.nombre = nombre
        x.email = email
        x.casa = y
        
        x.save()
        messages.success(request, f'Inquilino actualizado correctamente.')

        return redirect("modulo_inquilino")


def eliminarInquilino(request, id):
    casa = get_object_or_404(Inquilino, id=id)
    casa.delete()
    messages.success(request, f"Inquilino eliminado correctamente.")
    return redirect("modulo_inquilino")  # Cambia 'modulo_casa' por el nombre de tu url

def moduloPago(request):
    x = Pago.objects.all()
    return render(request, "modulo_pagos/ListarPagos.html",{
        "pagos":x
    })

def formularioPago(request,id=None):
    
    inquilinos = Inquilino.objects.all()
    if id == None:
        return render(request, "modulo_pagos/FormularioPagos.html",{
            "inquilinos":inquilinos
        })
    else:
        return render(request, "modulo_pagos/FormularioPagos.html",{
            "inquilinos":inquilinos,
            "tipo_form":"editar",
            "pago":Pago.objects.get(id=id)
        })
        
def crearPago(request):
    inquilino_id = request.POST.get("inquilino")
    fecha = request.POST.get("fecha")
    monto = request.POST.get("monto")
    descripcion = request.POST.get("descripcion")
    
    obj_inquilino = get_object_or_404(Inquilino,id=inquilino_id)
    x = Pago(
        inquilino=obj_inquilino,
        fecha=fecha,
        monto=monto,
        descripcion=descripcion
    )
    
    x.save()
    messages.success(request, f"pago registrado correctamente.")

    return redirect('modulo_pago')

def editarPago(request,id):
    inquilino_id = request.POST.get("inquilino")
    fecha = request.POST.get("fecha")
    monto = request.POST.get("monto")
    descripcion = request.POST.get("descripcion")
    
    obj_inquilino = get_object_or_404(Inquilino,id=inquilino_id)
    x = get_object_or_404(Pago,id=id)
    x.inquilino = obj_inquilino
    x.fecha = fecha
    x.monto = monto
    x.descripcion = descripcion
    x.save()
    messages.success(request, f"pago actualizado correctamente.")

    return redirect('modulo_pago')
