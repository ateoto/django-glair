from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from .views import PhotoDetail, UploadView, PhotoBasicEdit


urlpatterns = patterns('',
	url(r'^photo/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', PhotoDetail.as_view(), name='photo-detail'),
	url(r'^photo/edit/(?P<pk>\d+)/$', PhotoBasicEdit.as_view(), name='photo-basic-edit'),
	url(r'^upload/', login_required(UploadView.as_view()), name='glair-upload'),
)