from django.db import models
from datetime import datetime
from consumer.models import UserInfo


# Create your models here.
class IMG(models.Model):  # 视频图片上传
    vodel = models.FileField(upload_to='media/%Y/%m', max_length=100)


class COSbucket(models.Model):  # 腾讯云存储图片和视频地址
    vodel_address = models.CharField(max_length=200, default='')
    image_address = models.CharField(max_length=200, default='')


class Music(models.Model):
    name = models.CharField(verbose_name='音乐名称', max_length=50, null=True)
    music_url = models.CharField(verbose_name='音乐地址', max_length=100, null=True)

    class Meta:
        verbose_name = '音乐'
        verbose_name_plural = verbose_name


class TravelsNote(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
    permission = models.CharField(choices=(('private', u'仅对自己可见'), ('common', u'全部可见'), ('part_visual', '部分可见')),
                                  max_length=20, default='private', verbose_name='权限')
    image_url = models.CharField(max_length=200, default='', verbose_name='图片地址')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    end_edit = models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')

    class Meta:
        verbose_name = '游记'
        verbose_name_plural = verbose_name


class VideoComment(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500, verbose_name='评论', default='')

    class Meta:
        verbose_name = '视频评论'
        verbose_name_plural = verbose_name


class TravelsNoteComment(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500, verbose_name='评论', default='')

    class Meta:
        verbose_name = '游记评论'
        verbose_name_plural = verbose_name


class Video(models.Model):
    permission = models.CharField(choices=(('private', u'仅对自己可见'), ('common', u'全部可见'), ('part_visual', '部分可见')),
                                  max_length=20, default='private', verbose_name='权限')
    video_url = models.CharField(max_length=200, default='', verbose_name='视频地址')
    image_url = models.CharField(max_length=200, default='', verbose_name='头像地址')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')
    user = models.ForeignKey(UserInfo, verbose_name='用户', on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=20, verbose_name='标签', default='')
    fav_num = models.IntegerField(verbose_name='点赞数', default=0)
    comment_num = models.IntegerField(verbose_name='评论数', default=0)
    forwarding_num = models.IntegerField(verbose_name='转发数', default=0)
    desc = models.CharField(max_length=500, verbose_name='描述', default='')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, default='')
    travelsnote = models.ForeignKey(TravelsNote, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=20, verbose_name=u'位置', default='')


class FavRecord(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
    travelsnote = models.ForeignKey(TravelsNote, on_delete=models.CASCADE, null=True)
    video_comment = models.ForeignKey(VideoComment, on_delete=models.CASCADE, default='')


class Attention(models.Model):
    self_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='user_attention')
    is_attented = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='user_attented')
