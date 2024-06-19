from django.urls import path, include


from .views import MainCategoryView

app_name = 'product'

urlpatterns = [
  path('category/', MainCategoryView.as_view(), name='category'),
]