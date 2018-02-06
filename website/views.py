# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm
# Create your views here.

def home(request):
    template = loader.get_template('website/index.html')
    context = {
        'name': "SMS - Social Media Survey",
    }
    r = template.render(context, request)
    return HttpResponse(r)
    # instead we can use return render(request, 'website/index.html', context)
def user(request):

    template = loader.get_template('website/user.html')
    context = {

    }

    r = template.render(context, request)
    return HttpResponse(r)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html',{'form': form})

