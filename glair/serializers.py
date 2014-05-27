from rest_framework import serializers

from .models import Photo


class BasicPhotoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Photo
		fields = ('name', 'is_private', 'description')