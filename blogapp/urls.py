from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register',views.register, name='register'),
    path('login',views.user_login, name='login'),
    path('logout',views.user_logout, name='logout'),
    path('post_blog',views.post_blog, name='post_blog'),
    path('blog_detail/<int:id>',views.blog_detail, name='blog_detail'),
    path('post_delete/<int:id>',views.post_delete, name='post_delete'),
    path('edit_post/<int:id>',views.edit_post, name='edit_post'),
]