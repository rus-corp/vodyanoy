from django.shortcuts import render
from django.views import generic


from .models import MainCategory, SubCategory, Product


class MainCategoryView(generic.ListView):
  model = MainCategory.objects.all()
  template_name = 'produts/catalog.html'