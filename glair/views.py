import json

import logging

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.template import Context
from django.template.loader import get_template
from crispy_forms.utils import render_crispy_form

from rest_framework import viewsets
from rest_framework import permissions

from .models import Photo
from .forms import UploadForm, BasicEditForm
from .serializers import BasicPhotoSerializer
from .permissions import IsOwnerOrReadOnly

logger = logging.getLogger('dev.console')

class PhotoDetail(DetailView):
    model = Photo

class UploadView(FormView):
    template_name = 'glair/upload.html'
    form_class = UploadForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        image = form.save()
        edit_form = BasicEditForm(initial={ 'name': image.name, 
                                            'is_private': image.is_private,
                                            'tags': image.tags,
                                            'description': image.description})

        template = get_template('glair/photo_inline_edit.html')
        html = template.render(Context({'object': image, 'form': edit_form}))
        return HttpResponse(json.dumps({'pk': image.pk, 'html': html}), content_type='application/json')

class BasicPhotoViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
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