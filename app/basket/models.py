from django.db import models


from ..users.models import CustomUser
from ..product.models import Product



class Order(models.Model):
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
  user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='orders', verbose_name='Пользоватль заказа')
  is_payd = models.BooleanField(verbose_name='Оплата', default=False)
  order_summ = models.IntegerField(verbose_name='Сумма заказа')
  
  class Meta:
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'
    
  def __str__(self) -> str:
    return self.pk
  
  def save(self, *args, **kwargs):
    self.order_summ = sum(item.get_cost() for item in self.order_items.all())
    return super().save(*args, **kwargs)



class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_items', verbose_name='Заказ')
  product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items', verbose_name='Продукт')
  quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
  
  class Meta:
    verbose_name = 'Позиция в заказе'
    verbose_name_plural = 'Позиции в заказе'
  
  def get_cost(self):
    return self.product.price * self.quantity
  
  def __str__(self) -> str:
    return self.pk


