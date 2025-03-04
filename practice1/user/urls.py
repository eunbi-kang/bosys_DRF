# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.user_list, name='user_list'),
# ]

from django.urls import path
from . import views
app_name = 'user'  # alias 설정
urlpatterns = [
    path('', views.user_list, name='user_list'),  # ✅ 기본 페이지 추가
    path('user/', views.get_all_users, name='get_all_users'),
    path('create/', views.create_user, name='create_user'),
    path('<int:id>/', views.get_user_by_id, name='get_user_by_id'),
    path('name/<str:name>/', views.get_users_by_name, name='get_users_by_name'),
    path('age_gte/<int:age>/', views.get_users_by_age_gte, name='get_users_by_age_gte'),
    path('delete/<int:id>/', views.delete_user_by_id, name='delete_user_by_id'),

]

