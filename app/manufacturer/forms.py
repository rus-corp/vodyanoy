from django import forms


from .models import Manufacturer

class ManufacturerForm(forms.Form):
  name = forms.CharField()
  is_active = forms.BooleanField()