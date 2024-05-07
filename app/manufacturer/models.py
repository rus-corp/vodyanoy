from django.db import models
from django.utils.text import slugify
from transliterate import translit




class ManufacturerCountry(models.Model):
  name = models.CharField(max_length=200, verbose_name='Название', unique=True)
  image = models.ImageField(upload_to='counties_flags/', verbose_name='Флаг')
  
  class Meta:
    verbose_name = 'Страна производителя'
    verbose_name_plural = 'Страны производителей'
  
  def __str__(self) -> str:
    return self.name


class Manufacturer(models.Model):
  name = models.CharField(max_length=200, verbose_name='Название', unique=True)
  slug = models.SlugField(max_length=255, verbose_name='слаг', unique=True)
  image = models.ImageField(upload_to='manufacturer/', verbose_name='Логотип')
  country = models.ForeignKey(ManufacturerCountry, related_name='manufacurers', on_delete=models.PROTECT, verbose_name='страна')
  
  class Meta:
    verbose_name = 'Производитель'
    verbose_name_plural = 'Производители'
  
  def __str__(self) -> str:
    return self.name
  
  def save(self, *args, **kwargs):
    try:
      name = translit(self.name, reversed=True)
      self.slug = slugify(name)
    except:
      self.slug = slugify(self.name)
    return super().save(*args, **kwargs)