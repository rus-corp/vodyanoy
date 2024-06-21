from django.urls import path, include


from .views import MainCategoryView, SubCategoryView

app_name = 'product'

urlpatterns = [
  path('category/', MainCategoryView.as_view(), name='main_category'),
  path('category/<str:slug>/', SubCategoryView.as_view(), name='main_sub_category'),
]