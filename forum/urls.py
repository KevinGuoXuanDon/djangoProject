from django.urls import path

from forum import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('publish/', views.publish, name='publish'),
    path('register/', views.register, name='register'),#用户注册3.17
]