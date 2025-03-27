from django.contrib import admin
from django.urls import path, include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorListCreateAPIView.as_view()),
    path('api/v1/movies/', views.MovieListCreateAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewCreateAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('api/v1/users/', include('users.urls')),
]
