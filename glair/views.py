from django.views.generic.detail import DetailView

from .models import Photo


class PhotoDetail(DetailView):
	model = Photo