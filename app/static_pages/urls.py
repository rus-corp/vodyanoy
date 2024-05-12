from django.urls import path, include


from .views import HomePageView, AboutPageView, DeliveryPageView

app_name = 'static_pages'

urlpatterns = [
  path('', HomePageView.as_view(), name='home_page'),
  path('about/', AboutPageView.as_view(), name='about_page'),
  path('delivery/', DeliveryPageView.as_view(), name='delivery')
]