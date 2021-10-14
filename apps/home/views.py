# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from base64 import b64encode, b64decode

from django import template
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from Crypto.Random import get_random_bytes

from apps.home.models import Message
from apps.home.helper import encrypt, decrypt


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

class InboxListView(ListView):

    model = Message
    paginate_by = 10  # if pagination is desired

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for message in context['object_list']:
            message.subject = decrypt(message.subject, message.iv)
            message.content = decrypt(message.content, message.iv)
        context['segment'] = 'inbox'
        return context

class SentListView(ListView):

    model = Message
    paginate_by = 10  # if pagination is desired

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for message in context['object_list']:
            message.subject = decrypt(message.subject, message.iv)
            message.content = decrypt(message.content, message.iv)
        context['segment'] = 'sent'
        return context

class MessageCreateView(CreateView):

    model = Message
    fields = ['receiver', 'subject', 'content']
    success_url = '/message/'

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        iv = get_random_bytes(16)
        message.iv = b64encode(iv).decode()
        message.subject = encrypt(message.subject.encode(), iv).decode()
        message.content = encrypt(message.content.encode(), iv).decode()
        message.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'message'
        return context
