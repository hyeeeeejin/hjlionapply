from django.db import models

# Create your models here.
class Apply(models.Model):
    name = models.CharField(max_length=10)
    snum = models.CharField(max_length=10)
    dept = models.CharField(max_length=20)
    motive = models.TextField(max_length=500)
    service = models.TextField(max_length=500)
    saw = models.TextField(max_length=500)
    aspire = models.TextField(max_length=100)
    time = models.DateTimeField()
    image = models.ImageField(upload_to = 'apply', blank = True, null = True)   # 업로드할 폴더 지정. 빈칸 허용. 널값 허용.
