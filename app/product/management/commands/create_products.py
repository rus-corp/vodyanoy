from typing import Any
from django.core.management.base import BaseCommand


from app.product.models import Product


class Command(BaseCommand):
  def handle(self, *args: Any, **options: Any):
    pass