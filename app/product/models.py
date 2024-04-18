from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


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
    try:
      name = translit(self.name, reversed=True)
      self.slug = slugify(name)
    except:
      self.slug = slugify(self.name)
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
    try:
      name = translit(self.name, reversed=True)
      self.slug = slugify(name)
    except:
      self.slug = slugify(self.name)
    return super().save(*args, **kwargs)


class Product(models.Model):
  name = models.CharField(max_length=255, verbose_name='')
  desc = models.TextField(max_length=800, verbose_name='')
  price = models.IntegerField(verbose_name='')
  photo = models.ImageField(verbose_name='', upload_to='products_img')
  slug = models.SlugField(max_length=255, verbose_name='')
  sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='products', verbose_name='')
  
  class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'
  
  def __str__(self) -> str:
    return self.name
  
  def save(self, *args, **kwargs):
    try:
      name = translit(self.name, reversed=True)
      self.slug = slugify(name)
    except:
      self.slug = slugify(self.name)
    return super().save(*args, **kwargs)
  
  def get_absolute_url(self):
    return reverse('product:product_detail', kwargs={'product_slug': self.slug})