from django.db import models


class Label(models.Model):
    """ 歌曲标签 """
    id = models.AutoField(verbose_name='序号', primary_key=True)
    name = models.CharField(verbose_name='分类标签', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '歌曲标签'
        verbose_name_plural = verbose_name


class Song(models.Model):
    """ 歌曲基础信息 """
    id = models.AutoField(verbose_name='序号', primary_key=True)
    name = models.CharField(verbose_name='歌曲名称', max_length=50)
    singer = models.CharField(verbose_name='歌手姓名', max_length=50)
    time = models.CharField(verbose_name='歌曲时长', max_length=10)
    album = models.CharField(verbose_name='所属专辑', max_length=50)
    languages = models.CharField(verbose_name='歌曲语种', max_length=20)
    type = models.CharField(verbose_name='歌曲类型', max_length=20)
    release = models.DateField(verbose_name='发行时间')
    img = models.ImageField(verbose_name='歌曲图片', upload_to='songImg/')
    lyrics = models.FileField(verbose_name='歌曲歌词', upload_to='songLyric/', default='暂无歌词')
    file = models.FileField(verbose_name='歌曲文件', upload_to='songFile/')
    label = models.ForeignKey(verbose_name='歌曲标签', to=Label, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '歌曲信息'
        verbose_name_plural = verbose_name


class Dynamic(models.Model):
    """ 歌曲动态信息 """
    id = models.AutoField(verbose_name='序号', primary_key=True)
    plays = models.IntegerField(verbose_name='播放次数', default=0)
    search = models.IntegerField(verbose_name='搜索次数', default=0)
    download = models.IntegerField(verbose_name='下载次数', default=0)
    song = models.ForeignKey(verbose_name='关联歌曲', to=Song, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '歌曲动态'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    id = models.AutoField(verbose_name='序号', primary_key=True)
    text = models.CharField(verbose_name='评论内容', max_length=500)
    user = models.CharField(verbose_name='用户姓名', max_length=20)
    date = models.DateField(verbose_name='评论日期', auto_now=True)
    song = models.ForeignKey(verbose_name='关联歌曲', to=Song, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '歌曲评论'
        verbose_name_plural = verbose_name
