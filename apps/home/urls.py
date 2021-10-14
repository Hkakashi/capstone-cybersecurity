# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('message/', views.InboxListView.as_view(), name='inbox'),
    path('message/sent/', views.SentListView.as_view(), name='sent'),
    path('message/send/', views.MessageCreateView.as_view(), name='message'),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
