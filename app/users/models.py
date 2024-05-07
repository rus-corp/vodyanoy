from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from transliterate import translit
from django.utils.text import slugify


from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
  USER_STATUS_CHOICES = (
    ('Physic', 'Физик'),
    ('Legal', 'Юрик'),
    ('Installer', 'Монтажник'),
    ('Developer', 'Застройщик')
  )
  username = models.CharField(max_length=180, verbose_name='Юзернейм')
  email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
  status = models.CharField(max_length=20, choices=USER_STATUS_CHOICES, default=USER_STATUS_CHOICES[0], verbose_name='Статус клиента')
  date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
  slug = models.SlugField(max_length=255, verbose_name='slug')
  
  is_staff = models.BooleanField(default=False, verbose_name='Сотрудник компании')
  is_active = models.BooleanField(default=True, verbose_name='Активный пользователь')
  
  REQUIRED_FIELDS = []
  USERNAME_FIELD = 'email'
  
  objects = CustomUserManager()
  
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'
  
  def __str__(self) -> str:
    return self.email
  


class UserProfile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile', verbose_name='Юзер')
  
  first_name = models.CharField(max_length=180, verbose_name='Имя клиента')
  last_name = models.CharField(max_length=180, verbose_name='Фамилия клиента')
  retro_bonus_balance = models.IntegerField(default=0, verbose_name='Сумма бонусов клиента')
  phone = models.CharField(max_length=30, verbose_name='Телефон клиента', unique=True)
  delivery_address = models.TextField(max_length=3000, verbose_name='Адресс достаавки')
  
  class Meta:
    verbose_name = 'Юзер инфо'
    verbose_name_plural = 'Юзер инфо'
  
  def __str__(self) -> str:
    return self.user.username