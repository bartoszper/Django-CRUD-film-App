from django.db import models

# Create your models here.
class Film(models.Model):
    tytul = models.CharField(max_length=100)
    rok = models.PositiveSmallIntegerField(default=2000, blank=True)
    opis = models.TextField(default='', blank=True)
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank = True)
    plakat = models.ImageField(upload_to='plakaty', null=True, blank =
    True)

    def __str__(self):
        return self.tytul