from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.movie_set.count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    rating = models.FloatField(default=3)

    def __str__(self):
        return self.title


class Review(models.Model):
    STARS = (
        (star, '* ' * star) for star in range(1, 6)
    )
    stars = models.IntegerField(choices=STARS, default=5)
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text
