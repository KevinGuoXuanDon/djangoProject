from django.contrib import admin
from forum.models import UserProfile, Module, Post, Comment

# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    prepopulated_fileds = {'slug':('name',)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fileds = {'slug':('title',)}

admin.site.register(UserProfile)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

