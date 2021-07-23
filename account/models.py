from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):   # abstrac저거 f12눌러바.
    name = models.CharField(max_length=10)
    student_id = models.CharField(max_length=10)
    major = models.CharField(max_length=20)
