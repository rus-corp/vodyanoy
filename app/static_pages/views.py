from typing import Any
from django.shortcuts import render



from ..news.models import News
from ..product.models import MainCategory, SubCategory, Product
# from .mixins import StaticPageMixin

from .models import SpecialOffer
from django.views.generic.base import TemplateView





class HomePageView(TemplateView):
  template_name = 'main_page/main_page.html'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['page_title'] = 'Магазин инженерной сантехники'
    context['slider_images'] = SpecialOffer.objects.all()
    context['news_list'] = News.objects.all()[:8]
    context['brand_list'] = Product.objects.all()[:5]
    
    return context


class AboutPageView(TemplateView):
  template_name = 'static_page/about_page.html'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['page_title'] = 'О компании'
    context['sub_categories'] = SubCategory.objects.all()
    return context


class DeliveryPageView(TemplateView):
  template_name = 'static_page/delivery_page.html'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['page_title'] = 'Бесплатная Доставка в компании '
    return context
