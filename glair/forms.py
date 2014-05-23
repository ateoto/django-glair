from django import forms

from glair.models import Photo


class UploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'owner', 'image']
