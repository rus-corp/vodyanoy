from typing import Any
from django.core.management.base import BaseCommand
import os
import csv
import random

from app.product.models import SubCategory, Product
from app.manufacturer.models import Manufacturer

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'products.csv')


photos = ['santech1.jpg', 'unnamed.jpg', 'vanna2.jpg']


class Command(BaseCommand):
  def handle(self, *args: Any, **options: Any):
    with open(file_path, encoding='utf-8') as file:
      data = list(csv.DictReader(file, delimiter=';'))
    for prod in data:
      photo = random.choice(photos)
      photo_url = 'products_img/' + photo
      sub_categ = SubCategory.objects.get(pk=random.randint(1, 27))
      man = Manufacturer.objects.get(pk=random.randint(1 ,3))
      p = Product(name=prod['name'], desc=prod['desc'], price=prod['price'],
                  photo=prod['photo'], sub_category=sub_categ, manufacturer=man)
      p.save()
    