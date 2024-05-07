

# class StaticPageMixin:
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['page_title'] = 'Магазин инженерной сантехники'


# class CommonDataMixin:
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Общий код для всех страниц
#         context['common_data'] = 'Some common data'
#         return context

# class HomePageView(CommonDataMixin, TemplateView):
#     template_name = 'main_page/main_page.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Дополнительные данные для домашней страницы
#         context['home_specific_data'] = 'Some home specific data'
#         return context