from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from django.core.mail import EmailMultiAlternatives

from docker_test.celery import app

logger = get_task_logger(__name__)


@app.task
def test_task():
    html_content = '<html><body>%s</body></html>'
    tbl = '<table>'
    for i in range(1, 1000):
        tbl += '<tr><td>%s</td></tr>' % i
    tbl += '</table>'
    html_content = html_content % tbl
    msg = EmailMultiAlternatives('Subject here', html_content, 'mamoona.qayyum@fiveriverstech.com ',
                                 ['mhassan.frt@gmail.com', 'muhammad.mursaleen@fiveriverstech.com '], )
    msg.attach_alternative(html_content, "text/html")
    msg.send()