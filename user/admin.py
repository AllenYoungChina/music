from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'mobile', 'qq', 'weChat']
    # 用户新增或修改页面添加字段mobile、qq、WeChat
    # 将源码中的UserAdmin.filedsets转换为列表格式
    fieldsets = list(UserAdmin.fieldsets)
    # 重写UserAdmin的fieldsets，添加字段mobile，qq和WeChat
    fieldsets[1] = (_('Personal info'), {
        'fields': ('first_name', 'last_name', 'email', 'mobile', 'qq', 'weChat')
    })
