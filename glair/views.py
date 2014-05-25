import json

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import View
from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template

from .models import Photo
from .forms import UploadForm


class PhotoDetail(DetailView):
	model = Photo

class UploadView(FormView):
    template_name = 'glair/upload.html'
    form_class = UploadForm

    def form_valid(self, form):
    	form.instance.owner = self.request.user
        image = form.save()
        context = Context({'object': image})
        template = get_template('glair/photo_inline_edit.html')
        html = template.render(context)
        return HttpResponse(json.dumps({'id': image.id, 'html': html}), content_type='application/json')