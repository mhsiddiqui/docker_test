# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dt.tasks import test_task
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def add_task(request):
    result = test_task.delay()
    print result
    return HttpResponse('Task Added' + str(result))
