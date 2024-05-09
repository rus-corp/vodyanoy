from transliterate import translit
from django.utils.text import slugify


def create_slug(name: str):
  try:
    name = translit(name, reversed=True)
    slug = slugify(name)
  except:
    slug = slugify(name)
  return slug