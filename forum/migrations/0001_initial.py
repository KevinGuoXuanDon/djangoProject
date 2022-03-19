# Generated by Django 2.1.5 on 2022-03-19 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True, null=True, verbose_name='content')),
                ('picture', models.ImageField(blank=True, upload_to='post_images')),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('comment_number', models.IntegerField(default=0)),
                ('top', models.BooleanField(default=False)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='isDelete')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='deleteTime')),
                ('parent_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Module')),
            ],
        ),
        migrations.CreateModel(
            name='StarContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stared_post', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('post_number', models.IntegerField(default=0)),
                ('like_number', models.IntegerField(default=0)),
                ('follow_number', models.IntegerField(default=0)),
                ('follower_number', models.IntegerField(default=0)),
                ('follow_to', models.TextField(null=True)),
                ('follow_by', models.TextField(null=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('is_muted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='starcontent',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.UserProfile'),
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='forum.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_in',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forum.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_to',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='forum.UserProfile'),
        ),
    ]
