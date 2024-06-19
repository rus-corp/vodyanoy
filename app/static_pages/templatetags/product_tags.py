from django import template


from app.product.models import MainCategory



register = template.Library()




@register.inclusion_tag('product/main_category.html')
def main_category_aside():
  main_categories = MainCategory.objects.all()
  return {'main_categories': main_categories}
  