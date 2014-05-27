import json

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.template import Context
from django.template.loader import get_template
from crispy_forms.utils import render_crispy_form

from rest_framework import viewsets

from .models import Photo
from .forms import UploadForm, BasicEditForm
from .serializers import BasicPhotoSerializer


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

        edit_form.helper.form_action = reverse('photo-basic-edit', kwargs={'pk': image.pk})
        template = get_template('glair/photo_inline_edit.html')
        html = template.render(Context({'object': image, 'form': edit_form}))
        return HttpResponse(json.dumps({'pk': image.pk, 'html': html}), content_type='application/json')

class PhotoBasicEdit(UpdateView):
    model = Photo
    template_name = 'glair/photo_inline_edit.html'
    form_class = BasicEditForm

    def form_valid(self, form):
        image = form.save()
        return HttpResponse('word')

class BasicPhotoViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = BasicPhotoSerializer
