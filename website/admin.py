# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import query,fbquerymapper,request
from django.contrib import admin

# Register your models here.
admin.site.register(query)
admin.site.register(fbquerymapper)
admin.site.register(request)