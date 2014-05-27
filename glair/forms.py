from django import forms

from crispy_forms.helper import FormHelper

from glair.models import Photo


class UploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'image']

class BasicEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'is_private', 'description', 'tags']

    def __init__(self, *args, **kwargs):
        super(BasicEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'basic-edit'
        self.helper.form_method = 'post'

