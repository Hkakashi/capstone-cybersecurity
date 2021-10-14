# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE, blank=False)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    subject = models.CharField(blank=False, max_length=50)
    content = models.TextField(blank=False)
    time = models.DateTimeField(auto_now=True)
    iv = models.CharField(blank=False, max_length=50)