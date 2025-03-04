from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Orders
       fields = ["id", 'user', 'book', "quantity", "price", 'order_date']


