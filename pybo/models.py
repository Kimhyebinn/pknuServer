from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    subject = models.CharField(max_length=200) # 제목은 보통 한 줄이며 그렇게 만들어 주는 것이 charField임
    content = models.TextField() # 여러 줄 쓰고 싶을 때 TextField 사용
    create_date = models.DateTimeField() # 게시/발행된 날짜
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #다른 객체와 연결된 경우. 유저와 어쏘는 단짝.

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #연관된 필드인 경우 외래키 사용, 질문이 삭제되면 답변도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
