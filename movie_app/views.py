from django.db.models import Avg
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import models
from . import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = serializers.DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        name = serializer.validated_data.get('name')
        directors = models.Director.objects.create(
            name=name
        )
        return Response(data=serializers.DirectorDetailSerializer(directors).data,
                        status=status.HTTP_201_CREATED)


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorDetailSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        director = self.get_object()
        serializer = serializers.DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data=serializers.MovieDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        rating = serializer.validated_data.get('rating')

        movies = models.Movie.objects.create(
            title=title,
            duration=duration,
            director_id=director_id,
            rating=rating
        )
        return Response(data=serializers.MovieDetailSerializer(movies).data,
                        status=status.HTTP_201_CREATED)

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieDetailSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        movie.title = serializer.validated_data.get('title')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.rating = serializer.validated_data.get('rating')
        movie.save()
        return Response(data=serializers.MovieDetailSerializer(movie).data,
                        status=status.HTTP_201_CREATED)




class ReviewCreateAPIView(ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie_id')

        review = models.Review.objects.create(
            stars=stars,
            text=text,
            movie_id=movie_id
        )
        return Response(data=serializers.ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewDetailSerializer
    lookup_field = 'id'


    def update(self, request, *args, **kwargs):
        review = self.get_object()
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        review.stars = serializer.validated_data.get('stars')
        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie_id')
        review.save()
        return Response(data=serializers.ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)


