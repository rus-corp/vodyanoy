from typing import Any
from django.shortcuts import render


from .models import SpecialOffer
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
  template_name = 'main_page/main_page.html'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['page_title'] = 'Магазин инженерной сантехники'
    context['slider_images'] = SpecialOffer.objects.all()
    return context