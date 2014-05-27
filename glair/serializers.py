from rest_framework import serializers
from rest_framework.exceptions import ParseError

from taggit.utils import parse_tags

from .models import Photo


class TagListSerializer(serializers.WritableField):
	def from_native(self, data):
		if type(data) is not list:
			data = parse_tags(data)
		return data

	def to_native(self, obj):
		if type(obj) is not list:
			return [tag.name for tag in obj.all()]
		return obj

class BasicPhotoSerializer(serializers.HyperlinkedModelSerializer): 	
	tags = TagListSerializer(blank=True)
	owner = serializers.Field(source='owner.username')

	class Meta:
		model = Photo
		fields = ('name', 'is_private', 'description', 'tags')
