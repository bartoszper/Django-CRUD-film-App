from django.urls import path
from . import views 


urlpatterns = [
    path('', views.wszystkie_filmy, name = 'wszystkie_filmy'),
    path('nowy/', views.nowy_film, name = 'nowy_film'),
    path('edytuj/<int:id>/', views.edytuj_film, name='edytuj_film'),
    path('usun/<int:id>/', views.usun_film, name = 'usun_film'),
]