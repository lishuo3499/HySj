# Generated by Django 2.0.4 on 2018-06-04 19:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attented', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_attented', to=settings.AUTH_USER_MODEL)),
                ('self_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_attention', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='音乐名称')),
                ('music_url', models.CharField(max_length=100, null=True, verbose_name='音乐地址')),
            ],
            options={
                'verbose_name': '音乐',
                'verbose_name_plural': '音乐',
            },
        ),
        migrations.CreateModel(
            name='TravelsNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('private', '仅对自己可见'), ('common', '全部可见'), ('part_visual', '部分可见')], default='private', max_length=20, verbose_name='权限')),
                ('image_url', models.CharField(default='', max_length=200, verbose_name='图片地址')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('end_edit', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '游记',
                'verbose_name_plural': '游记',
            },
        ),
        migrations.CreateModel(
            name='TravelsNoteComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=500, verbose_name='评论')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '游记评论',
                'verbose_name_plural': '游记评论',
            },
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=500, verbose_name='评论')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '视频评论',
                'verbose_name_plural': '视频评论',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.CharField(default='', max_length=20, verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='video',
            name='comment_num',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
        migrations.AddField(
            model_name='video',
            name='desc',
            field=models.CharField(default='', max_length=500, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='video',
            name='fav_num',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AddField(
            model_name='video',
            name='forwarding_num',
            field=models.IntegerField(default=0, verbose_name='转发数'),
        ),
        migrations.AddField(
            model_name='video',
            name='position',
            field=models.CharField(default='', max_length=20, verbose_name='位置'),
        ),
        migrations.AddField(
            model_name='video',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='img',
            name='vodel',
            field=models.FileField(upload_to='media/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image_url',
            field=models.CharField(default='', max_length=200, verbose_name='头像地址'),
        ),
        migrations.AlterField(
            model_name='video',
            name='permission',
            field=models.CharField(choices=[('private', '仅对自己可见'), ('common', '全部可见'), ('part_visual', '部分可见')], default='private', max_length=20, verbose_name='权限'),
        ),
        migrations.AlterField(
            model_name='video',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.CharField(default='', max_length=200, verbose_name='视频地址'),
        ),
        migrations.AddField(
            model_name='favrecord',
            name='travelsnote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TravelsNote'),
        ),
        migrations.AddField(
            model_name='favrecord',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favrecord',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Video'),
        ),
        migrations.AddField(
            model_name='favrecord',
            name='video_comment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.VideoComment'),
        ),
        migrations.AddField(
            model_name='video',
            name='music',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.Music'),
        ),
        migrations.AddField(
            model_name='video',
            name='travelsnote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TravelsNote'),
        ),
    ]