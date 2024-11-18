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
    queryset = Product.objects.filter(sub_category__slug=self.kwargs['slug']).select_related('sub_category')
    # queryset = Product.objects.select_related('sub_category').values('id', 'name')
    # queryset = Product.objects.prefetch_related(Prefetch('sub_category', queryset=SubCategory.objects.all()))
    
    return queryset
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    self.sub_category = SubCategory.objects.select_related('main_category').get(slug=self.kwargs['slug'])
    main_category = self.sub_category.main_category
    context['sub_categories'] = SubCategory.objects.filter(main_category=main_category)
    context['page_title'] = 'Каталог товаров'
    return context

  


class ProductDetailView(generic.DetailView):
  template_name = 'product/product_detail.html'
  context_object_name = 'product'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['page_title'] = context['product'].name
    return context
  
  def get_queryset(self) -> QuerySet[Any]:
    queryset = Product.objects.filter(slug=self.kwargs['slug']).select_related('manufacturer').select_related('sub_category')
    return queryset
  