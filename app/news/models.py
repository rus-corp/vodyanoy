from django.db import models

class News(models.Model):
  name = models.CharField(max_length=200, verbose_name='Название новости')
  desc = models.TextField(verbose_name='Текст новости')
  image = models.ImageField(upload_to='news/%Y/%m/%d', blank=True, null=True, verbose_name='Фото обложки новости')
  is_active = models.BooleanField(verbose_name='Отоброжение на сайте', default=True)
  slug = models.SlugField(max_length=255, verbose_name='слаг')
  
  class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
  
  def __str__(self) -> str:
    return self.name