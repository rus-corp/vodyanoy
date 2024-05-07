from django.contrib import admin

from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'is_active']
  list_display_links= ['id', 'name']
  prepopulated_fields = {'slug': ('name',),}
  actions = ['change_status']
  list_editable = ('is_active',)
  
