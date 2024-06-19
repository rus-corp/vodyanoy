from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic


from .models import MainCategory, SubCategory, Product


class MainCategoryView(generic.ListView):
  model = MainCategory
  template_name = 'product/catalog.html'
  context_object_name = 'categories'