from django.urls import path, include

from .views import ManufacturerListView, ManuListView

app_name = 'manufacturer'

urlpatterns = [
  path('', ManufacturerListView.as_view(), name='manufacturer'),
  path('form_test', ManuListView.as_view(), name='form_test')
]