from django.db import models

from ..product.models import Product


# class ProductGroup(models.Model):
#   name = models.CharField(max_length=150, verbose_name='название группы')
#   product = models.ManyToManyField(Product, related_name='product_groups', verbose_name='товар')
  
#   class Meta:
#     verbose_name = 'Группа товара'
#     verbose_name_plural = 'Группы товаров'
  
#   def __str__(self) -> str:
#     return self.name




# class UserStatusSale(models.Model):
#   name = models.CharField(max_length='Тип клиента')
#   percent = models.PositiveSmallIntegerField(verbose_name='процент скидки', default=0)
  
#   class Meta:
#     verbose_name = 'verbose_name'
#     verbose_name_plural = 'verbose_name_plural'
  
#   def __str__(self) -> str:
#     return self.name