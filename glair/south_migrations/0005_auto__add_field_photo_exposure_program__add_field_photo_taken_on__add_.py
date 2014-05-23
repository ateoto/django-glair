# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Photo.exposure_program'
        db.add_column(u'glair_photo', 'exposure_program',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Photo.taken_on'
        db.add_column(u'glair_photo', 'taken_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 17, 0, 0)),
                      keep_default=False)

        # Adding field 'Photo.focal_length'
        db.add_column(u'glair_photo', 'focal_length',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 5, 17, 0, 0), max_length=20),
                      keep_default=False)

        # Adding field 'Photo.exposure_time'
        db.add_column(u'glair_photo', 'exposure_time',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=20),
                      keep_default=False)

        # Adding field 'Photo.fnumber'
        db.add_column(u'glair_photo', 'fnumber',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Photo.exposure_program'
        db.delete_column(u'glair_photo', 'exposure_program')

        # Deleting field 'Photo.taken_on'
        db.delete_column(u'glair_photo', 'taken_on')

        # Deleting field 'Photo.focal_length'
        db.delete_column(u'glair_photo', 'focal_length')

        # Deleting field 'Photo.exposure_time'
        db.delete_column(u'glair_photo', 'exposure_time')

        # Deleting field 'Photo.fnumber'
        db.delete_column(u'glair_photo', 'fnumber')


    models = {
        u'glair.camera': {
            'Meta': {'object_name': 'Camera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'glair.make': {
            'Meta': {'object_name': 'Make'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'glair.photo': {
            'Meta': {'object_name': 'Photo'},
            'camera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glair.Camera']"}),
            'exposure_program': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'exposure_time': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fnumber': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'focal_length': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'iso_speed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'make': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glair.Make']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'taken_on': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['glair']