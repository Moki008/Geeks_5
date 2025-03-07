from rest_framework import serializers
from . import models


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ['name']

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()

    class Meta:
        model = models.Movie
        fields = ['title', 'director']

class MovieDetailSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()

    class Meta:
        model = models.Movie
        fields = ['id', 'title','duration', 'director']

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()

    class Meta:
        model = models.Review
        fields = ['text', 'movie']

class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()

    class Meta:
        model = models.Review
        fields = ['id', 'text', 'movie']
