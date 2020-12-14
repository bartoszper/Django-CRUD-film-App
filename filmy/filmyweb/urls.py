from django.urls import path
from . import views 


urlpatterns = [
    path('', views.wszystkie_filmy),
]