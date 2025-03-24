from django.db.models import Avg
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import models
from . import serializers


@api_view(['GET', 'POST'])
def director_list_create_api_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        data = serializers.DirectorSerializer(directors, many=True).data
        return Response(data)
    elif request.method == 'POST':
        serializer = serializers.DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        name = serializer.validated_data.get('name')
        directors = models.Director.objects.create(
            name=name
        )
        return Response(data=serializers.DirectorDetailSerializer(directors).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.DirectorDetailSerializer(director).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.DirectorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data=serializers.DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def movie_list_create_api_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        data = serializers.MovieSerializer(movies, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
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


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.MovieDetailSerializer(movie).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
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
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method == 'GET':
        review = models.Review.objects.all()
        data = serializers.ReviewSerializer(review, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
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


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.ReviewDetailSerializer(review).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        review.stars = serializer.validated_data.get('stars')
        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie_id')
        review.save()
        return Response(data=serializers.ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def movies_review_list_api_view(request):
    movies = models.Movie.objects.all().annotate(average_rating=Avg('reviews__stars'))
    data = serializers.MovieSerializer(movies, many=True).data
    return Response(data, status=status.HTTP_200_OK)
