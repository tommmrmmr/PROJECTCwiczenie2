from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg


class Aktor(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Rezyser(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Film(models.Model):
    imie = models.CharField(max_length=200)
    slug = models.SlugField()
    opis = models.TextField()
    aktorzy = models.ManyToManyField("film.Aktor")
    rezyser = models.ForeignKey("film.Rezyser", on_delete=models.CASCADE)
    utworzony = models.DateTimeField(auto_now_add=True)
    zaktualizowany = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imie

    @property
    def average_rating(self):
        return self.ocena.aggregate(Avg("wartosc"))["value__avg"]

    @property
    def ratings_count(self):
        return self.ocena.count()


class Ocena(models.Model):
    wartosc = models.PositiveIntegerField()
    film = models.ForeignKey("film.Film", on_delete=models.CASCADE, related_name="ocena")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating for {self.film.imie}: {self.wartosc}"
