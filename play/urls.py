from django.urls import path

from .views import play, download

urlpatterns = [
    # 歌曲播放
    path('<int:id>.html', play, name='play'),
    # 歌曲下载
    path('download/<int:id>.html', download, name='download'),
]
