# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from .decorators import isAuthenticated, isAdmin
from .views import *

urlpatterns = [
    path('', isAuthenticated(IssueListView.as_view()), name='issue'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),

    path('issue/add/', isAdmin(IssueCreateView.as_view()), name='issue-add'),
    path('issue/delete/', isAdmin(issueDelete), name='issue-delete'),
    path('issue/<int:pk>/', isAdmin(IssueUpdateView.as_view()), name='issue-update'),

    path('user/', isAuthenticated(UserListView.as_view()), name='user'),
    path('user/add/', isAdmin(UserCreateView.as_view()), name='user-add'),
    path('user/delete/', isAdmin(userDelete), name='user-delete'),
    path('user/<int:pk>/', isAdmin(UserUpdateView.as_view()), name='user-update'),
]
