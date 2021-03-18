from django import forms

from .models import Confirmacion, InscripcionCampeonato, BestWishes


class ConfirmacionForm(forms.ModelForm):

    class Meta:
        model = Confirmacion
        fields = ('name', 'surname', 'have_a_partner', 'partner_name', 'partner_surname',
                  'bus_service', 'bus', 'bus_place', 'song_name', 'food_restrictions')


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = InscripcionCampeonato
        fields = ('name', 'surname', 'licencia', 'handicap')


class BestWishesForm(forms.ModelForm):
    class Meta:
        model = BestWishes
        fields = ('name', 'surname', 'message')


class SearchConfirmacion(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField()


class WebPasswordForm(forms.Form):
    password = forms.CharField()
