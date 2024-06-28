from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404


from .models import MainCategory, SubCategory, Product


class MainCategoryView(generic.ListView):
  model = MainCategory
  template_name = 'product/catalog.html'
  context_object_name = 'main_categories'


class SubCategoryView(generic.ListView):
  template_name = 'product/sub_category.html'
  context_object_name = 'sub_categories_list'
  
  def get_queryset(self) -> QuerySet[Any]:
    sub_categories = SubCategory.objects.filter(main_category__slug=self.kwargs['slug'])
    return sub_categories


class ProductListView(generic.ListView):
  template_name = 'product/products_list.html'
  context_object_name = 'product_list'
  
  def get_queryset(self) -> QuerySet[Any]:
    queryset = Product.objects.filter(sub_category__slug=self.kwargs['slug']).select_related('manufacturer')
    return queryset


class ProductDetailView(generic.DetailView):
  template_name = 'product/product_detail.html'
  context_object_name = 'product'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = context['product'].name
  
  def get_queryset(self) -> QuerySet[Any]:
    queryset = Product.objects.filter(slug=self.kwargs['product_slug']).select_related('manufacturer').select_related('sub_category')
    return queryset
  