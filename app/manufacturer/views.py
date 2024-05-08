from typing import Any
from django.shortcuts import render
from django.views import generic


from .models import Manufacturer, ManufacturerCountry


class ManufacturerListView(generic.ListView):
  model = Manufacturer
  template_name = 'manufacturer/manufacturer.html'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['countries'] = ManufacturerCountry.objects.all()
    return context