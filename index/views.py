from django.shortcuts import render
from .models import Label, Song, Dynamic


def index(request):
    # 获取歌曲的动态信息
    # 使用select_related('song')减少数据查询次数
    song_dynamic = Dynamic.objects.select_related('song')
    # 热搜歌曲
    searches = song_dynamic.order_by('-search').all()[:8]
    # 音乐分类
    labels = Label.objects.all()
    # 热门歌曲
    popular = song_dynamic.order_by('-plays').all()[:10]
    # 新歌推荐
    recommend = Song.objects.order_by('-release').all()[:3]
    # 热门搜索、热门下载
    downloads = song_dynamic.order_by('-download').all()[:6]
    tabs = [searches[:6], downloads]
    return render(request=request, template_name='index.html', context=locals())


def page_not_found(request, exception):
    return render(request=request, template_name='404.html', status=404)


def page_error(request):
    return render(request=request, template_name='404.html', status=500)
