from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import models
from . import serializer


@api_view(['GET'])
def director_list_api_view(request):
    directors = models.Director.objects.all()
    data = serializer.DirectorSerializer(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    data = serializer.DirectorDetailSerializer(director).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list_api_view(request):
    movies = models.Movie.objects.all()
    data = serializer.MovieSerializer(movies, many=True).data
    return Response(data=data , status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    data = serializer.MovieDetailSerializer(movie).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_list_api_view(request):
    review = models.Review.objects.all()
    data = serializer.ReviewSerializer(review, many=True).data
    return Response(data=data , status=status.HTTP_200_OK)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    data = serializer.ReviewDetailSerializer(review).data
    return Response(data=data, status=status.HTTP_200_OK)

