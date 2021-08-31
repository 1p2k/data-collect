"""datacollect URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .pets.views import IndexView

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('admin/', admin.site.urls),
                  path('pets/', include('datacollect.pets.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
