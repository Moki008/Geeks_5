from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . import serializers
from rest_framework.authtoken.models import Token
from . import models


@api_view(['POST'])
def registration_api_view(request):
    serializer = serializers.UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(username=username, password=password, is_active=False)

    verification_code = models.Code.objects.create(user=user)

    return Response(data={'code': verification_code.code}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = serializers.UserAuthorizationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = authenticate(username=username, password=password)
    if user is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response(data={'key': token.key}, status=status.HTTP_200_OK)


@api_view(['POST'])
def confirm_api_view(request):
    serializer = serializers.UserVerificationSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.get(username=serializer.validated_data['username'])
        verification = user.code

        user.is_active = True
        user.save()
        verification.is_used = True
        verification.save()

        return Response({"message": "Пользователь подтвержден."}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
