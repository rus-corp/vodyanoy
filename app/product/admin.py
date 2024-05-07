from django.contrib import admin

from .models import MainCategory, SubCategory, Product


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']
  prepopulated_fields = {'slug': ('name',),}


@admin.register(SubCategory)
class SubCategoryadmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'main_category']
  prepopulated_fields = {'slug': ('name',),}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'price', 'sub_category']
  prepopulated_fields = {'slug': ('name',),}