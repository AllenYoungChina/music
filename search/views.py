from django.shortcuts import render, redirect, reverse
from django.db.models import Q, F
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from index.models import Dynamic, Song


def search(request, page):
    if request.method == 'GET':
        # 热搜歌曲
        searches = Dynamic.objects.select_related('song').order_by('-search').all()[:6]
        # 获取搜索内容，如果kword为空，则查询全部歌曲（返回前50条数据）
        kword = request.session.get('kword', '')
        if kword:
            songs = Song.objects.filter(Q(name__icontains=kword) | Q(singer=kword)).order_by('-release').all()
        else:
            songs = Song.objects.order_by('-release').all()[:50]

        # 分页功能
        paginator = Paginator(object_list=songs, per_page=5)
        try:
            pages = paginator.page(number=page)
        except PageNotAnInteger:
            pages = paginator.page(number=1)
        except EmptyPage:
            pages = paginator.page(number=paginator.num_pages)

        # 添加搜索次数
        if kword:
            song_list = Song.objects.filter(name__icontains=kword)
            for song in song_list:
                # 判断歌曲动态信息是否存在，若存在则字段search值+1
                dynamics = Dynamic.objects.filter(song_id=song.id)
                if dynamics:
                    dynamics.update(search=F('search') + 1)
                else:
                    dynamics.create(plays=0, search=1, download=1, song=song)
        return render(request=request, template_name='search.html', context=locals())
    else:
        # 处理POST请求
        # 将浏览器提交的表单中的参数kword放入到session中
        request.session['kword'] = request.POST.get('kword', '')
        # 跳转至GET请求处理，并携带请求参数page=1
        return redirect(to=reverse(viewname='search', kwargs={'page': 1}))
