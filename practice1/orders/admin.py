from django.contrib import admin
from .models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
   list_display = ('id', 'user', 'book', "quantity", 'price', 'order_date')