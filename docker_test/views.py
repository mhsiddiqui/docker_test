import socket

from django.http import HttpResponse
from dt.models import Visitor


def index(request):
    v = Visitor.objects.create()
    html = "<b>Hostname:</b> {hostname}<br/> Number: {number} <br/> <a href='/dt/add_task'>Add Task</a>".format(
        **{"hostname": socket.gethostname(), 'number': v.id})

    return HttpResponse(html)