from django.urls import path, include

from .views import ManufacturerListView

app_name = 'manufacturer'

urlpatterns = [
  path('', ManufacturerListView.as_view(), name='manufacturer')
]