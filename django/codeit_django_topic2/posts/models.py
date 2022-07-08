from django.db import models

# Create your models here.

class Post(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    title = models.CharField(max_length=50)
    content = models.TextField()
    # auto_now_add : 처음 생성될 때의 시간을 자동적으로 해당 필드에 저장합니다.
    # auto_now : 마지막으로 저장될 때 시간을 자동적으로 해당 필드에 저장합니다.
    dt_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name='Date Modified', auto_now=True)

    def __str__(self):
        return self.title