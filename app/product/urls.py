from django.urls import path, include


from .views import MainCategoryView, SubCategoryView, ProductListView, ProductDetailView

app_name = 'product'

urlpatterns = [
  path('main_category/', MainCategoryView.as_view(), name='main_category'),
  path('sub_category/<str:slug>/', SubCategoryView.as_view(), name='main_sub_category'),
  path('products/<slug:slug>/', ProductListView.as_view(), name='products_list'),
  path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
]