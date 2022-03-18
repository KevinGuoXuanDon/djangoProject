from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from numpy import true_divide
from forum.forms import UserForm, UserProfileForm
from forum.models import Post
from forum.models import Module, Post


# Create your views here.

def index(request):
    topic_list = Module.objects.order_by('create_time')[:6]
    context_dict = {}
    context_dict['topics'] = topic_list


    return render(request, 'forum/index.html', context=context_dict)

def about(request):
    context_dict = {}

    return render(request, 'forum/about.html', context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('forum:index'))
            else:
                return HttpResponse("Your forum account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'forum/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:index'))


def publish(request):
    return HttpResponse("test")


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

def admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '123456':
            # 管理员登录成功
            return redirect(reverse('forum:admin_page'))
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'forum/admin.html')
        # if user:
        #     if user.is_active:
        #         login(request, user)
        #         return redirect(reverse('forum:index'))
        #     else:
        #         return HttpResponse("Your forum account is disabled.")
        # else:
        #     print(f"Invalid login details: {username}, {password}")
        #     return HttpResponse("Invalid login details supplied.")

def admin_page(request):
    return render(request, 'forum/admin_page.html', {"post_form":Post.objects.all()})

def post_delete(request, id):
    p=Post.objects.get(id=id)
    p.is_deleted = True
    p.delete_time = timezone.now()
    p.save()
    return HttpResponse("Delete post successfully!")
    
def topic(request):
    topic_list = Module.objects.order_by('create_time')[:6]
    post_list = Post.objects.order_by('-create_time')[:6]
    context_dict = {}
    context_dict['topics'] = topic_list
    context_dict['posts'] = post_list
    return render(request, 'forum/topic.html', context=context_dict)
