from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from docker_test.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docker_test.settings')

app = Celery('docker_test',
             broker=CELERY_BROKER_URL,
             backend=CELERY_RESULT_BACKEND,
             include=['dt.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()