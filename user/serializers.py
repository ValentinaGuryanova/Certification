from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from user.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def validate_password(self, password):
        validate_password(password=password, user=User)
        return password

    def validate(self, attrs: dict) -> dict:
        if attrs['password'] != attrs['password_repeat']:
            raise ValidationError({'password_repeat': 'Passwords must match'})
        return attrs

    def create(self, validated_data: dict) -> User:
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data: dict) -> User:
        if not (user := authenticate(
                username=validated_data['username'],
                password=validated_data['password'],
        )):
            raise AuthenticationFailed
        return user
