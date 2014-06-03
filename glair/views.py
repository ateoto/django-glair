import logging

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import View
from django.http import JsonResponse
from django.core.urlresolvers import reverse

from django.template import Context
from django.template.loader import get_template
from crispy_forms.utils import render_crispy_form

from rest_framework import viewsets
from rest_framework import permissions

from sorl.thumbnail import get_thumbnail

from .models import Photo, Album
from .forms import UploadForm, BasicEditForm
from .serializers import BasicPhotoSerializer, BasicAlbumSerializer
from .permissions import IsOwnerOrReadOnly

logger = logging.getLogger('dev.console')

class PhotoDetail(DetailView):
    model = Photo

class UploadView(FormView):
    template_name = 'glair/upload.html'
    form_class = UploadForm

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        context['edit_form'] = BasicEditForm()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        image = form.save()

        template = get_template('glair/photo_inline_edit.html')
        html = template.render(Context({'object': image}))

        return JsonResponse({
            'pk': image.pk, 
            'html': html
        })

class BasicPhotoViewset(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = BasicPhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def post_save(self, obj, *args, **kwargs):
        if type(obj.tags) is list:
            saved_photo = Photo.objects.get(pk=obj.pk)
            for tag in obj.tags:
                saved_photo.tags.add(tag)

class BasicAlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = BasicAlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
        #logger.info(obj.photos)

    def post_save(self, obj, *args, **kwargs):
        for p in obj.photos.all():
            logger.info(p)
