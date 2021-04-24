import time

from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404

from index.models import Dynamic, Comment, Song


def comment(request, id):
    # 热搜歌曲
    searches = Dynamic.objects.select_related('song').order_by('-search').all()[:6]
    # 点评内容提交功能
    if request.method == 'POST':
        text = request.POST.get('comment', '')
        # 如果用户处于登录状态，就使用用户名，否则使用匿名用户
        if request.user.is_authenticated:
            user = request.user.username
        else:
            user = '匿名用户'
        now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if text:
            Comment.objects.create(text=text, user=user, song_id=id, date=now)
        return redirect(to=reverse(viewname='comment', kwargs={'id': str(id)}))
    else:
        songs = Song.objects.filter(id=id).filter()
        # 若歌曲不存在，抛出404异常
        if not songs:
            raise Http404('歌曲不存在')
        c = Comment.objects.filter(song_id=id).order_by('date')
        page = int(request.GET.get('page', 1))
        paginator = Paginator(object_list=c, per_page=2)
        try:
            pages = paginator.page(number=page)
        except PageNotAnInteger:
            pages = paginator.page(number=1)
        except EmptyPage:
            pages = paginator.page(number=paginator.num_pages)
        return render(request=request, template_name='comment.html', context=locals())
