# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class query(models.Model):
    is_public = models.BooleanField()
    query = models.CharField(max_length=500)
    is_active = models.BooleanField()
    name = models.CharField(max_length=100)

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    query = models.ForeignKey(query, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    validity = models.DateField(null=True, blank=True,)

class fbquerymapper(models.Model):
    querry_mapper_id = models.AutoField(primary_key=True)
    page = models.CharField (max_length=200)

class socialdata(models.Model):
    page_id = models.ForeignKey(fbquerymapper,on_delete=models.CASCADE)
    message = models.CharField(max_length=2000)
    created_date = models.DateField()
    sentiment = models.CharField(max_length=20)
    source = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    like_count = models.IntegerField()
    love_count = models.IntegerField()
    haha_count = models.IntegerField()
    sad_count = models.IntegerField()
    wow_count = models.IntegerField()
    angry_count = models.IntegerField()
    link = models.CharField(max_length=100)

class socialdataquery(models.Model):
    socialdata = models.ForeignKey(socialdata,on_delete=models.CASCADE)
    query = models.ForeignKey(query, on_delete=models.CASCADE)
