from django import forms
from django.contrib.auth.models import User #用户注册3.17
from forum.models import UserProfile# 用户注册3.17


class UserForm(forms.ModelForm): #用户注册3.17
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):#用户注册3.17
    class Meta:
        model = UserProfile
        fields = ('picture',)
