from django.shortcuts import render
from django.views import generic

from .models import CustomUser


class UserView(generic.ListView):
  queryset = CustomUser.objects.all()
  template_name = 'base.html'