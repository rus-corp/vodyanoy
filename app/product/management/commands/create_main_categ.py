from typing import Any
from django.core.management.base import BaseCommand
import csv
import os


curent_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(curent_dir, 'main_categ.csv')


from app.product.models import MainCategory


class Command(BaseCommand):
  def handle(self, *args: Any, **options: Any):
    with open(file_path, encoding='utf-8') as file:
      data = list(csv.DictReader(file, delimiter=';'))
    data_list = []
    MainCategory.objects.all().delete()
    for item in data:
      categ = MainCategory(name=item['name'], photo=item['image'])
      categ.save()
