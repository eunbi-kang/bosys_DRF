from django.db import models

class User(models.Model):
   name = models.CharField(max_length=50, verbose_name='name')
   email = models.CharField(max_length=50, verbose_name='email')
   age = models.IntegerField(verbose_name='age')

   def __str__(self):
       return self.name

   class Meta:
    db_table = 'user' # 테이블 이름을 'user'로 설정
