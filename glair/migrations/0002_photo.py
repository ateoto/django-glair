# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.models
import taggit.managers
import glair.models


class Migration(migrations.Migration):

    dependencies = [
        ('glair', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', editable=False)),
                ('is_private', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('manufacturer', models.ForeignKey(to_field='id', editable=False, to='glair.Manufacturer', null=True)),
                ('camera', models.ForeignKey(to_field='id', editable=False, to='glair.Camera', null=True)),
                ('iso_speed', models.PositiveIntegerField(null=True, editable=False)),
                ('exposure_program', models.PositiveSmallIntegerField(null=True, editable=False, choices=[(0, b'Not defined'), (1, b'Manual'), (2, b'Automatic'), (3, b'Aperture priority'), (4, b'Shutter priority'), (5, b'Program'), (6, b'Action'), (7, b'Portrait'), (8, b'Landscape')])),
                ('taken_on', models.DateTimeField(null=True, editable=False)),
                ('image', models.ImageField(upload_to=glair.models.make_filename)),
                ('thumbnail', models.ImageField(upload_to=b'photos', null=True, editable=False)),
                ('focal_length', models.CharField(max_length=20, null=True, editable=False)),
                ('exposure_time', models.CharField(max_length=20, null=True, editable=False)),
                ('fnumber', models.DecimalField(null=True, editable=False, max_digits=3, decimal_places=1)),
                ('flash_fired', models.BooleanField(default=False, editable=False)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False)),
                ('tags', taggit.managers.TaggableManager(to=taggit.models.Tag, through=taggit.models.TaggedItem, blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'get_latest_by': b'uploaded_on',
            },
            bases=(models.Model,),
        ),
    ]
