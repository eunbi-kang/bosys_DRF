from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
# 기본 루트 요청을 처리하는 뷰 함수 추가
def home(request):
    return HttpResponse("<h1>Welcome to the API</h1>")
urlpatterns = [
    path('', home, name='home'),  # ✅ 루트 URL 요청 처리 (기본 페이지)
    path('admin/', admin.site.urls),  # ✅ Django Admin
    path('user/', include('user.urls')),  # ✅ user 앱 URL 포함
    path('book/', include('book.urls')),  # ✅ book 앱 URL 포함
    path('orders/', include('orders.urls')),  # ✅ orders 앱 URL 포함
]
