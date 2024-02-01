# detect/urls.py

from django.urls import path
from detect.views import upload_image, upload_success, detect_objects
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('upload_success/', upload_success, name='upload_success'),
    path('detect_objects/', detect_objects, name='detect_objects')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
