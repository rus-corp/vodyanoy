from django import template


from app.product.models import MainCategory



register = template.Library()



# def main_category_db():
#   main_categories = MainCategory.objects.all()
#   return main_categories


@register.simple_tag()
def get_main_categories():
  main_categories = MainCategory.objects.all()
  return main_categories




# @register.inclusion_tag('product/main_category.html')
# def main_category_aside():
#   main_categories = main_category_db()
#   return {'main_categories': main_categories}