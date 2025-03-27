from django.urls import path
from users import views

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view()),
    path('auth/', views.AuthorizationAPIView.as_view()),
    path('confirm/', views.ConfirmAPIView.as_view()),
]