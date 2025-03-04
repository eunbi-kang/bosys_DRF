from django.db import models


class Orders(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")  # 자동 증가 ID
    user = models.CharField(max_length=50, verbose_name="user")  # 주문한 사용자 이름
    book = models.CharField(max_length=50, verbose_name="book")  # 주문한 책 제목
    quantity = models.PositiveIntegerField(verbose_name="quantity")  # 주문한 개수 (양수만 가능)
    price = models.IntegerField(verbose_name="price")  # 총 가격
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="order_date")  # 주문 날짜 (자동 생성)


def __str__(self):
    return f"Orders {self.id} - {self.user}"


class Meta:
    db_table = 'orders'  # 테이블 이름을 'orders'로 설정
