from django.db import models

# Create your models here.
class WatchlistFilm(models.Model):
    film_watched = models.BooleanField(max_length=50)
    film_title = models.TextField()
    film_rating = models.IntegerField()
    film_release = models.TextField()
    film_review = models.TextField()