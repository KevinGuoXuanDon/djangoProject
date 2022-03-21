from django import forms
from django.contrib.auth.models import User
from forum.models import *

# record user's account and password
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

# record user's profile, but not in use for now
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

# post form is used to record posts
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=1000)
    parent_module = forms.ChoiceField(initial=1, choices=(
        ('hot posts', 'hot posts'), ('sale of used item', 'sale of used item'), ('flats to rent', 'flats to rent'), ('activity', 'activity'), ('university', 'university'),
        ('coffee break', 'coffee break')))


    class Meta:
        model = Post
        fields = ('title', 'content', 'picture')
