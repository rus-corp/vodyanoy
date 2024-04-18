from django.contrib import admin

from .models import SpecialOffer


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']