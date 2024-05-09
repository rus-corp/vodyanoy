from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic


from .models import Manufacturer, ManufacturerCountry





class ManufacturerListView(generic.ListView):
  template_name = 'manufacturer/manufacturer.html'
  context_object_name = 'manufacturers'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['countries'] = ManufacturerCountry.objects.all()
    context['page_title'] = 'Бренды в магазине'
    return context
  
  def get_queryset(self) -> QuerySet[Any]:
    price_segment = self.request.GET.get('price_segment')
    if price_segment:
      queryset = Manufacturer.objects.filter(price_segment=price_segment)
    queryset = Manufacturer.objects.all()
    return queryset