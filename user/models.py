from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    """ 自定义用户模型 """
    # 因为继承自AbstractUser类， 所以只需要添加自定义字段
    qq = models.CharField(verbose_name='QQ', max_length=20)
    weChat = models.CharField(verbose_name='微信', max_length=20)
    mobile = models.CharField(verbose_name='手机', max_length=20)

    def __str__(self):
        return self.username
