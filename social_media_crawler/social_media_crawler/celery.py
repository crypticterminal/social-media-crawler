from __future__ import absolute_import
import os

from celery import Celery, chain
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_crawler.settings')

app = Celery('social_media_crawler')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

