# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    template = loader.get_template('website/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
    # instead we can use return render(request, 'website/index.html', context)
