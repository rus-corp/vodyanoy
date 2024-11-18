from django.contrib import admin

from .models import MainCategory, SubCategory, Product, ProductParametr, ProductPhoto


class ProductParametrAdmin(admin.TabularInline):
  model = Product.parametr.through
  extra = 2


class ProducPhotoInline(admin.TabularInline):
  model = ProductPhoto
  extra = 2


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']
  prepopulated_fields = {'slug': ('name',),}
  list_display_links = ['id', 'name']


@admin.register(SubCategory)
class SubCategoryadmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'main_category']
  prepopulated_fields = {'slug': ('name',),}
  list_display_links = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'price', 'sub_category']
  prepopulated_fields = {'slug': ('name',),}
  list_display_links = ['id', 'name',]
  inlines = [ProductParametrAdmin, ProducPhotoInline,]


admin.site.register(ProductParametr)