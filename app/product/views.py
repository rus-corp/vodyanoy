from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404


from .models import MainCategory, SubCategory, Product


class MainCategoryView(generic.ListView):
  model = MainCategory
  template_name = 'product/catalog.html'
  context_object_name = 'categories'


class SubCategoryView(generic.ListView):
  template_name = 'product/sub_category.html'
  context_object_name = 'sub_categories'
  
  def get_queryset(self) -> QuerySet[Any]:
    main_category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
    queryset = main_category.sub_categories .all()
    return queryset