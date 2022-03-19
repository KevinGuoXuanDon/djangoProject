from django.contrib import admin
from forum.models import UserProfile, Module, Post

# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    prepopulated_fileds = {'slug':('name',)}

admin.site.register(UserProfile)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Post)

