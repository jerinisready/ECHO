# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Query,FbQueryMapper,request
from django.contrib import admin

# Register your models here.
admin.site.register(Query)
admin.site.register(FbQueryMapper)
admin.site.register(request)