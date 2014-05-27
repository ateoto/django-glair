from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from rest_framework import viewsets, routers

from .views import (PhotoDetail, UploadView, PhotoBasicEdit, BasicPhotoViewset)

router = routers.DefaultRouter()
router.register(r'photos', BasicPhotoViewset)

urlpatterns = patterns('',
	url(r'^api/', include(router.urls)),
	url(r'^photo/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', PhotoDetail.as_view(), name='photo-detail'),
	url(r'^photo/edit/(?P<pk>\d+)/$', PhotoBasicEdit.as_view(), name='photo-basic-edit'),
	url(r'^upload/', login_required(UploadView.as_view()), name='glair-upload'),
)