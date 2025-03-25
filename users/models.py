from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер телефона')
    birth_date = models.CharField(max_length=10, blank=True, null=True, verbose_name='Дата рождения')
    first_name = models.CharField(max_length=150, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Фамилия')
    surname = models.CharField(max_length=10, blank=True, null=True, verbose_name='Отчество')
    username = models.CharField(
        ("пользователь"),
        max_length=150,
        unique=True,
        validators=[AbstractUser.username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
