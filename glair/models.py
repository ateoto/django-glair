from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

import uuid
import os

from datetime import datetime
from taggit.managers import TaggableManager



class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Camera(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Photo(models.Model):
    def make_filename(instance, filename):
        f, ext = os.path.splitext(filename)
        return 'photos/%s%s' % (uuid.uuid4().hex, ext.lower())
 
    EXPOSURE_PROGRAM_CHOICES = (
        (0, 'Not defined'),
        (1, 'Manual'),
        (2, 'Automatic'),
        (3, 'Aperture priority'),
        (4, 'Shutter priority'),
        (5, 'Program'),
        (6, 'Action'),
        (7, 'Portrait'),
        (8, 'Landscape'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    is_private = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    manufacturer = models.ForeignKey(Manufacturer, editable=False, null=True)
    camera = models.ForeignKey(Camera, editable=False, null=True)
    iso_speed = models.PositiveIntegerField(editable=False, null=True)
    exposure_program = models.PositiveSmallIntegerField(choices=EXPOSURE_PROGRAM_CHOICES, editable=False, null=True)
    taken_on = models.DateTimeField(editable=False, null=True)
    image = models.ImageField(upload_to=make_filename)
    thumbnail = models.ImageField(upload_to='photos', editable=False, null=True)
    focal_length = models.CharField(max_length=20, editable=False, null=True)
    exposure_time = models.CharField(max_length=20, editable=False, null=True)
    fnumber = models.DecimalField(max_digits=3, decimal_places=1, editable=False, null=True)
    flash_fired = models.BooleanField(default=False, editable=False)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(editable=False)
    tags = TaggableManager(blank=True)

    class Meta:
        permissions = (
            ('glair_upload_allowed', 'Allows user to upload images')
        )
        get_latest_by = 'uploaded_on'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo-detail', kwargs={
            'id': self.id,
            'slug': str(self.slug)
        })
    
    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.name)

        if self.pk:
            old = Photo.objects.get(id=self.pk)
            if self.name != old.name:
                self.slug = slugify(self.name)

        super(Photo, self).save(*args, **kwargs)

        if not self.taken_on:
            self.get_exif()
        if not self.thumbnail:
            self.make_thumbnail()

    def get_exif(self):
        from django.utils import timezone

        from fractions import Fraction
        from decimal import Decimal

        from PIL import Image
        from PIL.ExifTags import TAGS
        img = Image.open(self.image.file.name)
        exif = {
            TAGS[k]: v
            for k, v in img._getexif().items()
            if k in TAGS
        }
        self.manufacturer, created = Manufacturer.objects.get_or_create(name=exif['Make'])
        self.camera, created = Camera.objects.get_or_create(name=exif['Model'])
        self.taken_on =  timezone.make_aware(datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S'), timezone.get_current_timezone())
        self.exposure_program = exif['ExposureProgram']
        self.iso_speed = exif['ISOSpeedRatings']
        self.fnumber = Decimal(exif['FNumber'][0]) / Decimal(exif['FNumber'][1])
        self.focal_length = '%fmm' % (Decimal(exif['FocalLength'][0]))
        exposure_time = Fraction(exif['ExposureTime'][0], exif['ExposureTime'][1])

        if exposure_time.numerator > 1:
            self.exposure_time = str(Decimal(exposure_time.numerator) / Decimal(exposure_time.denominator))
        else:
            self.exposure_time = '%i/%i' % (exposure_time.numerator, exposure_time.denominator)

        not_fired = ['0x0','0x5','0x7','0x10','0x18','0x20']
        fired = ['0x1','0x9','0xD','0xF','0x19','0x1D','0x1F',
                '0x41','0x45','0x47','0x49','0x4D','0x4F','0x59','0x5D','0x5F']
        flash = hex(exif['Flash'])
        self.flash_fired = flash in fired

        self.save()

    def make_thumbnail(self):
        from PIL import Image
        from django.core.files import File
        from cStringIO import StringIO
        import os

        base, ext = os.path.splitext(os.path.basename(self.image.file.name))
        
        img = Image.open(self.image.file.name)
        img.thumbnail((200,200))
        outfile = StringIO()
        img.save(outfile, "JPEG")

        thumbname = '%s_200%s' % (base, ext)
        self.thumbnail.save(thumbname, File(outfile))
        
        self.save()

class Album(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    is_private = models.BooleanField(default=False)    
    photos = models.ManyToManyField(Photo)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.name)

        super(Album, self).save(*args, **kwargs)
