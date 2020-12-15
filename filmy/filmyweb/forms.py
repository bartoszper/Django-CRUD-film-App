from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['gatunek', 'tytul', 'opis', 'premiera', 'rok', 'imdb_rating','plakat']