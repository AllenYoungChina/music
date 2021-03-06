from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    """ 用户登录or注册表单 """
    # 重写初始化方法
    # 设置字段password1和password2的样式和属性
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'txt tabInput',
            'placeholder': '密码，4-16位数字/字母/符号（空格除外）',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'txt tabInput',
            'placeholder': '重复密码',
        })

    class Meta:
        model = MyUser
        # 在注册页面添加模型字段：手机号
        fields = UserCreationForm.Meta.fields + ('mobile',)
        # 设置模型字段的样式和属性
        widgets = {
            'mobile': forms.widgets.TextInput(
                attrs={'class': 'txt tabInput', 'placeholder': '手机号'}
            ),
            'username': forms.widgets.TextInput(
                attrs={'class': 'txt tabInput', 'placeholder': '用户名'}
            )
        }
