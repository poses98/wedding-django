from django import forms

from .models import Confirmacion, InscripcionCampeonato, BestWishes


class ConfirmacionForm(forms.ModelForm):

    class Meta:
        model = Confirmacion
        fields = ('name', 'surname', 'bus_service', 'bus', 'bus_place', 'song_name', 'food_restrictions')


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = InscripcionCampeonato
        fields = ('name', 'surname', 'licencia', 'handicap','wantToRent','day_pref')


class BestWishesForm(forms.ModelForm):
    class Meta:
        model = BestWishes
        fields = ('name', 'surname', 'message')


class SearchConfirmacion(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField()


class WebPasswordForm(forms.Form):
    password = forms.CharField()
