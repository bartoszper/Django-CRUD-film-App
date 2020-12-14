from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def wszystkie_filmy(request):
    test = Film.objects.all()
    paginator = Paginator(test,4)
    page = request.GET.get('page')
    test = paginator.get_page(page)
    return render(request, 'filmy.html', {'filmy':test})


#Formularz dodawania nowych filmów do bazy danych
@login_required
def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save(commit = True)
        return redirect(wszystkie_filmy)

    return render(request, 'nowy_film.html',{'form':form, 'nowy':True})

#Edytuje istniejący film.
@login_required
def edytuj_film(request,id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save(commit = True)
        return redirect(wszystkie_filmy)

    return render(request, 'nowy_film.html',{'form':form, 'nowy':False})

#Funkcja usówa filmy
@login_required
def usun_film(request,id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html',{'film': film })