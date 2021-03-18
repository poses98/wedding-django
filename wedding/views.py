from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from wedding.models import *
from .forms import *


def password_view(request):

    form = WebPasswordForm(request.GET or None)
    if form.is_valid():
        password = request.GET.get('password')
        if password == WebPassword.objects.all()[0].password:
            request.session['password'] = True
            return redirect("index")
    else:
        print("form is not valid")

    return render(request, 'password.html')


def password_check(request):
    if WebPassword.objects.all()[0].is_required:
        check = True
        try:
            if request.session['password']:
                check = False
        except:
            check = True
        return check
    else:
        return False


def index(request):
    if password_check(request):
        return redirect("password")

    """View function for home page of site."""
    # Nombres novios
    nombres_pareja = NombresPareja.objects.all()[0]
    # Itinerario
    itinerario = Itinerario.objects.all()
    itinerario_header = ItinerarioHeader.objects.all()[0]
    # Fecha boda
    fecha_boda = FechaDeBoda.objects.all()[0]
    # Mes boda humanized
    mes_boda = getMonth(fecha_boda.get_month())
    # Lugar boda
    lugar_boda = LugarDeLaBoda.objects.all()[0]
    # Numero de confirmaciones
    confirmaciones_count = Confirmacion.objects.all().count()
    # Mensajes para los novios
    mensajes = BestWishes.objects.filter(accepted=True)

    context = {
        'nombres_pareja': nombres_pareja,
        'itinerario': itinerario,
        'itinerario_header': itinerario_header,
        'fecha_boda': fecha_boda,
        'mes_boda': mes_boda,
        'numero_invitados': confirmaciones_count,
        'mensajes': mensajes,
        'lugar_boda': lugar_boda
    }

    return render(request, 'index.html', context=context)


def SuccessForm(request):
    return render(request, 'inscripcion_realizada.html')


def golf_view(request):
    if password_check(request):
        return redirect("password")

    golf = CampeonatoGolf.objects.all()[0]

    context = {
        'golf': golf
    }
    return render(request, 'golf.html', context=context)


# FORMULARIOS
def confirmacion_create_view(request):
    if password_check(request):
        return redirect("password")
    form = ConfirmacionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ConfirmacionForm()
        SuccessForm(request)
    context = {
        'form': form
    }
    return render(request, 'wedding/confirmacion_create.html', context=context)


def confirmacion_search_view(request):
    if password_check(request):
        return redirect("password")

    form = SearchConfirmacion(request.GET or None)
    datos = None
    if request.method == 'GET':
        if form.is_valid():
            datos = Confirmacion.objects.filter(
                name=form.cleaned_data.get('name'),
                surname=form.cleaned_data.get('surname')).first()
    return render(request, 'wedding/confirmacion_search.html', {'form': form, 'datos': datos})


def confirmacion_edit_view(request):
    if password_check(request):
        return redirect("password")
    datos = Confirmacion.objects.filter(
        name=request.GET.get('name'),
        surname=request.GET.get('surname')).first()
    form = ConfirmacionForm(instance=datos)
    check = False
    if datos:
        check = True
    if request.method == "POST":
        form = ConfirmacionForm(request.POST, instance=datos)
        if form.is_valid():
            datos = form.save(commit=False)
            datos.save()
            SuccessForm(request)
    context = {
        "form": form,
        "check": check
    }
    return render(request, "wedding/confirmacion_edit.html", context=context)


def inscripcion_create_view(request):
    if password_check(request):
        return redirect("password")
    form = InscripcionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InscripcionForm()
        SuccessForm(request)
    context = {
        'form': form
    }
    return render(request, 'wedding/inscripcion_create.html', context=context)


def best_wishes_create_view(request):
    if password_check(request):
        return redirect("password")
    form = BestWishesForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BestWishesForm()
        SuccessForm(request)

    context = {
        'form': form
    }
    return render(request, 'wedding/best_wishes_create.html', context=context)


def SuccessForm(request):
    return render(request, 'inscripcion_realizada.html')


class SitiosInteresListView(generic.ListView):
    model = SitiosInteres


def getMonth(monthNumber):
    """Function that returns the month in Spanish with a given month number."""
    MESES = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre'
    }
    return MESES[monthNumber]
