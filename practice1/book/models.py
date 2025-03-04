from django.db import models

class Book(models.Model):
   id = models.AutoField(primary_key=True, verbose_name="id")  # 자동 증가 ID
   title = models.CharField(max_length=50, verbose_name='title')
   author = models.CharField(max_length=50, verbose_name='author')
   publisher = models.CharField(max_length=50, verbose_name='publisher')
   price = models.IntegerField(verbose_name='price')

   def __str__(self):
       return f"Book {self.id} - {self.title}"
   class Meta:
    db_table = 'book' # 테이블 이름을 'book'로 설정
