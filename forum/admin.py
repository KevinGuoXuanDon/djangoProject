from django.contrib import admin
from forum.models import UserProfile, Module, Post

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Module)
admin.site.register(Post)