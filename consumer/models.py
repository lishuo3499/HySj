from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):  # 用户信息
    header_url = models.CharField(max_length=200, default='')  # 头像地址
    nick_name = models.CharField(max_length=200, default='')  # 昵称

    def __str__(self):
        return self.username

