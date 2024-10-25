from django.urls import re_path
from CardScanning.consumers import *


websocket_urlpatterns=[
    re_path('ws/Card/',CardConsumer.as_asgi()),
]