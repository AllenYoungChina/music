from django.shortcuts import render
from django.views.generic import ListView

from index.models import Dynamic, Label


class RankingListView(ListView):
    # 设置模板的某个变量名
    context_object_name = 'dynamics'
    # 设定模板文件
    template_name = 'ranking.html'

    # 设置变量dynamics的数据
    def get_queryset(self):
        # 获取请求参数
        t = self.request.GET.get('type', '')
        if t:
            dynamics = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:10]
        else:
            dynamics = Dynamic.objects.select_related('song').order_by('-plays').all()[:10]
        return dynamics

    # 添加其他变量到上下文
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 搜索歌曲
        context['searches'] = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
        # 所有歌曲分类
        labels = Label.objects.all()
        return context
