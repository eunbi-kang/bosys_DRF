from django.urls import path
from . import views
from .views import delete_order_by_id

app_name = 'orders'  # alias 설정

urlpatterns = [
    path('', views.order_list, name='order_list'),  # ✅ 기본 페이지 추가
    path('list/', views.get_all_orders, name='get_all_orders'),  # `orders/` 중복 제거
    path('delete/', delete_order_by_id, name='delete_order_by_id'),  # ✅ `?id=1` 방식 지원
    path('create/', views.create_order, name='create_order'),
    path('<int:id>/', views.get_order_by_id, name='get_order_by_id'),
    path('name/<str:name>/', views.get_order_by_name, name='get_order_by_name'),
    path('age_gte/<int:age>/', views.get_order_by_age_gte, name='get_order_by_age_gte'),
]
