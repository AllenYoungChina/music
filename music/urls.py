"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from index.views import page_not_found, page_error

urlpatterns = [
    path('admin/', admin.site.urls),
    # 设置各个应用的路由空间
    # 路由数量很少，无需使用namespace参数
    path('', include('index.urls')),
    path('ranking.html', include('ranking.urls')),
    path('play/', include('play.urls')),
    path('comment/', include('comment.urls')),
    path('search/', include('search.urls')),
    path('user/', include('user.urls')),
    # 定义媒体资源访问路由
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # 定义静态文件路由（上线模式，Django模板文件需要使用静态文件）
    re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}, name='static')
]

# 设置404和500页面
handler404 = page_not_found
handler500 = page_error
