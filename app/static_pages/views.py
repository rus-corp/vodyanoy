from typing import Any
from django.shortcuts import render

from ..news.models import News
from ..product.models import MainCategory

from .models import SpecialOffer, Brands
from django.views.generic.base import TemplateView



class HomePageView(TemplateView):
  template_name = 'main_page/main_page.html'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['page_title'] = 'Магазин инженерной сантехники'
    context['slider_images'] = SpecialOffer.objects.all()
    context['news_list'] = News.objects.all()[:4]
    context['brand_list'] = Brands.objects.all()
    context['main_categories'] = MainCategory.objects.all()
    return context


class AboutPageView():
  pass