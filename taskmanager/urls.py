# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from .decorators import isAuthenticated, isAdmin
from .views import *

urlpatterns = [
    path('', isAuthenticated(IssueListView.as_view()), name='issue'),
    path('issue/add/', isAdmin(IssueAddView.as_view()), name='issue-add'),
    path('issue/delete/<int:pk>/', isAdmin(issueDelete), name='issue-delete'),
    path('issue/<int:pk>/', isAdmin(IssueUpdateView.as_view()), name='issue-update'),

    path('user/', isAuthenticated(UserListView.as_view()), name='user'),
    path('user/add/', isAdmin(UserAddView.as_view()), name='user-add'),
    path('user/delete/<int:pk>/', isAdmin(userDelete), name='user-delete'),
    path('user/<int:pk>/', isAdmin(UserUpdateView.as_view()), name='user-update'),

    path('tag/', isAuthenticated(TagListView.as_view()), name='tag'),
    path('tag/add/', isAdmin(TagAddView.as_view()), name='tag-add'),
    path('tag/delete/<int:pk>/', isAdmin(tagDelete), name='tag-delete'),
    path('tag/<int:pk>/', isAdmin(TagUpdateView.as_view()), name='tag-update'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]
