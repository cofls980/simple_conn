from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Text(models.Model):
    tid = models.IntegerField(default=0, primary_key=True)
    txt = models.CharField(max_length=20)


class Color(models.Model):
    cid = models.IntegerField(default=0, primary_key=True)
    color = models.CharField(max_length=10)
    time_update = models.DateTimeField(auto_now=True)
    time_access = models.DateTimeField(auto_now=True)