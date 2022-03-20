from django import forms
from django.contrib.auth.models import User
from forum.models import *


class UserForm(forms.ModelForm):
    # 如果需要的话，这里还可以添加其他字段。目前肯定需要password，可能可以添加username等，看你们业务需求
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    # 同上，如果需要则添加其他字段，下面我写了用户可能有的图片和网站
    class Meta:
        model = UserProfile
        fields = ('picture',)


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=1000)
    parent_module = forms.ChoiceField(initial=6, choices=(
    (1, 'Hot Posts'), (2, 'Sale of Used Items'), (3, 'Flat to Rent'), (4, 'Activities'), (5, 'Universities'),
    (6, 'Coffee Break')))

    class Meta:
        model = Post
        fields = ('title', 'content','picture' ,'parent_module')
