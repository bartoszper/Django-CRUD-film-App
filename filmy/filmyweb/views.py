from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm

# Create your views here.

def wszystkie_filmy(request):
    test = Film.objects.all()
    return render(request, 'filmy.html', {'filmy':test})

def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    return render(request, 'nowy_film.html',{'form':form})