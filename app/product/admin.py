from django.contrib import admin

from .models import MainCategory, SubCategory, Product


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']


@admin.register(SubCategory)
class SubCategoryadmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'main_category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'price', 'sub_category']