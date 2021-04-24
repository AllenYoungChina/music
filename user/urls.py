from django.urls import path

from .views import user_login, user_home, user_logout

urlpatterns = [
    # 用户登录或注册
    path('login.html', user_login, name='login'),
    # 用户个人中心
    path('home/<int:page>.html', user_home, name='home'),
    # 用户退出登录
    path('logout.html', user_logout, name='logout'),
]
