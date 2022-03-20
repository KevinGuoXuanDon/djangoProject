from base64 import standard_b64decode

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from forum import models
# from numpy import true_divide
from forum.forms import PostForm, UserForm, UserProfileForm
from forum.models import Module, Post, UserProfile
from django import forms
from django.views import View


# Create your views here.

def index(request):
    topic_list = Module.objects.order_by('create_time')[:6]
    standard_list = Module.objects.order_by('create_time')[:6]
    for topic in standard_list:
        topic.name = str.lower(topic.name)
        topic.name = topic.name.replace(" ", "-")

    context_dict = {}
    context_dict['topics'] = topic_list
    context_dict['standards'] = standard_list

    return render(request, 'forum/index.html', context=context_dict)


def about(request):
    context_dict = {}

    return render(request, 'forum/about.html', context_dict)


@login_required
def published(request):
    context_dict = {}

    return render(request, 'forum/published.html', context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                next = request.POST.get('next')
                if next:
                    redirect(next)
                return JsonResponse(data={
                    'code': 0,
                    'msg': 'login success',
                    'data': {
                        'url': reverse('forum:index'),
                        'next': next
                    }
                })
            else:
                return JsonResponse(data={
                    'code': -1,
                    'msg': 'user is inactive',
                    'data': {}
                })
        else:
            return JsonResponse(data={
                'code': -1,
                'msg': 'Invalid login details supplied.',
                'data': {}
            })
    else:
        return render(request, 'forum/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:index'))


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

            return JsonResponse(data={
                'code': 0,
                'msg': 'ok',
                'data': {'url': reverse('forum:login')}
            })

        else:
            return JsonResponse(data={
                'code': -1,
                'msg': str(user_form.errors)
            })
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'forum/register.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '123456':
            # admin login successful
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
    return render(request, 'forum/admin_page.html', {"post_form": Post.objects.all()})


@login_required
def delete_post(request, id):
    p = Post.objects.get(id=id)
    p.is_deleted = True
    p.delete_time = timezone.now()
    p.save()
    return HttpResponseRedirect(reverse('forum:admin_page'))


@login_required
def topic(request, topic_name_slug):
    context_dict = {}
    try:
        topic_list = Module.objects.order_by('create_time')[:6]
        topic = Module.objects.get(slug=topic_name_slug)
        post_list_before = Post.posts.filter(parent_module=topic)
        post_list = post_list_before.order_by('-create_time')[:20]
        standard_list = Module.objects.order_by('create_time')[:6]
        for standard in standard_list:
            standard.name = str.lower(standard.name)
            standard.name = standard.name.replace(" ", "-")
        context_dict['posts'] = post_list
        context_dict['topic'] = topic
        context_dict['topiclist'] = topic_list
        context_dict['standards'] = standard_list
    except Module.DoesNotExist:
        context_dict['posts'] = None
        context_dict['topic'] = None
        context_dict['topiclist'] = None
        context_dict['standards'] = None
    return render(request, 'forum/topic.html', context=context_dict)


@login_required
def post(request, id):
    context_dict = {}
    try:

        post = Post.posts.get(id=id)
        topic = post.parent_module.name
        topic = str.lower(topic)
        topic = topic.replace(" ", "-")
        context_dict['post'] = post
        context_dict['topic'] = topic

    except Post.DoesNotExist:
        context_dict['post'] = None
        context_dict['topic'] = None
    return render(request, 'forum/post.html', context_dict)


@login_required
def publish(request):
    standard_list = Module.objects.order_by('create_time')[:1]
    for topic in standard_list:
        topic.name = str.lower(topic.name)
        topic.name = topic.name.replace(" ", "-")

    context_dict = {}
    context_dict['standards'] = standard_list

    if request.method == "POST":
        post_form = PostForm(request.POST)
        title = post_form.data.get("title")
        content = post_form.data.get("content")
        parent_module_name = post_form.data.get("parent_module")
        print(parent_module_name)
        parent_module = Module.objects.get(name=parent_module_name)
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user=user)
        if post_form.is_valid():
            post = Post.posts.create(title=title, content=content, parent_module=parent_module, poster=userprofile)
            if 'picture' in request.FILES:
                post.picture = request.FILES['picture']
            post.save()
        else:
            print(post_form.errors)

    else:
        post_form = PostForm()

    return render(request, 'forum/publish.html', context_dict)


class IncreaseLikesView(View):
    def post(self, request, *args, **kwargs):
        post = Post.posts.get(id=kwargs.get('id'))
        post.likes += 1
        post.save()
        return HttpResponse('success')

