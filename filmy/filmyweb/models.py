from django.db import models

# Create your models here.
class Film(models.Model):
    tytul = models.CharField(max_length=100)
    rok = models.PositiveSmallIntegerField(default=2000)


    def __str__(self):
        return self.tytul