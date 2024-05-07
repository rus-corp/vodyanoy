from django.db import models






class SpecialOffer(models.Model):
  name = models.CharField(max_length=150, verbose_name='Название')
  image = models.ImageField(verbose_name='Фото', upload_to='special_offers/%Y/m', help_text='Максимальное разрешение изображения 2400х600px')
  
  class Meta:
    verbose_name = 'Спец.предложение на главной странице'
    verbose_name_plural = 'Спец.предложения на главной странице'

  def __str__(self) -> str:
    return self.name



class Brands(models.Model):
  name = models.CharField(max_length=200, verbose_name='Название бренда')
  image = models.ImageField(verbose_name='Лого бренда', upload_to='', blank=True, null=True, help_text='Перед загрузкой удалить фон у фото')
  
  class Meta:
    verbose_name = 'Бренд'
    verbose_name_plural = 'Бренды'
  
  def __str__(self) -> str:
    return self.name



class AboutInfo(models.Model):
  name = models.CharField(max_length=200, verbose_name='название пункта')
  desc = models.TextField(verbose_name='Описание пункта')
  
  class Meta:
    verbose_name = 'Инфо О нас'
    verbose_name_plural = 'Инфо О нас'
  
  def __str__(self) -> str:
    return self.name