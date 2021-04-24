from django.contrib import admin

from .models import Label, Song, Dynamic, Comment


# 修改Admin后台管理页面的标题（浏览器tab栏标题）
admin.site.site_title = '我的音乐后台管理系统'
# 修改Admin后台管理页面标题（页面内容的标题）
admin.site.site_header = '我的音乐'


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    # 设置列表页显示字段
    list_display = ['id', 'name']
    # 设置可用于搜索的字段
    search_fields = ['name']
    # 设置排序方式（默认主键，递增，可不设置）
    ordering = ['id']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'singer', 'album', 'languages', 'release', 'img', 'lyrics', 'file']
    search_fields = ['name', 'singer', 'album', 'languages']
    # 设置可用于过滤的字段
    list_filter =['singer', 'album', 'languages']
    ordering = ['id']


@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ['id', 'song', 'plays', 'search', 'download']
    search_fields = ['song__name']
    list_filter = ['plays', 'search', 'download']
    ordering = ['id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'song', 'date']
    search_fields = ['user', 'song__name']
    list_filter = ['song', 'date']
    ordering = ['id']
