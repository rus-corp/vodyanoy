from django import template


register = template.Library()


@register.simple_tag
def head_title(page_title):
  total_title = page_title + " Водяной vodyanoy.asia"
  return total_title