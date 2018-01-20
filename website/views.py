# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    template = loader.get_template('website/index.html')
    context = {
        'name': "SMS - Social Media Survey",
        "r": [0,1,2,3,4],
    }
    r = template.render(context, request)
    print("hello World!")
    return HttpResponse(r)
    # instead we can use return render(request, 'website/index.html', context)
