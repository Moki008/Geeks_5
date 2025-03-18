from rest_framework import serializers
from rest_framework.response import Response

from . import models


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ['name', 'movies_count']


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


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()

    class Meta:
        model = models.Review
        fields = ['id', 'text', 'movie', 'stars']
