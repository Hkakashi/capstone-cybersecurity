# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.contrib.auth import login
from apps.home import views

urlpatterns = [

    path('message/', views.InboxListView.as_view(), name='inbox'),
    path('message/sent/', views.SentListView.as_view(), name='sent'),
    path('message/send/', views.MessageCreateView.as_view(), name='message'),
    path('message/delete/<int:pk>/', views.MessageDeleteView.as_view(), name='delete'),
    path('dbdump/', views.dump_database, name='dump'),
    path('', views.profile_view, name='profile'),
]
