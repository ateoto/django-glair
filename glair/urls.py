from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from .views import PhotoDetail, UploadView


urlpatterns = patterns('',
	url(r'^photo/(?P<id>\d+)-(?P<slug>[-\w]+)/$', PhotoDetail.as_view(), name='photo-detail'),
	url(r'^upload/', login_required(UploadView.as_view()), name='glair-upload'),
)