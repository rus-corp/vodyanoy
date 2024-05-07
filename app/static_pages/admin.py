from django.contrib import admin

from .models import SpecialOffer, Brands


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']
  list_display_links = ['id', 'name']


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']
  list_display_links = ['id', 'name']


