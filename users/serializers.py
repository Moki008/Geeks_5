from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Code


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=20)
    password = serializers.CharField(min_length=6, max_length=15)


class UserRegistrationSerializer(UserSerializer):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise serializers.ValidationError("Username already taken")


class UserAuthorizationSerializer(UserSerializer):
    pass

class UserVerificationSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=20)
    code = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        code = attrs.get('code')
        try:
            user = User.objects.get(username=username)
            if user.code.code != code:
                raise serializers.ValidationError("Неверный код подтверждения.")
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь не найден.")
        except Code.DoesNotExist:
            raise serializers.ValidationError("Код не найден.")

        return attrs