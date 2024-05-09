from django.db import models
from django.urls import reverse



from ..users.utils import create_slug
from app.manufacturer.models import Manufacturer

from ..users.models import CustomUser

class MainCategory(models.Model):
  name = models.CharField(max_length=150, verbose_name='Название', unique=True)
  slug = models.SlugField(max_length=200, verbose_name='слаг', unique=True)
  photo = models.ImageField(verbose_name='Фото', upload_to='category_img/main_category_img', blank=True, null=True)
  
  class Meta:
    verbose_name = 'Главная категория'
    verbose_name_plural = 'Главные категории'
  
  def __str__(self) -> str:
    return self.name
  
  def save(self, *args, **kwargs):
    self.slug = create_slug(self.name)
    return super().save(*args, **kwargs)



class SubCategory(models.Model):
  name = models.CharField(max_length=200, verbose_name='Название', unique=True)
  slug = models.SlugField(max_length=220, unique=True, verbose_name='слаг')
  photo = models.ImageField(verbose_name='Фото', upload_to='category_img/sub_category_img', blank=True, null=True)
  main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='sub_categories', verbose_name='')
  
  class Meta:
    verbose_name = 'Подкатегория'
    verbose_name_plural = 'Подкатегории'
  
  def __str__(self) -> str:
    return self.name
  
  def save(self, *args, **kwargs):
    self.slug = create_slug(self.name)
    return super().save(*args, **kwargs)


class Product(models.Model):
  name = models.CharField(max_length=255, verbose_name='название')
  desc = models.TextField(max_length=800, verbose_name='Описание')
  price = models.IntegerField(verbose_name='Цена')
  photo = models.ImageField(verbose_name='Фото', upload_to='products_img')
  slug = models.SlugField(max_length=255, verbose_name='слаг')
  retro_bonus = models.PositiveIntegerField(default=1, verbose_name='Ретро бонус за покупку клиенту %')
  
  sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='products', verbose_name='подкатегория')
  manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.PROTECT, verbose_name='производитель')
  
  
  class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'
  
  
  def __str__(self) -> str:
    return self.name
  
  
  def save(self, *args, **kwargs):
    self.slug = create_slug(self.name)
    return super().save(*args, **kwargs)
  
  def get_absolute_url(self):
    return reverse('product:product_detail', kwargs={'product_slug': self.slug})
  
  def give_retro_to_client(self) -> int:
    return int(self.retro_bonus * self.price / 100)
  
  def apply_retro_bonus(self, user: CustomUser):
    user.user_profile.retro_bonus_balance += self.give_retro_to_client()
    user.user_profile.save()
    