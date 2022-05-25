from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('hello/', views.helloworld),
    path('all/', views.graphList.as_view(), name='all'),
    path('login/', views.Login.as_view(), name='login'),
    path('post/', views.post, name='post'),
    path('logout/', LogoutView.as_view()),

]
