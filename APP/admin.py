from django.contrib import admin

from movie.models import Actor, Director, Movie, Rating


@admin.register(Aktor)
class Ac=ktorAdmin(admin.ModelAdmin):
    pass


@admin.register(Rezyser)
class RezyserAdmin(admin.ModelAdmin):
    pass


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    readonly_fields = [
        "average_rating",
        "ratings_count"
    ]


@admin.register(Ocena)
class OcenaAdmin(admin.ModelAdmin):
    pass