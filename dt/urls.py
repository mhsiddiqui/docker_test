from django.conf.urls import url
from django.contrib import admin

from dt.views import add_task

urlpatterns = [
    url(r'^add_task/$', add_task),
]
