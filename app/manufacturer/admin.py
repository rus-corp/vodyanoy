from django.contrib import admin

from .models import Manufacturer, ManufacturerCountry


@admin.register(ManufacturerCountry)
class ManufacturerCountryAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']
  list_display_links = ['id', 'name']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'country']
  list_display_links = ['id', 'name']