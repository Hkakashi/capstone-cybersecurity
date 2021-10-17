# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from base64 import b64encode, b64decode
from io import StringIO

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.core.management import call_command
from django.contrib.auth.mixins import LoginRequiredMixin
from Crypto.Random import get_random_bytes

from apps.home.models import Message
from apps.home.helper import encrypt, decrypt


@login_required(login_url="/login/")
def profile_view(request):
    context = {}
    context['segment'] = 'profile'
    context['message_count'] = Message.objects.filter(receiver=request.user).count()

    html_template = loader.get_template('home/profile.html')
    return HttpResponse(html_template.render(context, request))

class InboxListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    model = Message

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for message in context['object_list']:
            message.subject = decrypt(message.subject, message.iv)
            message.content = decrypt(message.content, message.iv)
        context['segment'] = 'inbox'
        context['message_count'] = Message.objects.filter(receiver=self.request.user).count()
        return context

class SentListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    model = Message

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for message in context['object_list']:
            message.subject = decrypt(message.subject, message.iv)
            message.content = decrypt(message.content, message.iv)
        context['segment'] = 'sent'
        context['message_count'] = Message.objects.filter(receiver=self.request.user).count()
        return context

class MessageCreateView(LoginRequiredMixin, CreateView):

    login_url = '/login/'
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
        context['message_sent'] = Message.objects.filter(sender=self.request.user).count()
        context['message_received'] = Message.objects.filter(receiver=self.request.user).count()
        context['message_count'] = Message.objects.filter(receiver=self.request.user).count()
        return context

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Message
    success_url = reverse_lazy('inbox')

    # bypass built-in confirmation
    # confirmation process was implemented in frontend
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

@login_required(login_url="/login/")
def dump_database(request):
    out = StringIO()
    call_command('dumpdata', 'auth.user', 'home.message', indent=4, stdout=out)
    response = HttpResponse(out.getvalue())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=Database.txt'
    return response