from django.urls import path

from forum import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('publish/', views.publish, name='publish'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('delete_post/<id>', views.delete_post, name='delete_post'),
    path('topic/<slug:topic_name_slug>/', views.topic, name='topic'),
    path('post/<id>/', views.post, name='post'),
    path('published/', views.published, name='published'),
    path('likes/<id>/',views.IncreaseLikesView.as_view(), name='increase_likes'),
]