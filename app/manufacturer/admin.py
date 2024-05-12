from django.contrib import admin

from .models import Manufacturer, ManufacturerCountry


@admin.register(ManufacturerCountry)
class ManufacturerCountryAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']
  list_display_links = ['id', 'name']
  prepopulated_fields = {'slug': ('name',),}


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'price_segment','country']
  list_display_links = ['id', 'name']
  prepopulated_fields = {'slug': ('name',),}