from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from forum.forms import UserForm, UserProfileForm


# Create your views here.

def index(request):

    context_dict = {'boldmessage': 'Hot Posts, Sale of Used Items, Flats to Rent, Activities, Universities, Coffee Break'}

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

# def publish(request):

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