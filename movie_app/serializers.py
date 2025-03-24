from rest_framework import serializers
from rest_framework.response import Response
from . import models
from .models import Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ['name', 'movies_count']

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=50)

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = models.Movie
        fields = ['title', 'director', 'average_rating']
        depth = 1

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=50)
    duration = serializers.IntegerField(min_value=20, max_value=400)
    director_id = serializers.IntegerField()
    rating = serializers.FloatField(min_value=1, max_value=5, default=5)

    def validate_director_id(self, director_id):
        try:
            models.Director.objects.get(id=director_id)
        except models.Director.DoesNotExist:
            raise serializers.ValidationError("Director does not exist")
        return director_id

class MovieDetailSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()

    class Meta:
        model = models.Movie
        fields = ['id', 'title', 'duration', 'director']
        depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()

    class Meta:
        model = models.Review
        fields = ['text', 'movie', 'stars']

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=3, max_length=255)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    movie_id = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            models.Movie.objects.get(id=movie_id)
        except models.Movie.DoesNotExist:
            raise serializers.ValidationError("Movie does not exist")
        return movie_id

class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()

    class Meta:
        model = models.Review
        fields = ['id', 'text', 'movie', 'stars']
