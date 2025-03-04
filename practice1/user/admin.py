from django.contrib import admin
from .models import User

@admin.register(User)
class BookAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'age')