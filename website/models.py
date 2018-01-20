# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class account(models.Model):
    user_id = models.AutoField(primary_key=True)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    payment_status = models.CharField(max_length=10)
    survey_status = models.CharField(max_length=10)
    user_key = models.CharField(max_length=35)


class topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    user_id = models.ForeignKey(account,default=0, on_delete=models.CASCADE)
    query_fb = models.CharField(max_length=500)
    query_twitter=models.CharField(max_length=500)
    status=models.CharField(max_length=10)


class fbquerymapper(models.Model):
    querry_mapper_id = models.AutoField(primary_key=True)
    fb_page_id = models.CharField (max_length=200)
    topic_id =models.ForeignKey(topic,on_delete=models.CASCADE)

class sentiwords(models.Model):
    topic_id = models.ForeignKey(topic,on_delete=models.CASCADE)
    sentiword = models.CharField(max_length=20)
    count = models.IntegerField()
