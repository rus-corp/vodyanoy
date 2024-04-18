from django.apps import AppConfig


class StaticPagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.static_pages'
    verbose_name = 'Статичные страницы'
