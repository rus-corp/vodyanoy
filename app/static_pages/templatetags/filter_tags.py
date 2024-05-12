from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def filter_tag(context):
  request = context['request']
  prices = request.GET.getlist('price_segment')
  return prices

@register.simple_tag(takes_context=True)
def country_filter(context):
  request = context['request']
  countries = request.GET.getlist('country')
  return countries
  