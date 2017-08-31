# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Visitor(models.Model):
    time = models.DateTimeField(auto_now_add=True)