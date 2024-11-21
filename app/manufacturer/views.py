from typing import Any
from django.shortcuts import render
from django.views import generic


from .models import Manufacturer, ManufacturerCountry

from .forms import ManufacturerForm



class ManufacturerListView(generic.ListView):
  queryset = Manufacturer.objects.all()
  template_name = 'manufacturer/manufacturer.html'
  context_object_name = 'manufacturers'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['countries'] = ManufacturerCountry.objects.all()
    context['page_title'] = 'Бренды в магазине'
    return context
  
  def get_queryset(self):
    queryset = Manufacturer.objects.all()
    price_segment = self.request.GET.getlist('price_segment')
    country_segment = self.request.GET.getlist('country')
    if price_segment:
      queryset = queryset.filter(price_segment__in=price_segment)
    if country_segment:
      queryset = queryset.filter(country__name__in=country_segment)
    return queryset



class ManuListView(generic.ListView):
  template_name = 'manufacturer/form_test.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'] = ManufacturerForm
    return context
  
  def get_queryset(self):
    queryset = Manufacturer.objects.all()
    price_segment = self.request.GET.get('price_segment', 'all')
    if 'econom' in price_segment:
      queryset = Manufacturer.objects.filter(price_segment='econom')
    return queryset