from django.contrib import admin


from .models import CustomUser, UserProfile

class ProfileInline(admin.TabularInline):
  model = UserProfile
  extra = 1


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
  list_display = ['id', 'email', 'date_joined']
  inlines = [ProfileInline,]
  save_on_top = True
  