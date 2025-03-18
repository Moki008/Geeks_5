from django.db.models import Avg
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import models
from . import serializer


@api_view(['GET', 'POST'])
def director_list_create_api_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        data = serializer.DirectorSerializer(directors, many=True).data
        return Response(data)
    elif request.method == 'POST':
        name = request.data.get('name')
        directors = models.Director.objects.create(
            name=name
        )
        return Response(data=serializer.DirectorDetailSerializer(directors).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializer.DirectorDetailSerializer(director).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=serializer.DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def movie_list_create_api_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        data = serializer.MovieSerializer(movies, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        rating = request.data.get('rating')

        movies = models.Movie.objects.create(
            title=title,
            duration=duration,
            director_id=director_id,
            rating=rating
        )
        return Response(data=serializer.MovieDetailSerializer(movies).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializer.MovieDetailSerializer(movie).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.rating = request.data.get('rating')
        movie.save()
        return Response(data=serializer.MovieDetailSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method == 'GET':
        review = models.Review.objects.all()
        data = serializer.ReviewSerializer(review, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review = models.Review.objects.create(
            stars=stars,
            text=text,
            movie_id=movie_id
        )
        return Response(data=serializer.ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializer.ReviewDetailSerializer(review).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        review.stars = request.data.get('stars')
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(data=serializer.ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def movies_review_list_api_view(request):
    movies = models.Movie.objects.all().annotate(average_rating=Avg('reviews__stars'))
    data = serializer.MovieSerializer(movies, many=True).data
    return Response(data, status=status.HTTP_200_OK)
