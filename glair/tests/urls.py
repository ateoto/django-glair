from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import viewsets, routers

from glair.views import BasicPhotoViewset

router = routers.DefaultRouter()
router.register(r'photos', BasicPhotoViewset)


urlpatterns = patterns('',
	url(r'^glair/', include('glair.urls')),
	url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
