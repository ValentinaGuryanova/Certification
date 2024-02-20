from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    username = models.CharField(max_length=20, unique=True, verbose_name='имя пользователя')
    password = models.CharField(max_length=200, verbose_name='пароль')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
