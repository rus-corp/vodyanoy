from typing import Any
from django.core.management.base import BaseCommand
import os
import csv

from app.product.models import SubCategory, MainCategory

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'sub_categ.csv')



class Command(BaseCommand):
  def handle(self, *args: Any, **options: Any):
    with open(file_path, encoding='utf-8') as file:
      data = list(csv.DictReader(file, delimiter=';'))
    for item in data:
      main_categ = MainCategory.objects.get(pk=item['main_category'])
      sub_categ = SubCategory(name=item['name'], photo=item['image'], main_category=main_categ)
      sub_categ.save()