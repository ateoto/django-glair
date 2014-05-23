from django.contrib import admin

from . import models


class PhotoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.owner = request.user
        obj.save()

class AlbumAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if not obj.id:
			obj.owner = request.user
		obj.save()


admin.site.register(models.Manufacturer)
admin.site.register(models.Camera)
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Album, AlbumAdmin)
