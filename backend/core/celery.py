# core/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django settings module নির্ধারণ
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# settings থেকে celery config load করবে
app.config_from_object("django.conf:settings", namespace="CELERY")

# Django app এর tasks auto-discover হবে
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
