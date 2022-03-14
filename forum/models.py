from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class UserProfile(models.Model):
    # simple call the django's User model, which has filed:
    # username,password,email,user_permissions,
    # is_staff,is_active,is_superuser,
    # last_login,date_joined
    # We will use: username,email,password,user_permissions, is_active,last_login,date_joined
    NAME_MAX_LENGTH = 30
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    sex = models.CharField(max_length=10,blank=True, null=True)
    post_number = models.IntegerField(default=0)
    like_number = models.IntegerField(default=0)
    follow_number = models.IntegerField(default=0)
    follower_number = models.IntegerField(default=0)
    follow_to = models.TextField(null=False)
    follow_by = models.TextField(null=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    is_muted = models.BooleanField(default=False)

    # customise get set method for two list
    def set_follow_to_list(self, element):
        if self.follow_to:
            self.follow_to = self.follow_to + "," + element
        else:
            self.follow_to = element

    def get_follow_to_list(self):
        if self.follow_to:
            return self.follow_to.split(",")

    def set_follow_by_list(self, element):
        if self.follow_by:
            self.follow_by = self.follow_by + "," + element
        else:
            self.follow_by = element

    def get_follow_by_list(self):
        if self.follow_by:
            return self.follow_by.split(",")

    # toString
    def __str__(self):
        return self.user.username


# Also can be called Category
class Module(models.Model):
    NAME_MAX_LENGTH = 50
    DES_MAX_LENGTH = 50
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=DES_MAX_LENGTH)
    create_time = models.DateTimeField(auto_created=True)
    slug = models.SlugField(unique= True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Module, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# Manager class, not real model
class PostManage(models.Manager):
    def get_query(self):
        return super(PostManage, self).get_queryset().filter(is_deleted=False)


class Post(models.Model):
    TITLE_MAX_LENGTH = 30
    title = models.CharField(max_length=TITLE_MAX_LENGTH, null=False)
    content = models.TextField('content', blank=True, null=True)
    picture = models.ImageField(upload_to='post_images', blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comment_number = models.IntegerField(default=0)
    top = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_created=True)
    update_time = models.DateTimeField(auto_now=True)
    # not truly delete in database, but marked as deleted, so it would not be queried out
    is_deleted = models.BooleanField('isDelete', default=False)
    delete_time = models.DateTimeField('deleteTime', blank=True, null=True)
    object = PostManage()
    parent_module = models.ForeignKey(Module,on_delete=models.CASCADE)
    poster = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# It can also write in UserProfile, but separates in order to share the load of UserProfile table
class StarContent(models.Model):
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stared_post = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.username


class Comment(models.Model):
    # one user only make a Comment to another user in a post
    comment_by = models.OneToOneField(UserProfile,on_delete=models.CASCADE, related_name='commenter')
    comment_to = models.OneToOneField(UserProfile,on_delete=models.CASCADE, related_name='receiver')
    comment_in = models.OneToOneField(Post,on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    # picture??? picture = models.ImageFiled()
    create_time = models.DateTimeField(auto_created=True)

    # there is no is_deleted filed in this class, so the comment can be truly be deleted

    def __str__(self):
        return self.comment_by + "comment in" + self.comment_in + "to" + self.comment_to
