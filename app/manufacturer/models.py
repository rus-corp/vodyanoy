from django.db import models




from ..users.utils import create_slug



class ManufacturerCountry(models.Model):
  name = models.CharField(max_length=200, verbose_name='Название', unique=True)
  image = models.FileField(upload_to='country_flags/', verbose_name='Флаг')
  slug = models.SlugField(max_length=255, unique=True)
  
  class Meta:
    verbose_name = 'Страна производителя'
    verbose_name_plural = 'Страны производителей'
  
  def __str__(self) -> str:
    return self.name
  
  def save(self, *args, **kwargs):
    self.slug = create_slug(self.name)
    return super().save(*args, **kwargs)


class Manufacturer(models.Model):
  PRICE_SEGMENT_CHOICE = (
    ('econom', 'эконом'),
    ('middle', 'средний'),
    ('premium', 'премиум'),
  )
  name = models.CharField(max_length=200, verbose_name='Название', unique=True)
  slug = models.SlugField(max_length=255, verbose_name='слаг', unique=True)
  image = models.FileField(upload_to='manufacturer_img/', verbose_name='Логотип')
  price_segment = models.CharField(max_length=20, choices=PRICE_SEGMENT_CHOICE, default=PRICE_SEGMENT_CHOICE[1], verbose_name='Ценовой сегмент')
  
  country = models.ForeignKey(ManufacturerCountry, related_name='manufacurers', on_delete=models.PROTECT, verbose_name='страна')
  
  class Meta:
    verbose_name = 'Производитель'
    verbose_name_plural = 'Производители'
  
  def __str__(self) -> str:
    return self.name
  
  def save(self, *args, **kwargs):
    self.slug = create_slug(self.name)
    return super().save(*args, **kwargs)