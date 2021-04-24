from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import MyUser
from .forms import MyUserCreationForm
from index.models import Dynamic


def user_login(request):
    # 实例化表单，用于传递到模板
    user = MyUserCreationForm()
    # 提交表单
    if request.method == 'POST':
        # 判断用户是登录还是注册（根据表单传递的变量的key是否有loginUser来判断）
        # 用户登录
        if request.POST.get('loginUser', ''):
            u = request.POST.get('loginUser', '')
            p = request.POST.get('password', '')
            if MyUser.objects.filter(Q(mobile=u) | Q(username=u)):
                user = MyUser.objects.filter(Q(mobile=u) | Q(username=u)).first()
                if check_password(p, user.password):
                    login(request=request, user=user)
                    return redirect(to=reverse(viewname='index'))
                else:
                    tips = '密码错误'
            else:
                tips = '用户不存在'
        # 用户注册
        else:
            u = MyUserCreationForm(request.POST)
            if u.is_valid():
                u.save()
                tips = '注册成功，请登录'
            else:
                # 获取验证失败字段的错误信息
                if u.errors.get('username', ''):
                    tips = u.errors.get('username', '注册失败')
                else:
                    tips = u.errors.get('mobile', '注册失败')
    return render(request=request, template_name='user.html', context=locals())


@login_required(login_url='/user/login.html')
def user_home(request, page):
    # 热搜歌曲
    searches = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    # 播放列表分页
    songs = request.session.get('play_list', [])
    paginator = Paginator(object_list=songs, per_page=3)
    try:
        pages = paginator.page(number=page)
    except PageNotAnInteger:
        pages = paginator.page(number=1)
    except EmptyPage:
        pages = paginator.page(number=paginator.num_pages)
    return render(request=request, template_name='home.html', context=locals())


def user_logout(request):
    logout(request=request)
    return redirect(to=reverse(viewname='index'))
