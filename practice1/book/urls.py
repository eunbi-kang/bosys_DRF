

from django.urls import path
from . import views
app_name = 'book'  # alias 설정
urlpatterns = [
    path('', views.book_list, name='book_list'),  # ✅ 기본 페이지 추가
    path('books/', views.get_all_books, name='get_all_books'),
    path('delete/', views.delete_book_by_id, name='delete_book_by_id'),
    path('create/', views.create_book, name='create_book'),
    path('<int:id>/', views.get_book_by_id, name='get_book_by_id'),
    path('name/<str:name>/', views.get_books_by_name, name='get_books_by_name'),
    path('age_gte/<int:age>/', views.get_books_by_age_gte, name='get_books_by_age_gte'),

]

