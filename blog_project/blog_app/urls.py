from django.urls import path
from .views import *
from . import views


urlpatterns=[
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('home', views.render_home),
    path('post_blog', views.submit_post),
    path('reply', views.reply),
]