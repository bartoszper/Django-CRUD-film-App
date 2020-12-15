from django.db import models

class Gatunek(models.Model):
    gatunek = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.gatunek


class Film(models.Model):
    gatunek = models.ForeignKey(Gatunek, on_delete=models.CASCADE, null=True)
    tytul = models.CharField(max_length=100)
    rok = models.PositiveSmallIntegerField(default=2000, blank=True)
    opis = models.TextField(default='', blank=True)
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank = True)
    plakat = models.ImageField(upload_to='plakaty', null=True, blank =
    True)
    

    def __str__(self):
        return self.tytul

class Ocena(models.Model):
    recenzja = models.TextField(blank=True, null=True)
    gwiazdki = models.PositiveSmallIntegerField(blank = True, null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True, blank=True)
